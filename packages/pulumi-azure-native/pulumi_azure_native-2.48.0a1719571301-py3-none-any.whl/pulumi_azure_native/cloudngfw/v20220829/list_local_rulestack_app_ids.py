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
    'ListLocalRulestackAppIdsResult',
    'AwaitableListLocalRulestackAppIdsResult',
    'list_local_rulestack_app_ids',
    'list_local_rulestack_app_ids_output',
]

@pulumi.output_type
class ListLocalRulestackAppIdsResult:
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        next Link
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence[str]:
        """
        List of AppIds
        """
        return pulumi.get(self, "value")


class AwaitableListLocalRulestackAppIdsResult(ListLocalRulestackAppIdsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListLocalRulestackAppIdsResult(
            next_link=self.next_link,
            value=self.value)


def list_local_rulestack_app_ids(app_id_version: Optional[str] = None,
                                 app_prefix: Optional[str] = None,
                                 local_rulestack_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 skip: Optional[str] = None,
                                 top: Optional[int] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListLocalRulestackAppIdsResult:
    """
    List of AppIds for LocalRulestack ApiVersion


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['appIdVersion'] = app_id_version
    __args__['appPrefix'] = app_prefix
    __args__['localRulestackName'] = local_rulestack_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['skip'] = skip
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20220829:listLocalRulestackAppIds', __args__, opts=opts, typ=ListLocalRulestackAppIdsResult).value

    return AwaitableListLocalRulestackAppIdsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_local_rulestack_app_ids)
def list_local_rulestack_app_ids_output(app_id_version: Optional[pulumi.Input[Optional[str]]] = None,
                                        app_prefix: Optional[pulumi.Input[Optional[str]]] = None,
                                        local_rulestack_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        skip: Optional[pulumi.Input[Optional[str]]] = None,
                                        top: Optional[pulumi.Input[Optional[int]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListLocalRulestackAppIdsResult]:
    """
    List of AppIds for LocalRulestack ApiVersion


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
