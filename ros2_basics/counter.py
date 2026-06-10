import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32




class Counter(Node):
    def __init__(self):
        super().__init__('counter')                               # nazwa node'a w grafie
        self.pub = self.create_publisher(Int32, 'count', 10)  # typ, temat, queue depth
        self.timer = self.create_timer(2, self.tick)           # callback co 0.5 s
        self.i = 0


    def tick(self):
        msg = Int32()
        msg.data = self.i
        self.pub.publish(msg)
        self.get_logger().info(f'wysłałem: "{msg.data}"')
        self.i += 1


def main():
    rclpy.init()
    
    rclpy.spin(Counter())        # blokuje i obsługuje callbacki aż do Ctrl+C
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()