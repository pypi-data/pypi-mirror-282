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

__all__ = ['GlobalRulestackArgs', 'GlobalRulestack']

@pulumi.input_type
class GlobalRulestackArgs:
    def __init__(__self__, *,
                 associated_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_mode: Optional[pulumi.Input[Union[str, 'DefaultMode']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_rulestack_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 min_app_id_version: Optional[pulumi.Input[str]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 pan_location: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[Union[str, 'ScopeType']]] = None,
                 security_services: Optional[pulumi.Input['SecurityServicesArgs']] = None):
        """
        The set of arguments for constructing a GlobalRulestack resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_subscriptions: subscription scope of global rulestack
        :param pulumi.Input[Union[str, 'DefaultMode']] default_mode: Mode for default rules creation
        :param pulumi.Input[str] description: rulestack description
        :param pulumi.Input[str] global_rulestack_name: GlobalRulestack resource name
        :param pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs'] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] location: Global Location
        :param pulumi.Input[str] min_app_id_version: minimum version
        :param pulumi.Input[str] pan_etag: PanEtag info
        :param pulumi.Input[str] pan_location: Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        :param pulumi.Input[Union[str, 'ScopeType']] scope: Rulestack Type
        :param pulumi.Input['SecurityServicesArgs'] security_services: Security Profile
        """
        if associated_subscriptions is not None:
            pulumi.set(__self__, "associated_subscriptions", associated_subscriptions)
        if default_mode is not None:
            pulumi.set(__self__, "default_mode", default_mode)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if global_rulestack_name is not None:
            pulumi.set(__self__, "global_rulestack_name", global_rulestack_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if min_app_id_version is not None:
            pulumi.set(__self__, "min_app_id_version", min_app_id_version)
        if pan_etag is not None:
            pulumi.set(__self__, "pan_etag", pan_etag)
        if pan_location is not None:
            pulumi.set(__self__, "pan_location", pan_location)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if security_services is not None:
            pulumi.set(__self__, "security_services", security_services)

    @property
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        subscription scope of global rulestack
        """
        return pulumi.get(self, "associated_subscriptions")

    @associated_subscriptions.setter
    def associated_subscriptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "associated_subscriptions", value)

    @property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[pulumi.Input[Union[str, 'DefaultMode']]]:
        """
        Mode for default rules creation
        """
        return pulumi.get(self, "default_mode")

    @default_mode.setter
    def default_mode(self, value: Optional[pulumi.Input[Union[str, 'DefaultMode']]]):
        pulumi.set(self, "default_mode", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        rulestack description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="globalRulestackName")
    def global_rulestack_name(self) -> Optional[pulumi.Input[str]]:
        """
        GlobalRulestack resource name
        """
        return pulumi.get(self, "global_rulestack_name")

    @global_rulestack_name.setter
    def global_rulestack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_rulestack_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['AzureResourceManagerManagedIdentityPropertiesArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Global Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> Optional[pulumi.Input[str]]:
        """
        minimum version
        """
        return pulumi.get(self, "min_app_id_version")

    @min_app_id_version.setter
    def min_app_id_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "min_app_id_version", value)

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[pulumi.Input[str]]:
        """
        PanEtag info
        """
        return pulumi.get(self, "pan_etag")

    @pan_etag.setter
    def pan_etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pan_etag", value)

    @property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> Optional[pulumi.Input[str]]:
        """
        Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        """
        return pulumi.get(self, "pan_location")

    @pan_location.setter
    def pan_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pan_location", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Union[str, 'ScopeType']]]:
        """
        Rulestack Type
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[Union[str, 'ScopeType']]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="securityServices")
    def security_services(self) -> Optional[pulumi.Input['SecurityServicesArgs']]:
        """
        Security Profile
        """
        return pulumi.get(self, "security_services")

    @security_services.setter
    def security_services(self, value: Optional[pulumi.Input['SecurityServicesArgs']]):
        pulumi.set(self, "security_services", value)


class GlobalRulestack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_mode: Optional[pulumi.Input[Union[str, 'DefaultMode']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_rulestack_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['AzureResourceManagerManagedIdentityPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 min_app_id_version: Optional[pulumi.Input[str]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 pan_location: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[Union[str, 'ScopeType']]] = None,
                 security_services: Optional[pulumi.Input[pulumi.InputType['SecurityServicesArgs']]] = None,
                 __props__=None):
        """
        PaloAltoNetworks GlobalRulestack

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_subscriptions: subscription scope of global rulestack
        :param pulumi.Input[Union[str, 'DefaultMode']] default_mode: Mode for default rules creation
        :param pulumi.Input[str] description: rulestack description
        :param pulumi.Input[str] global_rulestack_name: GlobalRulestack resource name
        :param pulumi.Input[pulumi.InputType['AzureResourceManagerManagedIdentityPropertiesArgs']] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] location: Global Location
        :param pulumi.Input[str] min_app_id_version: minimum version
        :param pulumi.Input[str] pan_etag: PanEtag info
        :param pulumi.Input[str] pan_location: Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        :param pulumi.Input[Union[str, 'ScopeType']] scope: Rulestack Type
        :param pulumi.Input[pulumi.InputType['SecurityServicesArgs']] security_services: Security Profile
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GlobalRulestackArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        PaloAltoNetworks GlobalRulestack

        :param str resource_name: The name of the resource.
        :param GlobalRulestackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalRulestackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_mode: Optional[pulumi.Input[Union[str, 'DefaultMode']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_rulestack_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['AzureResourceManagerManagedIdentityPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 min_app_id_version: Optional[pulumi.Input[str]] = None,
                 pan_etag: Optional[pulumi.Input[str]] = None,
                 pan_location: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[Union[str, 'ScopeType']]] = None,
                 security_services: Optional[pulumi.Input[pulumi.InputType['SecurityServicesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GlobalRulestackArgs.__new__(GlobalRulestackArgs)

            __props__.__dict__["associated_subscriptions"] = associated_subscriptions
            __props__.__dict__["default_mode"] = default_mode
            __props__.__dict__["description"] = description
            __props__.__dict__["global_rulestack_name"] = global_rulestack_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["min_app_id_version"] = min_app_id_version
            __props__.__dict__["pan_etag"] = pan_etag
            __props__.__dict__["pan_location"] = pan_location
            __props__.__dict__["scope"] = scope
            __props__.__dict__["security_services"] = security_services
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cloudngfw:GlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829preview:GlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901:GlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901preview:GlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20231010preview:GlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20240119preview:GlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20240207preview:GlobalRulestack")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GlobalRulestack, __self__).__init__(
            'azure-native:cloudngfw/v20220829:GlobalRulestack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GlobalRulestack':
        """
        Get an existing GlobalRulestack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GlobalRulestackArgs.__new__(GlobalRulestackArgs)

        __props__.__dict__["associated_subscriptions"] = None
        __props__.__dict__["default_mode"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["min_app_id_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pan_etag"] = None
        __props__.__dict__["pan_location"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["security_services"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return GlobalRulestack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        subscription scope of global rulestack
        """
        return pulumi.get(self, "associated_subscriptions")

    @property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Mode for default rules creation
        """
        return pulumi.get(self, "default_mode")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        rulestack description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.AzureResourceManagerManagedIdentityPropertiesResponse']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Global Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> pulumi.Output[Optional[str]]:
        """
        minimum version
        """
        return pulumi.get(self, "min_app_id_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> pulumi.Output[Optional[str]]:
        """
        PanEtag info
        """
        return pulumi.get(self, "pan_etag")

    @property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> pulumi.Output[Optional[str]]:
        """
        Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        """
        return pulumi.get(self, "pan_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        Rulestack Type
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="securityServices")
    def security_services(self) -> pulumi.Output[Optional['outputs.SecurityServicesResponse']]:
        """
        Security Profile
        """
        return pulumi.get(self, "security_services")

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

