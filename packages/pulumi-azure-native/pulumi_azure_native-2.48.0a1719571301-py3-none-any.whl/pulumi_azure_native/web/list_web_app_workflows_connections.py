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
    'ListWebAppWorkflowsConnectionsResult',
    'AwaitableListWebAppWorkflowsConnectionsResult',
    'list_web_app_workflows_connections',
    'list_web_app_workflows_connections_output',
]

@pulumi.output_type
class ListWebAppWorkflowsConnectionsResult:
    """
    Workflow properties definition.
    """
    def __init__(__self__, id=None, kind=None, location=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The resource kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.WorkflowEnvelopeResponseProperties':
        """
        Additional workflow properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")


class AwaitableListWebAppWorkflowsConnectionsResult(ListWebAppWorkflowsConnectionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebAppWorkflowsConnectionsResult(
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            properties=self.properties,
            type=self.type)


def list_web_app_workflows_connections(name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebAppWorkflowsConnectionsResult:
    """
    Workflow properties definition.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-12-01.


    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web:listWebAppWorkflowsConnections', __args__, opts=opts, typ=ListWebAppWorkflowsConnectionsResult).value

    return AwaitableListWebAppWorkflowsConnectionsResult(
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(list_web_app_workflows_connections)
def list_web_app_workflows_connections_output(name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWebAppWorkflowsConnectionsResult]:
    """
    Workflow properties definition.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-12-01.


    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
