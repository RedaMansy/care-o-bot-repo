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

    handle_arm = sss.move("arm_right", ["hello1", "side"], False)
    
    sss.say("sound", ["It is my turn again, hah hah. I was standing here politely the whole time. So it is time for me to stretch my limbs"])
    sss.set_mimic("mimic", "laughing")
    sss.say("sound", ["Oh, I mean arms"])

    rospy.sleep(7)
    # stretching actions here
    handle_arm = sss.move("arm_left", "home", False)
    handle_arm = sss.move("arm_right", "home")

    sss.set_mimic("mimic", "confused")
    sss.set_mimic("mimic", "confused")

    sss.move("torso", [[0,0.4]])
    sss.move("torso", [[0,-0.4]])
    sss.move("torso", "front")

    handle_arm = sss.move("arm_left", "home", False)
    handle_arm = sss.move("arm_right", "home")



    
    # sss.move("torso", [[-0.2,-0.3]])
    # sss.move("torso", "front")
    # sss.move("torso", [[-0.2, 0.3]])
    # sss.move("torso", "front")

    handle_arm = sss.move("arm_right", "side", False)
    handle_arm = sss.move("arm_left", "side")

    sss.set_mimic("mimic", "confused")
    sss.set_mimic("mimic", "confused")
    sss.set_mimic("mimic", "confused")

    # sss.move("arm_left", [[0, 0, 0, 1.5, 0, 0, 0]])
    # sss.move("arm_right", [[0, 0, 0, -1.5, 0, 0, 0]])
    sss.move("torso", [[-0.2,-0.3], "home"])
    sss.move("torso", [[-0.2, 0.5], "home"])
    sss.move("torso", [[-0.2,-0.3], "home"])

    sss.say("sound", ["A few more of those and I am on my way to a six pack"])
    sss.set_mimic("mimic", "laughing")
    sss.set_mimic("mimic", "laughing")


    handle_arm =  sss.move("arm_right", "folded", False)
    handle_arm = sss.move("arm_left", "folded")


    sss.say("sound", ["Well, thank you for joining us today. We hope that you enjoyed the tour as much as we enjoyed hosting it"], False)
    sss.move("torso", [[-0.3,0.2]])

    sss.move("torso", "home")
    sss.say("sound", ["We are really looking forward to meeting you and collaborating with you in the near future"]) 
    # move front arm to hello1, check if possible
    # handle_arm = sss.move("arm_left", ["side","hello1", "side"])
    handle_arm = sss.move("arm_right", "side", False)
    handle_arm = sss.move("arm_left", "side")

    sss.say("sound", ["We are at the end of the tour, so let us celebrate. Help yourself to a drink, while I enjoy a warm glass of electrons. Yum yum"], False)
    handle_arm = sss.move("arm_right", ["hello1", "side"], False)
    handle_arm = sss.move("arm_left", ["hello1", "side"])

    handle_arm = sss.move("arm_right", ["hello1", "hello2", "side"], False)
    sss.say("sound", ["Goodbye"])

    sss.set_mimic("mimic", "laughing")
    sss.set_mimic("mimic", "laughing")
    sss.set_mimic("mimic", "laughing")

    # and up to wave

    
    handle_arm.wait()