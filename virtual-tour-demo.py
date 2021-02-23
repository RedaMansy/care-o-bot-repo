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

    # handle_arm = sss.move("arm_right","hello",False)
    # sss.move("torso", [[0,0.45]])
    # sss.move("torso", [[0,-0.45]])
    # sss.move("torso", "home")

    sss.say("sound", ["Hello every one, and welcome to the Human Robot Interaction lab virtual tour. I am care o bot four"], False)
    sss.set_mimic("mimic", "sayYes")
    handle_arm = sss.move("arm_right", ["hello1", "hello2", "hello1", "side"], False)
    sss.move("torso", [[0,0.45]])
    sss.move("torso", [[0,-0.45]])
    sss.move("torso", "home")

    rospy.sleep(5)

    sss.say("sound", ["And today, together with my friends, we are going to give you a glimpse into our world and what we do in our amazing lab"], False)

    handle_arm = sss.move("arm_left", "hello1", False)
    handle_arm = sss.move("arm_right", "hello1")
    handle_arm = sss.move("arm_left", "side", False)
    handle_arm = sss.move("arm_right", "side")

    sss.say("sound", ["But first, allow me to begin with a robotic opening dance"])
    # handle_arm = sss.move("arm_left", "wave_demo",  False)
    # handle_arm = sss.move("arm_right", "wave_demo")
    handle_arm = sss.move("arm_left", ["home","wave1", "wave2", "wave3", "wave1", "home", "side"], False)
    handle_arm = sss.move("arm_right", ["home","wave1", "wave2", "wave3", "wave1", "home", "side"])
    
    sss.set_mimic("mimic","laughing")


    sss.say("sound", ["Hopefully there are no professional dancers in the audience."], False)
    # add delay between audience and okay
    handle_arm = sss.move("arm_right", ["hello1"])
    sss.say("sound", ["Okay, let me pass you over to my colleagues before they shut me down."], False)
    handle_arm = sss.move("arm_right", ["hello1", "side"])
    sss.set_mimic("mimic","confused")
    sss.set_mimic("mimic","sayYes")

    handle_arm.wait()