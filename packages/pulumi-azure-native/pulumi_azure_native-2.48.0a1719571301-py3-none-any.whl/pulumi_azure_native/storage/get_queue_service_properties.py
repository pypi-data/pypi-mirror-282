# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetQueueServicePropertiesResult',
    'AwaitableGetQueueServicePropertiesResult',
    'get_queue_service_properties',
    'get_queue_service_properties_output',
]

@pulumi.output_type
class GetQueueServicePropertiesResult:
    """
    The properties of a storage account’s Queue service.
    """
    def __init__(__self__, cors=None, id=None, name=None, type=None):
        if cors and not isinstance(cors, dict):
            raise TypeError("Expected argument 'cors' to be a dict")
        pulumi.set(__self__, "cors", cors)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cors(self) -> Optional['outputs.CorsRulesResponse']:
        """
        Specifies CORS rules for the Queue service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Queue service.
        """
        return pulumi.get(self, "cors")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetQueueServicePropertiesResult(GetQueueServicePropertiesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueueServicePropertiesResult(
            cors=self.cors,
            id=self.id,
            name=self.name,
            type=self.type)


def get_queue_service_properties(account_name: Optional[str] = None,
                                 queue_service_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueueServicePropertiesResult:
    """
    Gets the properties of a storage account’s Queue service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-04-01, 2023-05-01.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str queue_service_name: The name of the Queue Service within the specified storage account. Queue Service Name must be 'default'
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['queueServiceName'] = queue_service_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storage:getQueueServiceProperties', __args__, opts=opts, typ=GetQueueServicePropertiesResult).value

    return AwaitableGetQueueServicePropertiesResult(
        cors=pulumi.get(__ret__, 'cors'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_queue_service_properties)
def get_queue_service_properties_output(account_name: Optional[pulumi.Input[str]] = None,
                                        queue_service_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQueueServicePropertiesResult]:
    """
    Gets the properties of a storage account’s Queue service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-04-01, 2023-05-01.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str queue_service_name: The name of the Queue Service within the specified storage account. Queue Service Name must be 'default'
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
