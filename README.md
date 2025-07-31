# 🕹️ Web-Based TurtleBot3 Control with ROS2 + FastAPI + React

## 📖 Project Overview

This project enables **remote, web-based control** of a **simulated TurtleBot3 Burger robot** using a modern full-stack architecture:

- 🧭 The robot is simulated in **Gazebo**
- 🌐 A **React frontend** provides a clean web UI for control
- 🚀 A **FastAPI backend** accepts movement commands and publishes them to ROS2

### Why This Project?

Most ROS-based systems rely on command-line tools or local applications for control. This project modernizes that by introducing a **web-first interface**, useful for:

- Robotics students and developers learning ROS2
- Creating user-friendly interfaces for simulation or real robots
- Extending toward real-time dashboards, remote robot fleets, or IoT applications

---

## 🧱 Tech Stack and Components

| Layer       | Technology                          | Role                                       |
|------------|--------------------------------------|--------------------------------------------|
| Simulation | **ROS2 Humble**, **Gazebo**, **RViz2** | Simulate and visualize the TurtleBot3      |
| Backend    | **FastAPI** + **rclpy** (Python)     | Bridge between the UI and ROS2             |
| Frontend   | **React.js**        | Web interface to send commands             |
| Messaging  | **ROS2 Topics**                      | Publishes `geometry_msgs/Twist` to `/cmd_vel` |

---

## 🚀 How the System Works

1. User clicks a button on the **React UI** (e.g., "Move Forward")
2. A **POST request** is sent to the **FastAPI backend**
3. FastAPI converts the command into a **ROS2 message** of type `geometry_msgs/Twist`
4. ROS2 publishes it on the `/cmd_vel` topic
5. The simulated **TurtleBot3 in Gazebo** moves accordingly


## 🖼️ UI Preview

![screenshot placeholder](Images/image)

<<<<<<< HEAD
=======

>>>>>>> 17acb40 (images)
