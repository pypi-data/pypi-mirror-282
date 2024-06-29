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
    'ListGlobalRulestackPredefinedUrlCategoriesResult',
    'AwaitableListGlobalRulestackPredefinedUrlCategoriesResult',
    'list_global_rulestack_predefined_url_categories',
    'list_global_rulestack_predefined_url_categories_output',
]

@pulumi.output_type
class ListGlobalRulestackPredefinedUrlCategoriesResult:
    """
    predefined url categories response
    """
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
        next link
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.PredefinedUrlCategoryResponse']:
        """
        predefined url categories
        """
        return pulumi.get(self, "value")


class AwaitableListGlobalRulestackPredefinedUrlCategoriesResult(ListGlobalRulestackPredefinedUrlCategoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGlobalRulestackPredefinedUrlCategoriesResult(
            next_link=self.next_link,
            value=self.value)


def list_global_rulestack_predefined_url_categories(global_rulestack_name: Optional[str] = None,
                                                    skip: Optional[str] = None,
                                                    top: Optional[int] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGlobalRulestackPredefinedUrlCategoriesResult:
    """
    List predefined URL categories for rulestack


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    __args__ = dict()
    __args__['globalRulestackName'] = global_rulestack_name
    __args__['skip'] = skip
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20240119preview:listGlobalRulestackPredefinedUrlCategories', __args__, opts=opts, typ=ListGlobalRulestackPredefinedUrlCategoriesResult).value

    return AwaitableListGlobalRulestackPredefinedUrlCategoriesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_global_rulestack_predefined_url_categories)
def list_global_rulestack_predefined_url_categories_output(global_rulestack_name: Optional[pulumi.Input[str]] = None,
                                                           skip: Optional[pulumi.Input[Optional[str]]] = None,
                                                           top: Optional[pulumi.Input[Optional[int]]] = None,
                                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGlobalRulestackPredefinedUrlCategoriesResult]:
    """
    List predefined URL categories for rulestack


    :param str global_rulestack_name: GlobalRulestack resource name
    """
    ...
