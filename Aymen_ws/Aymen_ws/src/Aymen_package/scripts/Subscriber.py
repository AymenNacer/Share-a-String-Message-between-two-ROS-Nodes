#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback_str(data):
	rospy.loginfo(data.data) #to print the data


def message_listener():
	rospy.init_node('listener' , anonymous = False) # create a node
	rospy.Subscriber('hello' , String , callback_str) # subscibe to 'hello' topic
	rospy.spin() # to keep listening



if __name__ =='__main__':
		message_listener()
	

