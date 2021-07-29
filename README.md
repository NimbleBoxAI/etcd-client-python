# etcd-client-python
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: version not set
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import etcd_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import etcd_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import etcd_client
from etcd_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = etcd_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = etcd_client.AuthApi(etcd_client.ApiClient(configuration))
body = etcd_client.EtcdserverpbAuthDisableRequest() # EtcdserverpbAuthDisableRequest | 

try:
    # AuthDisable disables authentication.
    api_response = api_instance.auth_auth_disable(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_auth_disable: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_auth_disable**](docs/AuthApi.md#auth_auth_disable) | **POST** /v3/auth/disable | AuthDisable disables authentication.
*AuthApi* | [**auth_auth_enable**](docs/AuthApi.md#auth_auth_enable) | **POST** /v3/auth/enable | AuthEnable enables authentication.
*AuthApi* | [**auth_auth_status**](docs/AuthApi.md#auth_auth_status) | **POST** /v3/auth/status | AuthStatus displays authentication status.
*AuthApi* | [**auth_authenticate**](docs/AuthApi.md#auth_authenticate) | **POST** /v3/auth/authenticate | Authenticate processes an authenticate request.
*AuthApi* | [**auth_role_add**](docs/AuthApi.md#auth_role_add) | **POST** /v3/auth/role/add | RoleAdd adds a new role. Role name cannot be empty.
*AuthApi* | [**auth_role_delete**](docs/AuthApi.md#auth_role_delete) | **POST** /v3/auth/role/delete | RoleDelete deletes a specified role.
*AuthApi* | [**auth_role_get**](docs/AuthApi.md#auth_role_get) | **POST** /v3/auth/role/get | RoleGet gets detailed role information.
*AuthApi* | [**auth_role_grant_permission**](docs/AuthApi.md#auth_role_grant_permission) | **POST** /v3/auth/role/grant | RoleGrantPermission grants a permission of a specified key or range to a specified role.
*AuthApi* | [**auth_role_list**](docs/AuthApi.md#auth_role_list) | **POST** /v3/auth/role/list | RoleList gets lists of all roles.
*AuthApi* | [**auth_role_revoke_permission**](docs/AuthApi.md#auth_role_revoke_permission) | **POST** /v3/auth/role/revoke | RoleRevokePermission revokes a key or range permission of a specified role.
*AuthApi* | [**auth_user_add**](docs/AuthApi.md#auth_user_add) | **POST** /v3/auth/user/add | UserAdd adds a new user. User name cannot be empty.
*AuthApi* | [**auth_user_change_password**](docs/AuthApi.md#auth_user_change_password) | **POST** /v3/auth/user/changepw | UserChangePassword changes the password of a specified user.
*AuthApi* | [**auth_user_delete**](docs/AuthApi.md#auth_user_delete) | **POST** /v3/auth/user/delete | UserDelete deletes a specified user.
*AuthApi* | [**auth_user_get**](docs/AuthApi.md#auth_user_get) | **POST** /v3/auth/user/get | UserGet gets detailed user information.
*AuthApi* | [**auth_user_grant_role**](docs/AuthApi.md#auth_user_grant_role) | **POST** /v3/auth/user/grant | UserGrant grants a role to a specified user.
*AuthApi* | [**auth_user_list**](docs/AuthApi.md#auth_user_list) | **POST** /v3/auth/user/list | UserList gets a list of all users.
*AuthApi* | [**auth_user_revoke_role**](docs/AuthApi.md#auth_user_revoke_role) | **POST** /v3/auth/user/revoke | UserRevokeRole revokes a role of specified user.
*ClusterApi* | [**cluster_member_add**](docs/ClusterApi.md#cluster_member_add) | **POST** /v3/cluster/member/add | MemberAdd adds a member into the cluster.
*ClusterApi* | [**cluster_member_list**](docs/ClusterApi.md#cluster_member_list) | **POST** /v3/cluster/member/list | MemberList lists all the members in the cluster.
*ClusterApi* | [**cluster_member_promote**](docs/ClusterApi.md#cluster_member_promote) | **POST** /v3/cluster/member/promote | MemberPromote promotes a member from raft learner (non-voting) to raft voting member.
*ClusterApi* | [**cluster_member_remove**](docs/ClusterApi.md#cluster_member_remove) | **POST** /v3/cluster/member/remove | MemberRemove removes an existing member from the cluster.
*ClusterApi* | [**cluster_member_update**](docs/ClusterApi.md#cluster_member_update) | **POST** /v3/cluster/member/update | MemberUpdate updates the member configuration.
*KVApi* | [**k_v_compact**](docs/KVApi.md#k_v_compact) | **POST** /v3/kv/compaction | Compact compacts the event history in the etcd key-value store. The key-value store should be periodically compacted or the event history will continue to grow indefinitely.
*KVApi* | [**k_v_delete_range**](docs/KVApi.md#k_v_delete_range) | **POST** /v3/kv/deleterange | DeleteRange deletes the given range from the key-value store. A delete request increments the revision of the key-value store and generates a delete event in the event history for every deleted key.
*KVApi* | [**k_v_put**](docs/KVApi.md#k_v_put) | **POST** /v3/kv/put | Put puts the given key into the key-value store. A put request increments the revision of the key-value store and generates one event in the event history.
*KVApi* | [**k_v_range**](docs/KVApi.md#k_v_range) | **POST** /v3/kv/range | Range gets the keys in the range from the key-value store.
*KVApi* | [**k_v_txn**](docs/KVApi.md#k_v_txn) | **POST** /v3/kv/txn | Txn processes multiple requests in a single transaction. A txn request increments the revision of the key-value store and generates events with the same revision for every completed request. It is not allowed to modify the same key several times within one txn.
*LeaseApi* | [**lease_lease_grant**](docs/LeaseApi.md#lease_lease_grant) | **POST** /v3/lease/grant | LeaseGrant creates a lease which expires if the server does not receive a keepAlive within a given time to live period. All keys attached to the lease will be expired and deleted if the lease expires. Each expired key generates a delete event in the event history.
*LeaseApi* | [**lease_lease_keep_alive**](docs/LeaseApi.md#lease_lease_keep_alive) | **POST** /v3/lease/keepalive | LeaseKeepAlive keeps the lease alive by streaming keep alive requests from the client to the server and streaming keep alive responses from the server to the client.
*LeaseApi* | [**lease_lease_leases**](docs/LeaseApi.md#lease_lease_leases) | **POST** /v3/lease/leases | LeaseLeases lists all existing leases.
*LeaseApi* | [**lease_lease_leases2**](docs/LeaseApi.md#lease_lease_leases2) | **POST** /v3/kv/lease/leases | LeaseLeases lists all existing leases.
*LeaseApi* | [**lease_lease_revoke**](docs/LeaseApi.md#lease_lease_revoke) | **POST** /v3/lease/revoke | LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.
*LeaseApi* | [**lease_lease_revoke2**](docs/LeaseApi.md#lease_lease_revoke2) | **POST** /v3/kv/lease/revoke | LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted.
*LeaseApi* | [**lease_lease_time_to_live**](docs/LeaseApi.md#lease_lease_time_to_live) | **POST** /v3/lease/timetolive | LeaseTimeToLive retrieves lease information.
*LeaseApi* | [**lease_lease_time_to_live2**](docs/LeaseApi.md#lease_lease_time_to_live2) | **POST** /v3/kv/lease/timetolive | LeaseTimeToLive retrieves lease information.
*MaintenanceApi* | [**maintenance_alarm**](docs/MaintenanceApi.md#maintenance_alarm) | **POST** /v3/maintenance/alarm | Alarm activates, deactivates, and queries alarms regarding cluster health.
*MaintenanceApi* | [**maintenance_defragment**](docs/MaintenanceApi.md#maintenance_defragment) | **POST** /v3/maintenance/defragment | Defragment defragments a member&#39;s backend database to recover storage space.
*MaintenanceApi* | [**maintenance_downgrade**](docs/MaintenanceApi.md#maintenance_downgrade) | **POST** /v3/maintenance/downgrade | Downgrade requests downgrades, verifies feasibility or cancels downgrade on the cluster version. Supported since etcd 3.5.
*MaintenanceApi* | [**maintenance_hash_kv**](docs/MaintenanceApi.md#maintenance_hash_kv) | **POST** /v3/maintenance/hash | HashKV computes the hash of all MVCC keys up to a given revision. It only iterates \&quot;key\&quot; bucket in backend storage.
*MaintenanceApi* | [**maintenance_move_leader**](docs/MaintenanceApi.md#maintenance_move_leader) | **POST** /v3/maintenance/transfer-leadership | MoveLeader requests current leader node to transfer its leadership to transferee.
*MaintenanceApi* | [**maintenance_snapshot**](docs/MaintenanceApi.md#maintenance_snapshot) | **POST** /v3/maintenance/snapshot | Snapshot sends a snapshot of the entire backend from a member over a stream to a client.
*MaintenanceApi* | [**maintenance_status**](docs/MaintenanceApi.md#maintenance_status) | **POST** /v3/maintenance/status | Status gets the status of the member.
*WatchApi* | [**watch_watch**](docs/WatchApi.md#watch_watch) | **POST** /v3/watch | Watch watches for events happening or that have happened. Both input and output are streams; the input stream is for creating and canceling watchers and the output stream sends events. One watch RPC can watch on multiple key ranges, streaming events for several watches at once. The entire event history can be watched starting from the last compaction revision.


## Documentation For Models

 - [AlarmRequestAlarmAction](docs/AlarmRequestAlarmAction.md)
 - [AuthpbPermission](docs/AuthpbPermission.md)
 - [AuthpbPermissionType](docs/AuthpbPermissionType.md)
 - [AuthpbUserAddOptions](docs/AuthpbUserAddOptions.md)
 - [CompareCompareResult](docs/CompareCompareResult.md)
 - [CompareCompareTarget](docs/CompareCompareTarget.md)
 - [DowngradeRequestDowngradeAction](docs/DowngradeRequestDowngradeAction.md)
 - [EtcdserverpbAlarmMember](docs/EtcdserverpbAlarmMember.md)
 - [EtcdserverpbAlarmRequest](docs/EtcdserverpbAlarmRequest.md)
 - [EtcdserverpbAlarmResponse](docs/EtcdserverpbAlarmResponse.md)
 - [EtcdserverpbAlarmType](docs/EtcdserverpbAlarmType.md)
 - [EtcdserverpbAuthDisableRequest](docs/EtcdserverpbAuthDisableRequest.md)
 - [EtcdserverpbAuthDisableResponse](docs/EtcdserverpbAuthDisableResponse.md)
 - [EtcdserverpbAuthEnableRequest](docs/EtcdserverpbAuthEnableRequest.md)
 - [EtcdserverpbAuthEnableResponse](docs/EtcdserverpbAuthEnableResponse.md)
 - [EtcdserverpbAuthRoleAddRequest](docs/EtcdserverpbAuthRoleAddRequest.md)
 - [EtcdserverpbAuthRoleAddResponse](docs/EtcdserverpbAuthRoleAddResponse.md)
 - [EtcdserverpbAuthRoleDeleteRequest](docs/EtcdserverpbAuthRoleDeleteRequest.md)
 - [EtcdserverpbAuthRoleDeleteResponse](docs/EtcdserverpbAuthRoleDeleteResponse.md)
 - [EtcdserverpbAuthRoleGetRequest](docs/EtcdserverpbAuthRoleGetRequest.md)
 - [EtcdserverpbAuthRoleGetResponse](docs/EtcdserverpbAuthRoleGetResponse.md)
 - [EtcdserverpbAuthRoleGrantPermissionRequest](docs/EtcdserverpbAuthRoleGrantPermissionRequest.md)
 - [EtcdserverpbAuthRoleGrantPermissionResponse](docs/EtcdserverpbAuthRoleGrantPermissionResponse.md)
 - [EtcdserverpbAuthRoleListRequest](docs/EtcdserverpbAuthRoleListRequest.md)
 - [EtcdserverpbAuthRoleListResponse](docs/EtcdserverpbAuthRoleListResponse.md)
 - [EtcdserverpbAuthRoleRevokePermissionRequest](docs/EtcdserverpbAuthRoleRevokePermissionRequest.md)
 - [EtcdserverpbAuthRoleRevokePermissionResponse](docs/EtcdserverpbAuthRoleRevokePermissionResponse.md)
 - [EtcdserverpbAuthStatusRequest](docs/EtcdserverpbAuthStatusRequest.md)
 - [EtcdserverpbAuthStatusResponse](docs/EtcdserverpbAuthStatusResponse.md)
 - [EtcdserverpbAuthUserAddRequest](docs/EtcdserverpbAuthUserAddRequest.md)
 - [EtcdserverpbAuthUserAddResponse](docs/EtcdserverpbAuthUserAddResponse.md)
 - [EtcdserverpbAuthUserChangePasswordRequest](docs/EtcdserverpbAuthUserChangePasswordRequest.md)
 - [EtcdserverpbAuthUserChangePasswordResponse](docs/EtcdserverpbAuthUserChangePasswordResponse.md)
 - [EtcdserverpbAuthUserDeleteRequest](docs/EtcdserverpbAuthUserDeleteRequest.md)
 - [EtcdserverpbAuthUserDeleteResponse](docs/EtcdserverpbAuthUserDeleteResponse.md)
 - [EtcdserverpbAuthUserGetRequest](docs/EtcdserverpbAuthUserGetRequest.md)
 - [EtcdserverpbAuthUserGetResponse](docs/EtcdserverpbAuthUserGetResponse.md)
 - [EtcdserverpbAuthUserGrantRoleRequest](docs/EtcdserverpbAuthUserGrantRoleRequest.md)
 - [EtcdserverpbAuthUserGrantRoleResponse](docs/EtcdserverpbAuthUserGrantRoleResponse.md)
 - [EtcdserverpbAuthUserListRequest](docs/EtcdserverpbAuthUserListRequest.md)
 - [EtcdserverpbAuthUserListResponse](docs/EtcdserverpbAuthUserListResponse.md)
 - [EtcdserverpbAuthUserRevokeRoleRequest](docs/EtcdserverpbAuthUserRevokeRoleRequest.md)
 - [EtcdserverpbAuthUserRevokeRoleResponse](docs/EtcdserverpbAuthUserRevokeRoleResponse.md)
 - [EtcdserverpbAuthenticateRequest](docs/EtcdserverpbAuthenticateRequest.md)
 - [EtcdserverpbAuthenticateResponse](docs/EtcdserverpbAuthenticateResponse.md)
 - [EtcdserverpbCompactionRequest](docs/EtcdserverpbCompactionRequest.md)
 - [EtcdserverpbCompactionResponse](docs/EtcdserverpbCompactionResponse.md)
 - [EtcdserverpbCompare](docs/EtcdserverpbCompare.md)
 - [EtcdserverpbDefragmentRequest](docs/EtcdserverpbDefragmentRequest.md)
 - [EtcdserverpbDefragmentResponse](docs/EtcdserverpbDefragmentResponse.md)
 - [EtcdserverpbDeleteRangeRequest](docs/EtcdserverpbDeleteRangeRequest.md)
 - [EtcdserverpbDeleteRangeResponse](docs/EtcdserverpbDeleteRangeResponse.md)
 - [EtcdserverpbDowngradeRequest](docs/EtcdserverpbDowngradeRequest.md)
 - [EtcdserverpbDowngradeResponse](docs/EtcdserverpbDowngradeResponse.md)
 - [EtcdserverpbHashKVRequest](docs/EtcdserverpbHashKVRequest.md)
 - [EtcdserverpbHashKVResponse](docs/EtcdserverpbHashKVResponse.md)
 - [EtcdserverpbHashRequest](docs/EtcdserverpbHashRequest.md)
 - [EtcdserverpbHashResponse](docs/EtcdserverpbHashResponse.md)
 - [EtcdserverpbLeaseGrantRequest](docs/EtcdserverpbLeaseGrantRequest.md)
 - [EtcdserverpbLeaseGrantResponse](docs/EtcdserverpbLeaseGrantResponse.md)
 - [EtcdserverpbLeaseKeepAliveRequest](docs/EtcdserverpbLeaseKeepAliveRequest.md)
 - [EtcdserverpbLeaseKeepAliveResponse](docs/EtcdserverpbLeaseKeepAliveResponse.md)
 - [EtcdserverpbLeaseLeasesRequest](docs/EtcdserverpbLeaseLeasesRequest.md)
 - [EtcdserverpbLeaseLeasesResponse](docs/EtcdserverpbLeaseLeasesResponse.md)
 - [EtcdserverpbLeaseRevokeRequest](docs/EtcdserverpbLeaseRevokeRequest.md)
 - [EtcdserverpbLeaseRevokeResponse](docs/EtcdserverpbLeaseRevokeResponse.md)
 - [EtcdserverpbLeaseStatus](docs/EtcdserverpbLeaseStatus.md)
 - [EtcdserverpbLeaseTimeToLiveRequest](docs/EtcdserverpbLeaseTimeToLiveRequest.md)
 - [EtcdserverpbLeaseTimeToLiveResponse](docs/EtcdserverpbLeaseTimeToLiveResponse.md)
 - [EtcdserverpbMember](docs/EtcdserverpbMember.md)
 - [EtcdserverpbMemberAddRequest](docs/EtcdserverpbMemberAddRequest.md)
 - [EtcdserverpbMemberAddResponse](docs/EtcdserverpbMemberAddResponse.md)
 - [EtcdserverpbMemberListRequest](docs/EtcdserverpbMemberListRequest.md)
 - [EtcdserverpbMemberListResponse](docs/EtcdserverpbMemberListResponse.md)
 - [EtcdserverpbMemberPromoteRequest](docs/EtcdserverpbMemberPromoteRequest.md)
 - [EtcdserverpbMemberPromoteResponse](docs/EtcdserverpbMemberPromoteResponse.md)
 - [EtcdserverpbMemberRemoveRequest](docs/EtcdserverpbMemberRemoveRequest.md)
 - [EtcdserverpbMemberRemoveResponse](docs/EtcdserverpbMemberRemoveResponse.md)
 - [EtcdserverpbMemberUpdateRequest](docs/EtcdserverpbMemberUpdateRequest.md)
 - [EtcdserverpbMemberUpdateResponse](docs/EtcdserverpbMemberUpdateResponse.md)
 - [EtcdserverpbMoveLeaderRequest](docs/EtcdserverpbMoveLeaderRequest.md)
 - [EtcdserverpbMoveLeaderResponse](docs/EtcdserverpbMoveLeaderResponse.md)
 - [EtcdserverpbPutRequest](docs/EtcdserverpbPutRequest.md)
 - [EtcdserverpbPutResponse](docs/EtcdserverpbPutResponse.md)
 - [EtcdserverpbRangeRequest](docs/EtcdserverpbRangeRequest.md)
 - [EtcdserverpbRangeResponse](docs/EtcdserverpbRangeResponse.md)
 - [EtcdserverpbRequestOp](docs/EtcdserverpbRequestOp.md)
 - [EtcdserverpbResponseHeader](docs/EtcdserverpbResponseHeader.md)
 - [EtcdserverpbResponseOp](docs/EtcdserverpbResponseOp.md)
 - [EtcdserverpbSnapshotRequest](docs/EtcdserverpbSnapshotRequest.md)
 - [EtcdserverpbSnapshotResponse](docs/EtcdserverpbSnapshotResponse.md)
 - [EtcdserverpbStatusRequest](docs/EtcdserverpbStatusRequest.md)
 - [EtcdserverpbStatusResponse](docs/EtcdserverpbStatusResponse.md)
 - [EtcdserverpbTxnRequest](docs/EtcdserverpbTxnRequest.md)
 - [EtcdserverpbTxnResponse](docs/EtcdserverpbTxnResponse.md)
 - [EtcdserverpbWatchCancelRequest](docs/EtcdserverpbWatchCancelRequest.md)
 - [EtcdserverpbWatchCreateRequest](docs/EtcdserverpbWatchCreateRequest.md)
 - [EtcdserverpbWatchProgressRequest](docs/EtcdserverpbWatchProgressRequest.md)
 - [EtcdserverpbWatchRequest](docs/EtcdserverpbWatchRequest.md)
 - [EtcdserverpbWatchResponse](docs/EtcdserverpbWatchResponse.md)
 - [EventEventType](docs/EventEventType.md)
 - [MvccpbEvent](docs/MvccpbEvent.md)
 - [MvccpbKeyValue](docs/MvccpbKeyValue.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RangeRequestSortOrder](docs/RangeRequestSortOrder.md)
 - [RangeRequestSortTarget](docs/RangeRequestSortTarget.md)
 - [RuntimeError](docs/RuntimeError.md)
 - [RuntimeStreamError](docs/RuntimeStreamError.md)
 - [StreamResultOfEtcdserverpbLeaseKeepAliveResponse](docs/StreamResultOfEtcdserverpbLeaseKeepAliveResponse.md)
 - [StreamResultOfEtcdserverpbSnapshotResponse](docs/StreamResultOfEtcdserverpbSnapshotResponse.md)
 - [StreamResultOfEtcdserverpbWatchResponse](docs/StreamResultOfEtcdserverpbWatchResponse.md)
 - [WatchCreateRequestFilterType](docs/WatchCreateRequestFilterType.md)


## Documentation For Authorization


## ApiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


