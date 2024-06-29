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
    'ListComputeNodesResult',
    'AwaitableListComputeNodesResult',
    'list_compute_nodes',
    'list_compute_nodes_output',
]

@pulumi.output_type
class ListComputeNodesResult:
    """
    Result of AmlCompute Nodes
    """
    def __init__(__self__, next_link=None, nodes=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if nodes and not isinstance(nodes, list):
            raise TypeError("Expected argument 'nodes' to be a list")
        pulumi.set(__self__, "nodes", nodes)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        The continuation token.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def nodes(self) -> Sequence['outputs.AmlComputeNodeInformationResponse']:
        """
        The collection of returned AmlCompute nodes details.
        """
        return pulumi.get(self, "nodes")


class AwaitableListComputeNodesResult(ListComputeNodesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListComputeNodesResult(
            next_link=self.next_link,
            nodes=self.nodes)


def list_compute_nodes(compute_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       workspace_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListComputeNodesResult:
    """
    Get the details (e.g IP address, port etc) of all the compute nodes in the compute.


    :param str compute_name: Name of the Azure Machine Learning compute.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['computeName'] = compute_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20231001:listComputeNodes', __args__, opts=opts, typ=ListComputeNodesResult).value

    return AwaitableListComputeNodesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        nodes=pulumi.get(__ret__, 'nodes'))


@_utilities.lift_output_func(list_compute_nodes)
def list_compute_nodes_output(compute_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              workspace_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListComputeNodesResult]:
    """
    Get the details (e.g IP address, port etc) of all the compute nodes in the compute.


    :param str compute_name: Name of the Azure Machine Learning compute.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
