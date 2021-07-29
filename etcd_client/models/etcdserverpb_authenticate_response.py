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


class EtcdserverpbAuthenticateResponse(object):
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
        'header': 'EtcdserverpbResponseHeader',
        'token': 'str'
    }

    attribute_map = {
        'header': 'header',
        'token': 'token'
    }

    def __init__(self, header=None, token=None, _configuration=None):  # noqa: E501
        """EtcdserverpbAuthenticateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._header = None
        self._token = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if token is not None:
            self.token = token

    @property
    def header(self):
        """Gets the header of this EtcdserverpbAuthenticateResponse.  # noqa: E501


        :return: The header of this EtcdserverpbAuthenticateResponse.  # noqa: E501
        :rtype: EtcdserverpbResponseHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this EtcdserverpbAuthenticateResponse.


        :param header: The header of this EtcdserverpbAuthenticateResponse.  # noqa: E501
        :type: EtcdserverpbResponseHeader
        """

        self._header = header

    @property
    def token(self):
        """Gets the token of this EtcdserverpbAuthenticateResponse.  # noqa: E501


        :return: The token of this EtcdserverpbAuthenticateResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this EtcdserverpbAuthenticateResponse.


        :param token: The token of this EtcdserverpbAuthenticateResponse.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(EtcdserverpbAuthenticateResponse, dict):
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
        if not isinstance(other, EtcdserverpbAuthenticateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EtcdserverpbAuthenticateResponse):
            return True

        return self.to_dict() != other.to_dict()
