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
    'GetVirtualMachineResult',
    'AwaitableGetVirtualMachineResult',
    'get_virtual_machine',
    'get_virtual_machine_output',
]

@pulumi.output_type
class GetVirtualMachineResult:
    """
    The VirtualMachines resource definition.
    """
    def __init__(__self__, availability_sets=None, checkpoint_type=None, checkpoints=None, cloud_id=None, extended_location=None, generation=None, guest_agent_profile=None, hardware_profile=None, id=None, identity=None, inventory_item_id=None, last_restored_vm_checkpoint=None, location=None, name=None, network_profile=None, os_profile=None, power_state=None, provisioning_state=None, storage_profile=None, system_data=None, tags=None, template_id=None, type=None, uuid=None, vm_name=None, vmm_server_id=None):
        if availability_sets and not isinstance(availability_sets, list):
            raise TypeError("Expected argument 'availability_sets' to be a list")
        pulumi.set(__self__, "availability_sets", availability_sets)
        if checkpoint_type and not isinstance(checkpoint_type, str):
            raise TypeError("Expected argument 'checkpoint_type' to be a str")
        pulumi.set(__self__, "checkpoint_type", checkpoint_type)
        if checkpoints and not isinstance(checkpoints, list):
            raise TypeError("Expected argument 'checkpoints' to be a list")
        pulumi.set(__self__, "checkpoints", checkpoints)
        if cloud_id and not isinstance(cloud_id, str):
            raise TypeError("Expected argument 'cloud_id' to be a str")
        pulumi.set(__self__, "cloud_id", cloud_id)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if generation and not isinstance(generation, int):
            raise TypeError("Expected argument 'generation' to be a int")
        pulumi.set(__self__, "generation", generation)
        if guest_agent_profile and not isinstance(guest_agent_profile, dict):
            raise TypeError("Expected argument 'guest_agent_profile' to be a dict")
        pulumi.set(__self__, "guest_agent_profile", guest_agent_profile)
        if hardware_profile and not isinstance(hardware_profile, dict):
            raise TypeError("Expected argument 'hardware_profile' to be a dict")
        pulumi.set(__self__, "hardware_profile", hardware_profile)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if inventory_item_id and not isinstance(inventory_item_id, str):
            raise TypeError("Expected argument 'inventory_item_id' to be a str")
        pulumi.set(__self__, "inventory_item_id", inventory_item_id)
        if last_restored_vm_checkpoint and not isinstance(last_restored_vm_checkpoint, dict):
            raise TypeError("Expected argument 'last_restored_vm_checkpoint' to be a dict")
        pulumi.set(__self__, "last_restored_vm_checkpoint", last_restored_vm_checkpoint)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if os_profile and not isinstance(os_profile, dict):
            raise TypeError("Expected argument 'os_profile' to be a dict")
        pulumi.set(__self__, "os_profile", os_profile)
        if power_state and not isinstance(power_state, str):
            raise TypeError("Expected argument 'power_state' to be a str")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if storage_profile and not isinstance(storage_profile, dict):
            raise TypeError("Expected argument 'storage_profile' to be a dict")
        pulumi.set(__self__, "storage_profile", storage_profile)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template_id and not isinstance(template_id, str):
            raise TypeError("Expected argument 'template_id' to be a str")
        pulumi.set(__self__, "template_id", template_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if vm_name and not isinstance(vm_name, str):
            raise TypeError("Expected argument 'vm_name' to be a str")
        pulumi.set(__self__, "vm_name", vm_name)
        if vmm_server_id and not isinstance(vmm_server_id, str):
            raise TypeError("Expected argument 'vmm_server_id' to be a str")
        pulumi.set(__self__, "vmm_server_id", vmm_server_id)

    @property
    @pulumi.getter(name="availabilitySets")
    def availability_sets(self) -> Optional[Sequence['outputs.VirtualMachinePropertiesResponseAvailabilitySets']]:
        """
        Availability Sets in vm.
        """
        return pulumi.get(self, "availability_sets")

    @property
    @pulumi.getter(name="checkpointType")
    def checkpoint_type(self) -> Optional[str]:
        """
        Type of checkpoint supported for the vm.
        """
        return pulumi.get(self, "checkpoint_type")

    @property
    @pulumi.getter
    def checkpoints(self) -> Optional[Sequence['outputs.CheckpointResponse']]:
        """
        Checkpoints in the vm.
        """
        return pulumi.get(self, "checkpoints")

    @property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> Optional[str]:
        """
        ARM Id of the cloud resource to use for deploying the vm.
        """
        return pulumi.get(self, "cloud_id")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def generation(self) -> Optional[int]:
        """
        Gets or sets the generation for the vm.
        """
        return pulumi.get(self, "generation")

    @property
    @pulumi.getter(name="guestAgentProfile")
    def guest_agent_profile(self) -> Optional['outputs.GuestAgentProfileResponse']:
        """
        Guest agent status properties.
        """
        return pulumi.get(self, "guest_agent_profile")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional['outputs.HardwareProfileResponse']:
        """
        Hardware properties.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[str]:
        """
        Gets or sets the inventory Item ID for the resource.
        """
        return pulumi.get(self, "inventory_item_id")

    @property
    @pulumi.getter(name="lastRestoredVMCheckpoint")
    def last_restored_vm_checkpoint(self) -> 'outputs.CheckpointResponse':
        """
        Last restored checkpoint in the vm.
        """
        return pulumi.get(self, "last_restored_vm_checkpoint")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.NetworkProfileResponse']:
        """
        Network properties.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional['outputs.OsProfileResponse']:
        """
        OS properties.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> str:
        """
        Gets the power state of the virtual machine.
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional['outputs.StorageProfileResponse']:
        """
        Storage properties.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[str]:
        """
        ARM Id of the template resource to use for deploying the vm.
        """
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> Optional[str]:
        """
        Unique ID of the virtual machine.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> Optional[str]:
        """
        VMName is the name of VM on the SCVMM server.
        """
        return pulumi.get(self, "vm_name")

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[str]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")


class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineResult(
            availability_sets=self.availability_sets,
            checkpoint_type=self.checkpoint_type,
            checkpoints=self.checkpoints,
            cloud_id=self.cloud_id,
            extended_location=self.extended_location,
            generation=self.generation,
            guest_agent_profile=self.guest_agent_profile,
            hardware_profile=self.hardware_profile,
            id=self.id,
            identity=self.identity,
            inventory_item_id=self.inventory_item_id,
            last_restored_vm_checkpoint=self.last_restored_vm_checkpoint,
            location=self.location,
            name=self.name,
            network_profile=self.network_profile,
            os_profile=self.os_profile,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            storage_profile=self.storage_profile,
            system_data=self.system_data,
            tags=self.tags,
            template_id=self.template_id,
            type=self.type,
            uuid=self.uuid,
            vm_name=self.vm_name,
            vmm_server_id=self.vmm_server_id)


def get_virtual_machine(resource_group_name: Optional[str] = None,
                        virtual_machine_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineResult:
    """
    Implements VirtualMachine GET method.
    Azure REST API version: 2022-05-21-preview.

    Other available API versions: 2023-04-01-preview.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_machine_name: Name of the VirtualMachine.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualMachineName'] = virtual_machine_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm:getVirtualMachine', __args__, opts=opts, typ=GetVirtualMachineResult).value

    return AwaitableGetVirtualMachineResult(
        availability_sets=pulumi.get(__ret__, 'availability_sets'),
        checkpoint_type=pulumi.get(__ret__, 'checkpoint_type'),
        checkpoints=pulumi.get(__ret__, 'checkpoints'),
        cloud_id=pulumi.get(__ret__, 'cloud_id'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        generation=pulumi.get(__ret__, 'generation'),
        guest_agent_profile=pulumi.get(__ret__, 'guest_agent_profile'),
        hardware_profile=pulumi.get(__ret__, 'hardware_profile'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        inventory_item_id=pulumi.get(__ret__, 'inventory_item_id'),
        last_restored_vm_checkpoint=pulumi.get(__ret__, 'last_restored_vm_checkpoint'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        os_profile=pulumi.get(__ret__, 'os_profile'),
        power_state=pulumi.get(__ret__, 'power_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        storage_profile=pulumi.get(__ret__, 'storage_profile'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        template_id=pulumi.get(__ret__, 'template_id'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'),
        vm_name=pulumi.get(__ret__, 'vm_name'),
        vmm_server_id=pulumi.get(__ret__, 'vmm_server_id'))


@_utilities.lift_output_func(get_virtual_machine)
def get_virtual_machine_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               virtual_machine_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineResult]:
    """
    Implements VirtualMachine GET method.
    Azure REST API version: 2022-05-21-preview.

    Other available API versions: 2023-04-01-preview.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_machine_name: Name of the VirtualMachine.
    """
    ...
