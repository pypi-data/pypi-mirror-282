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

__all__ = ['DaprComponentArgs', 'DaprComponent']

@pulumi.input_type
class DaprComponentArgs:
    def __init__(__self__, *,
                 environment_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 component_type: Optional[pulumi.Input[str]] = None,
                 ignore_errors: Optional[pulumi.Input[bool]] = None,
                 init_timeout: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Sequence[pulumi.Input['DaprMetadataArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[Sequence[pulumi.Input['SecretArgs']]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DaprComponent resource.
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] component_type: Component type
        :param pulumi.Input[bool] ignore_errors: Boolean describing if the component errors are ignores
        :param pulumi.Input[str] init_timeout: Initialization timeout
        :param pulumi.Input[Sequence[pulumi.Input['DaprMetadataArgs']]] metadata: Component metadata
        :param pulumi.Input[str] name: Name of the Dapr Component.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Names of container apps that can use this Dapr component
        :param pulumi.Input[Sequence[pulumi.Input['SecretArgs']]] secrets: Collection of secrets used by a Dapr component
        :param pulumi.Input[str] version: Component version
        """
        pulumi.set(__self__, "environment_name", environment_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if component_type is not None:
            pulumi.set(__self__, "component_type", component_type)
        if ignore_errors is not None:
            pulumi.set(__self__, "ignore_errors", ignore_errors)
        if init_timeout is not None:
            pulumi.set(__self__, "init_timeout", init_timeout)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if secrets is not None:
            pulumi.set(__self__, "secrets", secrets)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[str]:
        """
        Name of the Managed Environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_name", value)

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
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[str]]:
        """
        Component type
        """
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean describing if the component errors are ignores
        """
        return pulumi.get(self, "ignore_errors")

    @ignore_errors.setter
    def ignore_errors(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_errors", value)

    @property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> Optional[pulumi.Input[str]]:
        """
        Initialization timeout
        """
        return pulumi.get(self, "init_timeout")

    @init_timeout.setter
    def init_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "init_timeout", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DaprMetadataArgs']]]]:
        """
        Component metadata
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DaprMetadataArgs']]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Dapr Component.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Names of container apps that can use this Dapr component
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecretArgs']]]]:
        """
        Collection of secrets used by a Dapr component
        """
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecretArgs']]]]):
        pulumi.set(self, "secrets", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Component version
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class DaprComponent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 ignore_errors: Optional[pulumi.Input[bool]] = None,
                 init_timeout: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DaprMetadataArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecretArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Dapr Component.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] component_type: Component type
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[bool] ignore_errors: Boolean describing if the component errors are ignores
        :param pulumi.Input[str] init_timeout: Initialization timeout
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DaprMetadataArgs']]]] metadata: Component metadata
        :param pulumi.Input[str] name: Name of the Dapr Component.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Names of container apps that can use this Dapr component
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecretArgs']]]] secrets: Collection of secrets used by a Dapr component
        :param pulumi.Input[str] version: Component version
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DaprComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Dapr Component.

        :param str resource_name: The name of the resource.
        :param DaprComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DaprComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 ignore_errors: Optional[pulumi.Input[bool]] = None,
                 init_timeout: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DaprMetadataArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecretArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DaprComponentArgs.__new__(DaprComponentArgs)

            __props__.__dict__["component_type"] = component_type
            if environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_name'")
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["ignore_errors"] = ignore_errors
            __props__.__dict__["init_timeout"] = init_timeout
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["secrets"] = secrets
            __props__.__dict__["version"] = version
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20220301:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20220601preview:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20221001:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20221101preview:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20230401preview:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20230501:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20230502preview:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20230801preview:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20231102preview:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20240202preview:DaprComponent"), pulumi.Alias(type_="azure-native:app/v20240301:DaprComponent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DaprComponent, __self__).__init__(
            'azure-native:app/v20220101preview:DaprComponent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DaprComponent':
        """
        Get an existing DaprComponent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DaprComponentArgs.__new__(DaprComponentArgs)

        __props__.__dict__["component_type"] = None
        __props__.__dict__["ignore_errors"] = None
        __props__.__dict__["init_timeout"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["secrets"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return DaprComponent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Output[Optional[str]]:
        """
        Component type
        """
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean describing if the component errors are ignores
        """
        return pulumi.get(self, "ignore_errors")

    @property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> pulumi.Output[Optional[str]]:
        """
        Initialization timeout
        """
        return pulumi.get(self, "init_timeout")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Sequence['outputs.DaprMetadataResponse']]]:
        """
        Component metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Names of container apps that can use this Dapr component
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def secrets(self) -> pulumi.Output[Optional[Sequence['outputs.SecretResponse']]]:
        """
        Collection of secrets used by a Dapr component
        """
        return pulumi.get(self, "secrets")

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

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Component version
        """
        return pulumi.get(self, "version")

