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
    'GetExperimentResult',
    'AwaitableGetExperimentResult',
    'get_experiment',
    'get_experiment_output',
]

@pulumi.output_type
class GetExperimentResult:
    """
    Defines the properties of an Experiment
    """
    def __init__(__self__, description=None, enabled_state=None, endpoint_a=None, endpoint_b=None, id=None, location=None, name=None, resource_state=None, script_file_uri=None, status=None, tags=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled_state and not isinstance(enabled_state, str):
            raise TypeError("Expected argument 'enabled_state' to be a str")
        pulumi.set(__self__, "enabled_state", enabled_state)
        if endpoint_a and not isinstance(endpoint_a, dict):
            raise TypeError("Expected argument 'endpoint_a' to be a dict")
        pulumi.set(__self__, "endpoint_a", endpoint_a)
        if endpoint_b and not isinstance(endpoint_b, dict):
            raise TypeError("Expected argument 'endpoint_b' to be a dict")
        pulumi.set(__self__, "endpoint_b", endpoint_b)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if script_file_uri and not isinstance(script_file_uri, str):
            raise TypeError("Expected argument 'script_file_uri' to be a str")
        pulumi.set(__self__, "script_file_uri", script_file_uri)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the details or intents of the Experiment
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[str]:
        """
        The state of the Experiment
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="endpointA")
    def endpoint_a(self) -> Optional['outputs.ExperimentEndpointResponse']:
        """
        The endpoint A of an experiment
        """
        return pulumi.get(self, "endpoint_a")

    @property
    @pulumi.getter(name="endpointB")
    def endpoint_b(self) -> Optional['outputs.ExperimentEndpointResponse']:
        """
        The endpoint B of an experiment
        """
        return pulumi.get(self, "endpoint_b")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Resource status.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="scriptFileUri")
    def script_file_uri(self) -> str:
        """
        The uri to the Script used in the Experiment
        """
        return pulumi.get(self, "script_file_uri")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The description of Experiment status from the server side
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetExperimentResult(GetExperimentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExperimentResult(
            description=self.description,
            enabled_state=self.enabled_state,
            endpoint_a=self.endpoint_a,
            endpoint_b=self.endpoint_b,
            id=self.id,
            location=self.location,
            name=self.name,
            resource_state=self.resource_state,
            script_file_uri=self.script_file_uri,
            status=self.status,
            tags=self.tags,
            type=self.type)


def get_experiment(experiment_name: Optional[str] = None,
                   profile_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExperimentResult:
    """
    Defines the properties of an Experiment
    Azure REST API version: 2019-11-01.


    :param str experiment_name: The Experiment identifier associated with the Experiment
    :param str profile_name: The Profile identifier associated with the Tenant and Partner
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['experimentName'] = experiment_name
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getExperiment', __args__, opts=opts, typ=GetExperimentResult).value

    return AwaitableGetExperimentResult(
        description=pulumi.get(__ret__, 'description'),
        enabled_state=pulumi.get(__ret__, 'enabled_state'),
        endpoint_a=pulumi.get(__ret__, 'endpoint_a'),
        endpoint_b=pulumi.get(__ret__, 'endpoint_b'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_state=pulumi.get(__ret__, 'resource_state'),
        script_file_uri=pulumi.get(__ret__, 'script_file_uri'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_experiment)
def get_experiment_output(experiment_name: Optional[pulumi.Input[str]] = None,
                          profile_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExperimentResult]:
    """
    Defines the properties of an Experiment
    Azure REST API version: 2019-11-01.


    :param str experiment_name: The Experiment identifier associated with the Experiment
    :param str profile_name: The Profile identifier associated with the Tenant and Partner
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
