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

__all__ = ['AgentArgs', 'Agent']

@pulumi.input_type
class AgentArgs:
    def __init__(__self__, *,
                 arc_resource_id: pulumi.Input[str],
                 arc_vm_uuid: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_mover_name: pulumi.Input[str],
                 agent_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Agent resource.
        :param pulumi.Input[str] arc_resource_id: The fully qualified resource ID of the Hybrid Compute resource for the Agent.
        :param pulumi.Input[str] arc_vm_uuid: The VM UUID of the Hybrid Compute resource for the Agent.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] storage_mover_name: The name of the Storage Mover resource.
        :param pulumi.Input[str] agent_name: The name of the Agent resource.
        :param pulumi.Input[str] description: A description for the Agent.
        """
        pulumi.set(__self__, "arc_resource_id", arc_resource_id)
        pulumi.set(__self__, "arc_vm_uuid", arc_vm_uuid)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_mover_name", storage_mover_name)
        if agent_name is not None:
            pulumi.set(__self__, "agent_name", agent_name)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="arcResourceId")
    def arc_resource_id(self) -> pulumi.Input[str]:
        """
        The fully qualified resource ID of the Hybrid Compute resource for the Agent.
        """
        return pulumi.get(self, "arc_resource_id")

    @arc_resource_id.setter
    def arc_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "arc_resource_id", value)

    @property
    @pulumi.getter(name="arcVmUuid")
    def arc_vm_uuid(self) -> pulumi.Input[str]:
        """
        The VM UUID of the Hybrid Compute resource for the Agent.
        """
        return pulumi.get(self, "arc_vm_uuid")

    @arc_vm_uuid.setter
    def arc_vm_uuid(self, value: pulumi.Input[str]):
        pulumi.set(self, "arc_vm_uuid", value)

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
    @pulumi.getter(name="storageMoverName")
    def storage_mover_name(self) -> pulumi.Input[str]:
        """
        The name of the Storage Mover resource.
        """
        return pulumi.get(self, "storage_mover_name")

    @storage_mover_name.setter
    def storage_mover_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_mover_name", value)

    @property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Agent resource.
        """
        return pulumi.get(self, "agent_name")

    @agent_name.setter
    def agent_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Agent.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class Agent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_name: Optional[pulumi.Input[str]] = None,
                 arc_resource_id: Optional[pulumi.Input[str]] = None,
                 arc_vm_uuid: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_mover_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Agent resource.
        Azure REST API version: 2023-03-01. Prior API version in Azure Native 1.x: 2022-07-01-preview.

        Other available API versions: 2023-07-01-preview, 2023-10-01, 2024-07-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_name: The name of the Agent resource.
        :param pulumi.Input[str] arc_resource_id: The fully qualified resource ID of the Hybrid Compute resource for the Agent.
        :param pulumi.Input[str] arc_vm_uuid: The VM UUID of the Hybrid Compute resource for the Agent.
        :param pulumi.Input[str] description: A description for the Agent.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] storage_mover_name: The name of the Storage Mover resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Agent resource.
        Azure REST API version: 2023-03-01. Prior API version in Azure Native 1.x: 2022-07-01-preview.

        Other available API versions: 2023-07-01-preview, 2023-10-01, 2024-07-01.

        :param str resource_name: The name of the resource.
        :param AgentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_name: Optional[pulumi.Input[str]] = None,
                 arc_resource_id: Optional[pulumi.Input[str]] = None,
                 arc_vm_uuid: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_mover_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AgentArgs.__new__(AgentArgs)

            __props__.__dict__["agent_name"] = agent_name
            if arc_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'arc_resource_id'")
            __props__.__dict__["arc_resource_id"] = arc_resource_id
            if arc_vm_uuid is None and not opts.urn:
                raise TypeError("Missing required property 'arc_vm_uuid'")
            __props__.__dict__["arc_vm_uuid"] = arc_vm_uuid
            __props__.__dict__["description"] = description
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_mover_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_mover_name'")
            __props__.__dict__["storage_mover_name"] = storage_mover_name
            __props__.__dict__["agent_status"] = None
            __props__.__dict__["agent_version"] = None
            __props__.__dict__["error_details"] = None
            __props__.__dict__["last_status_update"] = None
            __props__.__dict__["local_ip_address"] = None
            __props__.__dict__["memory_in_mb"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["number_of_cores"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uptime_in_seconds"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storagemover/v20220701preview:Agent"), pulumi.Alias(type_="azure-native:storagemover/v20230301:Agent"), pulumi.Alias(type_="azure-native:storagemover/v20230701preview:Agent"), pulumi.Alias(type_="azure-native:storagemover/v20231001:Agent"), pulumi.Alias(type_="azure-native:storagemover/v20240701:Agent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Agent, __self__).__init__(
            'azure-native:storagemover:Agent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Agent':
        """
        Get an existing Agent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgentArgs.__new__(AgentArgs)

        __props__.__dict__["agent_status"] = None
        __props__.__dict__["agent_version"] = None
        __props__.__dict__["arc_resource_id"] = None
        __props__.__dict__["arc_vm_uuid"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["error_details"] = None
        __props__.__dict__["last_status_update"] = None
        __props__.__dict__["local_ip_address"] = None
        __props__.__dict__["memory_in_mb"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["number_of_cores"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uptime_in_seconds"] = None
        return Agent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentStatus")
    def agent_status(self) -> pulumi.Output[str]:
        """
        The Agent status.
        """
        return pulumi.get(self, "agent_status")

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[str]:
        """
        The Agent version.
        """
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter(name="arcResourceId")
    def arc_resource_id(self) -> pulumi.Output[str]:
        """
        The fully qualified resource ID of the Hybrid Compute resource for the Agent.
        """
        return pulumi.get(self, "arc_resource_id")

    @property
    @pulumi.getter(name="arcVmUuid")
    def arc_vm_uuid(self) -> pulumi.Output[str]:
        """
        The VM UUID of the Hybrid Compute resource for the Agent.
        """
        return pulumi.get(self, "arc_vm_uuid")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the Agent.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> pulumi.Output['outputs.AgentPropertiesResponseErrorDetails']:
        return pulumi.get(self, "error_details")

    @property
    @pulumi.getter(name="lastStatusUpdate")
    def last_status_update(self) -> pulumi.Output[str]:
        """
        The last updated time of the Agent status.
        """
        return pulumi.get(self, "last_status_update")

    @property
    @pulumi.getter(name="localIPAddress")
    def local_ip_address(self) -> pulumi.Output[str]:
        """
        Local IP address reported by the Agent.
        """
        return pulumi.get(self, "local_ip_address")

    @property
    @pulumi.getter(name="memoryInMB")
    def memory_in_mb(self) -> pulumi.Output[float]:
        """
        Available memory reported by the Agent, in MB.
        """
        return pulumi.get(self, "memory_in_mb")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfCores")
    def number_of_cores(self) -> pulumi.Output[float]:
        """
        Available compute cores reported by the Agent.
        """
        return pulumi.get(self, "number_of_cores")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of this resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Resource system metadata.
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
    @pulumi.getter(name="uptimeInSeconds")
    def uptime_in_seconds(self) -> pulumi.Output[float]:
        """
        Uptime of the Agent in seconds.
        """
        return pulumi.get(self, "uptime_in_seconds")

