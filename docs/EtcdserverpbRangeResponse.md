# EtcdserverpbRangeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** | count is set to the number of keys within the range when requested. | [optional] 
**header** | [**EtcdserverpbResponseHeader**](EtcdserverpbResponseHeader.md) |  | [optional] 
**kvs** | [**list[MvccpbKeyValue]**](MvccpbKeyValue.md) | kvs is the list of key-value pairs matched by the range request. kvs is empty when count is requested. | [optional] 
**more** | **bool** | more indicates if there are more keys to return in the requested range. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


