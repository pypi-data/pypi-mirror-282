# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetFileShareResult',
    'AwaitableGetFileShareResult',
    'get_file_share',
    'get_file_share_output',
]

@pulumi.output_type
class GetFileShareResult:
    """
    Properties of the file share, including Id, resource name, resource type, Etag.
    """
    def __init__(__self__, access_tier=None, access_tier_change_time=None, access_tier_status=None, deleted=None, deleted_time=None, enabled_protocols=None, etag=None, id=None, last_modified_time=None, lease_duration=None, lease_state=None, lease_status=None, metadata=None, name=None, remaining_retention_days=None, root_squash=None, share_quota=None, share_usage_bytes=None, signed_identifiers=None, snapshot_time=None, type=None, version=None):
        if access_tier and not isinstance(access_tier, str):
            raise TypeError("Expected argument 'access_tier' to be a str")
        pulumi.set(__self__, "access_tier", access_tier)
        if access_tier_change_time and not isinstance(access_tier_change_time, str):
            raise TypeError("Expected argument 'access_tier_change_time' to be a str")
        pulumi.set(__self__, "access_tier_change_time", access_tier_change_time)
        if access_tier_status and not isinstance(access_tier_status, str):
            raise TypeError("Expected argument 'access_tier_status' to be a str")
        pulumi.set(__self__, "access_tier_status", access_tier_status)
        if deleted and not isinstance(deleted, bool):
            raise TypeError("Expected argument 'deleted' to be a bool")
        pulumi.set(__self__, "deleted", deleted)
        if deleted_time and not isinstance(deleted_time, str):
            raise TypeError("Expected argument 'deleted_time' to be a str")
        pulumi.set(__self__, "deleted_time", deleted_time)
        if enabled_protocols and not isinstance(enabled_protocols, str):
            raise TypeError("Expected argument 'enabled_protocols' to be a str")
        pulumi.set(__self__, "enabled_protocols", enabled_protocols)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if lease_duration and not isinstance(lease_duration, str):
            raise TypeError("Expected argument 'lease_duration' to be a str")
        pulumi.set(__self__, "lease_duration", lease_duration)
        if lease_state and not isinstance(lease_state, str):
            raise TypeError("Expected argument 'lease_state' to be a str")
        pulumi.set(__self__, "lease_state", lease_state)
        if lease_status and not isinstance(lease_status, str):
            raise TypeError("Expected argument 'lease_status' to be a str")
        pulumi.set(__self__, "lease_status", lease_status)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if remaining_retention_days and not isinstance(remaining_retention_days, int):
            raise TypeError("Expected argument 'remaining_retention_days' to be a int")
        pulumi.set(__self__, "remaining_retention_days", remaining_retention_days)
        if root_squash and not isinstance(root_squash, str):
            raise TypeError("Expected argument 'root_squash' to be a str")
        pulumi.set(__self__, "root_squash", root_squash)
        if share_quota and not isinstance(share_quota, int):
            raise TypeError("Expected argument 'share_quota' to be a int")
        pulumi.set(__self__, "share_quota", share_quota)
        if share_usage_bytes and not isinstance(share_usage_bytes, float):
            raise TypeError("Expected argument 'share_usage_bytes' to be a float")
        pulumi.set(__self__, "share_usage_bytes", share_usage_bytes)
        if signed_identifiers and not isinstance(signed_identifiers, list):
            raise TypeError("Expected argument 'signed_identifiers' to be a list")
        pulumi.set(__self__, "signed_identifiers", signed_identifiers)
        if snapshot_time and not isinstance(snapshot_time, str):
            raise TypeError("Expected argument 'snapshot_time' to be a str")
        pulumi.set(__self__, "snapshot_time", snapshot_time)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> Optional[str]:
        """
        Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium.
        """
        return pulumi.get(self, "access_tier")

    @property
    @pulumi.getter(name="accessTierChangeTime")
    def access_tier_change_time(self) -> str:
        """
        Indicates the last modification time for share access tier.
        """
        return pulumi.get(self, "access_tier_change_time")

    @property
    @pulumi.getter(name="accessTierStatus")
    def access_tier_status(self) -> str:
        """
        Indicates if there is a pending transition for access tier.
        """
        return pulumi.get(self, "access_tier_status")

    @property
    @pulumi.getter
    def deleted(self) -> bool:
        """
        Indicates whether the share was deleted.
        """
        return pulumi.get(self, "deleted")

    @property
    @pulumi.getter(name="deletedTime")
    def deleted_time(self) -> str:
        """
        The deleted time if the share was deleted.
        """
        return pulumi.get(self, "deleted_time")

    @property
    @pulumi.getter(name="enabledProtocols")
    def enabled_protocols(self) -> Optional[str]:
        """
        The authentication protocol that is used for the file share. Can only be specified when creating a share.
        """
        return pulumi.get(self, "enabled_protocols")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        Returns the date and time the share was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="leaseDuration")
    def lease_duration(self) -> str:
        """
        Specifies whether the lease on a share is of infinite or fixed duration, only when the share is leased.
        """
        return pulumi.get(self, "lease_duration")

    @property
    @pulumi.getter(name="leaseState")
    def lease_state(self) -> str:
        """
        Lease state of the share.
        """
        return pulumi.get(self, "lease_state")

    @property
    @pulumi.getter(name="leaseStatus")
    def lease_status(self) -> str:
        """
        The lease status of the share.
        """
        return pulumi.get(self, "lease_status")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, str]]:
        """
        A name-value pair to associate with the share as metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="remainingRetentionDays")
    def remaining_retention_days(self) -> int:
        """
        Remaining retention days for share that was soft deleted.
        """
        return pulumi.get(self, "remaining_retention_days")

    @property
    @pulumi.getter(name="rootSquash")
    def root_squash(self) -> Optional[str]:
        """
        The property is for NFS share only. The default is NoRootSquash.
        """
        return pulumi.get(self, "root_squash")

    @property
    @pulumi.getter(name="shareQuota")
    def share_quota(self) -> Optional[int]:
        """
        The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400.
        """
        return pulumi.get(self, "share_quota")

    @property
    @pulumi.getter(name="shareUsageBytes")
    def share_usage_bytes(self) -> float:
        """
        The approximate size of the data stored on the share. Note that this value may not include all recently created or recently resized files.
        """
        return pulumi.get(self, "share_usage_bytes")

    @property
    @pulumi.getter(name="signedIdentifiers")
    def signed_identifiers(self) -> Optional[Sequence['outputs.SignedIdentifierResponse']]:
        """
        List of stored access policies specified on the share.
        """
        return pulumi.get(self, "signed_identifiers")

    @property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> str:
        """
        Creation time of share snapshot returned in the response of list shares with expand param "snapshots".
        """
        return pulumi.get(self, "snapshot_time")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the share.
        """
        return pulumi.get(self, "version")


class AwaitableGetFileShareResult(GetFileShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileShareResult(
            access_tier=self.access_tier,
            access_tier_change_time=self.access_tier_change_time,
            access_tier_status=self.access_tier_status,
            deleted=self.deleted,
            deleted_time=self.deleted_time,
            enabled_protocols=self.enabled_protocols,
            etag=self.etag,
            id=self.id,
            last_modified_time=self.last_modified_time,
            lease_duration=self.lease_duration,
            lease_state=self.lease_state,
            lease_status=self.lease_status,
            metadata=self.metadata,
            name=self.name,
            remaining_retention_days=self.remaining_retention_days,
            root_squash=self.root_squash,
            share_quota=self.share_quota,
            share_usage_bytes=self.share_usage_bytes,
            signed_identifiers=self.signed_identifiers,
            snapshot_time=self.snapshot_time,
            type=self.type,
            version=self.version)


def get_file_share(account_name: Optional[str] = None,
                   expand: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   share_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileShareResult:
    """
    Gets properties of a specified share.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str expand: Optional, used to expand the properties within share's properties. Valid values are: stats. Should be passed as a string with delimiter ','.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storage/v20230101:getFileShare', __args__, opts=opts, typ=GetFileShareResult).value

    return AwaitableGetFileShareResult(
        access_tier=pulumi.get(__ret__, 'access_tier'),
        access_tier_change_time=pulumi.get(__ret__, 'access_tier_change_time'),
        access_tier_status=pulumi.get(__ret__, 'access_tier_status'),
        deleted=pulumi.get(__ret__, 'deleted'),
        deleted_time=pulumi.get(__ret__, 'deleted_time'),
        enabled_protocols=pulumi.get(__ret__, 'enabled_protocols'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        lease_duration=pulumi.get(__ret__, 'lease_duration'),
        lease_state=pulumi.get(__ret__, 'lease_state'),
        lease_status=pulumi.get(__ret__, 'lease_status'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        remaining_retention_days=pulumi.get(__ret__, 'remaining_retention_days'),
        root_squash=pulumi.get(__ret__, 'root_squash'),
        share_quota=pulumi.get(__ret__, 'share_quota'),
        share_usage_bytes=pulumi.get(__ret__, 'share_usage_bytes'),
        signed_identifiers=pulumi.get(__ret__, 'signed_identifiers'),
        snapshot_time=pulumi.get(__ret__, 'snapshot_time'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_file_share)
def get_file_share_output(account_name: Optional[pulumi.Input[str]] = None,
                          expand: Optional[pulumi.Input[Optional[str]]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          share_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFileShareResult]:
    """
    Gets properties of a specified share.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str expand: Optional, used to expand the properties within share's properties. Valid values are: stats. Should be passed as a string with delimiter ','.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    """
    ...
