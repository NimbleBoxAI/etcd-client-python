# coding: utf-8

"""
    api/etcdserverpb/rpc.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from etcd_client.configuration import Configuration


class EtcdserverpbTxnRequest(object):
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
        'compare': 'list[EtcdserverpbCompare]',
        'failure': 'list[EtcdserverpbRequestOp]',
        'success': 'list[EtcdserverpbRequestOp]'
    }

    attribute_map = {
        'compare': 'compare',
        'failure': 'failure',
        'success': 'success'
    }

    def __init__(self, compare=None, failure=None, success=None, _configuration=None):  # noqa: E501
        """EtcdserverpbTxnRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compare = None
        self._failure = None
        self._success = None
        self.discriminator = None

        if compare is not None:
            self.compare = compare
        if failure is not None:
            self.failure = failure
        if success is not None:
            self.success = success

    @property
    def compare(self):
        """Gets the compare of this EtcdserverpbTxnRequest.  # noqa: E501

        compare is a list of predicates representing a conjunction of terms. If the comparisons succeed, then the success requests will be processed in order, and the response will contain their respective responses in order. If the comparisons fail, then the failure requests will be processed in order, and the response will contain their respective responses in order.  # noqa: E501

        :return: The compare of this EtcdserverpbTxnRequest.  # noqa: E501
        :rtype: list[EtcdserverpbCompare]
        """
        return self._compare

    @compare.setter
    def compare(self, compare):
        """Sets the compare of this EtcdserverpbTxnRequest.

        compare is a list of predicates representing a conjunction of terms. If the comparisons succeed, then the success requests will be processed in order, and the response will contain their respective responses in order. If the comparisons fail, then the failure requests will be processed in order, and the response will contain their respective responses in order.  # noqa: E501

        :param compare: The compare of this EtcdserverpbTxnRequest.  # noqa: E501
        :type: list[EtcdserverpbCompare]
        """

        self._compare = compare

    @property
    def failure(self):
        """Gets the failure of this EtcdserverpbTxnRequest.  # noqa: E501

        failure is a list of requests which will be applied when compare evaluates to false.  # noqa: E501

        :return: The failure of this EtcdserverpbTxnRequest.  # noqa: E501
        :rtype: list[EtcdserverpbRequestOp]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this EtcdserverpbTxnRequest.

        failure is a list of requests which will be applied when compare evaluates to false.  # noqa: E501

        :param failure: The failure of this EtcdserverpbTxnRequest.  # noqa: E501
        :type: list[EtcdserverpbRequestOp]
        """

        self._failure = failure

    @property
    def success(self):
        """Gets the success of this EtcdserverpbTxnRequest.  # noqa: E501

        success is a list of requests which will be applied when compare evaluates to true.  # noqa: E501

        :return: The success of this EtcdserverpbTxnRequest.  # noqa: E501
        :rtype: list[EtcdserverpbRequestOp]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EtcdserverpbTxnRequest.

        success is a list of requests which will be applied when compare evaluates to true.  # noqa: E501

        :param success: The success of this EtcdserverpbTxnRequest.  # noqa: E501
        :type: list[EtcdserverpbRequestOp]
        """

        self._success = success

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
        if issubclass(EtcdserverpbTxnRequest, dict):
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
        if not isinstance(other, EtcdserverpbTxnRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EtcdserverpbTxnRequest):
            return True

        return self.to_dict() != other.to_dict()