import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node(
        #     package='lanes_ros2',
        #     executable='lane_publisher.py',
        #     output='screen'),
        Node(
            package='lanes_ros2',
            executable='lanedetector.py',
            output='screen'),
    ])
