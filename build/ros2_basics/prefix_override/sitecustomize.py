import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bartek/ros2_ws/src/ros2_basics/install/ros2_basics'
