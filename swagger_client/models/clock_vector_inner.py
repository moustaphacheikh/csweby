# coding: utf-8

"""
    CSPro Sync

    Web API for synchronizing data and files from devices in the field to a web server.   # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClockVectorInner(object):
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
        'device_id': 'str',
        'revision': 'int'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'revision': 'revision'
    }

    def __init__(self, device_id=None, revision=None):  # noqa: E501
        """ClockVectorInner - a model defined in Swagger"""  # noqa: E501

        self._device_id = None
        self._revision = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if revision is not None:
            self.revision = revision

    @property
    def device_id(self):
        """Gets the device_id of this ClockVectorInner.  # noqa: E501


        :return: The device_id of this ClockVectorInner.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ClockVectorInner.


        :param device_id: The device_id of this ClockVectorInner.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def revision(self):
        """Gets the revision of this ClockVectorInner.  # noqa: E501


        :return: The revision of this ClockVectorInner.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ClockVectorInner.


        :param revision: The revision of this ClockVectorInner.  # noqa: E501
        :type: int
        """

        self._revision = revision

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
        if issubclass(ClockVectorInner, dict):
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
        if not isinstance(other, ClockVectorInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
