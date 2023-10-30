# coding: utf-8

"""
    Robot service 3.0

    API сервис управления роботом - пылесосом.  # noqa: E501

    OpenAPI spec version: 1.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Schedule(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'date_time': 'str',
        'mode': 'int',
        'robot_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'date_time': 'dateTime',
        'mode': 'mode',
        'robot_id': 'robotId'
    }

    def __init__(self, id=None, date_time=None, mode=None, robot_id=None):  # noqa: E501
        """Schedule - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._date_time = None
        self._mode = None
        self._robot_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.date_time = date_time
        self.mode = mode
        self.robot_id = robot_id

    @property
    def id(self):
        """Gets the id of this Schedule.  # noqa: E501


        :return: The id of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schedule.


        :param id: The id of this Schedule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_time(self):
        """Gets the date_time of this Schedule.  # noqa: E501


        :return: The date_time of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this Schedule.


        :param date_time: The date_time of this Schedule.  # noqa: E501
        :type: str
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")  # noqa: E501

        self._date_time = date_time

    @property
    def mode(self):
        """Gets the mode of this Schedule.  # noqa: E501


        :return: The mode of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Schedule.


        :param mode: The mode of this Schedule.  # noqa: E501
        :type: int
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def robot_id(self):
        """Gets the robot_id of this Schedule.  # noqa: E501


        :return: The robot_id of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this Schedule.


        :param robot_id: The robot_id of this Schedule.  # noqa: E501
        :type: int
        """
        if robot_id is None:
            raise ValueError("Invalid value for `robot_id`, must not be `None`")  # noqa: E501

        self._robot_id = robot_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Schedule, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
