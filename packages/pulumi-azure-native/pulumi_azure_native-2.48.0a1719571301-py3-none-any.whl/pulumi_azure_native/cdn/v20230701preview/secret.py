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

__all__ = ['SecretArgs', 'Secret']

@pulumi.input_type
class SecretArgs:
    def __init__(__self__, *,
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 parameters: Optional[pulumi.Input[Union['AzureFirstPartyManagedCertificateParametersArgs', 'CustomerCertificateParametersArgs', 'ManagedCertificateParametersArgs', 'UrlSigningKeyParametersArgs']]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Secret resource.
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Union['AzureFirstPartyManagedCertificateParametersArgs', 'CustomerCertificateParametersArgs', 'ManagedCertificateParametersArgs', 'UrlSigningKeyParametersArgs']] parameters: object which contains secret parameters
        :param pulumi.Input[str] secret_name: Name of the Secret under the profile.
        """
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if secret_name is not None:
            pulumi.set(__self__, "secret_name", secret_name)

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
    def parameters(self) -> Optional[pulumi.Input[Union['AzureFirstPartyManagedCertificateParametersArgs', 'CustomerCertificateParametersArgs', 'ManagedCertificateParametersArgs', 'UrlSigningKeyParametersArgs']]]:
        """
        object which contains secret parameters
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Union['AzureFirstPartyManagedCertificateParametersArgs', 'CustomerCertificateParametersArgs', 'ManagedCertificateParametersArgs', 'UrlSigningKeyParametersArgs']]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Secret under the profile.
        """
        return pulumi.get(self, "secret_name")

    @secret_name.setter
    def secret_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_name", value)


class Secret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 parameters: Optional[pulumi.Input[Union[pulumi.InputType['AzureFirstPartyManagedCertificateParametersArgs'], pulumi.InputType['CustomerCertificateParametersArgs'], pulumi.InputType['ManagedCertificateParametersArgs'], pulumi.InputType['UrlSigningKeyParametersArgs']]]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Friendly Secret name mapping to the any Secret or secret related information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[pulumi.InputType['AzureFirstPartyManagedCertificateParametersArgs'], pulumi.InputType['CustomerCertificateParametersArgs'], pulumi.InputType['ManagedCertificateParametersArgs'], pulumi.InputType['UrlSigningKeyParametersArgs']]] parameters: object which contains secret parameters
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] secret_name: Name of the Secret under the profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Friendly Secret name mapping to the any Secret or secret related information.

        :param str resource_name: The name of the resource.
        :param SecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 parameters: Optional[pulumi.Input[Union[pulumi.InputType['AzureFirstPartyManagedCertificateParametersArgs'], pulumi.InputType['CustomerCertificateParametersArgs'], pulumi.InputType['ManagedCertificateParametersArgs'], pulumi.InputType['UrlSigningKeyParametersArgs']]]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecretArgs.__new__(SecretArgs)

            __props__.__dict__["parameters"] = parameters
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["secret_name"] = secret_name
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn:Secret"), pulumi.Alias(type_="azure-native:cdn/v20200901:Secret"), pulumi.Alias(type_="azure-native:cdn/v20210601:Secret"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:Secret"), pulumi.Alias(type_="azure-native:cdn/v20221101preview:Secret"), pulumi.Alias(type_="azure-native:cdn/v20230501:Secret"), pulumi.Alias(type_="azure-native:cdn/v20240201:Secret"), pulumi.Alias(type_="azure-native:cdn/v20240501preview:Secret")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Secret, __self__).__init__(
            'azure-native:cdn/v20230701preview:Secret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Secret':
        """
        Get an existing Secret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecretArgs.__new__(SecretArgs)

        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["profile_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Secret(resource_name, opts=opts, __props__=__props__)

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
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        object which contains secret parameters
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[str]:
        """
        The name of the profile which holds the secret.
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

