import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class Doubler(Node):
    def __init__(self):
        super().__init__('listener')                                   # nazwa node'a w grafie
        self.create_subscription(Int32, 'count', self.callback, 10) # typ, temat, callback, queue
        

    def callback(self, msg):
        result = 2*msg.data
        self.get_logger().info(f'odebrałem: "{result}"')


def main():
    rclpy.init()
    rclpy.spin(Doubler())        # blokuje i obsługuje callbacki aż do Ctrl+C
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

 