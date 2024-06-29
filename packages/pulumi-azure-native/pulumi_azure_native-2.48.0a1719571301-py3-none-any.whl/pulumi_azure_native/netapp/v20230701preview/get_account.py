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
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

@pulumi.output_type
class GetAccountResult:
    """
    NetApp account resource
    """
    def __init__(__self__, active_directories=None, disable_showmount=None, encryption=None, etag=None, id=None, identity=None, is_multi_ad_enabled=None, location=None, name=None, nfs_v4_id_domain=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if active_directories and not isinstance(active_directories, list):
            raise TypeError("Expected argument 'active_directories' to be a list")
        pulumi.set(__self__, "active_directories", active_directories)
        if disable_showmount and not isinstance(disable_showmount, bool):
            raise TypeError("Expected argument 'disable_showmount' to be a bool")
        pulumi.set(__self__, "disable_showmount", disable_showmount)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if is_multi_ad_enabled and not isinstance(is_multi_ad_enabled, bool):
            raise TypeError("Expected argument 'is_multi_ad_enabled' to be a bool")
        pulumi.set(__self__, "is_multi_ad_enabled", is_multi_ad_enabled)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nfs_v4_id_domain and not isinstance(nfs_v4_id_domain, str):
            raise TypeError("Expected argument 'nfs_v4_id_domain' to be a str")
        pulumi.set(__self__, "nfs_v4_id_domain", nfs_v4_id_domain)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="activeDirectories")
    def active_directories(self) -> Optional[Sequence['outputs.ActiveDirectoryResponse']]:
        """
        Active Directories
        """
        return pulumi.get(self, "active_directories")

    @property
    @pulumi.getter(name="disableShowmount")
    def disable_showmount(self) -> bool:
        """
        Shows the status of disableShowmount for all volumes under the subscription, null equals false
        """
        return pulumi.get(self, "disable_showmount")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.AccountEncryptionResponse']:
        """
        Encryption settings
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        The identity used for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isMultiAdEnabled")
    def is_multi_ad_enabled(self) -> bool:
        """
        This will have true value only if account is Multiple AD enabled.
        """
        return pulumi.get(self, "is_multi_ad_enabled")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nfsV4IDDomain")
    def nfs_v4_id_domain(self) -> Optional[str]:
        """
        Domain for NFSv4 user ID mapping. This property will be set for all NetApp accounts in the subscription and region and only affect non ldap NFSv4 volumes.
        """
        return pulumi.get(self, "nfs_v4_id_domain")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            active_directories=self.active_directories,
            disable_showmount=self.disable_showmount,
            encryption=self.encryption,
            etag=self.etag,
            id=self.id,
            identity=self.identity,
            is_multi_ad_enabled=self.is_multi_ad_enabled,
            location=self.location,
            name=self.name,
            nfs_v4_id_domain=self.nfs_v4_id_domain,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_account(account_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Get the NetApp account


    :param str account_name: The name of the NetApp account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20230701preview:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        active_directories=pulumi.get(__ret__, 'active_directories'),
        disable_showmount=pulumi.get(__ret__, 'disable_showmount'),
        encryption=pulumi.get(__ret__, 'encryption'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        is_multi_ad_enabled=pulumi.get(__ret__, 'is_multi_ad_enabled'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        nfs_v4_id_domain=pulumi.get(__ret__, 'nfs_v4_id_domain'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_account)
def get_account_output(account_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountResult]:
    """
    Get the NetApp account


    :param str account_name: The name of the NetApp account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
