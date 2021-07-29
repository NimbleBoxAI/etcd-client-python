# MvccpbKeyValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_revision** | **str** | create_revision is the revision of last creation on this key. | [optional] 
**key** | **str** | key is the key in bytes. An empty key is not allowed. | [optional] 
**lease** | **str** | lease is the ID of the lease that attached to key. When the attached lease expires, the key will be deleted. If lease is 0, then no lease is attached to the key. | [optional] 
**mod_revision** | **str** | mod_revision is the revision of last modification on this key. | [optional] 
**value** | **str** | value is the value held by the key, in bytes. | [optional] 
**version** | **str** | version is the version of the key. A deletion resets the version to zero and any modification of the key increases its version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


