# EtcdserverpbDeleteRangeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **str** | deleted is the number of keys deleted by the delete range request. | [optional] 
**header** | [**EtcdserverpbResponseHeader**](EtcdserverpbResponseHeader.md) |  | [optional] 
**prev_kvs** | [**list[MvccpbKeyValue]**](MvccpbKeyValue.md) | if prev_kv is set in the request, the previous key-value pairs will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


