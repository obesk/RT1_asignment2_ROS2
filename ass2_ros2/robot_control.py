#! /usr/bin/env python

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class RobotControl(Node):
    def __init__(self):
        super().__init__('robot_control')

        self.velocity_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_robot)
        self.subscriber = self.create_subscription(Odometry, '/odom', self.read_odom, 10)

        self.odometry = None

    def move_robot(self):
        if not self.odometry:
            self.get_logger().warning("No data received yet")
            return

        velocity_command = Twist()

        # Get the robot's current x position
        x_pos = self.odometry.pose.pose.position.x

        # Define linear velocity
        velocity_command.linear.x = 1.0

        # Adjust angular velocity based on x position
        if x_pos > 9.0:
            velocity_command.angular.z = 1.0
        elif x_pos < 2.0:
            velocity_command.angular.z = -1.0
        else:
            velocity_command.angular.z = 0.0

        self.velocity_publisher.publish(velocity_command)

    def read_odom(self, odometry_message):
        self.odometry = odometry_message


def main(args=None):
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create an instance of the RobotControl node
    robot_controller_node = RobotControl()

    rclpy.spin(robot_controller_node)

    robot_controller_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
