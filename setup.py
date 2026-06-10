import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros2_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bartek',
    maintainer_email='bartosz.tajak@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'counter = ros2_basics.counter:main',
            'doubler = ros2_basics.doubler:main',
            'object_position = ros2_basics.object_position:main',
            'reach_checker = ros2_basics.reach_checker:main',
        ],
    },
)
