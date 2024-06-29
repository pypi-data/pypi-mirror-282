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

__all__ = ['GroupsOperationArgs', 'GroupsOperation']

@pulumi.input_type
class GroupsOperationArgs:
    def __init__(__self__, *,
                 project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[Union[str, 'GroupType']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 supported_assessment_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AssessmentType']]]]] = None):
        """
        The set of arguments for constructing a GroupsOperation resource.
        :param pulumi.Input[str] project_name: Assessment Project Name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] group_name: Group ARM name
        :param pulumi.Input[Union[str, 'GroupType']] group_type: The type of group.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AssessmentType']]]] supported_assessment_types: List of assessment types supported on this group.
        """
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if group_type is not None:
            pulumi.set(__self__, "group_type", group_type)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if supported_assessment_types is not None:
            pulumi.set(__self__, "supported_assessment_types", supported_assessment_types)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        Assessment Project Name
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

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
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Group ARM name
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[pulumi.Input[Union[str, 'GroupType']]]:
        """
        The type of group.
        """
        return pulumi.get(self, "group_type")

    @group_type.setter
    def group_type(self, value: Optional[pulumi.Input[Union[str, 'GroupType']]]):
        pulumi.set(self, "group_type", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="supportedAssessmentTypes")
    def supported_assessment_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AssessmentType']]]]]:
        """
        List of assessment types supported on this group.
        """
        return pulumi.get(self, "supported_assessment_types")

    @supported_assessment_types.setter
    def supported_assessment_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AssessmentType']]]]]):
        pulumi.set(self, "supported_assessment_types", value)


class GroupsOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[Union[str, 'GroupType']]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 supported_assessment_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AssessmentType']]]]] = None,
                 __props__=None):
        """
        Group resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_name: Group ARM name
        :param pulumi.Input[Union[str, 'GroupType']] group_type: The type of group.
        :param pulumi.Input[str] project_name: Assessment Project Name
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AssessmentType']]]] supported_assessment_types: List of assessment types supported on this group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupsOperationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Group resource.

        :param str resource_name: The name of the resource.
        :param GroupsOperationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupsOperationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[Union[str, 'GroupType']]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 supported_assessment_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AssessmentType']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupsOperationArgs.__new__(GroupsOperationArgs)

            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["group_type"] = group_type
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["supported_assessment_types"] = supported_assessment_types
            __props__.__dict__["are_assessments_running"] = None
            __props__.__dict__["assessments"] = None
            __props__.__dict__["created_timestamp"] = None
            __props__.__dict__["group_status"] = None
            __props__.__dict__["machine_count"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_timestamp"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate:GroupsOperation"), pulumi.Alias(type_="azure-native:migrate/v20191001:GroupsOperation"), pulumi.Alias(type_="azure-native:migrate/v20230315:GroupsOperation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GroupsOperation, __self__).__init__(
            'azure-native:migrate/v20230401preview:GroupsOperation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GroupsOperation':
        """
        Get an existing GroupsOperation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroupsOperationArgs.__new__(GroupsOperationArgs)

        __props__.__dict__["are_assessments_running"] = None
        __props__.__dict__["assessments"] = None
        __props__.__dict__["created_timestamp"] = None
        __props__.__dict__["group_status"] = None
        __props__.__dict__["group_type"] = None
        __props__.__dict__["machine_count"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["supported_assessment_types"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_timestamp"] = None
        return GroupsOperation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="areAssessmentsRunning")
    def are_assessments_running(self) -> pulumi.Output[bool]:
        """
        If the assessments are in running state.
        """
        return pulumi.get(self, "are_assessments_running")

    @property
    @pulumi.getter
    def assessments(self) -> pulumi.Output[Sequence[str]]:
        """
        List of References to Assessments created on this group.
        """
        return pulumi.get(self, "assessments")

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[str]:
        """
        Time when this group was created. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter(name="groupStatus")
    def group_status(self) -> pulumi.Output[str]:
        """
        Whether the group has been created and is valid.
        """
        return pulumi.get(self, "group_status")

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of group.
        """
        return pulumi.get(self, "group_type")

    @property
    @pulumi.getter(name="machineCount")
    def machine_count(self) -> pulumi.Output[int]:
        """
        Number of machines part of this group.
        """
        return pulumi.get(self, "machine_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="supportedAssessmentTypes")
    def supported_assessment_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of assessment types supported on this group.
        """
        return pulumi.get(self, "supported_assessment_types")

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
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[str]:
        """
        Time when this group was last updated. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "updated_timestamp")

