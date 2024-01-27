#!/usr/bin/python3

import os
import cv2
import numpy as np
import torch
from utils import select_device, lane_line_mask, letterbox
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import torch

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('lanes_detector')
        self.image_sub = self.create_subscription(
            Image,
            '/zed/zed_node/point_cloud/cloud_registered',
            self.image_callback,
            10)
        self.image_sub  # prevent unused variable warning
        self.image_pub = self.create_publisher(Image, '/igvc/lanes_binary', 10)
        self.bridge = CvBridge()

        script_dir = os.path.dirname(os.path.realpath(__file__))
        # The path used is relative to this script's path!!
        weights_relative_path = 'yolopv2.pt'
        self.weights_path = os.path.join(script_dir, weights_relative_path)
        
        self.model  = torch.jit.load(self.weights_path)

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'rgb8')
            # Perform image processing with your PyTorch model
            processed_image = self.process_with_pytorch(cv_image)
            binary_image_msg = self.bridge.cv2_to_imgmsg(processed_image.astype(np.uint8), encoding='mono8')
            self.image_pub.publish(binary_image_msg)
        except CvBridgeError as e:
            self.get_logger().info(e)

    def process_with_pytorch(self, img):
        img0 = cv2.resize(img, (1280,720), interpolation=cv2.INTER_LINEAR)
        img = letterbox(img0, 640, stride=32)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
        img = np.ascontiguousarray(img)
        
        devi = '0'
        device = select_device(devi)
        half = device.type != 'cpu'  # half precision only supported on CUDA
        model = self.model.to(device)

        if half:
            model.half()  # to FP16  
        model.eval()
        if device.type != 'cpu':
            model(torch.zeros(1, 3, 640, 640).to(device).type_as(next(model.parameters())))  # run once
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        
        [_,_],_,ll= model(img)

        ll_seg_mask = lane_line_mask(ll) * 255
        return ll_seg_mask 


def main(args=None):
    rclpy.init(args=args)
    
    processor = ImageProcessor()
    processor.get_logger().info("shit is workin")
    rclpy.spin(processor)
    processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()