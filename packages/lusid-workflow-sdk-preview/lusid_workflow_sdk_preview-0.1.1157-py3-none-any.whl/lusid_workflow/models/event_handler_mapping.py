# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.1157
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_workflow.configuration import Configuration


class EventHandlerMapping(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'map_from': 'str',
        'set_to': 'str'
    }

    attribute_map = {
        'map_from': 'mapFrom',
        'set_to': 'setTo'
    }

    required_map = {
        'map_from': 'optional',
        'set_to': 'optional'
    }

    def __init__(self, map_from=None, set_to=None, local_vars_configuration=None):  # noqa: E501
        """EventHandlerMapping - a model defined in OpenAPI"
        
        :param map_from:  The field to map from
        :type map_from: str
        :param set_to:  The (constant) value to set
        :type set_to: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._map_from = None
        self._set_to = None
        self.discriminator = None

        self.map_from = map_from
        self.set_to = set_to

    @property
    def map_from(self):
        """Gets the map_from of this EventHandlerMapping.  # noqa: E501

        The field to map from  # noqa: E501

        :return: The map_from of this EventHandlerMapping.  # noqa: E501
        :rtype: str
        """
        return self._map_from

    @map_from.setter
    def map_from(self, map_from):
        """Sets the map_from of this EventHandlerMapping.

        The field to map from  # noqa: E501

        :param map_from: The map_from of this EventHandlerMapping.  # noqa: E501
        :type map_from: str
        """

        self._map_from = map_from

    @property
    def set_to(self):
        """Gets the set_to of this EventHandlerMapping.  # noqa: E501

        The (constant) value to set  # noqa: E501

        :return: The set_to of this EventHandlerMapping.  # noqa: E501
        :rtype: str
        """
        return self._set_to

    @set_to.setter
    def set_to(self, set_to):
        """Sets the set_to of this EventHandlerMapping.

        The (constant) value to set  # noqa: E501

        :param set_to: The set_to of this EventHandlerMapping.  # noqa: E501
        :type set_to: str
        """

        self._set_to = set_to

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventHandlerMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventHandlerMapping):
            return True

        return self.to_dict() != other.to_dict()
