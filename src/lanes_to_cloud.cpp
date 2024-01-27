// #include <ros/ros.h>
// #include <sensor_msgs/PointCloud2.h>
// #include <pcl_ros/point_cloud.h>
// #include <ros/console.h>
// #include <lanes_costmap/ArrayXY.h>
// #include <std_msgs/Bool.h>

// ros::Publisher cloud_pub;
// bool object_presence = false;

// void publish_cloud(std::vector<float> arr_X, std::vector<float> arr_Y, int cloud_height=10, int z_shift=0){
//     int n = arr_X.size();
//     std::cout<<n;

//     sensor_msgs::PointCloud2 cloud_msg;

//     pcl::PointCloud<pcl::PointXYZ> pcl_cloud;
//     pcl::PointXYZ point;


    

//     // Populate the PointCloud2 message header
    


    
    
//     if(object_presence)
//     {
//         ROS_INFO("TRUEE");

//         cloud_msg.header.stamp = ros::Time::now();
//         cloud_msg.header.frame_id = "base_link";
//         cloud_msg.height = 1;
//         cloud_msg.width = 0;
//         cloud_msg.fields = {};
//         cloud_msg.is_bigendian = false;
//         cloud_msg.point_step = 0;
//         cloud_msg.row_step = 0;
//         cloud_msg.is_dense = false;

//         // pcl::toROSMsg(pcl_cloud, cloud_msg);

        
//         cloud_pub.publish(cloud_msg);
        
//         ros::Duration(15).sleep();
        
//     }
//     else
//     {
//         ROS_INFO("FALSE");
        
//         for(int i{0};i<n;i++){
//             point.x = arr_X[i];
//             point.y = arr_Y[i];
//             point.z = z_shift;
//             pcl_cloud.push_back(point);
//         }

//         pcl::toROSMsg(pcl_cloud, cloud_msg);


//         cloud_msg.header.stamp = ros::Time::now();
//         cloud_msg.header.frame_id = "base_link";


        
//        cloud_pub.publish(cloud_msg);
//     }

// }

// void get_lanes(const lanes_costmap::ArrayXY::ConstPtr& msg)
// {
//     std::vector<float> x = msg->x;
//     std::vector<float> y = msg->y;


//     publish_cloud(x,y);
// }

// void check_object(const std_msgs::Bool::ConstPtr& object_status)
// {
//     if(object_status->data)
//     {
//         object_presence = true;

//     }

//     else
//     {
//         object_presence = false;
//     }
// }

// int main(int argc, char **argv) {
//     ros::init(argc, argv, "lanes_to_cloud");
//     ros::NodeHandle n;

//     // Publishers
//     cloud_pub = n.advertise<sensor_msgs::PointCloud2>("bolt/lanes_cloud", 1000);
//     ros::Rate loop_rate(50);

//     // Subscribers
//     ros::Subscriber sub = n.subscribe("bolt/lanes_xy_array", 1000, get_lanes);

//     ros::Subscriber obj = n.subscribe("/object_pressence_bool", 1000, check_object);

//     ros::spin();

//     return 0;
// }
