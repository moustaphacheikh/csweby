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


class Note(object):
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
        'operator_id': 'str',
        'content': 'str',
        'modified_time': 'datetime',
        'field': 'Field'
    }

    attribute_map = {
        'operator_id': 'operatorId',
        'content': 'content',
        'modified_time': 'modifiedTime',
        'field': 'field'
    }

    def __init__(self, operator_id=None, content=None, modified_time=None, field=None):  # noqa: E501
        """Note - a model defined in Swagger"""  # noqa: E501

        self._operator_id = None
        self._content = None
        self._modified_time = None
        self._field = None
        self.discriminator = None

        if operator_id is not None:
            self.operator_id = operator_id
        if content is not None:
            self.content = content
        if modified_time is not None:
            self.modified_time = modified_time
        if field is not None:
            self.field = field

    @property
    def operator_id(self):
        """Gets the operator_id of this Note.  # noqa: E501

        operator ID  for this note  # noqa: E501

        :return: The operator_id of this Note.  # noqa: E501
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        """Sets the operator_id of this Note.

        operator ID  for this note  # noqa: E501

        :param operator_id: The operator_id of this Note.  # noqa: E501
        :type: str
        """

        self._operator_id = operator_id

    @property
    def content(self):
        """Gets the content of this Note.  # noqa: E501

        text of note  # noqa: E501

        :return: The content of this Note.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Note.

        text of note  # noqa: E501

        :param content: The content of this Note.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def modified_time(self):
        """Gets the modified_time of this Note.  # noqa: E501

        Modified time in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z)  # noqa: E501

        :return: The modified_time of this Note.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this Note.

        Modified time in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z)  # noqa: E501

        :param modified_time: The modified_time of this Note.  # noqa: E501
        :type: datetime
        """

        self._modified_time = modified_time

    @property
    def field(self):
        """Gets the field of this Note.  # noqa: E501


        :return: The field of this Note.  # noqa: E501
        :rtype: Field
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Note.


        :param field: The field of this Note.  # noqa: E501
        :type: Field
        """

        self._field = field

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
        if issubclass(Note, dict):
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
        if not isinstance(other, Note):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
