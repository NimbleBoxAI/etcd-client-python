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


class EtcdserverpbRangeResponse(object):
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
        'count': 'str',
        'header': 'EtcdserverpbResponseHeader',
        'kvs': 'list[MvccpbKeyValue]',
        'more': 'bool'
    }

    attribute_map = {
        'count': 'count',
        'header': 'header',
        'kvs': 'kvs',
        'more': 'more'
    }

    def __init__(self, count=None, header=None, kvs=None, more=None, _configuration=None):  # noqa: E501
        """EtcdserverpbRangeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._header = None
        self._kvs = None
        self._more = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if header is not None:
            self.header = header
        if kvs is not None:
            self.kvs = kvs
        if more is not None:
            self.more = more

    @property
    def count(self):
        """Gets the count of this EtcdserverpbRangeResponse.  # noqa: E501

        count is set to the number of keys within the range when requested.  # noqa: E501

        :return: The count of this EtcdserverpbRangeResponse.  # noqa: E501
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EtcdserverpbRangeResponse.

        count is set to the number of keys within the range when requested.  # noqa: E501

        :param count: The count of this EtcdserverpbRangeResponse.  # noqa: E501
        :type: str
        """

        self._count = count

    @property
    def header(self):
        """Gets the header of this EtcdserverpbRangeResponse.  # noqa: E501


        :return: The header of this EtcdserverpbRangeResponse.  # noqa: E501
        :rtype: EtcdserverpbResponseHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this EtcdserverpbRangeResponse.


        :param header: The header of this EtcdserverpbRangeResponse.  # noqa: E501
        :type: EtcdserverpbResponseHeader
        """

        self._header = header

    @property
    def kvs(self):
        """Gets the kvs of this EtcdserverpbRangeResponse.  # noqa: E501

        kvs is the list of key-value pairs matched by the range request. kvs is empty when count is requested.  # noqa: E501

        :return: The kvs of this EtcdserverpbRangeResponse.  # noqa: E501
        :rtype: list[MvccpbKeyValue]
        """
        return self._kvs

    @kvs.setter
    def kvs(self, kvs):
        """Sets the kvs of this EtcdserverpbRangeResponse.

        kvs is the list of key-value pairs matched by the range request. kvs is empty when count is requested.  # noqa: E501

        :param kvs: The kvs of this EtcdserverpbRangeResponse.  # noqa: E501
        :type: list[MvccpbKeyValue]
        """

        self._kvs = kvs

    @property
    def more(self):
        """Gets the more of this EtcdserverpbRangeResponse.  # noqa: E501

        more indicates if there are more keys to return in the requested range.  # noqa: E501

        :return: The more of this EtcdserverpbRangeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._more

    @more.setter
    def more(self, more):
        """Sets the more of this EtcdserverpbRangeResponse.

        more indicates if there are more keys to return in the requested range.  # noqa: E501

        :param more: The more of this EtcdserverpbRangeResponse.  # noqa: E501
        :type: bool
        """

        self._more = more

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
        if issubclass(EtcdserverpbRangeResponse, dict):
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
        if not isinstance(other, EtcdserverpbRangeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EtcdserverpbRangeResponse):
            return True

        return self.to_dict() != other.to_dict()