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

__all__ = ['SmfDeploymentArgs', 'SmfDeployment']

@pulumi.input_type
class SmfDeploymentArgs:
    def __init__(__self__, *,
                 cluster_service: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 component_parameters: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 secrets_parameters: Optional[pulumi.Input[str]] = None,
                 smf_deployment_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SmfDeployment resource.
        :param pulumi.Input[str] cluster_service: Reference to cluster where the Network Function is deployed
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] component_parameters: Azure for Operators 5G Core SMF component parameters
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] secrets_parameters: Azure for Operators 5G Core SMF secrets parameters
        :param pulumi.Input[str] smf_deployment_name: The name of the SmfDeployment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "cluster_service", cluster_service)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if component_parameters is not None:
            pulumi.set(__self__, "component_parameters", component_parameters)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if secrets_parameters is not None:
            pulumi.set(__self__, "secrets_parameters", secrets_parameters)
        if smf_deployment_name is not None:
            pulumi.set(__self__, "smf_deployment_name", smf_deployment_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterService")
    def cluster_service(self) -> pulumi.Input[str]:
        """
        Reference to cluster where the Network Function is deployed
        """
        return pulumi.get(self, "cluster_service")

    @cluster_service.setter
    def cluster_service(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_service", value)

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
    @pulumi.getter(name="componentParameters")
    def component_parameters(self) -> Optional[pulumi.Input[str]]:
        """
        Azure for Operators 5G Core SMF component parameters
        """
        return pulumi.get(self, "component_parameters")

    @component_parameters.setter
    def component_parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_parameters", value)

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
    @pulumi.getter(name="secretsParameters")
    def secrets_parameters(self) -> Optional[pulumi.Input[str]]:
        """
        Azure for Operators 5G Core SMF secrets parameters
        """
        return pulumi.get(self, "secrets_parameters")

    @secrets_parameters.setter
    def secrets_parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secrets_parameters", value)

    @property
    @pulumi.getter(name="smfDeploymentName")
    def smf_deployment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SmfDeployment
        """
        return pulumi.get(self, "smf_deployment_name")

    @smf_deployment_name.setter
    def smf_deployment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "smf_deployment_name", value)

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


class SmfDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_service: Optional[pulumi.Input[str]] = None,
                 component_parameters: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secrets_parameters: Optional[pulumi.Input[str]] = None,
                 smf_deployment_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Azure for Operators 5G Core Session Management Function (SMF) Deployment Resource
        Azure REST API version: 2023-10-15-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_service: Reference to cluster where the Network Function is deployed
        :param pulumi.Input[str] component_parameters: Azure for Operators 5G Core SMF component parameters
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] secrets_parameters: Azure for Operators 5G Core SMF secrets parameters
        :param pulumi.Input[str] smf_deployment_name: The name of the SmfDeployment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SmfDeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure for Operators 5G Core Session Management Function (SMF) Deployment Resource
        Azure REST API version: 2023-10-15-preview.

        :param str resource_name: The name of the resource.
        :param SmfDeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SmfDeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_service: Optional[pulumi.Input[str]] = None,
                 component_parameters: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secrets_parameters: Optional[pulumi.Input[str]] = None,
                 smf_deployment_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SmfDeploymentArgs.__new__(SmfDeploymentArgs)

            if cluster_service is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_service'")
            __props__.__dict__["cluster_service"] = cluster_service
            __props__.__dict__["component_parameters"] = component_parameters
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["secrets_parameters"] = secrets_parameters
            __props__.__dict__["smf_deployment_name"] = smf_deployment_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["operational_status"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["release_version"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilepacketcore/v20231015preview:SmfDeployment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SmfDeployment, __self__).__init__(
            'azure-native:mobilepacketcore:SmfDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SmfDeployment':
        """
        Get an existing SmfDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SmfDeploymentArgs.__new__(SmfDeploymentArgs)

        __props__.__dict__["cluster_service"] = None
        __props__.__dict__["component_parameters"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operational_status"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["release_version"] = None
        __props__.__dict__["secrets_parameters"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SmfDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterService")
    def cluster_service(self) -> pulumi.Output[str]:
        """
        Reference to cluster where the Network Function is deployed
        """
        return pulumi.get(self, "cluster_service")

    @property
    @pulumi.getter(name="componentParameters")
    def component_parameters(self) -> pulumi.Output[Optional[str]]:
        """
        Azure for Operators 5G Core SMF component parameters
        """
        return pulumi.get(self, "component_parameters")

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
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> pulumi.Output['outputs.OperationalStatusResponse']:
        """
        Operational status
        """
        return pulumi.get(self, "operational_status")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> pulumi.Output[str]:
        """
        Release version. This is inherited from the cluster
        """
        return pulumi.get(self, "release_version")

    @property
    @pulumi.getter(name="secretsParameters")
    def secrets_parameters(self) -> pulumi.Output[Optional[str]]:
        """
        Azure for Operators 5G Core SMF secrets parameters
        """
        return pulumi.get(self, "secrets_parameters")

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

