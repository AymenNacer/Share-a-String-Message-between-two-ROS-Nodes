#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def message_talker():
	hello_pub = rospy.Publisher("hello", String, queue_size = 10) # to publish a string to 'hello' topic
	rospy.init_node("talker" , anonymous = False) # create a new node 
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		messageToPublish ='Hello_world' # message to be published
		rospy.loginfo(messageToPublish)
		hello_pub.publish(messageToPublish) # publishing the message
		rate.sleep()
if __name__ =='__main__':
	try:
		message_talker()
	except rospy.ROSInterruptException:
		pass

