# EtcdserverpbRangeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_only** | **bool** | count_only when set returns only the count of the keys in the range. | [optional] 
**key** | **str** | key is the first key for the range. If range_end is not given, the request only looks up key. | [optional] 
**keys_only** | **bool** | keys_only when set returns only the keys and not the values. | [optional] 
**limit** | **str** | limit is a limit on the number of keys returned for the request. When limit is set to 0, it is treated as no limit. | [optional] 
**max_create_revision** | **str** | max_create_revision is the upper bound for returned key create revisions; all keys with greater create revisions will be filtered away. | [optional] 
**max_mod_revision** | **str** | max_mod_revision is the upper bound for returned key mod revisions; all keys with greater mod revisions will be filtered away. | [optional] 
**min_create_revision** | **str** | min_create_revision is the lower bound for returned key create revisions; all keys with lesser create revisions will be filtered away. | [optional] 
**min_mod_revision** | **str** | min_mod_revision is the lower bound for returned key mod revisions; all keys with lesser mod revisions will be filtered away. | [optional] 
**range_end** | **str** | range_end is the upper bound on the requested range [key, range_end). If range_end is &#39;\\0&#39;, the range is all keys &gt;&#x3D; key. If range_end is key plus one (e.g., \&quot;aa\&quot;+1 &#x3D;&#x3D; \&quot;ab\&quot;, \&quot;a\\xff\&quot;+1 &#x3D;&#x3D; \&quot;b\&quot;), then the range request gets all keys prefixed with key. If both key and range_end are &#39;\\0&#39;, then the range request returns all keys. | [optional] 
**revision** | **str** | revision is the point-in-time of the key-value store to use for the range. If revision is less or equal to zero, the range is over the newest key-value store. If the revision has been compacted, ErrCompacted is returned as a response. | [optional] 
**serializable** | **bool** | serializable sets the range request to use serializable member-local reads. Range requests are linearizable by default; linearizable requests have higher latency and lower throughput than serializable requests but reflect the current consensus of the cluster. For better performance, in exchange for possible stale reads, a serializable range request is served locally without needing to reach consensus with other nodes in the cluster. | [optional] 
**sort_order** | [**RangeRequestSortOrder**](RangeRequestSortOrder.md) | sort_order is the order for returned sorted results. | [optional] 
**sort_target** | [**RangeRequestSortTarget**](RangeRequestSortTarget.md) | sort_target is the key-value field to use for sorting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


