#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSReliabilityPolicy
import time

class Turtlebot3ObstacleDetection(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance_bot')

        qos_profile = QoSProfile(
            durability=QoSDurabilityPolicy.VOLATILE,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            depth=100
        )

        self.velocity_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.laser_subscriber = self.create_subscription(LaserScan, '/scan', self.scan_callback, qos_profile)

        self.robot_velocities = Twist()
        self.current_state = 'idle'

    def scan_callback(self, msg):
        scan_threshold = 0.8
        angles_to_check = [0, 20, 340]

        if all(msg.ranges[i] > scan_threshold for i in angles_to_check):
            if self.current_state != 'forward':
                self.move_forward()
        else:
            if self.current_state != 'obstacle':
                self.avoid_obstacle(msg.ranges, angles_to_check)

        self.velocity_publisher.publish(self.robot_velocities)

    def move_forward(self):
        self.robot_velocities.linear.x = 0.6
        self.robot_velocities.angular.z = 0.0
        self.log_message('Moving Forward')

    def avoid_obstacle(self, ranges, angles_to_check):
        obstacle_distance = min(ranges[i] for i in angles_to_check)
        self.log_message(f'Obstacle Beep Beep! Distance: {obstacle_distance:.2f} meters')

        self.robot_velocities.linear.x = 0.0

        if all(ranges[i] > 0.8 for i in angles_to_check):
            self.move_forward()
        else:
            self.robot_velocities.angular.z = -0.25
            self.log_message('Rotating')

    def log_message(self, message):
        print(f'{message}\n{"-" * 50}')
        self.current_state = message.lower()

def main(args=None):
    rclpy.init(args=args)

    print("Initializing Turtlebot3 Obstacle Detection...")
    time.sleep(5)
    print("Initiation complete. Starting in:")
    
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    node = Turtlebot3ObstacleDetection()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
