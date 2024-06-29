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

__all__ = [
    'GetSenderUsernameResult',
    'AwaitableGetSenderUsernameResult',
    'get_sender_username',
    'get_sender_username_output',
]

@pulumi.output_type
class GetSenderUsernameResult:
    """
    A class representing a SenderUsername resource.
    """
    def __init__(__self__, data_location=None, display_name=None, id=None, name=None, provisioning_state=None, system_data=None, type=None, username=None):
        if data_location and not isinstance(data_location, str):
            raise TypeError("Expected argument 'data_location' to be a str")
        pulumi.set(__self__, "data_location", data_location)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> str:
        """
        The location where the SenderUsername resource data is stored at rest.
        """
        return pulumi.get(self, "data_location")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name for the senderUsername.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource. Unknown is the default state for Communication Services.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        A sender senderUsername to be used when sending emails.
        """
        return pulumi.get(self, "username")


class AwaitableGetSenderUsernameResult(GetSenderUsernameResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSenderUsernameResult(
            data_location=self.data_location,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type,
            username=self.username)


def get_sender_username(domain_name: Optional[str] = None,
                        email_service_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        sender_username: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSenderUsernameResult:
    """
    Get a valid sender username for a domains resource.


    :param str domain_name: The name of the Domains resource.
    :param str email_service_name: The name of the EmailService resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sender_username: The valid sender Username.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['emailServiceName'] = email_service_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['senderUsername'] = sender_username
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:communication/v20230601preview:getSenderUsername', __args__, opts=opts, typ=GetSenderUsernameResult).value

    return AwaitableGetSenderUsernameResult(
        data_location=pulumi.get(__ret__, 'data_location'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        username=pulumi.get(__ret__, 'username'))


@_utilities.lift_output_func(get_sender_username)
def get_sender_username_output(domain_name: Optional[pulumi.Input[str]] = None,
                               email_service_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               sender_username: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSenderUsernameResult]:
    """
    Get a valid sender username for a domains resource.


    :param str domain_name: The name of the Domains resource.
    :param str email_service_name: The name of the EmailService resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sender_username: The valid sender Username.
    """
    ...
