import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String
from datetime import datetime

class Talker(Node):
    def __init__(self):
        super().__init__('counter')                               # nazwa node'a w grafie
        self.pub = self.create_publisher(String, 'chatter', 10)  # typ, temat, queue depth
        self.timer = self.create_timer(1, self.tick)           # callback co 0.5 s
        self.i = 0

    def tick(self):
        msg = String()
        teraz = datetime.now()
        msg.data = f'hello {self.i},"____",{teraz}'
        self.pub.publish(msg)
        self.get_logger().info(f'wysłałem: "{msg.data}"')
        self.i += 1


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)        # blokuje i obsługuje callbacki aż do Ctrl+C
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()