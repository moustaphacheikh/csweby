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


class Field(object):
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
        'level_key': 'str',
        'record_occurrence': 'int',
        'item_occurrence': 'int',
        'subitem_occurrence': 'int'
    }

    attribute_map = {
        'name': 'name',
        'level_key': 'levelKey',
        'record_occurrence': 'recordOccurrence',
        'item_occurrence': 'itemOccurrence',
        'subitem_occurrence': 'subitemOccurrence'
    }

    def __init__(self, name=None, level_key=None, record_occurrence=None, item_occurrence=None, subitem_occurrence=None):  # noqa: E501
        """Field - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._level_key = None
        self._record_occurrence = None
        self._item_occurrence = None
        self._subitem_occurrence = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if level_key is not None:
            self.level_key = level_key
        if record_occurrence is not None:
            self.record_occurrence = record_occurrence
        if item_occurrence is not None:
            self.item_occurrence = item_occurrence
        if subitem_occurrence is not None:
            self.subitem_occurrence = subitem_occurrence

    @property
    def name(self):
        """Gets the name of this Field.  # noqa: E501

        name of field  # noqa: E501

        :return: The name of this Field.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Field.

        name of field  # noqa: E501

        :param name: The name of this Field.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def level_key(self):
        """Gets the level_key of this Field.  # noqa: E501

        id-items of second/third level node if field is not at first level  # noqa: E501

        :return: The level_key of this Field.  # noqa: E501
        :rtype: str
        """
        return self._level_key

    @level_key.setter
    def level_key(self, level_key):
        """Sets the level_key of this Field.

        id-items of second/third level node if field is not at first level  # noqa: E501

        :param level_key: The level_key of this Field.  # noqa: E501
        :type: str
        """

        self._level_key = level_key

    @property
    def record_occurrence(self):
        """Gets the record_occurrence of this Field.  # noqa: E501

        record occurrence number of field (optional)  # noqa: E501

        :return: The record_occurrence of this Field.  # noqa: E501
        :rtype: int
        """
        return self._record_occurrence

    @record_occurrence.setter
    def record_occurrence(self, record_occurrence):
        """Sets the record_occurrence of this Field.

        record occurrence number of field (optional)  # noqa: E501

        :param record_occurrence: The record_occurrence of this Field.  # noqa: E501
        :type: int
        """

        self._record_occurrence = record_occurrence

    @property
    def item_occurrence(self):
        """Gets the item_occurrence of this Field.  # noqa: E501

        item occurrence number of field (optional)  # noqa: E501

        :return: The item_occurrence of this Field.  # noqa: E501
        :rtype: int
        """
        return self._item_occurrence

    @item_occurrence.setter
    def item_occurrence(self, item_occurrence):
        """Sets the item_occurrence of this Field.

        item occurrence number of field (optional)  # noqa: E501

        :param item_occurrence: The item_occurrence of this Field.  # noqa: E501
        :type: int
        """

        self._item_occurrence = item_occurrence

    @property
    def subitem_occurrence(self):
        """Gets the subitem_occurrence of this Field.  # noqa: E501

        sub-item occurrence number of field (optional)  # noqa: E501

        :return: The subitem_occurrence of this Field.  # noqa: E501
        :rtype: int
        """
        return self._subitem_occurrence

    @subitem_occurrence.setter
    def subitem_occurrence(self, subitem_occurrence):
        """Sets the subitem_occurrence of this Field.

        sub-item occurrence number of field (optional)  # noqa: E501

        :param subitem_occurrence: The subitem_occurrence of this Field.  # noqa: E501
        :type: int
        """

        self._subitem_occurrence = subitem_occurrence

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
        if issubclass(Field, dict):
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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
