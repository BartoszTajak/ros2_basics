import random

from geometry_msgs.msg import Point
import rclpy
from rclpy.node import Node


class object_position(Node):

    def __init__(self):
        super().__init__('object_position')  # nazwa node'a w grafie
        self.pub = self.create_publisher(Point, 'position', 10)
        self.timer = self.create_timer(1, self.tick)
        self.i = 0

    def tick(self):
        lista_liczb = [random.uniform(-200.0, 200.0) for _ in range(3)]
        msg = Point()
        msg.x = round(lista_liczb[0], 1)      # uwaga: float (.0), nie int
        msg.y = round(lista_liczb[1], 1)
        msg.z = round(lista_liczb[2], 1)
        self.pub.publish(msg)
        self.get_logger().info(f'Pick_position : {msg.x, msg.y, msg.z}')
        self.i += 1


def main():
    rclpy.init()
    node = object_position()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
