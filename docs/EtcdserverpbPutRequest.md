# EtcdserverpbPutRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_lease** | **bool** | If ignore_lease is set, etcd updates the key using its current lease. Returns an error if the key does not exist. | [optional] 
**ignore_value** | **bool** | If ignore_value is set, etcd updates the key using its current value. Returns an error if the key does not exist. | [optional] 
**key** | **str** | key is the key, in bytes, to put into the key-value store. | [optional] 
**lease** | **str** | lease is the lease ID to associate with the key in the key-value store. A lease value of 0 indicates no lease. | [optional] 
**prev_kv** | **bool** | If prev_kv is set, etcd gets the previous key-value pair before changing it. The previous key-value pair will be returned in the put response. | [optional] 
**value** | **str** | value is the value, in bytes, to associate with the key in the key-value store. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


