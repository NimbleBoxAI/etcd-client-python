# coding: utf-8

"""
    api/etcdserverpb/rpc.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import etcd_client
from etcd_client.api.auth_api import AuthApi  # noqa: E501
from etcd_client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = etcd_client.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_auth_disable(self):
        """Test case for auth_auth_disable

        AuthDisable disables authentication.  # noqa: E501
        """
        pass

    def test_auth_auth_enable(self):
        """Test case for auth_auth_enable

        AuthEnable enables authentication.  # noqa: E501
        """
        pass

    def test_auth_auth_status(self):
        """Test case for auth_auth_status

        AuthStatus displays authentication status.  # noqa: E501
        """
        pass

    def test_auth_authenticate(self):
        """Test case for auth_authenticate

        Authenticate processes an authenticate request.  # noqa: E501
        """
        pass

    def test_auth_role_add(self):
        """Test case for auth_role_add

        RoleAdd adds a new role. Role name cannot be empty.  # noqa: E501
        """
        pass

    def test_auth_role_delete(self):
        """Test case for auth_role_delete

        RoleDelete deletes a specified role.  # noqa: E501
        """
        pass

    def test_auth_role_get(self):
        """Test case for auth_role_get

        RoleGet gets detailed role information.  # noqa: E501
        """
        pass

    def test_auth_role_grant_permission(self):
        """Test case for auth_role_grant_permission

        RoleGrantPermission grants a permission of a specified key or range to a specified role.  # noqa: E501
        """
        pass

    def test_auth_role_list(self):
        """Test case for auth_role_list

        RoleList gets lists of all roles.  # noqa: E501
        """
        pass

    def test_auth_role_revoke_permission(self):
        """Test case for auth_role_revoke_permission

        RoleRevokePermission revokes a key or range permission of a specified role.  # noqa: E501
        """
        pass

    def test_auth_user_add(self):
        """Test case for auth_user_add

        UserAdd adds a new user. User name cannot be empty.  # noqa: E501
        """
        pass

    def test_auth_user_change_password(self):
        """Test case for auth_user_change_password

        UserChangePassword changes the password of a specified user.  # noqa: E501
        """
        pass

    def test_auth_user_delete(self):
        """Test case for auth_user_delete

        UserDelete deletes a specified user.  # noqa: E501
        """
        pass

    def test_auth_user_get(self):
        """Test case for auth_user_get

        UserGet gets detailed user information.  # noqa: E501
        """
        pass

    def test_auth_user_grant_role(self):
        """Test case for auth_user_grant_role

        UserGrant grants a role to a specified user.  # noqa: E501
        """
        pass

    def test_auth_user_list(self):
        """Test case for auth_user_list

        UserList gets a list of all users.  # noqa: E501
        """
        pass

    def test_auth_user_revoke_role(self):
        """Test case for auth_user_revoke_role

        UserRevokeRole revokes a role of specified user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
