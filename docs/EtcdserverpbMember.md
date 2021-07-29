# EtcdserverpbMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the member ID for this member. | [optional] 
**client_ur_ls** | **list[str]** | clientURLs is the list of URLs the member exposes to clients for communication. If the member is not started, clientURLs will be empty. | [optional] 
**is_learner** | **bool** | isLearner indicates if the member is raft learner. | [optional] 
**name** | **str** | name is the human-readable name of the member. If the member is not started, the name will be an empty string. | [optional] 
**peer_ur_ls** | **list[str]** | peerURLs is the list of URLs the member exposes to the cluster for communication. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


