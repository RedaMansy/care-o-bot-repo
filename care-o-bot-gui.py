#!/usr/bin/env python
from Tkinter import *
import rospy
from simple_script_server import *
sss = simple_script_server()

def say_hello():
    sss.say("sound", ["Hello"])

    sss.move("arm_right", ["hello1", "hello2", "hello1"], False)
    sss.say("sound", ["Welcome to the H.R.I lab, may I help you?"])

    sss.move("arm_right", "side")

def bend_over():
    sss.move("torso", [[-0.3, 0.3]])

def answer_redbook():
    sss.say("sound", ["You can find the form in the red book. Would you like me to assist you in finding it?"], False)
    sss.move("arm_left", "hello1")
    sss.move("arm_left", "side")

def last_saw():
    sss.say("sound", ["The last time I saw it, someone was checking it over there."], False)
    sss.move("arm_right", "hello1")
    sss.move("arm_right",[[1.69,1.19,-0.48,-2.09,-0.34,0.4,0.12]])
    sss.move("arm_right", "side")

def check_redbook():
    sss.say("sound", ["Let me check"])

def not_redbook():
    sss.say("sound", ["This is not the red book, it might be in the drawer where all the documents usually are."], False)
    # sss.move("arm_left", [[0.5,1,0,0,0,0,0]])
    sss.move("torso",  [[0,0.5]])
    # sss.move("arm_left", [[-1.4, -1.3, 1.0472, 1.9, 1.0472, 0.6981, -1.0700]])
    # change this to hello1 - done
    sss.move("arm_left", "hello1")
    sss.move("arm_left", "side")
    sss.move("torso", "front")

def check_middle_drawer():
    sss.say("sound", ["Oh, the drawers on the right are for equipment, and the middle ones are for storing lab documents"])

def correct_redbook():
    sss.say("sound", ["Yes, a copy of the risk assessment form should be there."])

def assist_question():
    sss.say("sound", ["Is there anything else I can help you with?"])

def my_pleasure():
    sss.say("sound", ["My pleasure"])

def goodbye():
    sss.say("sound", ["Goodbye"], False)
    sss.move("arm_right", "hello")


def give_key():
    sss.say("sound", ["Yes, I have the key. Here you go."], False)
    sss.move("arm_right", [[1.4, 1.3, -1.0472, -2.3, -1.0472, -0.6981, 1.0700]])
    sss.move("arm_right", [[1.4, 1.3, -1.0472, -2.3, -1.0472, -0.6981, 1.0700]])
    sss.move("arm_right", [[1.4, 1.3, -1.0472, -2.3, -1.0472, -0.6981, 1.0700]])
    # make arm higher - change 2.1 if needed - done
    sss.move("arm_right", "side")


def main():
    tkWindow = Tk()
    tkWindow.geometry("500x500")
    tkWindow.title("Dashboard")



    button = Button(tkWindow, text="Say Hello", command=say_hello)
    button.place(height=50, width=100, relx=0, rely=0.25)

    button2 = Button(tkWindow, text="Assist you?", command=answer_redbook)
    button2.place(height=50, width=100, relx=0.25, rely=0.25)

    buttonx = Button(tkWindow, text="Last saw", command=last_saw)
    buttonx.place(height=50, width=100, relx=0.5, rely=0.25)

    button3 = Button(tkWindow, text="Check redbook", command=check_redbook)
    button3.place(height=50, width=100, relx=0.75, rely=0.25)

    button4= Button(tkWindow, text="Not redbook", command=not_redbook)
    button4.place(height=50, width=100, relx=0, rely=0.5)

    button5= Button(tkWindow, text="Check middle drawer", command=check_middle_drawer)
    button5.place(height=50, width=100, relx=0.25, rely=0.5)

    button6= Button(tkWindow, text="Correct redbook", command=correct_redbook)
    button6.place(height=50, width=100, relx=0.5, rely=0.5)

    button7= Button(tkWindow, text="Anything else?", command=assist_question)
    button7.place(height=50, width=100, relx=0.75, rely=0.5)

    button8= Button(tkWindow, text="My Pleasure", command=my_pleasure)
    button8.place(height=50, width=100, relx=0, rely=0.75)

    button9= Button(tkWindow, text="Give key", command=give_key)
    button9.place(height=50, width=100, relx=0.25, rely=0.75)

    button10 = Button(tkWindow, text="Goodbye", command=goodbye)
    button10.place(height=50, width=100, relx=0.5, rely=0.75)



    tkWindow.mainloop()

if __name__ == "__main__":
    rospy.init_node("test_script")
    main()
