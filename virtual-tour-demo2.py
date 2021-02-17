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
    

    sss.move("arm_right", "hello")
    sss.say("Thank you for joining us today. We hope that you enjoyed the tour and learned about our research as well as workflow.")
    # We are looking forward to meeting you and collaborating with you in the near future 
    # Something about delivering research and presentation
    # Something about taking a nap just be funny ya know
    # stretching

    sss.move("arm_right", "folded", False)
    sss.move("arm_left", "folded")

    sss.move("torso", [[-0.3,0.2]])
    sss.move("torso", "home")



    # introduce careobot
    # do something cool
