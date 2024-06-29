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


class ActionDefinitionResponse(object):
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
        'name': 'str',
        'run_as_user_id': 'str',
        'action_details': 'ActionDetailsResponse'
    }

    attribute_map = {
        'name': 'name',
        'run_as_user_id': 'runAsUserId',
        'action_details': 'actionDetails'
    }

    required_map = {
        'name': 'optional',
        'run_as_user_id': 'optional',
        'action_details': 'optional'
    }

    def __init__(self, name=None, run_as_user_id=None, action_details=None, local_vars_configuration=None):  # noqa: E501
        """ActionDefinitionResponse - a model defined in OpenAPI"
        
        :param name:  The Name of this Action
        :type name: str
        :param run_as_user_id:  The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \"current user\".
        :type run_as_user_id: str
        :param action_details: 
        :type action_details: lusid_workflow.ActionDetailsResponse

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._run_as_user_id = None
        self._action_details = None
        self.discriminator = None

        self.name = name
        self.run_as_user_id = run_as_user_id
        if action_details is not None:
            self.action_details = action_details

    @property
    def name(self):
        """Gets the name of this ActionDefinitionResponse.  # noqa: E501

        The Name of this Action  # noqa: E501

        :return: The name of this ActionDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActionDefinitionResponse.

        The Name of this Action  # noqa: E501

        :param name: The name of this ActionDefinitionResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def run_as_user_id(self):
        """Gets the run_as_user_id of this ActionDefinitionResponse.  # noqa: E501

        The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \"current user\".  # noqa: E501

        :return: The run_as_user_id of this ActionDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._run_as_user_id

    @run_as_user_id.setter
    def run_as_user_id(self, run_as_user_id):
        """Sets the run_as_user_id of this ActionDefinitionResponse.

        The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \"current user\".  # noqa: E501

        :param run_as_user_id: The run_as_user_id of this ActionDefinitionResponse.  # noqa: E501
        :type run_as_user_id: str
        """

        self._run_as_user_id = run_as_user_id

    @property
    def action_details(self):
        """Gets the action_details of this ActionDefinitionResponse.  # noqa: E501


        :return: The action_details of this ActionDefinitionResponse.  # noqa: E501
        :rtype: lusid_workflow.ActionDetailsResponse
        """
        return self._action_details

    @action_details.setter
    def action_details(self, action_details):
        """Sets the action_details of this ActionDefinitionResponse.


        :param action_details: The action_details of this ActionDefinitionResponse.  # noqa: E501
        :type action_details: lusid_workflow.ActionDetailsResponse
        """

        self._action_details = action_details

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
        if not isinstance(other, ActionDefinitionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionDefinitionResponse):
            return True

        return self.to_dict() != other.to_dict()
