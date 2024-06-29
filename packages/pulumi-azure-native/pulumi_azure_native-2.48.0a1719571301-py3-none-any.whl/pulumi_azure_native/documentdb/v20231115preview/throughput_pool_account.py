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

__all__ = ['ThroughputPoolAccountArgs', 'ThroughputPoolAccount']

@pulumi.input_type
class ThroughputPoolAccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 throughput_pool_name: pulumi.Input[str],
                 account_location: Optional[pulumi.Input[str]] = None,
                 account_resource_identifier: Optional[pulumi.Input[str]] = None,
                 throughput_pool_account_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ThroughputPoolAccount resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] throughput_pool_name: Cosmos DB Throughput Pool name.
        :param pulumi.Input[str] account_location: The location of  global database account in the throughputPool.
        :param pulumi.Input[str] account_resource_identifier: The resource identifier of global database account in the throughputPool.
        :param pulumi.Input[str] throughput_pool_account_name: Cosmos DB global database account in a Throughput Pool
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "throughput_pool_name", throughput_pool_name)
        if account_location is not None:
            pulumi.set(__self__, "account_location", account_location)
        if account_resource_identifier is not None:
            pulumi.set(__self__, "account_resource_identifier", account_resource_identifier)
        if throughput_pool_account_name is not None:
            pulumi.set(__self__, "throughput_pool_account_name", throughput_pool_account_name)

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
    @pulumi.getter(name="throughputPoolName")
    def throughput_pool_name(self) -> pulumi.Input[str]:
        """
        Cosmos DB Throughput Pool name.
        """
        return pulumi.get(self, "throughput_pool_name")

    @throughput_pool_name.setter
    def throughput_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "throughput_pool_name", value)

    @property
    @pulumi.getter(name="accountLocation")
    def account_location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of  global database account in the throughputPool.
        """
        return pulumi.get(self, "account_location")

    @account_location.setter
    def account_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_location", value)

    @property
    @pulumi.getter(name="accountResourceIdentifier")
    def account_resource_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of global database account in the throughputPool.
        """
        return pulumi.get(self, "account_resource_identifier")

    @account_resource_identifier.setter
    def account_resource_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_resource_identifier", value)

    @property
    @pulumi.getter(name="throughputPoolAccountName")
    def throughput_pool_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cosmos DB global database account in a Throughput Pool
        """
        return pulumi.get(self, "throughput_pool_account_name")

    @throughput_pool_account_name.setter
    def throughput_pool_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throughput_pool_account_name", value)


class ThroughputPoolAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_location: Optional[pulumi.Input[str]] = None,
                 account_resource_identifier: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 throughput_pool_account_name: Optional[pulumi.Input[str]] = None,
                 throughput_pool_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure Cosmos DB Throughputpool Account

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_location: The location of  global database account in the throughputPool.
        :param pulumi.Input[str] account_resource_identifier: The resource identifier of global database account in the throughputPool.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] throughput_pool_account_name: Cosmos DB global database account in a Throughput Pool
        :param pulumi.Input[str] throughput_pool_name: Cosmos DB Throughput Pool name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ThroughputPoolAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Cosmos DB Throughputpool Account

        :param str resource_name: The name of the resource.
        :param ThroughputPoolAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ThroughputPoolAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_location: Optional[pulumi.Input[str]] = None,
                 account_resource_identifier: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 throughput_pool_account_name: Optional[pulumi.Input[str]] = None,
                 throughput_pool_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ThroughputPoolAccountArgs.__new__(ThroughputPoolAccountArgs)

            __props__.__dict__["account_location"] = account_location
            __props__.__dict__["account_resource_identifier"] = account_resource_identifier
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["throughput_pool_account_name"] = throughput_pool_account_name
            if throughput_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'throughput_pool_name'")
            __props__.__dict__["throughput_pool_name"] = throughput_pool_name
            __props__.__dict__["account_instance_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb:ThroughputPoolAccount"), pulumi.Alias(type_="azure-native:documentdb/v20240215preview:ThroughputPoolAccount"), pulumi.Alias(type_="azure-native:documentdb/v20240515preview:ThroughputPoolAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ThroughputPoolAccount, __self__).__init__(
            'azure-native:documentdb/v20231115preview:ThroughputPoolAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ThroughputPoolAccount':
        """
        Get an existing ThroughputPoolAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ThroughputPoolAccountArgs.__new__(ThroughputPoolAccountArgs)

        __props__.__dict__["account_instance_id"] = None
        __props__.__dict__["account_location"] = None
        __props__.__dict__["account_resource_identifier"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ThroughputPoolAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountInstanceId")
    def account_instance_id(self) -> pulumi.Output[str]:
        """
        The instance id of global database account in the throughputPool.
        """
        return pulumi.get(self, "account_instance_id")

    @property
    @pulumi.getter(name="accountLocation")
    def account_location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of  global database account in the throughputPool.
        """
        return pulumi.get(self, "account_location")

    @property
    @pulumi.getter(name="accountResourceIdentifier")
    def account_resource_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The resource identifier of global database account in the throughputPool.
        """
        return pulumi.get(self, "account_resource_identifier")

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
        A provisioning state of the ThroughputPool Account.
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

