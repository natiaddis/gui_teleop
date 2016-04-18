#!/usr/bin/python

import Tkinter
import rospy
from geometry_msgs.msg import Twist

class simpleapp_tk(Tkinter.Tk):
    
    # inherits from the Tkinter class
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    # initialize basic components
    def initialize(self):

        self.twist = Twist()

        self.publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

        self.grid()

        #initialize the buttons
        button = Tkinter.Button(self,text="^",command=self.OnUpClicked)
        button.grid(column=1,row=2)
        button = Tkinter.Button(self,text="v",command=self.OnDownClicked)
        button.grid(column=1,row=4)
        button = Tkinter.Button(self,text=">",command=self.OnRightClicked)
        button.grid(column=2,row=3)
        button = Tkinter.Button(self,text="<",command=self.OnLeftClicked)
        button.grid(column=0,row=3)

        self.fwd_label = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.fwd_label, fg="white",bg="blue")
        label.grid(column=0,row=0,columnspan=2)
        self.fwd_label.set("forward speed:")

        # an entry for forward speed 
        self.fwd_speed = Tkinter.DoubleVar()
        self.fwd_entry = Tkinter.Entry(self,textvariable=self.fwd_speed,width=6)
        self.fwd_entry.grid(column=2,row=0)

        self.ang_label = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.ang_label,fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2)
        self.ang_label.set("angular speed:")


        # an entry for angular speed
        self.ang_speed = Tkinter.DoubleVar()
        self.ang_entry = Tkinter.Entry(self,textvariable=self.ang_speed,width=6)
        self.ang_entry.grid(column=2,row=1)

        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry()) 
        
    def OnUpClicked(self):
        self.reset_twist()
        self.twist.linear.x = self.fwd_speed.get()
        self.publisher.publish(self.twist)
    def OnDownClicked(self):
        self.reset_twist()
        self.twist.linear.x = -self.fwd_speed.get()
        self.publisher.publish(self.twist)
    def OnLeftClicked(self):
        self.reset_twist()
        self.twist.angular.z = self.ang_speed.get()
        self.publisher.publish(self.twist)
    def OnRightClicked(self):
        self.reset_twist()
        self.twist.angular.z = -self.ang_speed.get()
        self.publisher.publish(self.twist)

    def reset_twist(self):
        self.twist.linear.x = 0.0
        self.twist.linear.y = 0.0
        self.twist.linear.z = 0.0
        self.twist.angular.x = 0.0
        self.twist.angular.y = 0.0
        self.twist.angular.z = 0.0     

if __name__ == "__main__":
    rospy.init_node("turtle_gui_controller")
    app = simpleapp_tk(None)
    app.title('Turtle Controller')
    app.mainloop()
    
    