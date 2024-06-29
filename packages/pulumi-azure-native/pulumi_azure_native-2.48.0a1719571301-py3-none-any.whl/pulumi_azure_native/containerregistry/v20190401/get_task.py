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
    'GetTaskResult',
    'AwaitableGetTaskResult',
    'get_task',
    'get_task_output',
]

@pulumi.output_type
class GetTaskResult:
    """
    The task that has the ARM resource and task properties. 
    The task will have all information to schedule a run against it.
    """
    def __init__(__self__, agent_configuration=None, creation_date=None, credentials=None, id=None, identity=None, location=None, name=None, platform=None, provisioning_state=None, status=None, step=None, tags=None, timeout=None, trigger=None, type=None):
        if agent_configuration and not isinstance(agent_configuration, dict):
            raise TypeError("Expected argument 'agent_configuration' to be a dict")
        pulumi.set(__self__, "agent_configuration", agent_configuration)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if credentials and not isinstance(credentials, dict):
            raise TypeError("Expected argument 'credentials' to be a dict")
        pulumi.set(__self__, "credentials", credentials)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform and not isinstance(platform, dict):
            raise TypeError("Expected argument 'platform' to be a dict")
        pulumi.set(__self__, "platform", platform)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if step and not isinstance(step, dict):
            raise TypeError("Expected argument 'step' to be a dict")
        pulumi.set(__self__, "step", step)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timeout and not isinstance(timeout, int):
            raise TypeError("Expected argument 'timeout' to be a int")
        pulumi.set(__self__, "timeout", timeout)
        if trigger and not isinstance(trigger, dict):
            raise TypeError("Expected argument 'trigger' to be a dict")
        pulumi.set(__self__, "trigger", trigger)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional['outputs.AgentPropertiesResponse']:
        """
        The machine configuration of the run agent.
        """
        return pulumi.get(self, "agent_configuration")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of task.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.CredentialsResponse']:
        """
        The properties that describes a set of credentials that will be used when this run is invoked.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityPropertiesResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> 'outputs.PlatformPropertiesResponse':
        """
        The platform properties against which the run has to happen.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the task.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The current status of task.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def step(self) -> Any:
        """
        The properties of a task step.
        """
        return pulumi.get(self, "step")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> Optional[int]:
        """
        Run timeout in seconds.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def trigger(self) -> Optional['outputs.TriggerPropertiesResponse']:
        """
        The properties that describe all triggers for the task.
        """
        return pulumi.get(self, "trigger")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetTaskResult(GetTaskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTaskResult(
            agent_configuration=self.agent_configuration,
            creation_date=self.creation_date,
            credentials=self.credentials,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            platform=self.platform,
            provisioning_state=self.provisioning_state,
            status=self.status,
            step=self.step,
            tags=self.tags,
            timeout=self.timeout,
            trigger=self.trigger,
            type=self.type)


def get_task(registry_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             task_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTaskResult:
    """
    Get the properties of a specified task.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str task_name: The name of the container registry task.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['taskName'] = task_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20190401:getTask', __args__, opts=opts, typ=GetTaskResult).value

    return AwaitableGetTaskResult(
        agent_configuration=pulumi.get(__ret__, 'agent_configuration'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        credentials=pulumi.get(__ret__, 'credentials'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        platform=pulumi.get(__ret__, 'platform'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        step=pulumi.get(__ret__, 'step'),
        tags=pulumi.get(__ret__, 'tags'),
        timeout=pulumi.get(__ret__, 'timeout'),
        trigger=pulumi.get(__ret__, 'trigger'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_task)
def get_task_output(registry_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    task_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTaskResult]:
    """
    Get the properties of a specified task.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str task_name: The name of the container registry task.
    """
    ...
