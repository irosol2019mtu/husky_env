# Husky Gazebo Environment
### Clearpath Playpen

![](https://github.com/irosol2019mtu/husky_env/blob/main/playpen.jpg)

### Agriculture

![](https://github.com/irosol2019mtu/husky_env/blob/main/agriculture.jpg)

## Dependencies

 - fath_pivot_mount_description: `$ sudo apt-get install ros-noetic-fath-pivot-mount-description`
 - flir_camera_description: `$ sudo apt-get install ros-noetic-flir-camera-description`
 - velodyne_description: `$ sudo apt-get install ros-noetic-velodyne-description`
 - realsense2_description: `$ sudo apt install ros-noetic-realsense2-description`
 - LMS1xx: `$ sudo apt-get install ros-noetic-lms1xx`
 - robot_localization: `$ sudo apt-get install ros-noetic-robot-localization`
 - interactive_marker_twist_server: `$ sudo apt-get install ros-noetic-interactive-marker-twist-server`
 - twist_mux: `$ sudo apt-get install ros-noetic-twist-mux`
 - teleop_twist_keyboard: `$ sudo apt-get install ros-noetic-teleop-twist-keyboard`
 - teleop_twist_joy: `$ sudo apt-get install ros-noetic-teleop-twist-joy`
 - rviz_imu_plugin: `$ sudo apt-get install ros-noetic-rviz-imu-plugin`
 - gmapping: `$ sudo apt-get install ros-noetic-gmapping`

## Installation Guide

1. Create a workspace
  ```bash
mkdir -p husky_ws/src
  ```
2. Change the directory to the source space (`src`) of your workspace
  ```bash
cd husky_ws/src
  ```
3. Clone repository
  ```bash
git clone https://github.com/Tinker-Twins/Husky.git
  ```
  ```bash
git clone https://github.com/clearpathrobotics/cpr_gazebo.git
  ```
4. Change the directory back to the workspace
  ```bash
cd ..
  ```
5. Build the packages
  ```bash
catkin_make
  ```

## Gazebo Environment Usage

1. Playpen:
    ```bash
roslaunch husky_gazebo husky_playpen.launch
    ```

2. Agriculture:
    ```bash
roslaunch cpr_agriculture_gazebo agriculture_world.launch
    ```
