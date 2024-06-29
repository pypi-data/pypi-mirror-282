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

__all__ = ['AssessmentProjectsOperationArgs', 'AssessmentProjectsOperation']

@pulumi.input_type
class AssessmentProjectsOperationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 assessment_solution_id: Optional[pulumi.Input[str]] = None,
                 customer_storage_account_arm_id: Optional[pulumi.Input[str]] = None,
                 customer_workspace_id: Optional[pulumi.Input[str]] = None,
                 customer_workspace_location: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 project_status: Optional[pulumi.Input[Union[str, 'ProjectStatus']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 public_network_access: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AssessmentProjectsOperation resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] assessment_solution_id: Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects.
        :param pulumi.Input[str] customer_storage_account_arm_id: The ARM id of the storage account used for interactions when public access is
               disabled.
        :param pulumi.Input[str] customer_workspace_id: The ARM id of service map workspace created by customer.
        :param pulumi.Input[str] customer_workspace_location: Location of service map workspace created by customer.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] project_name: Assessment Project Name
        :param pulumi.Input[Union[str, 'ProjectStatus']] project_status: Assessment project status.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] public_network_access: This value can be set to 'enabled' to avoid breaking changes on existing
               customer resources and templates. If set to 'disabled', traffic over public
               interface is not allowed, and private endpoint connections would be the
               exclusive access method.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if assessment_solution_id is not None:
            pulumi.set(__self__, "assessment_solution_id", assessment_solution_id)
        if customer_storage_account_arm_id is not None:
            pulumi.set(__self__, "customer_storage_account_arm_id", customer_storage_account_arm_id)
        if customer_workspace_id is not None:
            pulumi.set(__self__, "customer_workspace_id", customer_workspace_id)
        if customer_workspace_location is not None:
            pulumi.set(__self__, "customer_workspace_location", customer_workspace_location)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
        if project_status is not None:
            pulumi.set(__self__, "project_status", project_status)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="assessmentSolutionId")
    def assessment_solution_id(self) -> Optional[pulumi.Input[str]]:
        """
        Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects.
        """
        return pulumi.get(self, "assessment_solution_id")

    @assessment_solution_id.setter
    def assessment_solution_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_solution_id", value)

    @property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARM id of the storage account used for interactions when public access is
        disabled.
        """
        return pulumi.get(self, "customer_storage_account_arm_id")

    @customer_storage_account_arm_id.setter
    def customer_storage_account_arm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_storage_account_arm_id", value)

    @property
    @pulumi.getter(name="customerWorkspaceId")
    def customer_workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARM id of service map workspace created by customer.
        """
        return pulumi.get(self, "customer_workspace_id")

    @customer_workspace_id.setter
    def customer_workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_workspace_id", value)

    @property
    @pulumi.getter(name="customerWorkspaceLocation")
    def customer_workspace_location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of service map workspace created by customer.
        """
        return pulumi.get(self, "customer_workspace_location")

    @customer_workspace_location.setter
    def customer_workspace_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_workspace_location", value)

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
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[str]]:
        """
        Assessment Project Name
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="projectStatus")
    def project_status(self) -> Optional[pulumi.Input[Union[str, 'ProjectStatus']]]:
        """
        Assessment project status.
        """
        return pulumi.get(self, "project_status")

    @project_status.setter
    def project_status(self, value: Optional[pulumi.Input[Union[str, 'ProjectStatus']]]):
        pulumi.set(self, "project_status", value)

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
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[str]]:
        """
        This value can be set to 'enabled' to avoid breaking changes on existing
        customer resources and templates. If set to 'disabled', traffic over public
        interface is not allowed, and private endpoint connections would be the
        exclusive access method.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_network_access", value)

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


class AssessmentProjectsOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_solution_id: Optional[pulumi.Input[str]] = None,
                 customer_storage_account_arm_id: Optional[pulumi.Input[str]] = None,
                 customer_workspace_id: Optional[pulumi.Input[str]] = None,
                 customer_workspace_location: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 project_status: Optional[pulumi.Input[Union[str, 'ProjectStatus']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 public_network_access: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An Assessment project site resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assessment_solution_id: Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects.
        :param pulumi.Input[str] customer_storage_account_arm_id: The ARM id of the storage account used for interactions when public access is
               disabled.
        :param pulumi.Input[str] customer_workspace_id: The ARM id of service map workspace created by customer.
        :param pulumi.Input[str] customer_workspace_location: Location of service map workspace created by customer.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] project_name: Assessment Project Name
        :param pulumi.Input[Union[str, 'ProjectStatus']] project_status: Assessment project status.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] public_network_access: This value can be set to 'enabled' to avoid breaking changes on existing
               customer resources and templates. If set to 'disabled', traffic over public
               interface is not allowed, and private endpoint connections would be the
               exclusive access method.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssessmentProjectsOperationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Assessment project site resource.

        :param str resource_name: The name of the resource.
        :param AssessmentProjectsOperationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssessmentProjectsOperationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_solution_id: Optional[pulumi.Input[str]] = None,
                 customer_storage_account_arm_id: Optional[pulumi.Input[str]] = None,
                 customer_workspace_id: Optional[pulumi.Input[str]] = None,
                 customer_workspace_location: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 project_status: Optional[pulumi.Input[Union[str, 'ProjectStatus']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 public_network_access: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssessmentProjectsOperationArgs.__new__(AssessmentProjectsOperationArgs)

            __props__.__dict__["assessment_solution_id"] = assessment_solution_id
            __props__.__dict__["customer_storage_account_arm_id"] = customer_storage_account_arm_id
            __props__.__dict__["customer_workspace_id"] = customer_workspace_id
            __props__.__dict__["customer_workspace_location"] = customer_workspace_location
            __props__.__dict__["location"] = location
            __props__.__dict__["project_name"] = project_name
            __props__.__dict__["project_status"] = project_status
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_timestamp"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["service_endpoint"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_timestamp"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate:AssessmentProjectsOperation"), pulumi.Alias(type_="azure-native:migrate/v20191001:AssessmentProjectsOperation"), pulumi.Alias(type_="azure-native:migrate/v20230315:AssessmentProjectsOperation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AssessmentProjectsOperation, __self__).__init__(
            'azure-native:migrate/v20230401preview:AssessmentProjectsOperation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AssessmentProjectsOperation':
        """
        Get an existing AssessmentProjectsOperation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssessmentProjectsOperationArgs.__new__(AssessmentProjectsOperationArgs)

        __props__.__dict__["assessment_solution_id"] = None
        __props__.__dict__["created_timestamp"] = None
        __props__.__dict__["customer_storage_account_arm_id"] = None
        __props__.__dict__["customer_workspace_id"] = None
        __props__.__dict__["customer_workspace_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["project_status"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["service_endpoint"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_timestamp"] = None
        return AssessmentProjectsOperation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assessmentSolutionId")
    def assessment_solution_id(self) -> pulumi.Output[Optional[str]]:
        """
        Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects.
        """
        return pulumi.get(self, "assessment_solution_id")

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[str]:
        """
        Time when this project was created. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ARM id of the storage account used for interactions when public access is
        disabled.
        """
        return pulumi.get(self, "customer_storage_account_arm_id")

    @property
    @pulumi.getter(name="customerWorkspaceId")
    def customer_workspace_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ARM id of service map workspace created by customer.
        """
        return pulumi.get(self, "customer_workspace_id")

    @property
    @pulumi.getter(name="customerWorkspaceLocation")
    def customer_workspace_location(self) -> pulumi.Output[Optional[str]]:
        """
        Location of service map workspace created by customer.
        """
        return pulumi.get(self, "customer_workspace_location")

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
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        The list of private endpoint connections to the project.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="projectStatus")
    def project_status(self) -> pulumi.Output[Optional[str]]:
        """
        Assessment project status.
        """
        return pulumi.get(self, "project_status")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        This value can be set to 'enabled' to avoid breaking changes on existing
        customer resources and templates. If set to 'disabled', traffic over public
        interface is not allowed, and private endpoint connections would be the
        exclusive access method.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint at which the collector agent can call agent REST API.
        """
        return pulumi.get(self, "service_endpoint")

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

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[str]:
        """
        Time when this project was last updated. Date-Time represented in ISO-8601
        format.
        """
        return pulumi.get(self, "updated_timestamp")

