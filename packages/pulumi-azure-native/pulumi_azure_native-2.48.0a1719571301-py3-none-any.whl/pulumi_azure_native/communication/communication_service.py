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

__all__ = ['CommunicationServiceArgs', 'CommunicationService']

@pulumi.input_type
class CommunicationServiceArgs:
    def __init__(__self__, *,
                 data_location: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 communication_service_name: Optional[pulumi.Input[str]] = None,
                 linked_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CommunicationService resource.
        :param pulumi.Input[str] data_location: The location where the communication service stores its data at rest.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] communication_service_name: The name of the CommunicationService resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] linked_domains: List of email Domain resource Ids.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "data_location", data_location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if communication_service_name is not None:
            pulumi.set(__self__, "communication_service_name", communication_service_name)
        if linked_domains is not None:
            pulumi.set(__self__, "linked_domains", linked_domains)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> pulumi.Input[str]:
        """
        The location where the communication service stores its data at rest.
        """
        return pulumi.get(self, "data_location")

    @data_location.setter
    def data_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_location", value)

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
    @pulumi.getter(name="communicationServiceName")
    def communication_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the CommunicationService resource.
        """
        return pulumi.get(self, "communication_service_name")

    @communication_service_name.setter
    def communication_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "communication_service_name", value)

    @property
    @pulumi.getter(name="linkedDomains")
    def linked_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of email Domain resource Ids.
        """
        return pulumi.get(self, "linked_domains")

    @linked_domains.setter
    def linked_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "linked_domains", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class CommunicationService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 communication_service_name: Optional[pulumi.Input[str]] = None,
                 data_location: Optional[pulumi.Input[str]] = None,
                 linked_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A class representing a CommunicationService resource.
        Azure REST API version: 2023-03-31. Prior API version in Azure Native 1.x: 2020-08-20.

        Other available API versions: 2023-04-01, 2023-04-01-preview, 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] communication_service_name: The name of the CommunicationService resource.
        :param pulumi.Input[str] data_location: The location where the communication service stores its data at rest.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] linked_domains: List of email Domain resource Ids.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CommunicationServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A class representing a CommunicationService resource.
        Azure REST API version: 2023-03-31. Prior API version in Azure Native 1.x: 2020-08-20.

        Other available API versions: 2023-04-01, 2023-04-01-preview, 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param CommunicationServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CommunicationServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 communication_service_name: Optional[pulumi.Input[str]] = None,
                 data_location: Optional[pulumi.Input[str]] = None,
                 linked_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CommunicationServiceArgs.__new__(CommunicationServiceArgs)

            __props__.__dict__["communication_service_name"] = communication_service_name
            if data_location is None and not opts.urn:
                raise TypeError("Missing required property 'data_location'")
            __props__.__dict__["data_location"] = data_location
            __props__.__dict__["linked_domains"] = linked_domains
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["host_name"] = None
            __props__.__dict__["immutable_resource_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["notification_hub_id"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:communication/v20200820:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20200820preview:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20211001preview:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20220701preview:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20230301preview:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20230331:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20230401:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20230401preview:CommunicationService"), pulumi.Alias(type_="azure-native:communication/v20230601preview:CommunicationService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CommunicationService, __self__).__init__(
            'azure-native:communication:CommunicationService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CommunicationService':
        """
        Get an existing CommunicationService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CommunicationServiceArgs.__new__(CommunicationServiceArgs)

        __props__.__dict__["data_location"] = None
        __props__.__dict__["host_name"] = None
        __props__.__dict__["immutable_resource_id"] = None
        __props__.__dict__["linked_domains"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_hub_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return CommunicationService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> pulumi.Output[str]:
        """
        The location where the communication service stores its data at rest.
        """
        return pulumi.get(self, "data_location")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        FQDN of the CommunicationService instance.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="immutableResourceId")
    def immutable_resource_id(self) -> pulumi.Output[str]:
        """
        The immutable resource Id of the communication service.
        """
        return pulumi.get(self, "immutable_resource_id")

    @property
    @pulumi.getter(name="linkedDomains")
    def linked_domains(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of email Domain resource Ids.
        """
        return pulumi.get(self, "linked_domains")

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
    @pulumi.getter(name="notificationHubId")
    def notification_hub_id(self) -> pulumi.Output[str]:
        """
        Resource ID of an Azure Notification Hub linked to this resource.
        """
        return pulumi.get(self, "notification_hub_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
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
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of the CommunicationService resource. Probably you need the same or higher version of client SDKs.
        """
        return pulumi.get(self, "version")

