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

__all__ = ['EndpointDeploymentArgs', 'EndpointDeployment']

@pulumi.input_type
class EndpointDeploymentArgs:
    def __init__(__self__, *,
                 endpoint_name: pulumi.Input[str],
                 properties: pulumi.Input[Union['ContentSafetyEndpointDeploymentResourcePropertiesArgs', 'ManagedOnlineEndpointDeploymentResourcePropertiesArgs', 'OpenAIEndpointDeploymentResourcePropertiesArgs', 'SpeechEndpointDeploymentResourcePropertiesArgs']],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 deployment_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EndpointDeployment resource.
        :param pulumi.Input[str] endpoint_name: Name of the endpoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Azure Machine Learning Workspace Name
        :param pulumi.Input[str] deployment_name: Name of the deployment resource
        """
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if deployment_name is not None:
            pulumi.set(__self__, "deployment_name", deployment_name)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[str]:
        """
        Name of the endpoint resource.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union['ContentSafetyEndpointDeploymentResourcePropertiesArgs', 'ManagedOnlineEndpointDeploymentResourcePropertiesArgs', 'OpenAIEndpointDeploymentResourcePropertiesArgs', 'SpeechEndpointDeploymentResourcePropertiesArgs']]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Union['ContentSafetyEndpointDeploymentResourcePropertiesArgs', 'ManagedOnlineEndpointDeploymentResourcePropertiesArgs', 'OpenAIEndpointDeploymentResourcePropertiesArgs', 'SpeechEndpointDeploymentResourcePropertiesArgs']]):
        pulumi.set(self, "properties", value)

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
        Azure Machine Learning Workspace Name
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the deployment resource
        """
        return pulumi.get(self, "deployment_name")

    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_name", value)


class EndpointDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ContentSafetyEndpointDeploymentResourcePropertiesArgs'], pulumi.InputType['ManagedOnlineEndpointDeploymentResourcePropertiesArgs'], pulumi.InputType['OpenAIEndpointDeploymentResourcePropertiesArgs'], pulumi.InputType['SpeechEndpointDeploymentResourcePropertiesArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure REST API version: 2024-01-01-preview.

        Other available API versions: 2024-04-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_name: Name of the deployment resource
        :param pulumi.Input[str] endpoint_name: Name of the endpoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Azure Machine Learning Workspace Name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointDeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure REST API version: 2024-01-01-preview.

        Other available API versions: 2024-04-01-preview.

        :param str resource_name: The name of the resource.
        :param EndpointDeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointDeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ContentSafetyEndpointDeploymentResourcePropertiesArgs'], pulumi.InputType['ManagedOnlineEndpointDeploymentResourcePropertiesArgs'], pulumi.InputType['OpenAIEndpointDeploymentResourcePropertiesArgs'], pulumi.InputType['SpeechEndpointDeploymentResourcePropertiesArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EndpointDeploymentArgs.__new__(EndpointDeploymentArgs)

            __props__.__dict__["deployment_name"] = deployment_name
            if endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_name'")
            __props__.__dict__["endpoint_name"] = endpoint_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices/v20240101preview:EndpointDeployment"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401preview:EndpointDeployment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EndpointDeployment, __self__).__init__(
            'azure-native:machinelearningservices:EndpointDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EndpointDeployment':
        """
        Get an existing EndpointDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EndpointDeploymentArgs.__new__(EndpointDeploymentArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return EndpointDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
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

