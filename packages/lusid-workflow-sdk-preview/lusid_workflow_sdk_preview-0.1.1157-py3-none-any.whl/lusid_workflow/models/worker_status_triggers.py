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


class WorkerStatusTriggers(object):
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
        'started': 'str',
        'completed_with_results': 'str',
        'completed_no_results': 'str',
        'failed_to_start': 'str',
        'failed_to_complete': 'str'
    }

    attribute_map = {
        'started': 'started',
        'completed_with_results': 'completedWithResults',
        'completed_no_results': 'completedNoResults',
        'failed_to_start': 'failedToStart',
        'failed_to_complete': 'failedToComplete'
    }

    required_map = {
        'started': 'optional',
        'completed_with_results': 'optional',
        'completed_no_results': 'optional',
        'failed_to_start': 'optional',
        'failed_to_complete': 'optional'
    }

    def __init__(self, started=None, completed_with_results=None, completed_no_results=None, failed_to_start=None, failed_to_complete=None, local_vars_configuration=None):  # noqa: E501
        """WorkerStatusTriggers - a model defined in OpenAPI"
        
        :param started:  Trigger to invoke when the Worker has Started
        :type started: str
        :param completed_with_results:  Trigger to invoke when the Worker has Completed (with results)
        :type completed_with_results: str
        :param completed_no_results:  Trigger to invoke when the Worker has Completed (no results)
        :type completed_no_results: str
        :param failed_to_start:  Trigger to invoke when the Worker has Failed to Start
        :type failed_to_start: str
        :param failed_to_complete:  Trigger to invoke when the Worker has Failed to Complete
        :type failed_to_complete: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._started = None
        self._completed_with_results = None
        self._completed_no_results = None
        self._failed_to_start = None
        self._failed_to_complete = None
        self.discriminator = None

        self.started = started
        self.completed_with_results = completed_with_results
        self.completed_no_results = completed_no_results
        self.failed_to_start = failed_to_start
        self.failed_to_complete = failed_to_complete

    @property
    def started(self):
        """Gets the started of this WorkerStatusTriggers.  # noqa: E501

        Trigger to invoke when the Worker has Started  # noqa: E501

        :return: The started of this WorkerStatusTriggers.  # noqa: E501
        :rtype: str
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this WorkerStatusTriggers.

        Trigger to invoke when the Worker has Started  # noqa: E501

        :param started: The started of this WorkerStatusTriggers.  # noqa: E501
        :type started: str
        """

        self._started = started

    @property
    def completed_with_results(self):
        """Gets the completed_with_results of this WorkerStatusTriggers.  # noqa: E501

        Trigger to invoke when the Worker has Completed (with results)  # noqa: E501

        :return: The completed_with_results of this WorkerStatusTriggers.  # noqa: E501
        :rtype: str
        """
        return self._completed_with_results

    @completed_with_results.setter
    def completed_with_results(self, completed_with_results):
        """Sets the completed_with_results of this WorkerStatusTriggers.

        Trigger to invoke when the Worker has Completed (with results)  # noqa: E501

        :param completed_with_results: The completed_with_results of this WorkerStatusTriggers.  # noqa: E501
        :type completed_with_results: str
        """

        self._completed_with_results = completed_with_results

    @property
    def completed_no_results(self):
        """Gets the completed_no_results of this WorkerStatusTriggers.  # noqa: E501

        Trigger to invoke when the Worker has Completed (no results)  # noqa: E501

        :return: The completed_no_results of this WorkerStatusTriggers.  # noqa: E501
        :rtype: str
        """
        return self._completed_no_results

    @completed_no_results.setter
    def completed_no_results(self, completed_no_results):
        """Sets the completed_no_results of this WorkerStatusTriggers.

        Trigger to invoke when the Worker has Completed (no results)  # noqa: E501

        :param completed_no_results: The completed_no_results of this WorkerStatusTriggers.  # noqa: E501
        :type completed_no_results: str
        """

        self._completed_no_results = completed_no_results

    @property
    def failed_to_start(self):
        """Gets the failed_to_start of this WorkerStatusTriggers.  # noqa: E501

        Trigger to invoke when the Worker has Failed to Start  # noqa: E501

        :return: The failed_to_start of this WorkerStatusTriggers.  # noqa: E501
        :rtype: str
        """
        return self._failed_to_start

    @failed_to_start.setter
    def failed_to_start(self, failed_to_start):
        """Sets the failed_to_start of this WorkerStatusTriggers.

        Trigger to invoke when the Worker has Failed to Start  # noqa: E501

        :param failed_to_start: The failed_to_start of this WorkerStatusTriggers.  # noqa: E501
        :type failed_to_start: str
        """

        self._failed_to_start = failed_to_start

    @property
    def failed_to_complete(self):
        """Gets the failed_to_complete of this WorkerStatusTriggers.  # noqa: E501

        Trigger to invoke when the Worker has Failed to Complete  # noqa: E501

        :return: The failed_to_complete of this WorkerStatusTriggers.  # noqa: E501
        :rtype: str
        """
        return self._failed_to_complete

    @failed_to_complete.setter
    def failed_to_complete(self, failed_to_complete):
        """Sets the failed_to_complete of this WorkerStatusTriggers.

        Trigger to invoke when the Worker has Failed to Complete  # noqa: E501

        :param failed_to_complete: The failed_to_complete of this WorkerStatusTriggers.  # noqa: E501
        :type failed_to_complete: str
        """

        self._failed_to_complete = failed_to_complete

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
        if not isinstance(other, WorkerStatusTriggers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerStatusTriggers):
            return True

        return self.to_dict() != other.to_dict()
