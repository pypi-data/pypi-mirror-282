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
    'GetHcxEnterpriseSiteResult',
    'AwaitableGetHcxEnterpriseSiteResult',
    'get_hcx_enterprise_site',
    'get_hcx_enterprise_site_output',
]

@pulumi.output_type
class GetHcxEnterpriseSiteResult:
    """
    An HCX Enterprise Site resource
    """
    def __init__(__self__, activation_key=None, id=None, name=None, status=None, type=None):
        if activation_key and not isinstance(activation_key, str):
            raise TypeError("Expected argument 'activation_key' to be a str")
        pulumi.set(__self__, "activation_key", activation_key)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> str:
        """
        The activation key
        """
        return pulumi.get(self, "activation_key")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the HCX Enterprise Site
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetHcxEnterpriseSiteResult(GetHcxEnterpriseSiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHcxEnterpriseSiteResult(
            activation_key=self.activation_key,
            id=self.id,
            name=self.name,
            status=self.status,
            type=self.type)


def get_hcx_enterprise_site(hcx_enterprise_site_name: Optional[str] = None,
                            private_cloud_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHcxEnterpriseSiteResult:
    """
    An HCX Enterprise Site resource


    :param str hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['hcxEnterpriseSiteName'] = hcx_enterprise_site_name
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20220501:getHcxEnterpriseSite', __args__, opts=opts, typ=GetHcxEnterpriseSiteResult).value

    return AwaitableGetHcxEnterpriseSiteResult(
        activation_key=pulumi.get(__ret__, 'activation_key'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_hcx_enterprise_site)
def get_hcx_enterprise_site_output(hcx_enterprise_site_name: Optional[pulumi.Input[str]] = None,
                                   private_cloud_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHcxEnterpriseSiteResult]:
    """
    An HCX Enterprise Site resource


    :param str hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
