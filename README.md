# Obstacle_Avoidance
Readme ENPM690 Kirti Kishore
1. Download and unzip the package
2. Make a workspace and paste the src folder in it
3. Open 2 Terminals side by side with the workspace opened in it
4. Colcon build inside the workspace in one of the terminals
5. Source the workspace with ros2 in both the terminals
6. For Teleop: 
        1. Run command: ros2 launch turtlebot3_gazebo neworld.launch.py in the 1st terminal
        2. Run command: ros2 run turtlebot3_teleop teleop_keyboard in the 2nd terminal
	The example video is in this link: 
	teleopkiki1.mp4 (https://drive.google.com/file/d/16TjEZ0LTKlwljZLOfqf8t3yXDTmjcwa0/view?usp=sharing)


7. For Part2 I have used obstacle avoiding behaviour:
        1. Run command: ros2 launch turtlebot3_gazebo neworld.launch.py in the 1st terminal
        2 Run command: ros2 run obstacle_avoid obstacle_avoid_bot
	The example video is in this link:
	obs_avoid.mp4  (https://drive.google.com/file/d/16Sb59vxQiFDuwdgR1fF9XMFZNY4t6hTN/view?usp=drive_link)
	
Note: I could not do screen recording for some reason kazam kept freezing, hence i opted to record from my phone. 
