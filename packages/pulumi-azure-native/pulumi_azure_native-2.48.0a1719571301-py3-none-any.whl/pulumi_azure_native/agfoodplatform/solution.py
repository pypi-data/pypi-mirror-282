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
from ._inputs import *

__all__ = ['SolutionArgs', 'Solution']

@pulumi.input_type
class SolutionArgs:
    def __init__(__self__, *,
                 data_manager_for_agriculture_resource_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input['SolutionPropertiesArgs']] = None,
                 solution_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Solution resource.
        :param pulumi.Input[str] data_manager_for_agriculture_resource_name: DataManagerForAgriculture resource name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SolutionPropertiesArgs'] properties: Solution resource properties.
        :param pulumi.Input[str] solution_id: SolutionId for Data Manager For Agriculture Resource.
        """
        pulumi.set(__self__, "data_manager_for_agriculture_resource_name", data_manager_for_agriculture_resource_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if solution_id is not None:
            pulumi.set(__self__, "solution_id", solution_id)

    @property
    @pulumi.getter(name="dataManagerForAgricultureResourceName")
    def data_manager_for_agriculture_resource_name(self) -> pulumi.Input[str]:
        """
        DataManagerForAgriculture resource name.
        """
        return pulumi.get(self, "data_manager_for_agriculture_resource_name")

    @data_manager_for_agriculture_resource_name.setter
    def data_manager_for_agriculture_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_manager_for_agriculture_resource_name", value)

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
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['SolutionPropertiesArgs']]:
        """
        Solution resource properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['SolutionPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="solutionId")
    def solution_id(self) -> Optional[pulumi.Input[str]]:
        """
        SolutionId for Data Manager For Agriculture Resource.
        """
        return pulumi.get(self, "solution_id")

    @solution_id.setter
    def solution_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_id", value)


class Solution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_manager_for_agriculture_resource_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['SolutionPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 solution_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Solution resource.
        Azure REST API version: 2023-06-01-preview.

        Other available API versions: 2021-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_manager_for_agriculture_resource_name: DataManagerForAgriculture resource name.
        :param pulumi.Input[pulumi.InputType['SolutionPropertiesArgs']] properties: Solution resource properties.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] solution_id: SolutionId for Data Manager For Agriculture Resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SolutionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Solution resource.
        Azure REST API version: 2023-06-01-preview.

        Other available API versions: 2021-09-01-preview.

        :param str resource_name: The name of the resource.
        :param SolutionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SolutionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_manager_for_agriculture_resource_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['SolutionPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 solution_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SolutionArgs.__new__(SolutionArgs)

            if data_manager_for_agriculture_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_manager_for_agriculture_resource_name'")
            __props__.__dict__["data_manager_for_agriculture_resource_name"] = data_manager_for_agriculture_resource_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["solution_id"] = solution_id
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:agfoodplatform/v20210901preview:Solution"), pulumi.Alias(type_="azure-native:agfoodplatform/v20230601preview:Solution")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Solution, __self__).__init__(
            'azure-native:agfoodplatform:Solution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Solution':
        """
        Get an existing Solution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SolutionArgs.__new__(SolutionArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Solution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        The ETag value to implement optimistic concurrency.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.SolutionPropertiesResponse']:
        """
        Solution resource properties.
        """
        return pulumi.get(self, "properties")

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

