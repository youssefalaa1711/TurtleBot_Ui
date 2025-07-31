#!/bin/bash

# Source ROS2 and set TurtleBot3 model
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger

# Launch Gazebo simulation
gnome-terminal --title="Gazebo" -- bash -c "ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py; exec bash"

# Launch FastAPI backend
gnome-terminal --title="FastAPI Backend" -- bash -c "cd ~/turtlebot3_web_control/backend && source venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000; exec bash"

# Launch React frontend
gnome-terminal --title="React Frontend" -- bash -c "cd ~/turtlebot3_web_control/frontend && npm start; exec bash"
