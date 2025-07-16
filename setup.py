import os
from setuptools import find_packages, setup

package_name = 'six_dof_arm_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), ['launch/esp32_6dof.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tarun',
    maintainer_email='hackerurfta@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'esp32_arm_controller = six_dof_arm_control.esp32_arm_controller:main',
            'ros2_send_joint_angles = six_dof_arm_control.ros2_send_joint_angles:main'
        ],
    },
)
