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
    'ListWorkflowRunActionRepetitionExpressionTracesResult',
    'AwaitableListWorkflowRunActionRepetitionExpressionTracesResult',
    'list_workflow_run_action_repetition_expression_traces',
    'list_workflow_run_action_repetition_expression_traces_output',
]

@pulumi.output_type
class ListWorkflowRunActionRepetitionExpressionTracesResult:
    """
    The expression traces.
    """
    def __init__(__self__, inputs=None, next_link=None, value=None):
        if inputs and not isinstance(inputs, list):
            raise TypeError("Expected argument 'inputs' to be a list")
        pulumi.set(__self__, "inputs", inputs)
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, dict):
            raise TypeError("Expected argument 'value' to be a dict")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence['outputs.ExpressionRootResponse']]:
        return pulumi.get(self, "inputs")

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The link used to get the next page of recommendations.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        return pulumi.get(self, "value")


class AwaitableListWorkflowRunActionRepetitionExpressionTracesResult(ListWorkflowRunActionRepetitionExpressionTracesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWorkflowRunActionRepetitionExpressionTracesResult(
            inputs=self.inputs,
            next_link=self.next_link,
            value=self.value)


def list_workflow_run_action_repetition_expression_traces(action_name: Optional[str] = None,
                                                          name: Optional[str] = None,
                                                          repetition_name: Optional[str] = None,
                                                          resource_group_name: Optional[str] = None,
                                                          run_name: Optional[str] = None,
                                                          workflow_name: Optional[str] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWorkflowRunActionRepetitionExpressionTracesResult:
    """
    Lists a workflow run expression trace.


    :param str action_name: The workflow action name.
    :param str name: Site name.
    :param str repetition_name: The workflow repetition.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str run_name: The workflow run name.
    :param str workflow_name: The workflow name.
    """
    __args__ = dict()
    __args__['actionName'] = action_name
    __args__['name'] = name
    __args__['repetitionName'] = repetition_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['runName'] = run_name
    __args__['workflowName'] = workflow_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20220901:listWorkflowRunActionRepetitionExpressionTraces', __args__, opts=opts, typ=ListWorkflowRunActionRepetitionExpressionTracesResult).value

    return AwaitableListWorkflowRunActionRepetitionExpressionTracesResult(
        inputs=pulumi.get(__ret__, 'inputs'),
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_workflow_run_action_repetition_expression_traces)
def list_workflow_run_action_repetition_expression_traces_output(action_name: Optional[pulumi.Input[str]] = None,
                                                                 name: Optional[pulumi.Input[str]] = None,
                                                                 repetition_name: Optional[pulumi.Input[str]] = None,
                                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                                 run_name: Optional[pulumi.Input[str]] = None,
                                                                 workflow_name: Optional[pulumi.Input[str]] = None,
                                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWorkflowRunActionRepetitionExpressionTracesResult]:
    """
    Lists a workflow run expression trace.


    :param str action_name: The workflow action name.
    :param str name: Site name.
    :param str repetition_name: The workflow repetition.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str run_name: The workflow run name.
    :param str workflow_name: The workflow name.
    """
    ...
