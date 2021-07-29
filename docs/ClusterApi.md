# etcd_client.ClusterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_member_add**](ClusterApi.md#cluster_member_add) | **POST** /v3/cluster/member/add | MemberAdd adds a member into the cluster.
[**cluster_member_list**](ClusterApi.md#cluster_member_list) | **POST** /v3/cluster/member/list | MemberList lists all the members in the cluster.
[**cluster_member_promote**](ClusterApi.md#cluster_member_promote) | **POST** /v3/cluster/member/promote | MemberPromote promotes a member from raft learner (non-voting) to raft voting member.
[**cluster_member_remove**](ClusterApi.md#cluster_member_remove) | **POST** /v3/cluster/member/remove | MemberRemove removes an existing member from the cluster.
[**cluster_member_update**](ClusterApi.md#cluster_member_update) | **POST** /v3/cluster/member/update | MemberUpdate updates the member configuration.


# **cluster_member_add**
> EtcdserverpbMemberAddResponse cluster_member_add(body)

MemberAdd adds a member into the cluster.

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
api_instance = etcd_client.ClusterApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbMemberAddRequest() # EtcdserverpbMemberAddRequest | 

try:
    # MemberAdd adds a member into the cluster.
    api_response = api_instance.cluster_member_add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_member_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbMemberAddRequest**](EtcdserverpbMemberAddRequest.md)|  | 

### Return type

[**EtcdserverpbMemberAddResponse**](EtcdserverpbMemberAddResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_member_list**
> EtcdserverpbMemberListResponse cluster_member_list(body)

MemberList lists all the members in the cluster.

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
api_instance = etcd_client.ClusterApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbMemberListRequest() # EtcdserverpbMemberListRequest | 

try:
    # MemberList lists all the members in the cluster.
    api_response = api_instance.cluster_member_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_member_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbMemberListRequest**](EtcdserverpbMemberListRequest.md)|  | 

### Return type

[**EtcdserverpbMemberListResponse**](EtcdserverpbMemberListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_member_promote**
> EtcdserverpbMemberPromoteResponse cluster_member_promote(body)

MemberPromote promotes a member from raft learner (non-voting) to raft voting member.

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
api_instance = etcd_client.ClusterApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbMemberPromoteRequest() # EtcdserverpbMemberPromoteRequest | 

try:
    # MemberPromote promotes a member from raft learner (non-voting) to raft voting member.
    api_response = api_instance.cluster_member_promote(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_member_promote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbMemberPromoteRequest**](EtcdserverpbMemberPromoteRequest.md)|  | 

### Return type

[**EtcdserverpbMemberPromoteResponse**](EtcdserverpbMemberPromoteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_member_remove**
> EtcdserverpbMemberRemoveResponse cluster_member_remove(body)

MemberRemove removes an existing member from the cluster.

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
api_instance = etcd_client.ClusterApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbMemberRemoveRequest() # EtcdserverpbMemberRemoveRequest | 

try:
    # MemberRemove removes an existing member from the cluster.
    api_response = api_instance.cluster_member_remove(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_member_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbMemberRemoveRequest**](EtcdserverpbMemberRemoveRequest.md)|  | 

### Return type

[**EtcdserverpbMemberRemoveResponse**](EtcdserverpbMemberRemoveResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_member_update**
> EtcdserverpbMemberUpdateResponse cluster_member_update(body)

MemberUpdate updates the member configuration.

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
api_instance = etcd_client.ClusterApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbMemberUpdateRequest() # EtcdserverpbMemberUpdateRequest | 

try:
    # MemberUpdate updates the member configuration.
    api_response = api_instance.cluster_member_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_member_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbMemberUpdateRequest**](EtcdserverpbMemberUpdateRequest.md)|  | 

### Return type

[**EtcdserverpbMemberUpdateResponse**](EtcdserverpbMemberUpdateResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

