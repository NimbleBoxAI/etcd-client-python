# etcd_client.AuthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_auth_disable**](AuthApi.md#auth_auth_disable) | **POST** /v3/auth/disable | AuthDisable disables authentication.
[**auth_auth_enable**](AuthApi.md#auth_auth_enable) | **POST** /v3/auth/enable | AuthEnable enables authentication.
[**auth_auth_status**](AuthApi.md#auth_auth_status) | **POST** /v3/auth/status | AuthStatus displays authentication status.
[**auth_authenticate**](AuthApi.md#auth_authenticate) | **POST** /v3/auth/authenticate | Authenticate processes an authenticate request.
[**auth_role_add**](AuthApi.md#auth_role_add) | **POST** /v3/auth/role/add | RoleAdd adds a new role. Role name cannot be empty.
[**auth_role_delete**](AuthApi.md#auth_role_delete) | **POST** /v3/auth/role/delete | RoleDelete deletes a specified role.
[**auth_role_get**](AuthApi.md#auth_role_get) | **POST** /v3/auth/role/get | RoleGet gets detailed role information.
[**auth_role_grant_permission**](AuthApi.md#auth_role_grant_permission) | **POST** /v3/auth/role/grant | RoleGrantPermission grants a permission of a specified key or range to a specified role.
[**auth_role_list**](AuthApi.md#auth_role_list) | **POST** /v3/auth/role/list | RoleList gets lists of all roles.
[**auth_role_revoke_permission**](AuthApi.md#auth_role_revoke_permission) | **POST** /v3/auth/role/revoke | RoleRevokePermission revokes a key or range permission of a specified role.
[**auth_user_add**](AuthApi.md#auth_user_add) | **POST** /v3/auth/user/add | UserAdd adds a new user. User name cannot be empty.
[**auth_user_change_password**](AuthApi.md#auth_user_change_password) | **POST** /v3/auth/user/changepw | UserChangePassword changes the password of a specified user.
[**auth_user_delete**](AuthApi.md#auth_user_delete) | **POST** /v3/auth/user/delete | UserDelete deletes a specified user.
[**auth_user_get**](AuthApi.md#auth_user_get) | **POST** /v3/auth/user/get | UserGet gets detailed user information.
[**auth_user_grant_role**](AuthApi.md#auth_user_grant_role) | **POST** /v3/auth/user/grant | UserGrant grants a role to a specified user.
[**auth_user_list**](AuthApi.md#auth_user_list) | **POST** /v3/auth/user/list | UserList gets a list of all users.
[**auth_user_revoke_role**](AuthApi.md#auth_user_revoke_role) | **POST** /v3/auth/user/revoke | UserRevokeRole revokes a role of specified user.


# **auth_auth_disable**
> EtcdserverpbAuthDisableResponse auth_auth_disable(body)

AuthDisable disables authentication.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthDisableRequest() # EtcdserverpbAuthDisableRequest | 

try:
    # AuthDisable disables authentication.
    api_response = api_instance.auth_auth_disable(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_auth_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthDisableRequest**](EtcdserverpbAuthDisableRequest.md)|  | 

### Return type

[**EtcdserverpbAuthDisableResponse**](EtcdserverpbAuthDisableResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_auth_enable**
> EtcdserverpbAuthEnableResponse auth_auth_enable(body)

AuthEnable enables authentication.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthEnableRequest() # EtcdserverpbAuthEnableRequest | 

try:
    # AuthEnable enables authentication.
    api_response = api_instance.auth_auth_enable(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_auth_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthEnableRequest**](EtcdserverpbAuthEnableRequest.md)|  | 

### Return type

[**EtcdserverpbAuthEnableResponse**](EtcdserverpbAuthEnableResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_auth_status**
> EtcdserverpbAuthStatusResponse auth_auth_status(body)

AuthStatus displays authentication status.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthStatusRequest() # EtcdserverpbAuthStatusRequest | 

try:
    # AuthStatus displays authentication status.
    api_response = api_instance.auth_auth_status(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_auth_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthStatusRequest**](EtcdserverpbAuthStatusRequest.md)|  | 

### Return type

[**EtcdserverpbAuthStatusResponse**](EtcdserverpbAuthStatusResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_authenticate**
> EtcdserverpbAuthenticateResponse auth_authenticate(body)

Authenticate processes an authenticate request.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthenticateRequest() # EtcdserverpbAuthenticateRequest | 

try:
    # Authenticate processes an authenticate request.
    api_response = api_instance.auth_authenticate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthenticateRequest**](EtcdserverpbAuthenticateRequest.md)|  | 

### Return type

[**EtcdserverpbAuthenticateResponse**](EtcdserverpbAuthenticateResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_role_add**
> EtcdserverpbAuthRoleAddResponse auth_role_add(body)

RoleAdd adds a new role. Role name cannot be empty.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthRoleAddRequest() # EtcdserverpbAuthRoleAddRequest | 

try:
    # RoleAdd adds a new role. Role name cannot be empty.
    api_response = api_instance.auth_role_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_role_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthRoleAddRequest**](EtcdserverpbAuthRoleAddRequest.md)|  | 

### Return type

[**EtcdserverpbAuthRoleAddResponse**](EtcdserverpbAuthRoleAddResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_role_delete**
> EtcdserverpbAuthRoleDeleteResponse auth_role_delete(body)

RoleDelete deletes a specified role.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthRoleDeleteRequest() # EtcdserverpbAuthRoleDeleteRequest | 

try:
    # RoleDelete deletes a specified role.
    api_response = api_instance.auth_role_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthRoleDeleteRequest**](EtcdserverpbAuthRoleDeleteRequest.md)|  | 

### Return type

[**EtcdserverpbAuthRoleDeleteResponse**](EtcdserverpbAuthRoleDeleteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_role_get**
> EtcdserverpbAuthRoleGetResponse auth_role_get(body)

RoleGet gets detailed role information.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthRoleGetRequest() # EtcdserverpbAuthRoleGetRequest | 

try:
    # RoleGet gets detailed role information.
    api_response = api_instance.auth_role_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_role_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthRoleGetRequest**](EtcdserverpbAuthRoleGetRequest.md)|  | 

### Return type

[**EtcdserverpbAuthRoleGetResponse**](EtcdserverpbAuthRoleGetResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_role_grant_permission**
> EtcdserverpbAuthRoleGrantPermissionResponse auth_role_grant_permission(body)

RoleGrantPermission grants a permission of a specified key or range to a specified role.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthRoleGrantPermissionRequest() # EtcdserverpbAuthRoleGrantPermissionRequest | 

try:
    # RoleGrantPermission grants a permission of a specified key or range to a specified role.
    api_response = api_instance.auth_role_grant_permission(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_role_grant_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthRoleGrantPermissionRequest**](EtcdserverpbAuthRoleGrantPermissionRequest.md)|  | 

### Return type

[**EtcdserverpbAuthRoleGrantPermissionResponse**](EtcdserverpbAuthRoleGrantPermissionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_role_list**
> EtcdserverpbAuthRoleListResponse auth_role_list(body)

RoleList gets lists of all roles.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthRoleListRequest() # EtcdserverpbAuthRoleListRequest | 

try:
    # RoleList gets lists of all roles.
    api_response = api_instance.auth_role_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthRoleListRequest**](EtcdserverpbAuthRoleListRequest.md)|  | 

### Return type

[**EtcdserverpbAuthRoleListResponse**](EtcdserverpbAuthRoleListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_role_revoke_permission**
> EtcdserverpbAuthRoleRevokePermissionResponse auth_role_revoke_permission(body)

RoleRevokePermission revokes a key or range permission of a specified role.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthRoleRevokePermissionRequest() # EtcdserverpbAuthRoleRevokePermissionRequest | 

try:
    # RoleRevokePermission revokes a key or range permission of a specified role.
    api_response = api_instance.auth_role_revoke_permission(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_role_revoke_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthRoleRevokePermissionRequest**](EtcdserverpbAuthRoleRevokePermissionRequest.md)|  | 

### Return type

[**EtcdserverpbAuthRoleRevokePermissionResponse**](EtcdserverpbAuthRoleRevokePermissionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_add**
> EtcdserverpbAuthUserAddResponse auth_user_add(body)

UserAdd adds a new user. User name cannot be empty.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthUserAddRequest() # EtcdserverpbAuthUserAddRequest | 

try:
    # UserAdd adds a new user. User name cannot be empty.
    api_response = api_instance.auth_user_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthUserAddRequest**](EtcdserverpbAuthUserAddRequest.md)|  | 

### Return type

[**EtcdserverpbAuthUserAddResponse**](EtcdserverpbAuthUserAddResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_change_password**
> EtcdserverpbAuthUserChangePasswordResponse auth_user_change_password(body)

UserChangePassword changes the password of a specified user.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthUserChangePasswordRequest() # EtcdserverpbAuthUserChangePasswordRequest | 

try:
    # UserChangePassword changes the password of a specified user.
    api_response = api_instance.auth_user_change_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthUserChangePasswordRequest**](EtcdserverpbAuthUserChangePasswordRequest.md)|  | 

### Return type

[**EtcdserverpbAuthUserChangePasswordResponse**](EtcdserverpbAuthUserChangePasswordResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_delete**
> EtcdserverpbAuthUserDeleteResponse auth_user_delete(body)

UserDelete deletes a specified user.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthUserDeleteRequest() # EtcdserverpbAuthUserDeleteRequest | 

try:
    # UserDelete deletes a specified user.
    api_response = api_instance.auth_user_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthUserDeleteRequest**](EtcdserverpbAuthUserDeleteRequest.md)|  | 

### Return type

[**EtcdserverpbAuthUserDeleteResponse**](EtcdserverpbAuthUserDeleteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_get**
> EtcdserverpbAuthUserGetResponse auth_user_get(body)

UserGet gets detailed user information.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthUserGetRequest() # EtcdserverpbAuthUserGetRequest | 

try:
    # UserGet gets detailed user information.
    api_response = api_instance.auth_user_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthUserGetRequest**](EtcdserverpbAuthUserGetRequest.md)|  | 

### Return type

[**EtcdserverpbAuthUserGetResponse**](EtcdserverpbAuthUserGetResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_grant_role**
> EtcdserverpbAuthUserGrantRoleResponse auth_user_grant_role(body)

UserGrant grants a role to a specified user.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthUserGrantRoleRequest() # EtcdserverpbAuthUserGrantRoleRequest | 

try:
    # UserGrant grants a role to a specified user.
    api_response = api_instance.auth_user_grant_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_grant_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthUserGrantRoleRequest**](EtcdserverpbAuthUserGrantRoleRequest.md)|  | 

### Return type

[**EtcdserverpbAuthUserGrantRoleResponse**](EtcdserverpbAuthUserGrantRoleResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_list**
> EtcdserverpbAuthUserListResponse auth_user_list(body)

UserList gets a list of all users.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthUserListRequest() # EtcdserverpbAuthUserListRequest | 

try:
    # UserList gets a list of all users.
    api_response = api_instance.auth_user_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthUserListRequest**](EtcdserverpbAuthUserListRequest.md)|  | 

### Return type

[**EtcdserverpbAuthUserListResponse**](EtcdserverpbAuthUserListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_revoke_role**
> EtcdserverpbAuthUserRevokeRoleResponse auth_user_revoke_role(body)

UserRevokeRole revokes a role of specified user.

### Example
```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthUserRevokeRoleRequest() # EtcdserverpbAuthUserRevokeRoleRequest | 

try:
    # UserRevokeRole revokes a role of specified user.
    api_response = api_instance.auth_user_revoke_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_user_revoke_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAuthUserRevokeRoleRequest**](EtcdserverpbAuthUserRevokeRoleRequest.md)|  | 

### Return type

[**EtcdserverpbAuthUserRevokeRoleResponse**](EtcdserverpbAuthUserRevokeRoleResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

