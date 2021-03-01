#!/usr/bin/env python

import rospy
from simple_script_server import *
sss = simple_script_server()

if __name__ == '__main__':
	rospy.init_node("test_script")
	# move to start position
	handle_arm = sss.move("arm_right","side", False)
	sss.move("arm_left","side")
	sss.move("gripper_left","close")
	sss.move("gripper_right","close")
	sss.move("torso","front")
	sss.move("sensorring","front")


	sss.say("sound", ["Ho, Ho, Ho, Merry christmas and happy new year from everyone at the Human robot interaction lab of I roms, at Cardiff University. We wish you and your loved ones peace, health, happiness, and prosperity in the coming year."], False)
	sss.set_mimic("mimic", "laughing")
	sss.set_mimic("mimic", "laughing")
	handle_arm = sss.move("arm_right", "hello", False)
	handle_arm = sss.move("arm_left", "hello")

	# handle_arm = sss.move("arm_right", "side", False)
	# handle_arm = sss.move("arm_left", "side")


	# sss.say("sound",["Hello, my name is care o bot. "],False)
	# sss.move("sensorring","left")
	handle_arm.wait()
	# sss.move("sensorring","front"):
	sss.set_light("light_torso","cyan",False)

# comment this is a comment more comments
