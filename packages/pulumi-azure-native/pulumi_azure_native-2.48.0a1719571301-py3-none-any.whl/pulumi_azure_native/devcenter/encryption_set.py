# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['EncryptionSetArgs', 'EncryptionSet']

@pulumi.input_type
class EncryptionSetArgs:
    def __init__(__self__, *,
                 dev_center_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 devbox_disks_encryption_enable_status: Optional[pulumi.Input[Union[str, 'DevboxDisksEncryptionEnableStatus']]] = None,
                 encryption_set_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 key_encryption_key_url: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a EncryptionSet resource.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'DevboxDisksEncryptionEnableStatus']] devbox_disks_encryption_enable_status: Devbox disk encryption enable or disable status. Indicates if Devbox disks encryption using DevCenter CMK is enabled or not.
        :param pulumi.Input[str] encryption_set_name: The name of the devcenter encryption set.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: Managed identity properties
        :param pulumi.Input[str] key_encryption_key_url: Key encryption key Url, versioned or non-versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "dev_center_name", dev_center_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if devbox_disks_encryption_enable_status is not None:
            pulumi.set(__self__, "devbox_disks_encryption_enable_status", devbox_disks_encryption_enable_status)
        if encryption_set_name is not None:
            pulumi.set(__self__, "encryption_set_name", encryption_set_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if key_encryption_key_url is not None:
            pulumi.set(__self__, "key_encryption_key_url", key_encryption_key_url)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="devCenterName")
    def dev_center_name(self) -> pulumi.Input[str]:
        """
        The name of the devcenter.
        """
        return pulumi.get(self, "dev_center_name")

    @dev_center_name.setter
    def dev_center_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dev_center_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="devboxDisksEncryptionEnableStatus")
    def devbox_disks_encryption_enable_status(self) -> Optional[pulumi.Input[Union[str, 'DevboxDisksEncryptionEnableStatus']]]:
        """
        Devbox disk encryption enable or disable status. Indicates if Devbox disks encryption using DevCenter CMK is enabled or not.
        """
        return pulumi.get(self, "devbox_disks_encryption_enable_status")

    @devbox_disks_encryption_enable_status.setter
    def devbox_disks_encryption_enable_status(self, value: Optional[pulumi.Input[Union[str, 'DevboxDisksEncryptionEnableStatus']]]):
        pulumi.set(self, "devbox_disks_encryption_enable_status", value)

    @property
    @pulumi.getter(name="encryptionSetName")
    def encryption_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the devcenter encryption set.
        """
        return pulumi.get(self, "encryption_set_name")

    @encryption_set_name.setter
    def encryption_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_set_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        Managed identity properties
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[pulumi.Input[str]]:
        """
        Key encryption key Url, versioned or non-versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        """
        return pulumi.get(self, "key_encryption_key_url")

    @key_encryption_key_url.setter
    def key_encryption_key_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_encryption_key_url", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class EncryptionSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 devbox_disks_encryption_enable_status: Optional[pulumi.Input[Union[str, 'DevboxDisksEncryptionEnableStatus']]] = None,
                 encryption_set_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 key_encryption_key_url: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a devcenter encryption set resource.
        Azure REST API version: 2024-05-01-preview.

        Other available API versions: 2024-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[Union[str, 'DevboxDisksEncryptionEnableStatus']] devbox_disks_encryption_enable_status: Devbox disk encryption enable or disable status. Indicates if Devbox disks encryption using DevCenter CMK is enabled or not.
        :param pulumi.Input[str] encryption_set_name: The name of the devcenter encryption set.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: Managed identity properties
        :param pulumi.Input[str] key_encryption_key_url: Key encryption key Url, versioned or non-versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EncryptionSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a devcenter encryption set resource.
        Azure REST API version: 2024-05-01-preview.

        Other available API versions: 2024-06-01-preview.

        :param str resource_name: The name of the resource.
        :param EncryptionSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EncryptionSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 devbox_disks_encryption_enable_status: Optional[pulumi.Input[Union[str, 'DevboxDisksEncryptionEnableStatus']]] = None,
                 encryption_set_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 key_encryption_key_url: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EncryptionSetArgs.__new__(EncryptionSetArgs)

            if dev_center_name is None and not opts.urn:
                raise TypeError("Missing required property 'dev_center_name'")
            __props__.__dict__["dev_center_name"] = dev_center_name
            __props__.__dict__["devbox_disks_encryption_enable_status"] = devbox_disks_encryption_enable_status
            __props__.__dict__["encryption_set_name"] = encryption_set_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["key_encryption_key_url"] = key_encryption_key_url
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter/v20240501preview:EncryptionSet"), pulumi.Alias(type_="azure-native:devcenter/v20240601preview:EncryptionSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EncryptionSet, __self__).__init__(
            'azure-native:devcenter:EncryptionSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EncryptionSet':
        """
        Get an existing EncryptionSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EncryptionSetArgs.__new__(EncryptionSetArgs)

        __props__.__dict__["devbox_disks_encryption_enable_status"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["key_encryption_key_url"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return EncryptionSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="devboxDisksEncryptionEnableStatus")
    def devbox_disks_encryption_enable_status(self) -> pulumi.Output[Optional[str]]:
        """
        Devbox disk encryption enable or disable status. Indicates if Devbox disks encryption using DevCenter CMK is enabled or not.
        """
        return pulumi.get(self, "devbox_disks_encryption_enable_status")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        Managed identity properties
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> pulumi.Output[Optional[str]]:
        """
        Key encryption key Url, versioned or non-versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        """
        return pulumi.get(self, "key_encryption_key_url")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

