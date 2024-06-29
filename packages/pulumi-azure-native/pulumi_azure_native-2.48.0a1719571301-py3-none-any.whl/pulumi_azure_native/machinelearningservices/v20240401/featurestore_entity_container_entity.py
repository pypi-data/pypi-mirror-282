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

__all__ = ['FeaturestoreEntityContainerEntityArgs', 'FeaturestoreEntityContainerEntity']

@pulumi.input_type
class FeaturestoreEntityContainerEntityArgs:
    def __init__(__self__, *,
                 featurestore_entity_container_properties: pulumi.Input['FeaturestoreEntityContainerArgs'],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FeaturestoreEntityContainerEntity resource.
        :param pulumi.Input['FeaturestoreEntityContainerArgs'] featurestore_entity_container_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] name: Container name. This is case-sensitive.
        """
        pulumi.set(__self__, "featurestore_entity_container_properties", featurestore_entity_container_properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="featurestoreEntityContainerProperties")
    def featurestore_entity_container_properties(self) -> pulumi.Input['FeaturestoreEntityContainerArgs']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "featurestore_entity_container_properties")

    @featurestore_entity_container_properties.setter
    def featurestore_entity_container_properties(self, value: pulumi.Input['FeaturestoreEntityContainerArgs']):
        pulumi.set(self, "featurestore_entity_container_properties", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Container name. This is case-sensitive.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class FeaturestoreEntityContainerEntity(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 featurestore_entity_container_properties: Optional[pulumi.Input[pulumi.InputType['FeaturestoreEntityContainerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure Resource Manager resource envelope.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FeaturestoreEntityContainerArgs']] featurestore_entity_container_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] name: Container name. This is case-sensitive.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FeaturestoreEntityContainerEntityArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure Resource Manager resource envelope.

        :param str resource_name: The name of the resource.
        :param FeaturestoreEntityContainerEntityArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FeaturestoreEntityContainerEntityArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 featurestore_entity_container_properties: Optional[pulumi.Input[pulumi.InputType['FeaturestoreEntityContainerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FeaturestoreEntityContainerEntityArgs.__new__(FeaturestoreEntityContainerEntityArgs)

            if featurestore_entity_container_properties is None and not opts.urn:
                raise TypeError("Missing required property 'featurestore_entity_container_properties'")
            __props__.__dict__["featurestore_entity_container_properties"] = featurestore_entity_container_properties
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices:FeaturestoreEntityContainerEntity"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230201preview:FeaturestoreEntityContainerEntity"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401preview:FeaturestoreEntityContainerEntity"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230601preview:FeaturestoreEntityContainerEntity"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230801preview:FeaturestoreEntityContainerEntity"), pulumi.Alias(type_="azure-native:machinelearningservices/v20231001:FeaturestoreEntityContainerEntity"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240101preview:FeaturestoreEntityContainerEntity"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401preview:FeaturestoreEntityContainerEntity")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FeaturestoreEntityContainerEntity, __self__).__init__(
            'azure-native:machinelearningservices/v20240401:FeaturestoreEntityContainerEntity',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FeaturestoreEntityContainerEntity':
        """
        Get an existing FeaturestoreEntityContainerEntity resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FeaturestoreEntityContainerEntityArgs.__new__(FeaturestoreEntityContainerEntityArgs)

        __props__.__dict__["featurestore_entity_container_properties"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return FeaturestoreEntityContainerEntity(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="featurestoreEntityContainerProperties")
    def featurestore_entity_container_properties(self) -> pulumi.Output['outputs.FeaturestoreEntityContainerResponse']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "featurestore_entity_container_properties")

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
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

