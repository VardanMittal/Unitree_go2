import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vardan/Introduction-to-Robotics/Unitree_go2/go2_ws/install/go2_gazebo'
