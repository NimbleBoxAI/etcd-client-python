# EtcdserverpbLeaseTimeToLiveResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the lease ID from the keep alive request. | [optional] 
**ttl** | **str** | TTL is the remaining TTL in seconds for the lease; the lease will expire in under TTL+1 seconds. | [optional] 
**granted_ttl** | **str** | GrantedTTL is the initial granted time in seconds upon lease creation/renewal. | [optional] 
**header** | [**EtcdserverpbResponseHeader**](EtcdserverpbResponseHeader.md) |  | [optional] 
**keys** | **list[str]** | Keys is the list of keys attached to this lease. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


