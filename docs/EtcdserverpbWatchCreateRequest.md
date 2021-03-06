# EtcdserverpbWatchCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**list[WatchCreateRequestFilterType]**](WatchCreateRequestFilterType.md) | filters filter the events at server side before it sends back to the watcher. | [optional] 
**fragment** | **bool** | fragment enables splitting large revisions into multiple watch responses. | [optional] 
**key** | **str** | key is the key to register for watching. | [optional] 
**prev_kv** | **bool** | If prev_kv is set, created watcher gets the previous KV before the event happens. If the previous KV is already compacted, nothing will be returned. | [optional] 
**progress_notify** | **bool** | progress_notify is set so that the etcd server will periodically send a WatchResponse with no events to the new watcher if there are no recent events. It is useful when clients wish to recover a disconnected watcher starting from a recent known revision. The etcd server may decide how often it will send notifications based on current load. | [optional] 
**range_end** | **str** | range_end is the end of the range [key, range_end) to watch. If range_end is not given, only the key argument is watched. If range_end is equal to &#39;\\0&#39;, all keys greater than or equal to the key argument are watched. If the range_end is one bit larger than the given key, then all keys with the prefix (the given key) will be watched. | [optional] 
**start_revision** | **str** | start_revision is an optional revision to watch from (inclusive). No start_revision is \&quot;now\&quot;. | [optional] 
**watch_id** | **str** | If watch_id is provided and non-zero, it will be assigned to this watcher. Since creating a watcher in etcd is not a synchronous operation, this can be used ensure that ordering is correct when creating multiple watchers on the same stream. Creating a watcher with an ID already in use on the stream will cause an error to be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


