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

__all__ = ['ConnectorArgs', 'Connector']

@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 source_resource_id: pulumi.Input[str],
                 connector_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['UserAssignedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input['ManagedRGConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Connector resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] source_resource_id: Defines the ID of the connector's source resource.
        :param pulumi.Input[str] connector_name: The name of the connector resource
        :param pulumi.Input['UserAssignedServiceIdentityArgs'] identity: Managed service identity (user assigned identities)
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ManagedRGConfigurationArgs'] managed_resource_group_configuration: Managed resource group configuration
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_resource_id", source_resource_id)
        if connector_name is not None:
            pulumi.set(__self__, "connector_name", connector_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration is not None:
            pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
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
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Input[str]:
        """
        Defines the ID of the connector's source resource.
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_resource_id", value)

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connector resource
        """
        return pulumi.get(self, "connector_name")

    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['UserAssignedServiceIdentityArgs']]:
        """
        Managed service identity (user assigned identities)
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['UserAssignedServiceIdentityArgs']]):
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
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional[pulumi.Input['ManagedRGConfigurationArgs']]:
        """
        Managed resource group configuration
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @managed_resource_group_configuration.setter
    def managed_resource_group_configuration(self, value: Optional[pulumi.Input['ManagedRGConfigurationArgs']]):
        pulumi.set(self, "managed_resource_group_configuration", value)

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


class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['UserAssignedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[pulumi.InputType['ManagedRGConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Define the connector resource.
        Azure REST API version: 2023-10-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connector_name: The name of the connector resource
        :param pulumi.Input[pulumi.InputType['UserAssignedServiceIdentityArgs']] identity: Managed service identity (user assigned identities)
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['ManagedRGConfigurationArgs']] managed_resource_group_configuration: Managed resource group configuration
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] source_resource_id: Defines the ID of the connector's source resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Define the connector resource.
        Azure REST API version: 2023-10-01-preview.

        :param str resource_name: The name of the resource.
        :param ConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['UserAssignedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[pulumi.InputType['ManagedRGConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorArgs.__new__(ConnectorArgs)

            __props__.__dict__["connector_name"] = connector_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_resource_group_configuration"] = managed_resource_group_configuration
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_resource_id'")
            __props__.__dict__["source_resource_id"] = source_resource_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["errors"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:workloads/v20231001preview:Connector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Connector, __self__).__init__(
            'azure-native:workloads:Connector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Connector':
        """
        Get an existing Connector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectorArgs.__new__(ConnectorArgs)

        __props__.__dict__["errors"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_resource_group_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_resource_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Connector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output['outputs.ConnectorErrorDefinitionResponse']:
        """
        Indicates any errors on the connector resource.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.UserAssignedServiceIdentityResponse']]:
        """
        Managed service identity (user assigned identities)
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> pulumi.Output[Optional['outputs.ManagedRGConfigurationResponse']]:
        """
        Managed resource group configuration
        """
        return pulumi.get(self, "managed_resource_group_configuration")

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
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Output[str]:
        """
        Defines the ID of the connector's source resource.
        """
        return pulumi.get(self, "source_resource_id")

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

