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
from ._enums import *

__all__ = ['InventoryItemArgs', 'InventoryItem']

@pulumi.input_type
class InventoryItemArgs:
    def __init__(__self__, *,
                 inventory_type: pulumi.Input[Union[str, 'InventoryType']],
                 resource_group_name: pulumi.Input[str],
                 vmm_server_name: pulumi.Input[str],
                 inventory_item_resource_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InventoryItem resource.
        :param pulumi.Input[Union[str, 'InventoryType']] inventory_type: They inventory type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] vmm_server_name: Name of the VmmServer.
        :param pulumi.Input[str] inventory_item_resource_name: Name of the inventoryItem.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        pulumi.set(__self__, "inventory_type", inventory_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vmm_server_name", vmm_server_name)
        if inventory_item_resource_name is not None:
            pulumi.set(__self__, "inventory_item_resource_name", inventory_item_resource_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter(name="inventoryType")
    def inventory_type(self) -> pulumi.Input[Union[str, 'InventoryType']]:
        """
        They inventory type.
        """
        return pulumi.get(self, "inventory_type")

    @inventory_type.setter
    def inventory_type(self, value: pulumi.Input[Union[str, 'InventoryType']]):
        pulumi.set(self, "inventory_type", value)

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
    @pulumi.getter(name="vmmServerName")
    def vmm_server_name(self) -> pulumi.Input[str]:
        """
        Name of the VmmServer.
        """
        return pulumi.get(self, "vmm_server_name")

    @vmm_server_name.setter
    def vmm_server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vmm_server_name", value)

    @property
    @pulumi.getter(name="inventoryItemResourceName")
    def inventory_item_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the inventoryItem.
        """
        return pulumi.get(self, "inventory_item_resource_name")

    @inventory_item_resource_name.setter
    def inventory_item_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inventory_item_resource_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)


class InventoryItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inventory_item_resource_name: Optional[pulumi.Input[str]] = None,
                 inventory_type: Optional[pulumi.Input[Union[str, 'InventoryType']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vmm_server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the inventory item.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] inventory_item_resource_name: Name of the inventoryItem.
        :param pulumi.Input[Union[str, 'InventoryType']] inventory_type: They inventory type.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] vmm_server_name: Name of the VmmServer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InventoryItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the inventory item.

        :param str resource_name: The name of the resource.
        :param InventoryItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InventoryItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inventory_item_resource_name: Optional[pulumi.Input[str]] = None,
                 inventory_type: Optional[pulumi.Input[Union[str, 'InventoryType']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vmm_server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InventoryItemArgs.__new__(InventoryItemArgs)

            __props__.__dict__["inventory_item_resource_name"] = inventory_item_resource_name
            if inventory_type is None and not opts.urn:
                raise TypeError("Missing required property 'inventory_type'")
            __props__.__dict__["inventory_type"] = inventory_type
            __props__.__dict__["kind"] = kind
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if vmm_server_name is None and not opts.urn:
                raise TypeError("Missing required property 'vmm_server_name'")
            __props__.__dict__["vmm_server_name"] = vmm_server_name
            __props__.__dict__["inventory_item_name"] = None
            __props__.__dict__["managed_resource_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uuid"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:scvmm:InventoryItem"), pulumi.Alias(type_="azure-native:scvmm/v20200605preview:InventoryItem"), pulumi.Alias(type_="azure-native:scvmm/v20220521preview:InventoryItem"), pulumi.Alias(type_="azure-native:scvmm/v20230401preview:InventoryItem")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InventoryItem, __self__).__init__(
            'azure-native:scvmm/v20231007:InventoryItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InventoryItem':
        """
        Get an existing InventoryItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InventoryItemArgs.__new__(InventoryItemArgs)

        __props__.__dict__["inventory_item_name"] = None
        __props__.__dict__["inventory_type"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["managed_resource_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uuid"] = None
        return InventoryItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="inventoryItemName")
    def inventory_item_name(self) -> pulumi.Output[str]:
        """
        Gets the Managed Object name in Vmm for the inventory item.
        """
        return pulumi.get(self, "inventory_item_name")

    @property
    @pulumi.getter(name="inventoryType")
    def inventory_type(self) -> pulumi.Output[str]:
        """
        They inventory type.
        """
        return pulumi.get(self, "inventory_type")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="managedResourceId")
    def managed_resource_id(self) -> pulumi.Output[str]:
        """
        Gets the tracked resource id corresponding to the inventory resource.
        """
        return pulumi.get(self, "managed_resource_id")

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
        Provisioning state of the resource.
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
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        Gets the UUID (which is assigned by Vmm) for the inventory item.
        """
        return pulumi.get(self, "uuid")

