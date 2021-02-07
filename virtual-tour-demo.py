import rospy
from simple_script_server import *
sss = simple_script_server()



if __name__ == "__main__":
    rospy.init_node("test_script")
	handle_arm = sss.move("arm_right","side", False)
	sss.move("arm_left","side")
	sss.move("gripper_left","close")
	sss.move("gripper_right","close")
	sss.move("torso","front")
	sss.move("sensorring","front")


    sss.say("sound", ["Welcome to the virtual tour of the HRI Lab."])
    sss.move("arm_right", "hello", False)

    # introduce careobot
    # do something cool

