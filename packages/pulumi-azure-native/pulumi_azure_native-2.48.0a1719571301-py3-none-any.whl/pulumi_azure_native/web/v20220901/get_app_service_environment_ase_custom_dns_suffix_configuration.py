# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult',
    'AwaitableGetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult',
    'get_app_service_environment_ase_custom_dns_suffix_configuration',
    'get_app_service_environment_ase_custom_dns_suffix_configuration_output',
]

@pulumi.output_type
class GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult:
    """
    Full view of the custom domain suffix configuration for ASEv3.
    """
    def __init__(__self__, certificate_url=None, dns_suffix=None, id=None, key_vault_reference_identity=None, kind=None, name=None, provisioning_details=None, provisioning_state=None, type=None):
        if certificate_url and not isinstance(certificate_url, str):
            raise TypeError("Expected argument 'certificate_url' to be a str")
        pulumi.set(__self__, "certificate_url", certificate_url)
        if dns_suffix and not isinstance(dns_suffix, str):
            raise TypeError("Expected argument 'dns_suffix' to be a str")
        pulumi.set(__self__, "dns_suffix", dns_suffix)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_reference_identity and not isinstance(key_vault_reference_identity, str):
            raise TypeError("Expected argument 'key_vault_reference_identity' to be a str")
        pulumi.set(__self__, "key_vault_reference_identity", key_vault_reference_identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_details and not isinstance(provisioning_details, str):
            raise TypeError("Expected argument 'provisioning_details' to be a str")
        pulumi.set(__self__, "provisioning_details", provisioning_details)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[str]:
        """
        The URL referencing the Azure Key Vault certificate secret that should be used as the default SSL/TLS certificate for sites with the custom domain suffix.
        """
        return pulumi.get(self, "certificate_url")

    @property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[str]:
        """
        The default custom domain suffix to use for all sites deployed on the ASE.
        """
        return pulumi.get(self, "dns_suffix")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> Optional[str]:
        """
        The user-assigned identity to use for resolving the key vault certificate reference. If not specified, the system-assigned ASE identity will be used if available.
        """
        return pulumi.get(self, "key_vault_reference_identity")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningDetails")
    def provisioning_details(self) -> str:
        return pulumi.get(self, "provisioning_details")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult(GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult(
            certificate_url=self.certificate_url,
            dns_suffix=self.dns_suffix,
            id=self.id,
            key_vault_reference_identity=self.key_vault_reference_identity,
            kind=self.kind,
            name=self.name,
            provisioning_details=self.provisioning_details,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_app_service_environment_ase_custom_dns_suffix_configuration(name: Optional[str] = None,
                                                                    resource_group_name: Optional[str] = None,
                                                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult:
    """
    Full view of the custom domain suffix configuration for ASEv3.


    :param str name: Name of the App Service Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20220901:getAppServiceEnvironmentAseCustomDnsSuffixConfiguration', __args__, opts=opts, typ=GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult).value

    return AwaitableGetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult(
        certificate_url=pulumi.get(__ret__, 'certificate_url'),
        dns_suffix=pulumi.get(__ret__, 'dns_suffix'),
        id=pulumi.get(__ret__, 'id'),
        key_vault_reference_identity=pulumi.get(__ret__, 'key_vault_reference_identity'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_details=pulumi.get(__ret__, 'provisioning_details'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_app_service_environment_ase_custom_dns_suffix_configuration)
def get_app_service_environment_ase_custom_dns_suffix_configuration_output(name: Optional[pulumi.Input[str]] = None,
                                                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult]:
    """
    Full view of the custom domain suffix configuration for ASEv3.


    :param str name: Name of the App Service Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
