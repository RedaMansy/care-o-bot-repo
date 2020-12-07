#!/usr/bin/env python
from Tkinter import *
import rospy
from simple_script_server import *
sss = simple_script_server()

def say_hello():
    sss.say("sound", ["Hello"], False)
    sss.move("arm_right", "hello")

def bend_over():
    sss.move("torso", [[-0.3, 0.3]])

def answer_redbook():
    sss.say("sound", ["You can find it in the red book. Would you like me to assist you?"], False)
    sss.move("arm_left", "hello1")
    sss.move("arm_left", "side")

def check_redbook():
    sss.say("sound", ["I see something red on the table. would you like me to check it?"])

def not_redbook():
    sss.say("sound", ["This does not seem to be the red book. It might be in the drawer where all the documents usually are."], False)
    sss.move("arm_left", [[0.5,1,0,0,0,0,0]])
    sss.move("arm_left", "side")

def check_middle_drawer():
    sss.say("sound", ["The drawers on the right are for equipment, the one in the middle is for storing documents"])

def correct_redbook():
    sss.say("sound," ["Yes, a copy of the risk assessment form should be there."])

def assist_question():
    sss.say("sound", ["Would you like me to assist you with anything else?"])

def goodbye():
    sss.say("sound", ["Goodbye"], False)
    sss.move("arm_right", "hello")

def main():
    tkWindow = Tk()
    tkWindow.geometry("500x500")
    tkWindow.title("Dashboard")



    button = Button(tkWindow, text="Say Hello", command=say_hello)
    button.place(height=50, width=100, relx=0, rely=0.25)

    button2 = Button(tkWindow, text="Would you like me to assist you?", command=answer_redbook)
    button2.place(height=50, width=100, relx=0.25, rely=0.25)

    button3 = Button(tkWindow, text="I see something red", command=check_redbook)
    button3.place(height=50, width=100, relx=0.5, rely=0.25)

    button4= Button(tkWindow, text="Not redbook", command=not_redbook)
    button4.place(height=50, width=100, relx=0.75, rely=0.25)

    button5= Button(tkWindow, text="Check middle drawer", command=check_middle_drawer)
    button5.place(height=50, width=100, relx=0, rely=0.5)

    button6= Button(tkWindow, text="Correct redbook", command=correct_redbook)
    button6.place(height=50, width=100, relx=0.25, rely=0.5)

    button7= Button(tkWindow, text="Anything else?", command=assist_question)
    button7.place(height=50, width=100, relx=0.5, rely=0.5)

    button8= Button(tkWindow, text="Goodbye", command=goodbye)
    button8.place(height=50, width=100, relx=0.75, rely=0.5)


    tkWindow.mainloop()

if __name__ == "__main__":
    rospy.init_node("test_script")
    main()
