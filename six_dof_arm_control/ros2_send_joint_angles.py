#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial
import struct

class JointStateSerialPublisher(Node):
    def __init__(self):
        super().__init__('joint_state_serial_publisher')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.listener_callback,
            10
        )
        # Change to your correct serial port (you already confirmed it is /dev/ttyUSB0)
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200)

    def listener_callback(self, msg: JointState):
        if len(msg.position) >= 1:
            angles = msg.position[0]
            angles_deg = angles * 180.0 / 3.14159265 
            
            data = struct.pack('<f', *angles_deg)
            self.serial_port.write(data)

            self.get_logger().info(f"Sent: {angles_deg:.2f}°")


def main(args=None):
    rclpy.init(args=args)
    node = JointStateSerialPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
