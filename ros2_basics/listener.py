import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__('listener')                                   # nazwa node'a w grafie
        self.create_subscription(String, 'chatter', self.callback, 10) # typ, temat, callback, queue
        # brak timera — listener reaguje na wiadomości, nie tyka zegarem

    def callback(self, msg):                  # ROS wywoła to, gdy na /chatter przyjdzie wiadomość
        self.get_logger().info(f'odebrałem: "{msg.data}"')


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)        # blokuje i obsługuje callbacki aż do Ctrl+C
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

 