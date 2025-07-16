#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial
import time

class ArmController(Node):
    def __init__(self):
        super().__init__('esp32_arm_controller')
        self.subscription = self.create_subscription(JointState, 'joint_states', self.listener_callback, 10)
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        time.sleep(2)  # Wait for ESP32 to initialize

    def listener_callback(self, msg):
        angles = [int(a * 180 / 3.1415) for a in msg.position]  # convert radians to degrees
        if len(angles) < 6:
            angles += [0] * (6 - len(angles))  # pad if fewer joints
        angle_str = ','.join(str(a) for a in angles)
        self.ser.write((angle_str + '\n').encode())
        self.get_logger().info(f"Sent: {angle_str}")

def main(args=None):
    rclpy.init(args=args)
    controller = ArmController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
