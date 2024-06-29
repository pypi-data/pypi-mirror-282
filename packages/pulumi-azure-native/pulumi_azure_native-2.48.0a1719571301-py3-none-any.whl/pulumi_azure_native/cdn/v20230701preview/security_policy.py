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

__all__ = ['SecurityPolicyArgs', 'SecurityPolicy']

@pulumi.input_type
class SecurityPolicyArgs:
    def __init__(__self__, *,
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 parameters: Optional[pulumi.Input['SecurityPolicyWebApplicationFirewallParametersArgs']] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityPolicy resource.
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['SecurityPolicyWebApplicationFirewallParametersArgs'] parameters: object which contains security policy parameters
        :param pulumi.Input[str] security_policy_name: Name of the security policy under the profile.
        """
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if security_policy_name is not None:
            pulumi.set(__self__, "security_policy_name", security_policy_name)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input['SecurityPolicyWebApplicationFirewallParametersArgs']]:
        """
        object which contains security policy parameters
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input['SecurityPolicyWebApplicationFirewallParametersArgs']]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the security policy under the profile.
        """
        return pulumi.get(self, "security_policy_name")

    @security_policy_name.setter
    def security_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_policy_name", value)


class SecurityPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['SecurityPolicyWebApplicationFirewallParametersArgs']]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        SecurityPolicy association for AzureFrontDoor profile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SecurityPolicyWebApplicationFirewallParametersArgs']] parameters: object which contains security policy parameters
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] security_policy_name: Name of the security policy under the profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SecurityPolicy association for AzureFrontDoor profile

        :param str resource_name: The name of the resource.
        :param SecurityPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['SecurityPolicyWebApplicationFirewallParametersArgs']]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityPolicyArgs.__new__(SecurityPolicyArgs)

            __props__.__dict__["parameters"] = parameters
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["security_policy_name"] = security_policy_name
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn:SecurityPolicy"), pulumi.Alias(type_="azure-native:cdn/v20200901:SecurityPolicy"), pulumi.Alias(type_="azure-native:cdn/v20210601:SecurityPolicy"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:SecurityPolicy"), pulumi.Alias(type_="azure-native:cdn/v20221101preview:SecurityPolicy"), pulumi.Alias(type_="azure-native:cdn/v20230501:SecurityPolicy"), pulumi.Alias(type_="azure-native:cdn/v20240201:SecurityPolicy"), pulumi.Alias(type_="azure-native:cdn/v20240501preview:SecurityPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SecurityPolicy, __self__).__init__(
            'azure-native:cdn/v20230701preview:SecurityPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityPolicy':
        """
        Get an existing SecurityPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityPolicyArgs.__new__(SecurityPolicyArgs)

        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["profile_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SecurityPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional['outputs.SecurityPolicyWebApplicationFirewallParametersResponse']]:
        """
        object which contains security policy parameters
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[str]:
        """
        The name of the profile which holds the security policy.
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

