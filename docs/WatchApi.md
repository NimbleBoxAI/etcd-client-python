# etcd_client.WatchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watch_watch**](WatchApi.md#watch_watch) | **POST** /v3/watch | Watch watches for events happening or that have happened. Both input and output are streams; the input stream is for creating and canceling watchers and the output stream sends events. One watch RPC can watch on multiple key ranges, streaming events for several watches at once. The entire event history can be watched starting from the last compaction revision.


# **watch_watch**
> StreamResultOfEtcdserverpbWatchResponse watch_watch(body)

Watch watches for events happening or that have happened. Both input and output are streams; the input stream is for creating and canceling watchers and the output stream sends events. One watch RPC can watch on multiple key ranges, streaming events for several watches at once. The entire event history can be watched starting from the last compaction revision.

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
api_instance = etcd_client.WatchApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbWatchRequest() # EtcdserverpbWatchRequest |  (streaming inputs)

try:
    # Watch watches for events happening or that have happened. Both input and output are streams; the input stream is for creating and canceling watchers and the output stream sends events. One watch RPC can watch on multiple key ranges, streaming events for several watches at once. The entire event history can be watched starting from the last compaction revision.
    api_response = api_instance.watch_watch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EtcdserverpbWatchRequest**](EtcdserverpbWatchRequest.md)|  (streaming inputs) | 

### Return type

[**StreamResultOfEtcdserverpbWatchResponse**](StreamResultOfEtcdserverpbWatchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

