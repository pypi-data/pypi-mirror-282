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
from ._inputs import *

__all__ = ['PoolArgs', 'Pool']

@pulumi.input_type
class PoolArgs:
    def __init__(__self__, *,
                 dev_box_definition_name: pulumi.Input[str],
                 license_type: pulumi.Input[Union[str, 'LicenseType']],
                 local_administrator: pulumi.Input[Union[str, 'LocalAdminStatus']],
                 network_connection_name: pulumi.Input[str],
                 project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 single_sign_on_status: Optional[pulumi.Input[Union[str, 'SingleSignOnStatus']]] = None,
                 stop_on_disconnect: Optional[pulumi.Input['StopOnDisconnectConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_type: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]] = None):
        """
        The set of arguments for constructing a Pool resource.
        :param pulumi.Input[str] dev_box_definition_name: Name of a Dev Box definition in parent Project of this Pool
        :param pulumi.Input[Union[str, 'LicenseType']] license_type: Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created.
        :param pulumi.Input[Union[str, 'LocalAdminStatus']] local_administrator: Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box.
        :param pulumi.Input[str] network_connection_name: Name of a Network Connection in parent Project of this Pool
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] display_name: The display name of the pool.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input[str]]] managed_virtual_network_regions: The regions of the managed virtual network (required when managedNetworkType is Managed).
        :param pulumi.Input[str] pool_name: Name of the pool.
        :param pulumi.Input[Union[str, 'SingleSignOnStatus']] single_sign_on_status: Indicates whether Dev Boxes in this pool are created with single sign on enabled. The also requires that single sign on be enabled on the tenant.
        :param pulumi.Input['StopOnDisconnectConfigurationArgs'] stop_on_disconnect: Stop on disconnect configuration settings for Dev Boxes created in this pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'VirtualNetworkType']] virtual_network_type: Indicates whether the pool uses a Virtual Network managed by Microsoft or a customer provided network.
        """
        pulumi.set(__self__, "dev_box_definition_name", dev_box_definition_name)
        pulumi.set(__self__, "license_type", license_type)
        pulumi.set(__self__, "local_administrator", local_administrator)
        pulumi.set(__self__, "network_connection_name", network_connection_name)
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_virtual_network_regions is not None:
            pulumi.set(__self__, "managed_virtual_network_regions", managed_virtual_network_regions)
        if pool_name is not None:
            pulumi.set(__self__, "pool_name", pool_name)
        if single_sign_on_status is not None:
            pulumi.set(__self__, "single_sign_on_status", single_sign_on_status)
        if stop_on_disconnect is not None:
            pulumi.set(__self__, "stop_on_disconnect", stop_on_disconnect)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_network_type is not None:
            pulumi.set(__self__, "virtual_network_type", virtual_network_type)

    @property
    @pulumi.getter(name="devBoxDefinitionName")
    def dev_box_definition_name(self) -> pulumi.Input[str]:
        """
        Name of a Dev Box definition in parent Project of this Pool
        """
        return pulumi.get(self, "dev_box_definition_name")

    @dev_box_definition_name.setter
    def dev_box_definition_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dev_box_definition_name", value)

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Input[Union[str, 'LicenseType']]:
        """
        Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created.
        """
        return pulumi.get(self, "license_type")

    @license_type.setter
    def license_type(self, value: pulumi.Input[Union[str, 'LicenseType']]):
        pulumi.set(self, "license_type", value)

    @property
    @pulumi.getter(name="localAdministrator")
    def local_administrator(self) -> pulumi.Input[Union[str, 'LocalAdminStatus']]:
        """
        Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box.
        """
        return pulumi.get(self, "local_administrator")

    @local_administrator.setter
    def local_administrator(self, value: pulumi.Input[Union[str, 'LocalAdminStatus']]):
        pulumi.set(self, "local_administrator", value)

    @property
    @pulumi.getter(name="networkConnectionName")
    def network_connection_name(self) -> pulumi.Input[str]:
        """
        Name of a Network Connection in parent Project of this Pool
        """
        return pulumi.get(self, "network_connection_name")

    @network_connection_name.setter
    def network_connection_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_connection_name", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        The name of the project.
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the pool.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

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
    @pulumi.getter(name="managedVirtualNetworkRegions")
    def managed_virtual_network_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The regions of the managed virtual network (required when managedNetworkType is Managed).
        """
        return pulumi.get(self, "managed_virtual_network_regions")

    @managed_virtual_network_regions.setter
    def managed_virtual_network_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "managed_virtual_network_regions", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the pool.
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter(name="singleSignOnStatus")
    def single_sign_on_status(self) -> Optional[pulumi.Input[Union[str, 'SingleSignOnStatus']]]:
        """
        Indicates whether Dev Boxes in this pool are created with single sign on enabled. The also requires that single sign on be enabled on the tenant.
        """
        return pulumi.get(self, "single_sign_on_status")

    @single_sign_on_status.setter
    def single_sign_on_status(self, value: Optional[pulumi.Input[Union[str, 'SingleSignOnStatus']]]):
        pulumi.set(self, "single_sign_on_status", value)

    @property
    @pulumi.getter(name="stopOnDisconnect")
    def stop_on_disconnect(self) -> Optional[pulumi.Input['StopOnDisconnectConfigurationArgs']]:
        """
        Stop on disconnect configuration settings for Dev Boxes created in this pool.
        """
        return pulumi.get(self, "stop_on_disconnect")

    @stop_on_disconnect.setter
    def stop_on_disconnect(self, value: Optional[pulumi.Input['StopOnDisconnectConfigurationArgs']]):
        pulumi.set(self, "stop_on_disconnect", value)

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

    @property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]]:
        """
        Indicates whether the pool uses a Virtual Network managed by Microsoft or a customer provided network.
        """
        return pulumi.get(self, "virtual_network_type")

    @virtual_network_type.setter
    def virtual_network_type(self, value: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]]):
        pulumi.set(self, "virtual_network_type", value)


class Pool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_box_definition_name: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[Union[str, 'LicenseType']]] = None,
                 local_administrator: Optional[pulumi.Input[Union[str, 'LocalAdminStatus']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 network_connection_name: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 single_sign_on_status: Optional[pulumi.Input[Union[str, 'SingleSignOnStatus']]] = None,
                 stop_on_disconnect: Optional[pulumi.Input[pulumi.InputType['StopOnDisconnectConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_type: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]] = None,
                 __props__=None):
        """
        A pool of Virtual Machines.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dev_box_definition_name: Name of a Dev Box definition in parent Project of this Pool
        :param pulumi.Input[str] display_name: The display name of the pool.
        :param pulumi.Input[Union[str, 'LicenseType']] license_type: Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created.
        :param pulumi.Input[Union[str, 'LocalAdminStatus']] local_administrator: Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input[str]]] managed_virtual_network_regions: The regions of the managed virtual network (required when managedNetworkType is Managed).
        :param pulumi.Input[str] network_connection_name: Name of a Network Connection in parent Project of this Pool
        :param pulumi.Input[str] pool_name: Name of the pool.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'SingleSignOnStatus']] single_sign_on_status: Indicates whether Dev Boxes in this pool are created with single sign on enabled. The also requires that single sign on be enabled on the tenant.
        :param pulumi.Input[pulumi.InputType['StopOnDisconnectConfigurationArgs']] stop_on_disconnect: Stop on disconnect configuration settings for Dev Boxes created in this pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'VirtualNetworkType']] virtual_network_type: Indicates whether the pool uses a Virtual Network managed by Microsoft or a customer provided network.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A pool of Virtual Machines.

        :param str resource_name: The name of the resource.
        :param PoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_box_definition_name: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[Union[str, 'LicenseType']]] = None,
                 local_administrator: Optional[pulumi.Input[Union[str, 'LocalAdminStatus']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 network_connection_name: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 single_sign_on_status: Optional[pulumi.Input[Union[str, 'SingleSignOnStatus']]] = None,
                 stop_on_disconnect: Optional[pulumi.Input[pulumi.InputType['StopOnDisconnectConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_type: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PoolArgs.__new__(PoolArgs)

            if dev_box_definition_name is None and not opts.urn:
                raise TypeError("Missing required property 'dev_box_definition_name'")
            __props__.__dict__["dev_box_definition_name"] = dev_box_definition_name
            __props__.__dict__["display_name"] = display_name
            if license_type is None and not opts.urn:
                raise TypeError("Missing required property 'license_type'")
            __props__.__dict__["license_type"] = license_type
            if local_administrator is None and not opts.urn:
                raise TypeError("Missing required property 'local_administrator'")
            __props__.__dict__["local_administrator"] = local_administrator
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_virtual_network_regions"] = managed_virtual_network_regions
            if network_connection_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_connection_name'")
            __props__.__dict__["network_connection_name"] = network_connection_name
            __props__.__dict__["pool_name"] = pool_name
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["single_sign_on_status"] = single_sign_on_status
            __props__.__dict__["stop_on_disconnect"] = stop_on_disconnect
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_network_type"] = virtual_network_type
            __props__.__dict__["dev_box_count"] = None
            __props__.__dict__["health_status"] = None
            __props__.__dict__["health_status_details"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20220801preview:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20220901preview:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20221111preview:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20230101preview:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20230401:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20230801preview:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20231001preview:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20240201:Pool"), pulumi.Alias(type_="azure-native:devcenter/v20240601preview:Pool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Pool, __self__).__init__(
            'azure-native:devcenter/v20240501preview:Pool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pool':
        """
        Get an existing Pool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PoolArgs.__new__(PoolArgs)

        __props__.__dict__["dev_box_count"] = None
        __props__.__dict__["dev_box_definition_name"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["health_status"] = None
        __props__.__dict__["health_status_details"] = None
        __props__.__dict__["license_type"] = None
        __props__.__dict__["local_administrator"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_virtual_network_regions"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_connection_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["single_sign_on_status"] = None
        __props__.__dict__["stop_on_disconnect"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_type"] = None
        return Pool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="devBoxCount")
    def dev_box_count(self) -> pulumi.Output[int]:
        """
        Indicates the number of provisioned Dev Boxes in this pool.
        """
        return pulumi.get(self, "dev_box_count")

    @property
    @pulumi.getter(name="devBoxDefinitionName")
    def dev_box_definition_name(self) -> pulumi.Output[str]:
        """
        Name of a Dev Box definition in parent Project of this Pool
        """
        return pulumi.get(self, "dev_box_definition_name")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the pool.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> pulumi.Output[str]:
        """
        Overall health status of the Pool. Indicates whether or not the Pool is available to create Dev Boxes.
        """
        return pulumi.get(self, "health_status")

    @property
    @pulumi.getter(name="healthStatusDetails")
    def health_status_details(self) -> pulumi.Output[Sequence['outputs.HealthStatusDetailResponse']]:
        """
        Details on the Pool health status to help diagnose issues. This is only populated when the pool status indicates the pool is in a non-healthy state
        """
        return pulumi.get(self, "health_status_details")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[str]:
        """
        Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter(name="localAdministrator")
    def local_administrator(self) -> pulumi.Output[str]:
        """
        Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box.
        """
        return pulumi.get(self, "local_administrator")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedVirtualNetworkRegions")
    def managed_virtual_network_regions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The regions of the managed virtual network (required when managedNetworkType is Managed).
        """
        return pulumi.get(self, "managed_virtual_network_regions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConnectionName")
    def network_connection_name(self) -> pulumi.Output[str]:
        """
        Name of a Network Connection in parent Project of this Pool
        """
        return pulumi.get(self, "network_connection_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="singleSignOnStatus")
    def single_sign_on_status(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether Dev Boxes in this pool are created with single sign on enabled. The also requires that single sign on be enabled on the tenant.
        """
        return pulumi.get(self, "single_sign_on_status")

    @property
    @pulumi.getter(name="stopOnDisconnect")
    def stop_on_disconnect(self) -> pulumi.Output[Optional['outputs.StopOnDisconnectConfigurationResponse']]:
        """
        Stop on disconnect configuration settings for Dev Boxes created in this pool.
        """
        return pulumi.get(self, "stop_on_disconnect")

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
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether the pool uses a Virtual Network managed by Microsoft or a customer provided network.
        """
        return pulumi.get(self, "virtual_network_type")

