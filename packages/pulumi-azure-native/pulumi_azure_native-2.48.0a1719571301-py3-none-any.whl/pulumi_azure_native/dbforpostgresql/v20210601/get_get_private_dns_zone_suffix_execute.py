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
    'GetGetPrivateDnsZoneSuffixExecuteResult',
    'AwaitableGetGetPrivateDnsZoneSuffixExecuteResult',
    'get_get_private_dns_zone_suffix_execute',
    'get_get_private_dns_zone_suffix_execute_output',
]

@pulumi.output_type
class GetGetPrivateDnsZoneSuffixExecuteResult:
    """
    Represents a resource name availability.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


class AwaitableGetGetPrivateDnsZoneSuffixExecuteResult(GetGetPrivateDnsZoneSuffixExecuteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGetPrivateDnsZoneSuffixExecuteResult(
            value=self.value)


def get_get_private_dns_zone_suffix_execute(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGetPrivateDnsZoneSuffixExecuteResult:
    """
    Get private DNS zone suffix in the cloud
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20210601:getGetPrivateDnsZoneSuffixExecute', __args__, opts=opts, typ=GetGetPrivateDnsZoneSuffixExecuteResult).value

    return AwaitableGetGetPrivateDnsZoneSuffixExecuteResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_get_private_dns_zone_suffix_execute)
def get_get_private_dns_zone_suffix_execute_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGetPrivateDnsZoneSuffixExecuteResult]:
    """
    Get private DNS zone suffix in the cloud
    """
    ...
