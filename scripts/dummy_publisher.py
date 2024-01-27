#!/usr/bin/python3

from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

import rclpy
from rclpy.node import Node

class DummyLanes(Node):
    def __init__(self):
        super().__init__('dummy_lanes')
        self.binary_image_pub = self.create_publisher(Image, 'igvc/lanes_binary', 10)
        bin_img = cv2.imread("/home/joel/igvc_ws/src/lanes_costmap/images/left0002.jpg")
        self.image_message = CvBridge().cv2_to_imgmsg(bin_img,encoding="rgb8")
        timer_period = 1/30 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.binary_image_pub.publish(self.image_message)

def main(args=None):
    rclpy.init(args=args)
    dummy = DummyLanes()

    rclpy.spin(dummy)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    dummy.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()