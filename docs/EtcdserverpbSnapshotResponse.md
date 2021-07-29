# EtcdserverpbSnapshotResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob** | **str** | blob contains the next chunk of the snapshot in the snapshot stream. | [optional] 
**header** | [**EtcdserverpbResponseHeader**](EtcdserverpbResponseHeader.md) | header has the current key-value store information. The first header in the snapshot stream indicates the point in time of the snapshot. | [optional] 
**remaining_bytes** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


