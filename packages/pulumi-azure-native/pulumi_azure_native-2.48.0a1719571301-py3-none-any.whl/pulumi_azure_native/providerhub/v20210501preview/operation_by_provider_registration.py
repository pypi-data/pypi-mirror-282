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

__all__ = ['OperationByProviderRegistrationArgs', 'OperationByProviderRegistration']

@pulumi.input_type
class OperationByProviderRegistrationArgs:
    def __init__(__self__, *,
                 contents: pulumi.Input[Sequence[pulumi.Input['OperationsDefinitionArgs']]],
                 provider_namespace: pulumi.Input[str]):
        """
        The set of arguments for constructing a OperationByProviderRegistration resource.
        :param pulumi.Input[str] provider_namespace: The name of the resource provider hosted within ProviderHub.
        """
        pulumi.set(__self__, "contents", contents)
        pulumi.set(__self__, "provider_namespace", provider_namespace)

    @property
    @pulumi.getter
    def contents(self) -> pulumi.Input[Sequence[pulumi.Input['OperationsDefinitionArgs']]]:
        return pulumi.get(self, "contents")

    @contents.setter
    def contents(self, value: pulumi.Input[Sequence[pulumi.Input['OperationsDefinitionArgs']]]):
        pulumi.set(self, "contents", value)

    @property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> pulumi.Input[str]:
        """
        The name of the resource provider hosted within ProviderHub.
        """
        return pulumi.get(self, "provider_namespace")

    @provider_namespace.setter
    def provider_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_namespace", value)


class OperationByProviderRegistration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contents: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OperationsDefinitionArgs']]]]] = None,
                 provider_namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a OperationByProviderRegistration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] provider_namespace: The name of the resource provider hosted within ProviderHub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OperationByProviderRegistrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OperationByProviderRegistration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OperationByProviderRegistrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OperationByProviderRegistrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contents: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OperationsDefinitionArgs']]]]] = None,
                 provider_namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OperationByProviderRegistrationArgs.__new__(OperationByProviderRegistrationArgs)

            if contents is None and not opts.urn:
                raise TypeError("Missing required property 'contents'")
            __props__.__dict__["contents"] = contents
            if provider_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'provider_namespace'")
            __props__.__dict__["provider_namespace"] = provider_namespace
            __props__.__dict__["action_type"] = None
            __props__.__dict__["display"] = None
            __props__.__dict__["is_data_action"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["origin"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:providerhub:OperationByProviderRegistration"), pulumi.Alias(type_="azure-native:providerhub/v20201120:OperationByProviderRegistration"), pulumi.Alias(type_="azure-native:providerhub/v20210601preview:OperationByProviderRegistration"), pulumi.Alias(type_="azure-native:providerhub/v20210901preview:OperationByProviderRegistration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OperationByProviderRegistration, __self__).__init__(
            'azure-native:providerhub/v20210501preview:OperationByProviderRegistration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OperationByProviderRegistration':
        """
        Get an existing OperationByProviderRegistration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OperationByProviderRegistrationArgs.__new__(OperationByProviderRegistrationArgs)

        __props__.__dict__["action_type"] = None
        __props__.__dict__["display"] = None
        __props__.__dict__["is_data_action"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["origin"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return OperationByProviderRegistration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "action_type")

    @property
    @pulumi.getter
    def display(self) -> pulumi.Output['outputs.OperationsDefinitionResponseDisplay']:
        """
        Display information of the operation.
        """
        return pulumi.get(self, "display")

    @property
    @pulumi.getter(name="isDataAction")
    def is_data_action(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the operation applies to data-plane.
        """
        return pulumi.get(self, "is_data_action")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def origin(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

