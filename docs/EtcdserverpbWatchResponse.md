# EtcdserverpbWatchResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_reason** | **str** | cancel_reason indicates the reason for canceling the watcher. | [optional] 
**canceled** | **bool** | canceled is set to true if the response is for a cancel watch request. No further events will be sent to the canceled watcher. | [optional] 
**compact_revision** | **str** | compact_revision is set to the minimum index if a watcher tries to watch at a compacted index.  This happens when creating a watcher at a compacted revision or the watcher cannot catch up with the progress of the key-value store.  The client should treat the watcher as canceled and should not try to create any watcher with the same start_revision again. | [optional] 
**created** | **bool** | created is set to true if the response is for a create watch request. The client should record the watch_id and expect to receive events for the created watcher from the same stream. All events sent to the created watcher will attach with the same watch_id. | [optional] 
**events** | [**list[MvccpbEvent]**](MvccpbEvent.md) |  | [optional] 
**fragment** | **bool** | framgment is true if large watch response was split over multiple responses. | [optional] 
**header** | [**EtcdserverpbResponseHeader**](EtcdserverpbResponseHeader.md) |  | [optional] 
**watch_id** | **str** | watch_id is the ID of the watcher that corresponds to the response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


