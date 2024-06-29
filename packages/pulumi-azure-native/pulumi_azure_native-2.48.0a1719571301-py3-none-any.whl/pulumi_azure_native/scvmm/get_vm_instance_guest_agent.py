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
    'GetVMInstanceGuestAgentResult',
    'AwaitableGetVMInstanceGuestAgentResult',
    'get_vm_instance_guest_agent',
    'get_vm_instance_guest_agent_output',
]

@pulumi.output_type
class GetVMInstanceGuestAgentResult:
    """
    Defines the GuestAgent.
    """
    def __init__(__self__, credentials=None, custom_resource_name=None, http_proxy_config=None, id=None, name=None, provisioning_action=None, provisioning_state=None, status=None, system_data=None, type=None, uuid=None):
        if credentials and not isinstance(credentials, dict):
            raise TypeError("Expected argument 'credentials' to be a dict")
        pulumi.set(__self__, "credentials", credentials)
        if custom_resource_name and not isinstance(custom_resource_name, str):
            raise TypeError("Expected argument 'custom_resource_name' to be a str")
        pulumi.set(__self__, "custom_resource_name", custom_resource_name)
        if http_proxy_config and not isinstance(http_proxy_config, dict):
            raise TypeError("Expected argument 'http_proxy_config' to be a dict")
        pulumi.set(__self__, "http_proxy_config", http_proxy_config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_action and not isinstance(provisioning_action, str):
            raise TypeError("Expected argument 'provisioning_action' to be a str")
        pulumi.set(__self__, "provisioning_action", provisioning_action)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.GuestCredentialResponse']:
        """
        Username / Password Credentials to provision guest agent.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> str:
        """
        Gets the name of the corresponding resource in Kubernetes.
        """
        return pulumi.get(self, "custom_resource_name")

    @property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> Optional['outputs.HttpProxyConfigurationResponse']:
        """
        HTTP Proxy configuration for the VM.
        """
        return pulumi.get(self, "http_proxy_config")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter(name="provisioningAction")
    def provisioning_action(self) -> Optional[str]:
        """
        Gets or sets the guest agent provisioning action.
        """
        return pulumi.get(self, "provisioning_action")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Gets or sets the guest agent status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        Gets or sets a unique identifier for this resource.
        """
        return pulumi.get(self, "uuid")


class AwaitableGetVMInstanceGuestAgentResult(GetVMInstanceGuestAgentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVMInstanceGuestAgentResult(
            credentials=self.credentials,
            custom_resource_name=self.custom_resource_name,
            http_proxy_config=self.http_proxy_config,
            id=self.id,
            name=self.name,
            provisioning_action=self.provisioning_action,
            provisioning_state=self.provisioning_state,
            status=self.status,
            system_data=self.system_data,
            type=self.type,
            uuid=self.uuid)


def get_vm_instance_guest_agent(resource_uri: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVMInstanceGuestAgentResult:
    """
    Implements GuestAgent GET method.
    Azure REST API version: 2023-04-01-preview.


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm:getVMInstanceGuestAgent', __args__, opts=opts, typ=GetVMInstanceGuestAgentResult).value

    return AwaitableGetVMInstanceGuestAgentResult(
        credentials=pulumi.get(__ret__, 'credentials'),
        custom_resource_name=pulumi.get(__ret__, 'custom_resource_name'),
        http_proxy_config=pulumi.get(__ret__, 'http_proxy_config'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_action=pulumi.get(__ret__, 'provisioning_action'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'))


@_utilities.lift_output_func(get_vm_instance_guest_agent)
def get_vm_instance_guest_agent_output(resource_uri: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVMInstanceGuestAgentResult]:
    """
    Implements GuestAgent GET method.
    Azure REST API version: 2023-04-01-preview.


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
    """
    ...
