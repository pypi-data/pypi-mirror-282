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
from ._enums import *
from ._inputs import *

__all__ = ['VirtualMachineInstanceArgs', 'VirtualMachineInstance']

@pulumi.input_type
class VirtualMachineInstanceArgs:
    def __init__(__self__, *,
                 resource_uri: pulumi.Input[str],
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 hardware_profile: Optional[pulumi.Input['HardwareProfileArgs']] = None,
                 infrastructure_profile: Optional[pulumi.Input['InfrastructureProfileArgs']] = None,
                 network_profile: Optional[pulumi.Input['NetworkProfileArgs']] = None,
                 os_profile: Optional[pulumi.Input['OsProfileForVMInstanceArgs']] = None,
                 placement_profile: Optional[pulumi.Input['PlacementProfileArgs']] = None,
                 security_profile: Optional[pulumi.Input['SecurityProfileArgs']] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None):
        """
        The set of arguments for constructing a VirtualMachineInstance resource.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: Gets or sets the extended location.
        :param pulumi.Input['HardwareProfileArgs'] hardware_profile: Hardware properties.
        :param pulumi.Input['InfrastructureProfileArgs'] infrastructure_profile: Gets the infrastructure profile.
        :param pulumi.Input['NetworkProfileArgs'] network_profile: Network properties.
        :param pulumi.Input['OsProfileForVMInstanceArgs'] os_profile: OS properties.
        :param pulumi.Input['PlacementProfileArgs'] placement_profile: Placement properties.
        :param pulumi.Input['SecurityProfileArgs'] security_profile: Gets the security profile.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Storage properties.
        """
        pulumi.set(__self__, "resource_uri", resource_uri)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if hardware_profile is not None:
            pulumi.set(__self__, "hardware_profile", hardware_profile)
        if infrastructure_profile is not None:
            pulumi.set(__self__, "infrastructure_profile", infrastructure_profile)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)
        if placement_profile is not None:
            pulumi.set(__self__, "placement_profile", placement_profile)
        if security_profile is not None:
            pulumi.set(__self__, "security_profile", security_profile)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[str]:
        """
        The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input['HardwareProfileArgs']]:
        """
        Hardware properties.
        """
        return pulumi.get(self, "hardware_profile")

    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input['HardwareProfileArgs']]):
        pulumi.set(self, "hardware_profile", value)

    @property
    @pulumi.getter(name="infrastructureProfile")
    def infrastructure_profile(self) -> Optional[pulumi.Input['InfrastructureProfileArgs']]:
        """
        Gets the infrastructure profile.
        """
        return pulumi.get(self, "infrastructure_profile")

    @infrastructure_profile.setter
    def infrastructure_profile(self, value: Optional[pulumi.Input['InfrastructureProfileArgs']]):
        pulumi.set(self, "infrastructure_profile", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NetworkProfileArgs']]:
        """
        Network properties.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['OsProfileForVMInstanceArgs']]:
        """
        OS properties.
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['OsProfileForVMInstanceArgs']]):
        pulumi.set(self, "os_profile", value)

    @property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> Optional[pulumi.Input['PlacementProfileArgs']]:
        """
        Placement properties.
        """
        return pulumi.get(self, "placement_profile")

    @placement_profile.setter
    def placement_profile(self, value: Optional[pulumi.Input['PlacementProfileArgs']]):
        pulumi.set(self, "placement_profile", value)

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input['SecurityProfileArgs']]:
        """
        Gets the security profile.
        """
        return pulumi.get(self, "security_profile")

    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input['SecurityProfileArgs']]):
        pulumi.set(self, "security_profile", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Storage properties.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)


class VirtualMachineInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['HardwareProfileArgs']]] = None,
                 infrastructure_profile: Optional[pulumi.Input[pulumi.InputType['InfrastructureProfileArgs']]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OsProfileForVMInstanceArgs']]] = None,
                 placement_profile: Optional[pulumi.Input[pulumi.InputType['PlacementProfileArgs']]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['SecurityProfileArgs']]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 __props__=None):
        """
        Define the virtualMachineInstance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: Gets or sets the extended location.
        :param pulumi.Input[pulumi.InputType['HardwareProfileArgs']] hardware_profile: Hardware properties.
        :param pulumi.Input[pulumi.InputType['InfrastructureProfileArgs']] infrastructure_profile: Gets the infrastructure profile.
        :param pulumi.Input[pulumi.InputType['NetworkProfileArgs']] network_profile: Network properties.
        :param pulumi.Input[pulumi.InputType['OsProfileForVMInstanceArgs']] os_profile: OS properties.
        :param pulumi.Input[pulumi.InputType['PlacementProfileArgs']] placement_profile: Placement properties.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
        :param pulumi.Input[pulumi.InputType['SecurityProfileArgs']] security_profile: Gets the security profile.
        :param pulumi.Input[pulumi.InputType['StorageProfileArgs']] storage_profile: Storage properties.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Define the virtualMachineInstance.

        :param str resource_name: The name of the resource.
        :param VirtualMachineInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['HardwareProfileArgs']]] = None,
                 infrastructure_profile: Optional[pulumi.Input[pulumi.InputType['InfrastructureProfileArgs']]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OsProfileForVMInstanceArgs']]] = None,
                 placement_profile: Optional[pulumi.Input[pulumi.InputType['PlacementProfileArgs']]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['SecurityProfileArgs']]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualMachineInstanceArgs.__new__(VirtualMachineInstanceArgs)

            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["hardware_profile"] = hardware_profile
            __props__.__dict__["infrastructure_profile"] = infrastructure_profile
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["os_profile"] = os_profile
            __props__.__dict__["placement_profile"] = placement_profile
            if resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'resource_uri'")
            __props__.__dict__["resource_uri"] = resource_uri
            __props__.__dict__["security_profile"] = security_profile
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["name"] = None
            __props__.__dict__["power_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_uid"] = None
            __props__.__dict__["statuses"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:connectedvmwarevsphere:VirtualMachineInstance"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20230301preview:VirtualMachineInstance"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20231201:VirtualMachineInstance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachineInstance, __self__).__init__(
            'azure-native:connectedvmwarevsphere/v20231001:VirtualMachineInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualMachineInstance':
        """
        Get an existing VirtualMachineInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualMachineInstanceArgs.__new__(VirtualMachineInstanceArgs)

        __props__.__dict__["extended_location"] = None
        __props__.__dict__["hardware_profile"] = None
        __props__.__dict__["infrastructure_profile"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["os_profile"] = None
        __props__.__dict__["placement_profile"] = None
        __props__.__dict__["power_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_uid"] = None
        __props__.__dict__["security_profile"] = None
        __props__.__dict__["statuses"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return VirtualMachineInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional['outputs.HardwareProfileResponse']]:
        """
        Hardware properties.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter(name="infrastructureProfile")
    def infrastructure_profile(self) -> pulumi.Output[Optional['outputs.InfrastructureProfileResponse']]:
        """
        Gets the infrastructure profile.
        """
        return pulumi.get(self, "infrastructure_profile")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.NetworkProfileResponse']]:
        """
        Network properties.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional['outputs.OsProfileForVMInstanceResponse']]:
        """
        OS properties.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> pulumi.Output[Optional['outputs.PlacementProfileResponse']]:
        """
        Placement properties.
        """
        return pulumi.get(self, "placement_profile")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[str]:
        """
        Gets the power state of the virtual machine.
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> pulumi.Output[str]:
        """
        Gets or sets a unique identifier for the vm resource.
        """
        return pulumi.get(self, "resource_uid")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[Optional['outputs.SecurityProfileResponse']]:
        """
        Gets the security profile.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence['outputs.ResourceStatusResponse']]:
        """
        The resource status information.
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.StorageProfileResponse']]:
        """
        Storage properties.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

