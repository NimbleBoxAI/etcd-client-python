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


class EtcdserverpbAuthUserGrantRoleRequest(object):
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
        'role': 'str',
        'user': 'str'
    }

    attribute_map = {
        'role': 'role',
        'user': 'user'
    }

    def __init__(self, role=None, user=None, _configuration=None):  # noqa: E501
        """EtcdserverpbAuthUserGrantRoleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._role = None
        self._user = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if user is not None:
            self.user = user

    @property
    def role(self):
        """Gets the role of this EtcdserverpbAuthUserGrantRoleRequest.  # noqa: E501

        role is the name of the role to grant to the user.  # noqa: E501

        :return: The role of this EtcdserverpbAuthUserGrantRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this EtcdserverpbAuthUserGrantRoleRequest.

        role is the name of the role to grant to the user.  # noqa: E501

        :param role: The role of this EtcdserverpbAuthUserGrantRoleRequest.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def user(self):
        """Gets the user of this EtcdserverpbAuthUserGrantRoleRequest.  # noqa: E501

        user is the name of the user which should be granted a given role.  # noqa: E501

        :return: The user of this EtcdserverpbAuthUserGrantRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this EtcdserverpbAuthUserGrantRoleRequest.

        user is the name of the user which should be granted a given role.  # noqa: E501

        :param user: The user of this EtcdserverpbAuthUserGrantRoleRequest.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(EtcdserverpbAuthUserGrantRoleRequest, dict):
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
        if not isinstance(other, EtcdserverpbAuthUserGrantRoleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EtcdserverpbAuthUserGrantRoleRequest):
            return True

        return self.to_dict() != other.to_dict()
