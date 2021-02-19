import rospy
from simple_script_server import *
sss = simple_script_server()



if __name__ == "__main__":
    rospy.init_node("test_script")
    handle_arm = sss.move("arm_right","side", False)
    sss.move("arm_left","side")
    sss.move("gripper_left","close")
    sss.move("gripper_right","close")
    sss.move("sensorring","front")

    sss.move("torso","front")
    
    sss.say("sound", ["It is my turn again, hah hah. But this unfortunately means our time is up, and I need to do some stretching."])
    # stretching actions here
    # sss.move("arm_left", [[0, 0, 0, 1.5, 0, 0, 0]])
    # sss.move("arm_right", [[0, 0, 0, -1.5, 0, 0, 0]])
    # sss.move("torso". [[-0.2,-0,3]])
    # sss.move("torso". [[-0.2, 0,3]])

    sss.say("sound", ["Thank you for joining us today. We hope that you enjoyed the tour and learned about our research as well as our workflow."])
    sss.say("sound", ["We are looking forward to meeting you and collaborating with you in the near future"]) 
    sss.say("sound", ["I do not know about you, but I am ready for my afternoon nap. Goodbye"])

    sss.move("arm_right", "folded", False)
    sss.move("arm_left", "folded")

    sss.move("torso", [[-0.3,0.2]])
    sss.move("torso", "home")
