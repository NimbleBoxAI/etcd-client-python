# EtcdserverpbStatusResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_size** | **str** | dbSize is the size of the backend database physically allocated, in bytes, of the responding member. | [optional] 
**db_size_in_use** | **str** | dbSizeInUse is the size of the backend database logically in use, in bytes, of the responding member. | [optional] 
**errors** | **list[str]** | errors contains alarm/health information and status. | [optional] 
**header** | [**EtcdserverpbResponseHeader**](EtcdserverpbResponseHeader.md) |  | [optional] 
**is_learner** | **bool** | isLearner indicates if the member is raft learner. | [optional] 
**leader** | **str** | leader is the member ID which the responding member believes is the current leader. | [optional] 
**raft_applied_index** | **str** | raftAppliedIndex is the current raft applied index of the responding member. | [optional] 
**raft_index** | **str** | raftIndex is the current raft committed index of the responding member. | [optional] 
**raft_term** | **str** | raftTerm is the current raft term of the responding member. | [optional] 
**version** | **str** | version is the cluster protocol version used by the responding member. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


