from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    urdf_file = os.path.expanduser('~/6dof_arm_ws/src/six_dof_arm_control/urdf/6dof_robot.urdf')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=[urdf_file],
            output='screen'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='six_dof_arm_control',
            executable='esp32_arm_controller',
            output='screen'
        ),
        # Node(
        #     package='six_dof_arm_control',
        #     executable='ros2_send_joint_angles',
        #     output='screen'
        # ),

    ])
