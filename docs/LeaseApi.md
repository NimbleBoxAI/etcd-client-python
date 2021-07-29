# etcd_client.LeaseApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lease_lease_grant**](LeaseApi.md#lease_lease_grant) | **POST** /v3/lease/grant | LeaseGrant creates a lease which expires if the server does not receive a keepAlive within a given time to live period. All keys attached to the lease will be expired and deleted if the lease expires. Each expired key generates a delete event in the event history.
[**lease_lease_keep_alive**](LeaseApi.md#lease_lease_keep_alive) | **POST** /v3/lease/keepalive | LeaseKeepAlive keeps the lease alive by streaming keep alive requests from the client to the server and streaming keep alive responses from the server to the client.
[**lease_lease_leases**](LeaseApi.md#lease_lease_leases) | **POST** /v3/lease/leases | LeaseLeases lists all existing leases.
[**lease_lease_leases2**](LeaseApi.md#lease_lease_leases2) | **POST** /v3/kv/lease/leases | LeaseLeases lists all existing leases.
[**lease_lease_revoke**](LeaseApi.md#lease_lease_revoke) | **POST** /v3/lease/revoke | LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.
[**lease_lease_revoke2**](LeaseApi.md#lease_lease_revoke2) | **POST** /v3/kv/lease/revoke | LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.
[**lease_lease_time_to_live**](LeaseApi.md#lease_lease_time_to_live) | **POST** /v3/lease/timetolive | LeaseTimeToLive retrieves lease information.
[**lease_lease_time_to_live2**](LeaseApi.md#lease_lease_time_to_live2) | **POST** /v3/kv/lease/timetolive | LeaseTimeToLive retrieves lease information.


# **lease_lease_grant**
> EtcdserverpbLeaseGrantResponse lease_lease_grant(body)

LeaseGrant creates a lease which expires if the server does not receive a keepAlive within a given time to live period. All keys attached to the lease will be expired and deleted if the lease expires. Each expired key generates a delete event in the event history.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseGrantRequest() # EtcdserverpbLeaseGrantRequest | 

try:
    # LeaseGrant creates a lease which expires if the server does not receive a keepAlive within a given time to live period. All keys attached to the lease will be expired and deleted if the lease expires. Each expired key generates a delete event in the event history.
    api_response = api_instance.lease_lease_grant(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseGrantRequest**](EtcdserverpbLeaseGrantRequest.md)|  | 

### Return type

[**EtcdserverpbLeaseGrantResponse**](EtcdserverpbLeaseGrantResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lease_lease_keep_alive**
> StreamResultOfEtcdserverpbLeaseKeepAliveResponse lease_lease_keep_alive(body)

LeaseKeepAlive keeps the lease alive by streaming keep alive requests from the client to the server and streaming keep alive responses from the server to the client.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseKeepAliveRequest() # EtcdserverpbLeaseKeepAliveRequest |  (streaming inputs)

try:
    # LeaseKeepAlive keeps the lease alive by streaming keep alive requests from the client to the server and streaming keep alive responses from the server to the client.
    api_response = api_instance.lease_lease_keep_alive(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_keep_alive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseKeepAliveRequest**](EtcdserverpbLeaseKeepAliveRequest.md)|  (streaming inputs) | 

### Return type

[**StreamResultOfEtcdserverpbLeaseKeepAliveResponse**](StreamResultOfEtcdserverpbLeaseKeepAliveResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lease_lease_leases**
> EtcdserverpbLeaseLeasesResponse lease_lease_leases(body)

LeaseLeases lists all existing leases.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseLeasesRequest() # EtcdserverpbLeaseLeasesRequest | 

try:
    # LeaseLeases lists all existing leases.
    api_response = api_instance.lease_lease_leases(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_leases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseLeasesRequest**](EtcdserverpbLeaseLeasesRequest.md)|  | 

### Return type

[**EtcdserverpbLeaseLeasesResponse**](EtcdserverpbLeaseLeasesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lease_lease_leases2**
> EtcdserverpbLeaseLeasesResponse lease_lease_leases2(body)

LeaseLeases lists all existing leases.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseLeasesRequest() # EtcdserverpbLeaseLeasesRequest | 

try:
    # LeaseLeases lists all existing leases.
    api_response = api_instance.lease_lease_leases2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_leases2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseLeasesRequest**](EtcdserverpbLeaseLeasesRequest.md)|  | 

### Return type

[**EtcdserverpbLeaseLeasesResponse**](EtcdserverpbLeaseLeasesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lease_lease_revoke**
> EtcdserverpbLeaseRevokeResponse lease_lease_revoke(body)

LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseRevokeRequest() # EtcdserverpbLeaseRevokeRequest | 

try:
    # LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.
    api_response = api_instance.lease_lease_revoke(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseRevokeRequest**](EtcdserverpbLeaseRevokeRequest.md)|  | 

### Return type

[**EtcdserverpbLeaseRevokeResponse**](EtcdserverpbLeaseRevokeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lease_lease_revoke2**
> EtcdserverpbLeaseRevokeResponse lease_lease_revoke2(body)

LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseRevokeRequest() # EtcdserverpbLeaseRevokeRequest | 

try:
    # LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.
    api_response = api_instance.lease_lease_revoke2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_revoke2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseRevokeRequest**](EtcdserverpbLeaseRevokeRequest.md)|  | 

### Return type

[**EtcdserverpbLeaseRevokeResponse**](EtcdserverpbLeaseRevokeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lease_lease_time_to_live**
> EtcdserverpbLeaseTimeToLiveResponse lease_lease_time_to_live(body)

LeaseTimeToLive retrieves lease information.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseTimeToLiveRequest() # EtcdserverpbLeaseTimeToLiveRequest | 

try:
    # LeaseTimeToLive retrieves lease information.
    api_response = api_instance.lease_lease_time_to_live(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_time_to_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseTimeToLiveRequest**](EtcdserverpbLeaseTimeToLiveRequest.md)|  | 

### Return type

[**EtcdserverpbLeaseTimeToLiveResponse**](EtcdserverpbLeaseTimeToLiveResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lease_lease_time_to_live2**
> EtcdserverpbLeaseTimeToLiveResponse lease_lease_time_to_live2(body)

LeaseTimeToLive retrieves lease information.

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
api_instance = etcd_client.LeaseApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbLeaseTimeToLiveRequest() # EtcdserverpbLeaseTimeToLiveRequest | 

try:
    # LeaseTimeToLive retrieves lease information.
    api_response = api_instance.lease_lease_time_to_live2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseApi->lease_lease_time_to_live2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbLeaseTimeToLiveRequest**](EtcdserverpbLeaseTimeToLiveRequest.md)|  | 

### Return type

[**EtcdserverpbLeaseTimeToLiveResponse**](EtcdserverpbLeaseTimeToLiveResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

