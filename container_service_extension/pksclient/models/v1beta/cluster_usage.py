# coding: utf-8

"""
    PKS

    PKS API  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClusterUsage(object):
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
        'name': 'str',
        'cpu': 'int',
        'memory': 'float'
    }

    attribute_map = {
        'name': 'name',
        'cpu': 'cpu',
        'memory': 'memory'
    }

    def __init__(self, name=None, cpu=None, memory=None):  # noqa: E501
        """ClusterUsage - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._cpu = None
        self._memory = None
        self.discriminator = None

        self.name = name
        self.cpu = cpu
        self.memory = memory

    @property
    def name(self):
        """Gets the name of this ClusterUsage.  # noqa: E501


        :return: The name of this ClusterUsage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterUsage.


        :param name: The name of this ClusterUsage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cpu(self):
        """Gets the cpu of this ClusterUsage.  # noqa: E501


        :return: The cpu of this ClusterUsage.  # noqa: E501
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ClusterUsage.


        :param cpu: The cpu of this ClusterUsage.  # noqa: E501
        :type: int
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this ClusterUsage.  # noqa: E501


        :return: The memory of this ClusterUsage.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ClusterUsage.


        :param memory: The memory of this ClusterUsage.  # noqa: E501
        :type: float
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
