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

    sss.say("sound", ["Hello every one, and welcome to the Human Robot Interaction lab virtual tour. I am care o bot four"], False)
    handle_arm = sss.move("arm_right", ["hello1", "hello2", "side"])
    # shake torso
    

    # something about a fun presentatino planned for the next hour

    sss.say("sound", ["And today, together with my friends, we are going to give you a glimpse into our world and what we do in our awesome lab"])
    sss.set_mimic("mimic","laughing")
    sss.set_mimic("mimic","laughing")
    sss.set_mimic("mimic","laughing")


    # sss.say("sound", ["Today, my teammates and I will be showing you around the lab, and introducing you to the various equipment we have around."], False)
    sss.move("arm_left", "hello1", False)
    sss.move("arm_right", "hello1")
    sss.move("arm_left", "side", False)
    sss.move("arm_right", "side")

    sss.say("sound", ["But first, an opening dance"])
    # handle_arm = sss.move("arm_left", "wave_demo",  False)
    # handle_arm = sss.move("arm_right", "wave_demo")
    handle_arm = sss.move("arm_left", ["home","wave1", "wave2", "wave3", "wave1", "home", "side"], False)
    handle_arm = sss.move("arm_right", ["home","wave1", "wave2", "wave3", "wave1", "home", "side"])
    
    sss.set_mimic("mimic","laughing")

    sss.say("sound", ["Hopefully there are no professional dancers in the audience. Okay, let me pass you over to my colleagues now before they shut me down."])
    sss.move("arm_right", "hello1")
    sss.move("arm_right", "side")
    sss.set_mimic("mimic","laughing")
    sss.set_mimic("mimic","laughing")

    handle_arm.wait()