import math

from geometry_msgs.msg import Point
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool  # ← nowy import: typ wiadomości Bool


class reach_checker(Node):
    def __init__(self):
        super().__init__('reach_checker')
        self.create_subscription(Point, 'position', self.callback, 10)

        # publisher werdyktu — to słyszy brain_node
        self.pub = self.create_publisher(Bool, 'in_reach', 10)

        # parametr konfigurowalny z zewnątrz (launch / CLI), domyślnie 200.0 mm
        self.declare_parameter('max_reach', 200.0)

    def callback(self, msg):
        # odczyt parametru przy każdym callbacku — pozwala zmieniać go w locie
        max_reach = self.get_parameter('max_reach').value

        odleglosc = round(math.hypot(msg.x, msg.y, msg.z), 1)
        reachable = odleglosc < max_reach     # ← czysty bool (True/False)

        # publikacja werdyktu jako Bool
        out = Bool()
        out.data = reachable
        self.pub.publish(out)

        # log dla człowieka — czytelny opis zamiast samego True/False
        status = 'reachable' if reachable else 'not reachable'
        self.get_logger().info(
            f'dist={odleglosc} mm | max_reach={max_reach} mm | {status}'
        )


def main():
    rclpy.init()
    node = reach_checker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
