# odom_subscriber.py
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    rospy.loginfo("Received Odometry Message:")
    rospy.loginfo(f"Position (x, y): ({msg.pose.pose.position.x}, {msg.pose.pose.position.y})")
    rospy.loginfo(f"Orientation (w, x, y, z): "
                  f"({msg.pose.pose.orientation.w}, {msg.pose.pose.orientation.x}, "
                  f"{msg.pose.pose.orientation.y}, {msg.pose.pose.orientation.z})")

def subscribe_odom():
    rospy.init_node('odom_subscriber', anonymous=True)
    rospy.Subscriber('/odom', Odometry, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_odom()
    except rospy.ROSInterruptException:
        pass
