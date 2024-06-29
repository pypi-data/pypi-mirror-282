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
from ._inputs import *

__all__ = ['WorkspaceManagerAssignmentArgs', 'WorkspaceManagerAssignment']

@pulumi.input_type
class WorkspaceManagerAssignmentArgs:
    def __init__(__self__, *,
                 items: pulumi.Input[Sequence[pulumi.Input['AssignmentItemArgs']]],
                 resource_group_name: pulumi.Input[str],
                 target_resource_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 workspace_manager_assignment_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceManagerAssignment resource.
        :param pulumi.Input[Sequence[pulumi.Input['AssignmentItemArgs']]] items: List of resources included in this workspace manager assignment
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] target_resource_name: The resource name of the workspace manager group targeted by the workspace manager assignment
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] workspace_manager_assignment_name: The name of the workspace manager assignment
        """
        pulumi.set(__self__, "items", items)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "target_resource_name", target_resource_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if workspace_manager_assignment_name is not None:
            pulumi.set(__self__, "workspace_manager_assignment_name", workspace_manager_assignment_name)

    @property
    @pulumi.getter
    def items(self) -> pulumi.Input[Sequence[pulumi.Input['AssignmentItemArgs']]]:
        """
        List of resources included in this workspace manager assignment
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: pulumi.Input[Sequence[pulumi.Input['AssignmentItemArgs']]]):
        pulumi.set(self, "items", value)

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
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> pulumi.Input[str]:
        """
        The resource name of the workspace manager group targeted by the workspace manager assignment
        """
        return pulumi.get(self, "target_resource_name")

    @target_resource_name.setter
    def target_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="workspaceManagerAssignmentName")
    def workspace_manager_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workspace manager assignment
        """
        return pulumi.get(self, "workspace_manager_assignment_name")

    @workspace_manager_assignment_name.setter
    def workspace_manager_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_manager_assignment_name", value)


class WorkspaceManagerAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssignmentItemArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_resource_name: Optional[pulumi.Input[str]] = None,
                 workspace_manager_assignment_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The workspace manager assignment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssignmentItemArgs']]]] items: List of resources included in this workspace manager assignment
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] target_resource_name: The resource name of the workspace manager group targeted by the workspace manager assignment
        :param pulumi.Input[str] workspace_manager_assignment_name: The name of the workspace manager assignment
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceManagerAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The workspace manager assignment

        :param str resource_name: The name of the resource.
        :param WorkspaceManagerAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceManagerAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssignmentItemArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_resource_name: Optional[pulumi.Input[str]] = None,
                 workspace_manager_assignment_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceManagerAssignmentArgs.__new__(WorkspaceManagerAssignmentArgs)

            if items is None and not opts.urn:
                raise TypeError("Missing required property 'items'")
            __props__.__dict__["items"] = items
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if target_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_name'")
            __props__.__dict__["target_resource_name"] = target_resource_name
            __props__.__dict__["workspace_manager_assignment_name"] = workspace_manager_assignment_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_job_end_time"] = None
            __props__.__dict__["last_job_provisioning_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:WorkspaceManagerAssignment"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:WorkspaceManagerAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceManagerAssignment, __self__).__init__(
            'azure-native:securityinsights/v20230601preview:WorkspaceManagerAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceManagerAssignment':
        """
        Get an existing WorkspaceManagerAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceManagerAssignmentArgs.__new__(WorkspaceManagerAssignmentArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["items"] = None
        __props__.__dict__["last_job_end_time"] = None
        __props__.__dict__["last_job_provisioning_state"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_resource_name"] = None
        __props__.__dict__["type"] = None
        return WorkspaceManagerAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def items(self) -> pulumi.Output[Sequence['outputs.AssignmentItemResponse']]:
        """
        List of resources included in this workspace manager assignment
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="lastJobEndTime")
    def last_job_end_time(self) -> pulumi.Output[str]:
        """
        The time the last job associated to this assignment ended at
        """
        return pulumi.get(self, "last_job_end_time")

    @property
    @pulumi.getter(name="lastJobProvisioningState")
    def last_job_provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the last job associated to this assignment
        """
        return pulumi.get(self, "last_job_provisioning_state")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> pulumi.Output[str]:
        """
        The resource name of the workspace manager group targeted by the workspace manager assignment
        """
        return pulumi.get(self, "target_resource_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

