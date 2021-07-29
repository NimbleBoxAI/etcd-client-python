# EtcdserverpbTxnRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compare** | [**list[EtcdserverpbCompare]**](EtcdserverpbCompare.md) | compare is a list of predicates representing a conjunction of terms. If the comparisons succeed, then the success requests will be processed in order, and the response will contain their respective responses in order. If the comparisons fail, then the failure requests will be processed in order, and the response will contain their respective responses in order. | [optional] 
**failure** | [**list[EtcdserverpbRequestOp]**](EtcdserverpbRequestOp.md) | failure is a list of requests which will be applied when compare evaluates to false. | [optional] 
**success** | [**list[EtcdserverpbRequestOp]**](EtcdserverpbRequestOp.md) | success is a list of requests which will be applied when compare evaluates to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


