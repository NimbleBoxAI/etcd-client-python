# EtcdserverpbCompare

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_revision** | **str** |  | [optional] 
**key** | **str** | key is the subject key for the comparison operation. | [optional] 
**lease** | **str** | lease is the lease id of the given key. | [optional] 
**mod_revision** | **str** | mod_revision is the last modified revision of the given key. | [optional] 
**range_end** | **str** | range_end compares the given target to all keys in the range [key, range_end). See RangeRequest for more details on key ranges. | [optional] 
**result** | [**CompareCompareResult**](CompareCompareResult.md) | result is logical comparison operation for this comparison. | [optional] 
**target** | [**CompareCompareTarget**](CompareCompareTarget.md) | target is the key-value field to inspect for the comparison. | [optional] 
**value** | **str** | value is the value of the given key, in bytes. | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


