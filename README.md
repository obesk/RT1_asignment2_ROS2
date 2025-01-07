# Assignment 2 Research Track 1 - ROS2

This assignment interacts with the gazebo simulation environment provided by the package https://github.com/CarmineD8/robot_urdf and interacts with the robot in it.

The purpose of the assignment is to show the interaction between nodes in ROS2.

When this package is run the robot should move in a zig-zag motion.


## Prerequisites

You should have a working ROS2 installation. This package has been tested with foxy

Be sure to add to also have installed the package https://github.com/CarmineD8/robot_urdf, which provides the simulation.


## How torun

1. Run the simulation environment:
    ```bash
    ros2 launch robot_urdf gazebo.launch.py
    ```
1. In a new terminal, run the controller node: 
    ```bash
    ros2 run ass2_ros2 robot_control_node
    ```
