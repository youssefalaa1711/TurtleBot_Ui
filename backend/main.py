from fastapi import FastAPI
from pydantic import BaseModel
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import threading
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VelocityCommand(BaseModel):
    linear_x: float
    angular_z: float

class RosNode(Node):
    def __init__(self):
        super().__init__('web_control_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

    def send_velocity(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        self.publisher.publish(msg)

# Initialize ROS2 node and start spinning in background
rclpy.init()
ros_node = RosNode()
threading.Thread(target=rclpy.spin, args=(ros_node,), daemon=True).start()

@app.post("/move")
def move(cmd: VelocityCommand):
    ros_node.send_velocity(cmd.linear_x, cmd.angular_z)
    return {"status": "Command sent", "linear_x": cmd.linear_x, "angular_z": cmd.angular_z}
