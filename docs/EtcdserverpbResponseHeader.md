# EtcdserverpbResponseHeader

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | cluster_id is the ID of the cluster which sent the response. | [optional] 
**member_id** | **str** | member_id is the ID of the member which sent the response. | [optional] 
**raft_term** | **str** | raft_term is the raft term when the request was applied. | [optional] 
**revision** | **str** | revision is the key-value store revision when the request was applied. For watch progress responses, the header.revision indicates progress. All future events recieved in this stream are guaranteed to have a higher revision number than the header.revision number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


