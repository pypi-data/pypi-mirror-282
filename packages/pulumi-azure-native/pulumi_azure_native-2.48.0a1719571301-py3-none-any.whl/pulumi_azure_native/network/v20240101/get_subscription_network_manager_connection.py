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
    'GetSubscriptionNetworkManagerConnectionResult',
    'AwaitableGetSubscriptionNetworkManagerConnectionResult',
    'get_subscription_network_manager_connection',
    'get_subscription_network_manager_connection_output',
]

@pulumi.output_type
class GetSubscriptionNetworkManagerConnectionResult:
    """
    The Network Manager Connection resource
    """
    def __init__(__self__, description=None, etag=None, id=None, name=None, network_manager_id=None, system_data=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_manager_id and not isinstance(network_manager_id, str):
            raise TypeError("Expected argument 'network_manager_id' to be a str")
        pulumi.set(__self__, "network_manager_id", network_manager_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the network manager connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

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
    @pulumi.getter(name="networkManagerId")
    def network_manager_id(self) -> Optional[str]:
        """
        Network Manager Id.
        """
        return pulumi.get(self, "network_manager_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetSubscriptionNetworkManagerConnectionResult(GetSubscriptionNetworkManagerConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubscriptionNetworkManagerConnectionResult(
            description=self.description,
            etag=self.etag,
            id=self.id,
            name=self.name,
            network_manager_id=self.network_manager_id,
            system_data=self.system_data,
            type=self.type)


def get_subscription_network_manager_connection(network_manager_connection_name: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubscriptionNetworkManagerConnectionResult:
    """
    Get a specified connection created by this subscription.


    :param str network_manager_connection_name: Name for the network manager connection.
    """
    __args__ = dict()
    __args__['networkManagerConnectionName'] = network_manager_connection_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20240101:getSubscriptionNetworkManagerConnection', __args__, opts=opts, typ=GetSubscriptionNetworkManagerConnectionResult).value

    return AwaitableGetSubscriptionNetworkManagerConnectionResult(
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network_manager_id=pulumi.get(__ret__, 'network_manager_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_subscription_network_manager_connection)
def get_subscription_network_manager_connection_output(network_manager_connection_name: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubscriptionNetworkManagerConnectionResult]:
    """
    Get a specified connection created by this subscription.


    :param str network_manager_connection_name: Name for the network manager connection.
    """
    ...
