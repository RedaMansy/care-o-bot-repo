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

    sss.say("sound", ["Hello everyone, and welcome to the Human Robot Interaction lab s virtual tour. My name is care.o.bot"], False)
    rospy.sleep(3)
    handle_arm = sss.move("arm_right", "hello")
    

    # something about a fun presentatino planned for the next hour

    sss.say("sound", ["Today, we will be showing you around the lab, and introducing you to the various equipment we have around."])

    sss.say("sound", ["But first"])
    handle_arm = sss.move("arm_left", "wave_demo",  False)
    handle_arm = sss.move("arm_right", "wave_demo")
    

    sss.say("sound", ["Now that that is out of the way, here is an overview of our lab equipment."])
    handle_arm.wait()

    print(handle_arm.get_state())