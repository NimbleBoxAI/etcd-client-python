# etcd_client.MaintenanceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maintenance_alarm**](MaintenanceApi.md#maintenance_alarm) | **POST** /v3/maintenance/alarm | Alarm activates, deactivates, and queries alarms regarding cluster health.
[**maintenance_defragment**](MaintenanceApi.md#maintenance_defragment) | **POST** /v3/maintenance/defragment | Defragment defragments a member&#39;s backend database to recover storage space.
[**maintenance_downgrade**](MaintenanceApi.md#maintenance_downgrade) | **POST** /v3/maintenance/downgrade | Downgrade requests downgrades, verifies feasibility or cancels downgrade on the cluster version. Supported since etcd 3.5.
[**maintenance_hash_kv**](MaintenanceApi.md#maintenance_hash_kv) | **POST** /v3/maintenance/hash | HashKV computes the hash of all MVCC keys up to a given revision. It only iterates \&quot;key\&quot; bucket in backend storage.
[**maintenance_move_leader**](MaintenanceApi.md#maintenance_move_leader) | **POST** /v3/maintenance/transfer-leadership | MoveLeader requests current leader node to transfer its leadership to transferee.
[**maintenance_snapshot**](MaintenanceApi.md#maintenance_snapshot) | **POST** /v3/maintenance/snapshot | Snapshot sends a snapshot of the entire backend from a member over a stream to a client.
[**maintenance_status**](MaintenanceApi.md#maintenance_status) | **POST** /v3/maintenance/status | Status gets the status of the member.


# **maintenance_alarm**
> EtcdserverpbAlarmResponse maintenance_alarm(body)

Alarm activates, deactivates, and queries alarms regarding cluster health.

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
api_instance = etcd_client.MaintenanceApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAlarmRequest() # EtcdserverpbAlarmRequest | 

try:
    # Alarm activates, deactivates, and queries alarms regarding cluster health.
    api_response = api_instance.maintenance_alarm(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_alarm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbAlarmRequest**](EtcdserverpbAlarmRequest.md)|  | 

### Return type

[**EtcdserverpbAlarmResponse**](EtcdserverpbAlarmResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_defragment**
> EtcdserverpbDefragmentResponse maintenance_defragment(body)

Defragment defragments a member's backend database to recover storage space.

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
api_instance = etcd_client.MaintenanceApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbDefragmentRequest() # EtcdserverpbDefragmentRequest | 

try:
    # Defragment defragments a member's backend database to recover storage space.
    api_response = api_instance.maintenance_defragment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_defragment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbDefragmentRequest**](EtcdserverpbDefragmentRequest.md)|  | 

### Return type

[**EtcdserverpbDefragmentResponse**](EtcdserverpbDefragmentResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_downgrade**
> EtcdserverpbDowngradeResponse maintenance_downgrade(body)

Downgrade requests downgrades, verifies feasibility or cancels downgrade on the cluster version. Supported since etcd 3.5.

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
api_instance = etcd_client.MaintenanceApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbDowngradeRequest() # EtcdserverpbDowngradeRequest | 

try:
    # Downgrade requests downgrades, verifies feasibility or cancels downgrade on the cluster version. Supported since etcd 3.5.
    api_response = api_instance.maintenance_downgrade(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_downgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbDowngradeRequest**](EtcdserverpbDowngradeRequest.md)|  | 

### Return type

[**EtcdserverpbDowngradeResponse**](EtcdserverpbDowngradeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_hash_kv**
> EtcdserverpbHashKVResponse maintenance_hash_kv(body)

HashKV computes the hash of all MVCC keys up to a given revision. It only iterates \"key\" bucket in backend storage.

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
api_instance = etcd_client.MaintenanceApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbHashKVRequest() # EtcdserverpbHashKVRequest | 

try:
    # HashKV computes the hash of all MVCC keys up to a given revision. It only iterates \"key\" bucket in backend storage.
    api_response = api_instance.maintenance_hash_kv(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_hash_kv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbHashKVRequest**](EtcdserverpbHashKVRequest.md)|  | 

### Return type

[**EtcdserverpbHashKVResponse**](EtcdserverpbHashKVResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_move_leader**
> EtcdserverpbMoveLeaderResponse maintenance_move_leader(body)

MoveLeader requests current leader node to transfer its leadership to transferee.

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
api_instance = etcd_client.MaintenanceApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbMoveLeaderRequest() # EtcdserverpbMoveLeaderRequest | 

try:
    # MoveLeader requests current leader node to transfer its leadership to transferee.
    api_response = api_instance.maintenance_move_leader(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_move_leader: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbMoveLeaderRequest**](EtcdserverpbMoveLeaderRequest.md)|  | 

### Return type

[**EtcdserverpbMoveLeaderResponse**](EtcdserverpbMoveLeaderResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_snapshot**
> StreamResultOfEtcdserverpbSnapshotResponse maintenance_snapshot(body)

Snapshot sends a snapshot of the entire backend from a member over a stream to a client.

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
api_instance = etcd_client.MaintenanceApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbSnapshotRequest() # EtcdserverpbSnapshotRequest | 

try:
    # Snapshot sends a snapshot of the entire backend from a member over a stream to a client.
    api_response = api_instance.maintenance_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbSnapshotRequest**](EtcdserverpbSnapshotRequest.md)|  | 

### Return type

[**StreamResultOfEtcdserverpbSnapshotResponse**](StreamResultOfEtcdserverpbSnapshotResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_status**
> EtcdserverpbStatusResponse maintenance_status(body)

Status gets the status of the member.

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
api_instance = etcd_client.MaintenanceApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbStatusRequest() # EtcdserverpbStatusRequest | 

try:
    # Status gets the status of the member.
    api_response = api_instance.maintenance_status(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbStatusRequest**](EtcdserverpbStatusRequest.md)|  | 

### Return type

[**EtcdserverpbStatusResponse**](EtcdserverpbStatusResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

