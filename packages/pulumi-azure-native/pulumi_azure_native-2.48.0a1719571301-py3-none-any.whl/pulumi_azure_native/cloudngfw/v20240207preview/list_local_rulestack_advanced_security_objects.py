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
    'ListLocalRulestackAdvancedSecurityObjectsResult',
    'AwaitableListLocalRulestackAdvancedSecurityObjectsResult',
    'list_local_rulestack_advanced_security_objects',
    'list_local_rulestack_advanced_security_objects_output',
]

@pulumi.output_type
class ListLocalRulestackAdvancedSecurityObjectsResult:
    """
    advanced security object
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, dict):
            raise TypeError("Expected argument 'value' to be a dict")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        next link
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> 'outputs.AdvSecurityObjectModelResponse':
        """
        response value
        """
        return pulumi.get(self, "value")


class AwaitableListLocalRulestackAdvancedSecurityObjectsResult(ListLocalRulestackAdvancedSecurityObjectsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListLocalRulestackAdvancedSecurityObjectsResult(
            next_link=self.next_link,
            value=self.value)


def list_local_rulestack_advanced_security_objects(local_rulestack_name: Optional[str] = None,
                                                   resource_group_name: Optional[str] = None,
                                                   skip: Optional[str] = None,
                                                   top: Optional[int] = None,
                                                   type: Optional[str] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListLocalRulestackAdvancedSecurityObjectsResult:
    """
    Get the list of advanced security objects


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['localRulestackName'] = local_rulestack_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['skip'] = skip
    __args__['top'] = top
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20240207preview:listLocalRulestackAdvancedSecurityObjects', __args__, opts=opts, typ=ListLocalRulestackAdvancedSecurityObjectsResult).value

    return AwaitableListLocalRulestackAdvancedSecurityObjectsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_local_rulestack_advanced_security_objects)
def list_local_rulestack_advanced_security_objects_output(local_rulestack_name: Optional[pulumi.Input[str]] = None,
                                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                                          skip: Optional[pulumi.Input[Optional[str]]] = None,
                                                          top: Optional[pulumi.Input[Optional[int]]] = None,
                                                          type: Optional[pulumi.Input[str]] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListLocalRulestackAdvancedSecurityObjectsResult]:
    """
    Get the list of advanced security objects


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
