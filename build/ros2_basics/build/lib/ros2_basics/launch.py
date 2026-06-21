from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='ros2_basics', executable='object_position'),
        Node(package='ros2_basics', executable='reach_checker'),
    ])
