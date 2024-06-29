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

__all__ = ['DataManagerForAgricultureResourceArgs', 'DataManagerForAgricultureResource']

@pulumi.input_type
class DataManagerForAgricultureResourceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 data_manager_for_agriculture_resource_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 sensor_integration: Optional[pulumi.Input['SensorIntegrationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DataManagerForAgricultureResource resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] data_manager_for_agriculture_resource_name: DataManagerForAgriculture resource name.
        :param pulumi.Input['IdentityArgs'] identity: Identity for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Property to allow or block public traffic for an Azure Data Manager For Agriculture resource.
        :param pulumi.Input['SensorIntegrationArgs'] sensor_integration: Sensor integration request model.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_manager_for_agriculture_resource_name is not None:
            pulumi.set(__self__, "data_manager_for_agriculture_resource_name", data_manager_for_agriculture_resource_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if sensor_integration is not None:
            pulumi.set(__self__, "sensor_integration", sensor_integration)
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
    @pulumi.getter(name="dataManagerForAgricultureResourceName")
    def data_manager_for_agriculture_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        DataManagerForAgriculture resource name.
        """
        return pulumi.get(self, "data_manager_for_agriculture_resource_name")

    @data_manager_for_agriculture_resource_name.setter
    def data_manager_for_agriculture_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_manager_for_agriculture_resource_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        Property to allow or block public traffic for an Azure Data Manager For Agriculture resource.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="sensorIntegration")
    def sensor_integration(self) -> Optional[pulumi.Input['SensorIntegrationArgs']]:
        """
        Sensor integration request model.
        """
        return pulumi.get(self, "sensor_integration")

    @sensor_integration.setter
    def sensor_integration(self, value: Optional[pulumi.Input['SensorIntegrationArgs']]):
        pulumi.set(self, "sensor_integration", value)

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


class DataManagerForAgricultureResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_manager_for_agriculture_resource_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sensor_integration: Optional[pulumi.Input[pulumi.InputType['SensorIntegrationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Data Manager For Agriculture ARM Resource.
        Azure REST API version: 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_manager_for_agriculture_resource_name: DataManagerForAgriculture resource name.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: Identity for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Property to allow or block public traffic for an Azure Data Manager For Agriculture resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SensorIntegrationArgs']] sensor_integration: Sensor integration request model.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataManagerForAgricultureResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data Manager For Agriculture ARM Resource.
        Azure REST API version: 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param DataManagerForAgricultureResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataManagerForAgricultureResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_manager_for_agriculture_resource_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sensor_integration: Optional[pulumi.Input[pulumi.InputType['SensorIntegrationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataManagerForAgricultureResourceArgs.__new__(DataManagerForAgricultureResourceArgs)

            __props__.__dict__["data_manager_for_agriculture_resource_name"] = data_manager_for_agriculture_resource_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sensor_integration"] = sensor_integration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["instance_uri"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:agfoodplatform/v20200512preview:DataManagerForAgricultureResource"), pulumi.Alias(type_="azure-native:agfoodplatform/v20210901preview:DataManagerForAgricultureResource"), pulumi.Alias(type_="azure-native:agfoodplatform/v20230601preview:DataManagerForAgricultureResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataManagerForAgricultureResource, __self__).__init__(
            'azure-native:agfoodplatform:DataManagerForAgricultureResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataManagerForAgricultureResource':
        """
        Get an existing DataManagerForAgricultureResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataManagerForAgricultureResourceArgs.__new__(DataManagerForAgricultureResourceArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["instance_uri"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["sensor_integration"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DataManagerForAgricultureResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="instanceUri")
    def instance_uri(self) -> pulumi.Output[str]:
        """
        Uri of the Data Manager For Agriculture instance.
        """
        return pulumi.get(self, "instance_uri")

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
        Private endpoints.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Data Manager For Agriculture instance provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Property to allow or block public traffic for an Azure Data Manager For Agriculture resource.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="sensorIntegration")
    def sensor_integration(self) -> pulumi.Output[Optional['outputs.SensorIntegrationResponse']]:
        """
        Sensor integration request model.
        """
        return pulumi.get(self, "sensor_integration")

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

