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


class EtcdserverpbMemberListResponse(object):
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
        'members': 'list[EtcdserverpbMember]'
    }

    attribute_map = {
        'header': 'header',
        'members': 'members'
    }

    def __init__(self, header=None, members=None, _configuration=None):  # noqa: E501
        """EtcdserverpbMemberListResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._header = None
        self._members = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if members is not None:
            self.members = members

    @property
    def header(self):
        """Gets the header of this EtcdserverpbMemberListResponse.  # noqa: E501


        :return: The header of this EtcdserverpbMemberListResponse.  # noqa: E501
        :rtype: EtcdserverpbResponseHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this EtcdserverpbMemberListResponse.


        :param header: The header of this EtcdserverpbMemberListResponse.  # noqa: E501
        :type: EtcdserverpbResponseHeader
        """

        self._header = header

    @property
    def members(self):
        """Gets the members of this EtcdserverpbMemberListResponse.  # noqa: E501

        members is a list of all members associated with the cluster.  # noqa: E501

        :return: The members of this EtcdserverpbMemberListResponse.  # noqa: E501
        :rtype: list[EtcdserverpbMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this EtcdserverpbMemberListResponse.

        members is a list of all members associated with the cluster.  # noqa: E501

        :param members: The members of this EtcdserverpbMemberListResponse.  # noqa: E501
        :type: list[EtcdserverpbMember]
        """

        self._members = members

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
        if issubclass(EtcdserverpbMemberListResponse, dict):
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
        if not isinstance(other, EtcdserverpbMemberListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EtcdserverpbMemberListResponse):
            return True

        return self.to_dict() != other.to_dict()
