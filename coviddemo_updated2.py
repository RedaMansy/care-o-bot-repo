#!/usr/bin/env python
import rospy
from simple_script_server import *
sss = simple_script_server()

if __name__ == '__main__':
	rospy.init_node("test_script")
	sss.move("arm_right","side",False)
	sss.move("arm_left","side")
	sss.move("gripper_left","close")
	sss.move("gripper_right","close")
	sss.move("torso","front")
	sss.move("sensorring","front")
	sss.set_light("light_torso","cyan")
	rospy.sleep(3)

	"""
	===========
	Demo Intro
	===========

	"""

	
	# start demo
	sss.say("sound",["start"])
	rospy.sleep(2)
	
	sss.say("sound", ["Hello my name is Care-O-Bot from the Human robot interaction lab, Centre for Artificial Intelligence, Robotics and Human-Machine Systems, I roms, at Cardiff University. On behalf of I rohms, I am going to guide you through some of the rules you need to follow if you are visiting campus during these unprecedented times."], False) 
	sss.set_mimic("mimic", "laughing")
	sss.set_mimic("mimic", "laughing")
	handle_arm = sss.move("arm_right","hello",False)
	sss.move("torso", [[0,0.75]])
	sss.move("torso", [[0,-0.75]])
	sss.move("torso", "home")
	handle_arm = sss.move("arm_right", "hello")
	# rospy.sleep(10)
	# handle_arm = sss.move("arm_left", "hello")

	# rospy.sleep(1.5)

	"""
	===========================
	Face Covering 
	TODO: Gesture for face mask
	===========================

	"""


	sss.say("sound",["Firstly, make sure to wear a face covering when inside University buildings like me"], False)
	handle_arm = sss.move("arm_right", [[0,-1,0.9,-2.1,1,0,0]], False)
	handle_arm = sss.move("arm_left", [[0,1,-0.9,2.1,-1,0,0]])

	sss.move("arm_right", "side", False)
	sss.move("arm_left", "side")




	"""
	==================================
	Social Distancing + One Way System
	==================================

	"""


	sss.say("sound", ["Adhere to social distancing guidelines and stay two metres away from others where possible. You must also follow the signs around campus, including following the one way system."], False)
	handle_arm = sss.move("arm_right", "home", False)
	handle_arm = sss.move("arm_left", "home")
	sss.move("torso", [[0,0.3]])
	sss.move("torso", [[0,-0.3]])
	sss.move("torso", "home")
	# handle_arm = sss.move("arm_right", [[2.4, 1.4, -1.0472, 0, -1.0472, -0.6981, 1.0700]], False)
	# handle_arm = sss.move("arm_left", [[-2.4, -1.4, 1.0472, 0, 1.0472, 0.6981, -1.0700]])
	for i in range(3):
		handle_arm = sss.move("arm_right", [[1.4, 1.3, -1.0472, -1.9, -1.0472, -0.6981, 1.0700]], False)
		handle_arm = sss.move("arm_left", [[-1.4, -1.3, 1.0472, 1.9, 1.0472, 0.6981, -1.0700]])
		handle_arm = sss.move("arm_right", [[1.4, 1.3, -1.0472, -1.5, -1.0472, -0.6981, 1.0700]], False)
		handle_arm = sss.move("arm_left", [[-1.4, -1.3, 1.0472, 1.5, 1.0472, 0.6981, -1.0700]])

	"""
	==================================
	Hand Washing
	TODO: Rotate one of the grippers
	==================================

	"""
	sss.say("sound",["Remember to sanitise your hands regularly using the sanitisers available around the buildings and on arrival at the campus, as well as regular 20 second hand washing"], False)

######################## safest option (same height of hand, but further apart now) ############################
	for i in range(3):
 		handle_arm = sss.move("arm_left", [[1.02, 1.5, -1.4, 1.9, -1.84, -1.12, -0.64]], False)
 		handle_arm = sss.move("arm_right", [[-1.25, -1.5, 1.4, -1.9, 1.84, 1.12, 0.64]])
 		handle_arm = sss.move("arm_left", [[1.02, 1.3, -1.4, 1.9, -1.84, -1.12, -0.64]], False)
 		handle_arm = sss.move("arm_right", [[-1.25, -1.2, 1.4, -1.9, 1.84, 1.12, 0.64]])

 	sss.move("arm_left", "side", False)
 	sss.move("arm_right", "side")



 	"""
	==========
	Conclusion
	==========

	"""	

	handle_arm = sss.move("arm_right", "folded", False)
	handle_arm = sss.move("arm_left", "folded")

	sss.say("sound",["Thank you for your co operation"], False)
	# sss.set_mimic("mimic", "blinkingRight")
	
	sss.move("torso", [[-0.3,0.2]])
	sss.move("torso", "front")


	handle_arm = sss.move("arm_right", "side", False)
	handle_arm = sss.move("arm_left", "side")
	sss.say("sound",["Stay Safe"], False)

	


	handle_arm.wait()