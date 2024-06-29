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

__all__ = ['AttachedNetworkByDevCenterArgs', 'AttachedNetworkByDevCenter']

@pulumi.input_type
class AttachedNetworkByDevCenterArgs:
    def __init__(__self__, *,
                 dev_center_name: pulumi.Input[str],
                 network_connection_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 attached_network_connection_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AttachedNetworkByDevCenter resource.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[str] network_connection_id: The resource ID of the NetworkConnection you want to attach.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] attached_network_connection_name: The name of the attached NetworkConnection.
        """
        pulumi.set(__self__, "dev_center_name", dev_center_name)
        pulumi.set(__self__, "network_connection_id", network_connection_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if attached_network_connection_name is not None:
            pulumi.set(__self__, "attached_network_connection_name", attached_network_connection_name)

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
    @pulumi.getter(name="networkConnectionId")
    def network_connection_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the NetworkConnection you want to attach.
        """
        return pulumi.get(self, "network_connection_id")

    @network_connection_id.setter
    def network_connection_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_connection_id", value)

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
    @pulumi.getter(name="attachedNetworkConnectionName")
    def attached_network_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the attached NetworkConnection.
        """
        return pulumi.get(self, "attached_network_connection_name")

    @attached_network_connection_name.setter
    def attached_network_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attached_network_connection_name", value)


class AttachedNetworkByDevCenter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_network_connection_name: Optional[pulumi.Input[str]] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 network_connection_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents an attached NetworkConnection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attached_network_connection_name: The name of the attached NetworkConnection.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[str] network_connection_id: The resource ID of the NetworkConnection you want to attach.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttachedNetworkByDevCenterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an attached NetworkConnection.

        :param str resource_name: The name of the resource.
        :param AttachedNetworkByDevCenterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttachedNetworkByDevCenterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_network_connection_name: Optional[pulumi.Input[str]] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 network_connection_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttachedNetworkByDevCenterArgs.__new__(AttachedNetworkByDevCenterArgs)

            __props__.__dict__["attached_network_connection_name"] = attached_network_connection_name
            if dev_center_name is None and not opts.urn:
                raise TypeError("Missing required property 'dev_center_name'")
            __props__.__dict__["dev_center_name"] = dev_center_name
            if network_connection_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_connection_id'")
            __props__.__dict__["network_connection_id"] = network_connection_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["domain_join_type"] = None
            __props__.__dict__["health_check_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["network_connection_location"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20220801preview:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20220901preview:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20221111preview:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20230101preview:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20230401:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20230801preview:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20240201:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20240501preview:AttachedNetworkByDevCenter"), pulumi.Alias(type_="azure-native:devcenter/v20240601preview:AttachedNetworkByDevCenter")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AttachedNetworkByDevCenter, __self__).__init__(
            'azure-native:devcenter/v20231001preview:AttachedNetworkByDevCenter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AttachedNetworkByDevCenter':
        """
        Get an existing AttachedNetworkByDevCenter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AttachedNetworkByDevCenterArgs.__new__(AttachedNetworkByDevCenterArgs)

        __props__.__dict__["domain_join_type"] = None
        __props__.__dict__["health_check_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_connection_id"] = None
        __props__.__dict__["network_connection_location"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return AttachedNetworkByDevCenter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(self) -> pulumi.Output[str]:
        """
        AAD Join type of the network. This is populated based on the referenced Network Connection.
        """
        return pulumi.get(self, "domain_join_type")

    @property
    @pulumi.getter(name="healthCheckStatus")
    def health_check_status(self) -> pulumi.Output[str]:
        """
        Health check status values
        """
        return pulumi.get(self, "health_check_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConnectionId")
    def network_connection_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the NetworkConnection you want to attach.
        """
        return pulumi.get(self, "network_connection_id")

    @property
    @pulumi.getter(name="networkConnectionLocation")
    def network_connection_location(self) -> pulumi.Output[str]:
        """
        The geo-location where the NetworkConnection resource specified in 'networkConnectionResourceId' property lives.
        """
        return pulumi.get(self, "network_connection_location")

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
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

