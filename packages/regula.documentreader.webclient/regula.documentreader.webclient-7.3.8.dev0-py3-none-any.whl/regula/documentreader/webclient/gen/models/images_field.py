# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


"""

"""
class ImagesField(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'field_name': 'str',
        'field_type': 'GraphicFieldType',
        'value_list': 'list[ImagesFieldValue]'
    }

    attribute_map = {
        'field_name': 'fieldName',
        'field_type': 'fieldType',
        'value_list': 'valueList'
    }

    def __init__(self, field_name=None, field_type=None, value_list=None, local_vars_configuration=None):  # noqa: E501
        """ImagesField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_name = None
        self._field_type = None
        self._value_list = None
        self.discriminator = None

        self.field_name = field_name
        self.field_type = field_type
        self.value_list = value_list

    @property
    def field_name(self):
        """Gets the field_name of this ImagesField.  # noqa: E501

        Human readable field name. Do not bind to this name - use GraphicFieldType instead.  # noqa: E501

        :return: The field_name of this ImagesField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ImagesField.

        Human readable field name. Do not bind to this name - use GraphicFieldType instead.  # noqa: E501

        :param field_name: The field_name of this ImagesField.  # noqa: E501
        :type field_name: str
        """
        if self.local_vars_configuration.client_side_validation and field_name is None:  # noqa: E501
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def field_type(self):
        """Gets the field_type of this ImagesField.  # noqa: E501


        :return: The field_type of this ImagesField.  # noqa: E501
        :rtype: GraphicFieldType
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this ImagesField.


        :param field_type: The field_type of this ImagesField.  # noqa: E501
        :type field_type: GraphicFieldType
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501

        self._field_type = field_type

    @property
    def value_list(self):
        """Gets the value_list of this ImagesField.  # noqa: E501


        :return: The value_list of this ImagesField.  # noqa: E501
        :rtype: list[ImagesFieldValue]
        """
        return self._value_list

    @value_list.setter
    def value_list(self, value_list):
        """Sets the value_list of this ImagesField.


        :param value_list: The value_list of this ImagesField.  # noqa: E501
        :type value_list: list[ImagesFieldValue]
        """
        if self.local_vars_configuration.client_side_validation and value_list is None:  # noqa: E501
            raise ValueError("Invalid value for `value_list`, must not be `None`")  # noqa: E501

        self._value_list = value_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, ImagesField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImagesField):
            return True

        return self.to_dict() != other.to_dict()
