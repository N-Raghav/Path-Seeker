import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Point, Quaternion

def get_destination_coordinates():
    x = float(input("Enter the x-coordinate for the destination: "))
    y = float(input("Enter the y-coordinate for the destination: "))
    return x, y

def publish_odom(x, y):
    rospy.init_node('odom_publisher', anonymous=True)
    publisher_odom = rospy.Publisher('/odom', Odometry, queue_size=10)

    while not rospy.is_shutdown():
        msg = Odometry()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "odom"
        msg.pose.pose = Pose(Point(x, y, 0), Quaternion(0, 0, 0, 1))

        publisher_odom.publish(msg)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        x, y = get_destination_coordinates()
        publish_odom(x, y)
    except rospy.ROSInterruptException:
        pass
