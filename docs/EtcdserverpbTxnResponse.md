# EtcdserverpbTxnResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**EtcdserverpbResponseHeader**](EtcdserverpbResponseHeader.md) |  | [optional] 
**responses** | [**list[EtcdserverpbResponseOp]**](EtcdserverpbResponseOp.md) | responses is a list of responses corresponding to the results from applying success if succeeded is true or failure if succeeded is false. | [optional] 
**succeeded** | **bool** | succeeded is set to true if the compare evaluated to true or false otherwise. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


