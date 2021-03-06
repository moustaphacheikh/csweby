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


class SyncHistoryEntry(object):
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
        'dictionary': 'str',
        'direction': 'str',
        'universe': 'str',
        'date_time': 'datetime'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'dictionary': 'dictionary',
        'direction': 'direction',
        'universe': 'universe',
        'date_time': 'dateTime'
    }

    def __init__(self, device_id=None, dictionary=None, direction=None, universe=None, date_time=None):  # noqa: E501
        """SyncHistoryEntry - a model defined in Swagger"""  # noqa: E501

        self._device_id = None
        self._dictionary = None
        self._direction = None
        self._universe = None
        self._date_time = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if dictionary is not None:
            self.dictionary = dictionary
        if direction is not None:
            self.direction = direction
        if universe is not None:
            self.universe = universe
        if date_time is not None:
            self.date_time = date_time

    @property
    def device_id(self):
        """Gets the device_id of this SyncHistoryEntry.  # noqa: E501

        device id of client synced with  # noqa: E501

        :return: The device_id of this SyncHistoryEntry.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this SyncHistoryEntry.

        device id of client synced with  # noqa: E501

        :param device_id: The device_id of this SyncHistoryEntry.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def dictionary(self):
        """Gets the dictionary of this SyncHistoryEntry.  # noqa: E501

        name of dictionary synced  # noqa: E501

        :return: The dictionary of this SyncHistoryEntry.  # noqa: E501
        :rtype: str
        """
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        """Sets the dictionary of this SyncHistoryEntry.

        name of dictionary synced  # noqa: E501

        :param dictionary: The dictionary of this SyncHistoryEntry.  # noqa: E501
        :type: str
        """

        self._dictionary = dictionary

    @property
    def direction(self):
        """Gets the direction of this SyncHistoryEntry.  # noqa: E501

        direction of sync  # noqa: E501

        :return: The direction of this SyncHistoryEntry.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this SyncHistoryEntry.

        direction of sync  # noqa: E501

        :param direction: The direction of this SyncHistoryEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["put", "get", "both"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def universe(self):
        """Gets the universe of this SyncHistoryEntry.  # noqa: E501

        universe used for the sync  # noqa: E501

        :return: The universe of this SyncHistoryEntry.  # noqa: E501
        :rtype: str
        """
        return self._universe

    @universe.setter
    def universe(self, universe):
        """Sets the universe of this SyncHistoryEntry.

        universe used for the sync  # noqa: E501

        :param universe: The universe of this SyncHistoryEntry.  # noqa: E501
        :type: str
        """

        self._universe = universe

    @property
    def date_time(self):
        """Gets the date_time of this SyncHistoryEntry.  # noqa: E501

        date/time of synchronization in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z)  # noqa: E501

        :return: The date_time of this SyncHistoryEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this SyncHistoryEntry.

        date/time of synchronization in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z)  # noqa: E501

        :param date_time: The date_time of this SyncHistoryEntry.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

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
        if issubclass(SyncHistoryEntry, dict):
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
        if not isinstance(other, SyncHistoryEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
