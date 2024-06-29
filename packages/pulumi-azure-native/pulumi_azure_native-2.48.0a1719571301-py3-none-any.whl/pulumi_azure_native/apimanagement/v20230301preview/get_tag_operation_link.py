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
    'GetTagOperationLinkResult',
    'AwaitableGetTagOperationLinkResult',
    'get_tag_operation_link',
    'get_tag_operation_link_output',
]

@pulumi.output_type
class GetTagOperationLinkResult:
    """
    Tag-operation link details.
    """
    def __init__(__self__, id=None, name=None, operation_id=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operation_id and not isinstance(operation_id, str):
            raise TypeError("Expected argument 'operation_id' to be a str")
        pulumi.set(__self__, "operation_id", operation_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter(name="operationId")
    def operation_id(self) -> str:
        """
        Full resource Id of an API operation.
        """
        return pulumi.get(self, "operation_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetTagOperationLinkResult(GetTagOperationLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagOperationLinkResult(
            id=self.id,
            name=self.name,
            operation_id=self.operation_id,
            type=self.type)


def get_tag_operation_link(operation_link_id: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           service_name: Optional[str] = None,
                           tag_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagOperationLinkResult:
    """
    Gets the operation link for the tag.


    :param str operation_link_id: Tag-operation link identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str tag_id: Tag identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['operationLinkId'] = operation_link_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['tagId'] = tag_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:getTagOperationLink', __args__, opts=opts, typ=GetTagOperationLinkResult).value

    return AwaitableGetTagOperationLinkResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        operation_id=pulumi.get(__ret__, 'operation_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_tag_operation_link)
def get_tag_operation_link_output(operation_link_id: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  service_name: Optional[pulumi.Input[str]] = None,
                                  tag_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagOperationLinkResult]:
    """
    Gets the operation link for the tag.


    :param str operation_link_id: Tag-operation link identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str tag_id: Tag identifier. Must be unique in the current API Management service instance.
    """
    ...
