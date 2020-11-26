#!/usr/bin/env python
from Tkinter import *
import rospy
from simple_script_server import *
sss = simple_script_server()

def test_funct():
    print("hello world")

def say_hello():
    sss.say("sound", ["say something here"], False)
    sss.move("arm_right", "hello")

def shake_torso():
    sss.move("torso", [[0,0.75]])
    sss.move("torso", [[0,-0.75]])


def main():
    tkWindow = Tk()
    tkWindow.geometry("500x500")
    tkWindow.title("Dashboard")



    button = Button(tkWindow, text="Say Hello", command=say_hello)
    button.place(height=50, width=100, relx=0, rely=0.25)

    button2 = Button(tkWindow, text="Wave")
    button2.place(height=50, width=100, relx=0.25, rely=0.25)

    button3 = Button(tkWindow, text="Assist user")
    button3.place(height=50, width=100, relx=0.5, rely=0.25)

    button4= Button(tkWindow, text="Say thank you")
    button4.place(height=50, width=100, relx=0.75, rely=0.25)

    button5= Button(tkWindow, text="example5")
    button5.place(height=50, width=100, relx=0, rely=0.5)

    button6= Button(tkWindow, text="example6")
    button6.place(height=50, width=100, relx=0.25, rely=0.5)

    button7= Button(tkWindow, text="example7")
    button7.place(height=50, width=100, relx=0.5, rely=0.5)

    button8= Button(tkWindow, text="example8")
    button8.place(height=50, width=100, relx=0.75, rely=0.5)


    tkWindow.mainloop()

if __name__ == "__main__":
    rospy.init_node("test_script")
    main()
