from StringIO import StringIO

import rospy
from std_msgs.msg import Int64

from python_bindings_tutorial._add_two_ints_wrapper_cpp import AddTwoIntsWrapper


class AddTwoInts(object):
    def __init__(self):
        self._add_two_ints = AddTwoIntsWrapper()

    def _to_cpp(self, msg):
        """Return a serialized string from a ROS message

        Parameters
        ----------
        - msg: a ROS message instance.
        """
        buf = StringIO()
        msg.serialize(buf)
        return buf.getvalue()

    def _from_cpp(self, str_msg, cls):
        """Return a ROS message from a serialized string

        Parameters
        ----------
        - str_msg: str, serialized message
        - cls: ROS message class, e.g. sensor_msgs.msg.LaserScan.
        """
        msg = cls()
        return msg.deserialize(str_msg)

    def add(self, a, b):
        """Add two std_mgs/Int64 messages

        Return a std_msgs/Int64 instance.

        Parameters
        ----------
        - a: a std_msgs/Int64 instance.
        - b: a std_msgs/Int64 instance.
        """
        if not isinstance(a, Int64):
            rospy.ROSException('Argument 1 is not a std_msgs/Int64')
        if not isinstance(b, Int64):
            rospy.ROSException('Argument 2 is not a std_msgs/Int64')
        str_a = self._to_cpp(a)
        str_b = self._to_cpp(b)
        str_sum = self._add_two_ints.add(str_a, str_b)
        return self._from_cpp(str_sum, Int64)
