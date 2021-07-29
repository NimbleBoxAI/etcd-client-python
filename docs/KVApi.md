# etcd_client.KVApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**k_v_compact**](KVApi.md#k_v_compact) | **POST** /v3/kv/compaction | Compact compacts the event history in the etcd key-value store. The key-value store should be periodically compacted or the event history will continue to grow indefinitely.
[**k_v_delete_range**](KVApi.md#k_v_delete_range) | **POST** /v3/kv/deleterange | DeleteRange deletes the given range from the key-value store. A delete request increments the revision of the key-value store and generates a delete event in the event history for every deleted key.
[**k_v_put**](KVApi.md#k_v_put) | **POST** /v3/kv/put | Put puts the given key into the key-value store. A put request increments the revision of the key-value store and generates one event in the event history.
[**k_v_range**](KVApi.md#k_v_range) | **POST** /v3/kv/range | Range gets the keys in the range from the key-value store.
[**k_v_txn**](KVApi.md#k_v_txn) | **POST** /v3/kv/txn | Txn processes multiple requests in a single transaction. A txn request increments the revision of the key-value store and generates events with the same revision for every completed request. It is not allowed to modify the same key several times within one txn.


# **k_v_compact**
> EtcdserverpbCompactionResponse k_v_compact(body)

Compact compacts the event history in the etcd key-value store. The key-value store should be periodically compacted or the event history will continue to grow indefinitely.

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
api_instance = etcd_client.KVApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbCompactionRequest() # EtcdserverpbCompactionRequest | 

try:
    # Compact compacts the event history in the etcd key-value store. The key-value store should be periodically compacted or the event history will continue to grow indefinitely.
    api_response = api_instance.k_v_compact(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KVApi->k_v_compact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbCompactionRequest**](EtcdserverpbCompactionRequest.md)|  | 

### Return type

[**EtcdserverpbCompactionResponse**](EtcdserverpbCompactionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_v_delete_range**
> EtcdserverpbDeleteRangeResponse k_v_delete_range(body)

DeleteRange deletes the given range from the key-value store. A delete request increments the revision of the key-value store and generates a delete event in the event history for every deleted key.

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
api_instance = etcd_client.KVApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbDeleteRangeRequest() # EtcdserverpbDeleteRangeRequest | 

try:
    # DeleteRange deletes the given range from the key-value store. A delete request increments the revision of the key-value store and generates a delete event in the event history for every deleted key.
    api_response = api_instance.k_v_delete_range(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KVApi->k_v_delete_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbDeleteRangeRequest**](EtcdserverpbDeleteRangeRequest.md)|  | 

### Return type

[**EtcdserverpbDeleteRangeResponse**](EtcdserverpbDeleteRangeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_v_put**
> EtcdserverpbPutResponse k_v_put(body)

Put puts the given key into the key-value store. A put request increments the revision of the key-value store and generates one event in the event history.

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
api_instance = etcd_client.KVApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbPutRequest() # EtcdserverpbPutRequest | 

try:
    # Put puts the given key into the key-value store. A put request increments the revision of the key-value store and generates one event in the event history.
    api_response = api_instance.k_v_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KVApi->k_v_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbPutRequest**](EtcdserverpbPutRequest.md)|  | 

### Return type

[**EtcdserverpbPutResponse**](EtcdserverpbPutResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_v_range**
> EtcdserverpbRangeResponse k_v_range(body)

Range gets the keys in the range from the key-value store.

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
api_instance = etcd_client.KVApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbRangeRequest() # EtcdserverpbRangeRequest | 

try:
    # Range gets the keys in the range from the key-value store.
    api_response = api_instance.k_v_range(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KVApi->k_v_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbRangeRequest**](EtcdserverpbRangeRequest.md)|  | 

### Return type

[**EtcdserverpbRangeResponse**](EtcdserverpbRangeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_v_txn**
> EtcdserverpbTxnResponse k_v_txn(body)

Txn processes multiple requests in a single transaction. A txn request increments the revision of the key-value store and generates events with the same revision for every completed request. It is not allowed to modify the same key several times within one txn.

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
api_instance = etcd_client.KVApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbTxnRequest() # EtcdserverpbTxnRequest | 

try:
    # Txn processes multiple requests in a single transaction. A txn request increments the revision of the key-value store and generates events with the same revision for every completed request. It is not allowed to modify the same key several times within one txn.
    api_response = api_instance.k_v_txn(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KVApi->k_v_txn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbTxnRequest**](EtcdserverpbTxnRequest.md)|  | 

### Return type

[**EtcdserverpbTxnResponse**](EtcdserverpbTxnResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

