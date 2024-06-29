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

__all__ = ['SapDiscoverySiteArgs', 'SapDiscoverySite']

@pulumi.input_type
class SapDiscoverySiteArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 master_site_id: Optional[pulumi.Input[str]] = None,
                 migrate_project_id: Optional[pulumi.Input[str]] = None,
                 sap_discovery_site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SapDiscoverySite resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location definition.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] master_site_id: The master site ID from Azure Migrate.
        :param pulumi.Input[str] migrate_project_id: The migrate project ID from Azure Migrate.
        :param pulumi.Input[str] sap_discovery_site_name: The name of the discovery site resource for SAP Migration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if master_site_id is not None:
            pulumi.set(__self__, "master_site_id", master_site_id)
        if migrate_project_id is not None:
            pulumi.set(__self__, "migrate_project_id", migrate_project_id)
        if sap_discovery_site_name is not None:
            pulumi.set(__self__, "sap_discovery_site_name", sap_discovery_site_name)
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
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extended location definition.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

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
    @pulumi.getter(name="masterSiteId")
    def master_site_id(self) -> Optional[pulumi.Input[str]]:
        """
        The master site ID from Azure Migrate.
        """
        return pulumi.get(self, "master_site_id")

    @master_site_id.setter
    def master_site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_site_id", value)

    @property
    @pulumi.getter(name="migrateProjectId")
    def migrate_project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The migrate project ID from Azure Migrate.
        """
        return pulumi.get(self, "migrate_project_id")

    @migrate_project_id.setter
    def migrate_project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "migrate_project_id", value)

    @property
    @pulumi.getter(name="sapDiscoverySiteName")
    def sap_discovery_site_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the discovery site resource for SAP Migration.
        """
        return pulumi.get(self, "sap_discovery_site_name")

    @sap_discovery_site_name.setter
    def sap_discovery_site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sap_discovery_site_name", value)

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


class SapDiscoverySite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 master_site_id: Optional[pulumi.Input[str]] = None,
                 migrate_project_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sap_discovery_site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Define the SAP Migration discovery site resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location definition.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] master_site_id: The master site ID from Azure Migrate.
        :param pulumi.Input[str] migrate_project_id: The migrate project ID from Azure Migrate.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sap_discovery_site_name: The name of the discovery site resource for SAP Migration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SapDiscoverySiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Define the SAP Migration discovery site resource.

        :param str resource_name: The name of the resource.
        :param SapDiscoverySiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SapDiscoverySiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 master_site_id: Optional[pulumi.Input[str]] = None,
                 migrate_project_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sap_discovery_site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SapDiscoverySiteArgs.__new__(SapDiscoverySiteArgs)

            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            __props__.__dict__["master_site_id"] = master_site_id
            __props__.__dict__["migrate_project_id"] = migrate_project_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sap_discovery_site_name"] = sap_discovery_site_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["errors"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:workloads:SapDiscoverySite")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SapDiscoverySite, __self__).__init__(
            'azure-native:workloads/v20231001preview:SapDiscoverySite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SapDiscoverySite':
        """
        Get an existing SapDiscoverySite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SapDiscoverySiteArgs.__new__(SapDiscoverySiteArgs)

        __props__.__dict__["errors"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["master_site_id"] = None
        __props__.__dict__["migrate_project_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SapDiscoverySite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output['outputs.SAPMigrateErrorResponse']:
        """
        Indicates any errors on the SAP Migration discovery site resource.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extended location definition.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="masterSiteId")
    def master_site_id(self) -> pulumi.Output[Optional[str]]:
        """
        The master site ID from Azure Migrate.
        """
        return pulumi.get(self, "master_site_id")

    @property
    @pulumi.getter(name="migrateProjectId")
    def migrate_project_id(self) -> pulumi.Output[Optional[str]]:
        """
        The migrate project ID from Azure Migrate.
        """
        return pulumi.get(self, "migrate_project_id")

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
        Defines the provisioning states.
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

