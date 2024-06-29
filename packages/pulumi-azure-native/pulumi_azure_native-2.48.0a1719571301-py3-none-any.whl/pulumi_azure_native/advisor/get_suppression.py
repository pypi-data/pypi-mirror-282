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
    'GetSuppressionResult',
    'AwaitableGetSuppressionResult',
    'get_suppression',
    'get_suppression_output',
]

@pulumi.output_type
class GetSuppressionResult:
    """
    The details of the snoozed or dismissed rule; for example, the duration, name, and GUID associated with the rule.
    """
    def __init__(__self__, expiration_time_stamp=None, id=None, name=None, suppression_id=None, system_data=None, ttl=None, type=None):
        if expiration_time_stamp and not isinstance(expiration_time_stamp, str):
            raise TypeError("Expected argument 'expiration_time_stamp' to be a str")
        pulumi.set(__self__, "expiration_time_stamp", expiration_time_stamp)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if suppression_id and not isinstance(suppression_id, str):
            raise TypeError("Expected argument 'suppression_id' to be a str")
        pulumi.set(__self__, "suppression_id", suppression_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if ttl and not isinstance(ttl, str):
            raise TypeError("Expected argument 'ttl' to be a str")
        pulumi.set(__self__, "ttl", ttl)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="expirationTimeStamp")
    def expiration_time_stamp(self) -> str:
        """
        Gets or sets the expiration time stamp.
        """
        return pulumi.get(self, "expiration_time_stamp")

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
    @pulumi.getter(name="suppressionId")
    def suppression_id(self) -> Optional[str]:
        """
        The GUID of the suppression.
        """
        return pulumi.get(self, "suppression_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def ttl(self) -> Optional[str]:
        """
        The duration for which the suppression is valid.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSuppressionResult(GetSuppressionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSuppressionResult(
            expiration_time_stamp=self.expiration_time_stamp,
            id=self.id,
            name=self.name,
            suppression_id=self.suppression_id,
            system_data=self.system_data,
            ttl=self.ttl,
            type=self.type)


def get_suppression(name: Optional[str] = None,
                    recommendation_id: Optional[str] = None,
                    resource_uri: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSuppressionResult:
    """
    Obtains the details of a suppression.
    Azure REST API version: 2023-01-01.

    Other available API versions: 2016-07-12-preview.


    :param str name: The name of the suppression.
    :param str recommendation_id: The recommendation ID.
    :param str resource_uri: The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['recommendationId'] = recommendation_id
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:advisor:getSuppression', __args__, opts=opts, typ=GetSuppressionResult).value

    return AwaitableGetSuppressionResult(
        expiration_time_stamp=pulumi.get(__ret__, 'expiration_time_stamp'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        suppression_id=pulumi.get(__ret__, 'suppression_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        ttl=pulumi.get(__ret__, 'ttl'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_suppression)
def get_suppression_output(name: Optional[pulumi.Input[str]] = None,
                           recommendation_id: Optional[pulumi.Input[str]] = None,
                           resource_uri: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSuppressionResult]:
    """
    Obtains the details of a suppression.
    Azure REST API version: 2023-01-01.

    Other available API versions: 2016-07-12-preview.


    :param str name: The name of the suppression.
    :param str recommendation_id: The recommendation ID.
    :param str resource_uri: The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    """
    ...
