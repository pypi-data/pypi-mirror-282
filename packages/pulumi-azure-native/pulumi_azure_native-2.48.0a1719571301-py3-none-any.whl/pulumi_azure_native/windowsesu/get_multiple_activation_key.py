# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetMultipleActivationKeyResult',
    'AwaitableGetMultipleActivationKeyResult',
    'get_multiple_activation_key',
    'get_multiple_activation_key_output',
]

@pulumi.output_type
class GetMultipleActivationKeyResult:
    """
    MAK key details.
    """
    def __init__(__self__, agreement_number=None, expiration_date=None, id=None, installed_server_number=None, is_eligible=None, location=None, multiple_activation_key=None, name=None, os_type=None, provisioning_state=None, support_type=None, tags=None, type=None):
        if agreement_number and not isinstance(agreement_number, str):
            raise TypeError("Expected argument 'agreement_number' to be a str")
        pulumi.set(__self__, "agreement_number", agreement_number)
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        pulumi.set(__self__, "expiration_date", expiration_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if installed_server_number and not isinstance(installed_server_number, int):
            raise TypeError("Expected argument 'installed_server_number' to be a int")
        pulumi.set(__self__, "installed_server_number", installed_server_number)
        if is_eligible and not isinstance(is_eligible, bool):
            raise TypeError("Expected argument 'is_eligible' to be a bool")
        pulumi.set(__self__, "is_eligible", is_eligible)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if multiple_activation_key and not isinstance(multiple_activation_key, str):
            raise TypeError("Expected argument 'multiple_activation_key' to be a str")
        pulumi.set(__self__, "multiple_activation_key", multiple_activation_key)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if support_type and not isinstance(support_type, str):
            raise TypeError("Expected argument 'support_type' to be a str")
        pulumi.set(__self__, "support_type", support_type)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="agreementNumber")
    def agreement_number(self) -> Optional[str]:
        """
        Agreement number under which the key is requested.
        """
        return pulumi.get(self, "agreement_number")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> str:
        """
        End of support of security updates activated by the MAK key.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="installedServerNumber")
    def installed_server_number(self) -> Optional[int]:
        """
        Number of activations/servers using the MAK key.
        """
        return pulumi.get(self, "installed_server_number")

    @property
    @pulumi.getter(name="isEligible")
    def is_eligible(self) -> Optional[bool]:
        """
        <code> true </code> if user has eligible on-premises Windows physical or virtual machines, and that the requested key will only be used in their organization; <code> false </code> otherwise.
        """
        return pulumi.get(self, "is_eligible")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="multipleActivationKey")
    def multiple_activation_key(self) -> str:
        """
        MAK 5x5 key.
        """
        return pulumi.get(self, "multiple_activation_key")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        Type of OS for which the key is requested.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="supportType")
    def support_type(self) -> Optional[str]:
        """
        Type of support
        """
        return pulumi.get(self, "support_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetMultipleActivationKeyResult(GetMultipleActivationKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMultipleActivationKeyResult(
            agreement_number=self.agreement_number,
            expiration_date=self.expiration_date,
            id=self.id,
            installed_server_number=self.installed_server_number,
            is_eligible=self.is_eligible,
            location=self.location,
            multiple_activation_key=self.multiple_activation_key,
            name=self.name,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            support_type=self.support_type,
            tags=self.tags,
            type=self.type)


def get_multiple_activation_key(multiple_activation_key_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMultipleActivationKeyResult:
    """
    Get a MAK key.
    Azure REST API version: 2019-09-16-preview.


    :param str multiple_activation_key_name: The name of the MAK key.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['multipleActivationKeyName'] = multiple_activation_key_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:windowsesu:getMultipleActivationKey', __args__, opts=opts, typ=GetMultipleActivationKeyResult).value

    return AwaitableGetMultipleActivationKeyResult(
        agreement_number=pulumi.get(__ret__, 'agreement_number'),
        expiration_date=pulumi.get(__ret__, 'expiration_date'),
        id=pulumi.get(__ret__, 'id'),
        installed_server_number=pulumi.get(__ret__, 'installed_server_number'),
        is_eligible=pulumi.get(__ret__, 'is_eligible'),
        location=pulumi.get(__ret__, 'location'),
        multiple_activation_key=pulumi.get(__ret__, 'multiple_activation_key'),
        name=pulumi.get(__ret__, 'name'),
        os_type=pulumi.get(__ret__, 'os_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        support_type=pulumi.get(__ret__, 'support_type'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_multiple_activation_key)
def get_multiple_activation_key_output(multiple_activation_key_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMultipleActivationKeyResult]:
    """
    Get a MAK key.
    Azure REST API version: 2019-09-16-preview.


    :param str multiple_activation_key_name: The name of the MAK key.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
