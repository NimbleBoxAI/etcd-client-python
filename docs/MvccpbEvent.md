# MvccpbEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kv** | [**MvccpbKeyValue**](MvccpbKeyValue.md) | kv holds the KeyValue for the event. A PUT event contains current kv pair. A PUT event with kv.Version&#x3D;1 indicates the creation of a key. A DELETE/EXPIRE event contains the deleted key with its modification revision set to the revision of deletion. | [optional] 
**prev_kv** | [**MvccpbKeyValue**](MvccpbKeyValue.md) | prev_kv holds the key-value pair before the event happens. | [optional] 
**type** | [**EventEventType**](EventEventType.md) | type is the kind of event. If type is a PUT, it indicates new data has been stored to the key. If type is a DELETE, it indicates the key was deleted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


