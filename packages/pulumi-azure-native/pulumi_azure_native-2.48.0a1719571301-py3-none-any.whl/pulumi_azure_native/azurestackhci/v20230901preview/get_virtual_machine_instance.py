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
    'GetVirtualMachineInstanceResult',
    'AwaitableGetVirtualMachineInstanceResult',
    'get_virtual_machine_instance',
    'get_virtual_machine_instance_output',
]

@pulumi.output_type
class GetVirtualMachineInstanceResult:
    """
    The virtual machine instance resource definition.
    """
    def __init__(__self__, extended_location=None, guest_agent_install_status=None, hardware_profile=None, http_proxy_config=None, id=None, identity=None, instance_view=None, name=None, network_profile=None, os_profile=None, provisioning_state=None, resource_uid=None, security_profile=None, status=None, storage_profile=None, system_data=None, type=None, vm_id=None):
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if guest_agent_install_status and not isinstance(guest_agent_install_status, dict):
            raise TypeError("Expected argument 'guest_agent_install_status' to be a dict")
        pulumi.set(__self__, "guest_agent_install_status", guest_agent_install_status)
        if hardware_profile and not isinstance(hardware_profile, dict):
            raise TypeError("Expected argument 'hardware_profile' to be a dict")
        pulumi.set(__self__, "hardware_profile", hardware_profile)
        if http_proxy_config and not isinstance(http_proxy_config, dict):
            raise TypeError("Expected argument 'http_proxy_config' to be a dict")
        pulumi.set(__self__, "http_proxy_config", http_proxy_config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if instance_view and not isinstance(instance_view, dict):
            raise TypeError("Expected argument 'instance_view' to be a dict")
        pulumi.set(__self__, "instance_view", instance_view)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if os_profile and not isinstance(os_profile, dict):
            raise TypeError("Expected argument 'os_profile' to be a dict")
        pulumi.set(__self__, "os_profile", os_profile)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_uid and not isinstance(resource_uid, str):
            raise TypeError("Expected argument 'resource_uid' to be a str")
        pulumi.set(__self__, "resource_uid", resource_uid)
        if security_profile and not isinstance(security_profile, dict):
            raise TypeError("Expected argument 'security_profile' to be a dict")
        pulumi.set(__self__, "security_profile", security_profile)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if storage_profile and not isinstance(storage_profile, dict):
            raise TypeError("Expected argument 'storage_profile' to be a dict")
        pulumi.set(__self__, "storage_profile", storage_profile)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_id and not isinstance(vm_id, str):
            raise TypeError("Expected argument 'vm_id' to be a str")
        pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="guestAgentInstallStatus")
    def guest_agent_install_status(self) -> Optional['outputs.GuestAgentInstallStatusResponse']:
        """
        Guest agent install status.
        """
        return pulumi.get(self, "guest_agent_install_status")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional['outputs.VirtualMachineInstancePropertiesResponseHardwareProfile']:
        """
        HardwareProfile - Specifies the hardware settings for the virtual machine instance.
        """
        return pulumi.get(self, "hardware_profile")

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
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> 'outputs.VirtualMachineInstanceViewResponse':
        """
        The virtual machine instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.VirtualMachineInstancePropertiesResponseNetworkProfile']:
        """
        NetworkProfile - describes the network configuration the virtual machine instance
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional['outputs.VirtualMachineInstancePropertiesResponseOsProfile']:
        """
        OsProfile - describes the configuration of the operating system and sets login data
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the virtual machine instance.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[str]:
        """
        Unique identifier defined by ARC to identify the guest of the VM.
        """
        return pulumi.get(self, "resource_uid")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional['outputs.VirtualMachineInstancePropertiesResponseSecurityProfile']:
        """
        SecurityProfile - Specifies the security settings for the virtual machine instance.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.VirtualMachineInstanceStatusResponse':
        """
        The observed state of virtual machine instances
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional['outputs.VirtualMachineInstancePropertiesResponseStorageProfile']:
        """
        StorageProfile - contains information about the disks and storage information for the virtual machine instance
        """
        return pulumi.get(self, "storage_profile")

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
    @pulumi.getter(name="vmId")
    def vm_id(self) -> str:
        """
        Unique identifier for the vm resource.
        """
        return pulumi.get(self, "vm_id")


class AwaitableGetVirtualMachineInstanceResult(GetVirtualMachineInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineInstanceResult(
            extended_location=self.extended_location,
            guest_agent_install_status=self.guest_agent_install_status,
            hardware_profile=self.hardware_profile,
            http_proxy_config=self.http_proxy_config,
            id=self.id,
            identity=self.identity,
            instance_view=self.instance_view,
            name=self.name,
            network_profile=self.network_profile,
            os_profile=self.os_profile,
            provisioning_state=self.provisioning_state,
            resource_uid=self.resource_uid,
            security_profile=self.security_profile,
            status=self.status,
            storage_profile=self.storage_profile,
            system_data=self.system_data,
            type=self.type,
            vm_id=self.vm_id)


def get_virtual_machine_instance(resource_uri: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineInstanceResult:
    """
    Gets a virtual machine instance


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20230901preview:getVirtualMachineInstance', __args__, opts=opts, typ=GetVirtualMachineInstanceResult).value

    return AwaitableGetVirtualMachineInstanceResult(
        extended_location=pulumi.get(__ret__, 'extended_location'),
        guest_agent_install_status=pulumi.get(__ret__, 'guest_agent_install_status'),
        hardware_profile=pulumi.get(__ret__, 'hardware_profile'),
        http_proxy_config=pulumi.get(__ret__, 'http_proxy_config'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        instance_view=pulumi.get(__ret__, 'instance_view'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        os_profile=pulumi.get(__ret__, 'os_profile'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_uid=pulumi.get(__ret__, 'resource_uid'),
        security_profile=pulumi.get(__ret__, 'security_profile'),
        status=pulumi.get(__ret__, 'status'),
        storage_profile=pulumi.get(__ret__, 'storage_profile'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        vm_id=pulumi.get(__ret__, 'vm_id'))


@_utilities.lift_output_func(get_virtual_machine_instance)
def get_virtual_machine_instance_output(resource_uri: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineInstanceResult]:
    """
    Gets a virtual machine instance


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
    """
    ...
