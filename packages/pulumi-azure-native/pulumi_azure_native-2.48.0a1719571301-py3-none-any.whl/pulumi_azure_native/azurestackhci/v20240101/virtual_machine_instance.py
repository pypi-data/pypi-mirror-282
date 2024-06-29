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
                 hardware_profile: Optional[pulumi.Input['VirtualMachineInstancePropertiesHardwareProfileArgs']] = None,
                 http_proxy_config: Optional[pulumi.Input['HttpProxyConfigurationArgs']] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 network_profile: Optional[pulumi.Input['VirtualMachineInstancePropertiesNetworkProfileArgs']] = None,
                 os_profile: Optional[pulumi.Input['VirtualMachineInstancePropertiesOsProfileArgs']] = None,
                 resource_uid: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input['VirtualMachineInstancePropertiesSecurityProfileArgs']] = None,
                 storage_profile: Optional[pulumi.Input['VirtualMachineInstancePropertiesStorageProfileArgs']] = None):
        """
        The set of arguments for constructing a VirtualMachineInstance resource.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extendedLocation of the resource.
        :param pulumi.Input['VirtualMachineInstancePropertiesHardwareProfileArgs'] hardware_profile: HardwareProfile - Specifies the hardware settings for the virtual machine instance.
        :param pulumi.Input['HttpProxyConfigurationArgs'] http_proxy_config: HTTP Proxy configuration for the VM.
        :param pulumi.Input['IdentityArgs'] identity: Identity for the resource.
        :param pulumi.Input['VirtualMachineInstancePropertiesNetworkProfileArgs'] network_profile: NetworkProfile - describes the network configuration the virtual machine instance
        :param pulumi.Input['VirtualMachineInstancePropertiesOsProfileArgs'] os_profile: OsProfile - describes the configuration of the operating system and sets login data
        :param pulumi.Input[str] resource_uid: Unique identifier defined by ARC to identify the guest of the VM.
        :param pulumi.Input['VirtualMachineInstancePropertiesSecurityProfileArgs'] security_profile: SecurityProfile - Specifies the security settings for the virtual machine instance.
        :param pulumi.Input['VirtualMachineInstancePropertiesStorageProfileArgs'] storage_profile: StorageProfile - contains information about the disks and storage information for the virtual machine instance
        """
        pulumi.set(__self__, "resource_uri", resource_uri)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if hardware_profile is not None:
            pulumi.set(__self__, "hardware_profile", hardware_profile)
        if http_proxy_config is not None:
            pulumi.set(__self__, "http_proxy_config", http_proxy_config)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)
        if resource_uid is not None:
            pulumi.set(__self__, "resource_uid", resource_uid)
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
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input['VirtualMachineInstancePropertiesHardwareProfileArgs']]:
        """
        HardwareProfile - Specifies the hardware settings for the virtual machine instance.
        """
        return pulumi.get(self, "hardware_profile")

    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input['VirtualMachineInstancePropertiesHardwareProfileArgs']]):
        pulumi.set(self, "hardware_profile", value)

    @property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> Optional[pulumi.Input['HttpProxyConfigurationArgs']]:
        """
        HTTP Proxy configuration for the VM.
        """
        return pulumi.get(self, "http_proxy_config")

    @http_proxy_config.setter
    def http_proxy_config(self, value: Optional[pulumi.Input['HttpProxyConfigurationArgs']]):
        pulumi.set(self, "http_proxy_config", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['VirtualMachineInstancePropertiesNetworkProfileArgs']]:
        """
        NetworkProfile - describes the network configuration the virtual machine instance
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['VirtualMachineInstancePropertiesNetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['VirtualMachineInstancePropertiesOsProfileArgs']]:
        """
        OsProfile - describes the configuration of the operating system and sets login data
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['VirtualMachineInstancePropertiesOsProfileArgs']]):
        pulumi.set(self, "os_profile", value)

    @property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier defined by ARC to identify the guest of the VM.
        """
        return pulumi.get(self, "resource_uid")

    @resource_uid.setter
    def resource_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_uid", value)

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input['VirtualMachineInstancePropertiesSecurityProfileArgs']]:
        """
        SecurityProfile - Specifies the security settings for the virtual machine instance.
        """
        return pulumi.get(self, "security_profile")

    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input['VirtualMachineInstancePropertiesSecurityProfileArgs']]):
        pulumi.set(self, "security_profile", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['VirtualMachineInstancePropertiesStorageProfileArgs']]:
        """
        StorageProfile - contains information about the disks and storage information for the virtual machine instance
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['VirtualMachineInstancePropertiesStorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)


class VirtualMachineInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesHardwareProfileArgs']]] = None,
                 http_proxy_config: Optional[pulumi.Input[pulumi.InputType['HttpProxyConfigurationArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesNetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesOsProfileArgs']]] = None,
                 resource_uid: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesSecurityProfileArgs']]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesStorageProfileArgs']]] = None,
                 __props__=None):
        """
        The virtual machine instance resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesHardwareProfileArgs']] hardware_profile: HardwareProfile - Specifies the hardware settings for the virtual machine instance.
        :param pulumi.Input[pulumi.InputType['HttpProxyConfigurationArgs']] http_proxy_config: HTTP Proxy configuration for the VM.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: Identity for the resource.
        :param pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesNetworkProfileArgs']] network_profile: NetworkProfile - describes the network configuration the virtual machine instance
        :param pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesOsProfileArgs']] os_profile: OsProfile - describes the configuration of the operating system and sets login data
        :param pulumi.Input[str] resource_uid: Unique identifier defined by ARC to identify the guest of the VM.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
        :param pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesSecurityProfileArgs']] security_profile: SecurityProfile - Specifies the security settings for the virtual machine instance.
        :param pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesStorageProfileArgs']] storage_profile: StorageProfile - contains information about the disks and storage information for the virtual machine instance
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The virtual machine instance resource definition.

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
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesHardwareProfileArgs']]] = None,
                 http_proxy_config: Optional[pulumi.Input[pulumi.InputType['HttpProxyConfigurationArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesNetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesOsProfileArgs']]] = None,
                 resource_uid: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesSecurityProfileArgs']]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineInstancePropertiesStorageProfileArgs']]] = None,
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
            __props__.__dict__["http_proxy_config"] = http_proxy_config
            __props__.__dict__["identity"] = identity
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["os_profile"] = os_profile
            __props__.__dict__["resource_uid"] = resource_uid
            if resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'resource_uri'")
            __props__.__dict__["resource_uri"] = resource_uri
            __props__.__dict__["security_profile"] = security_profile
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["guest_agent_install_status"] = None
            __props__.__dict__["instance_view"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vm_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:VirtualMachineInstance"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:VirtualMachineInstance"), pulumi.Alias(type_="azure-native:azurestackhci/v20230901preview:VirtualMachineInstance"), pulumi.Alias(type_="azure-native:azurestackhci/v20240201preview:VirtualMachineInstance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachineInstance, __self__).__init__(
            'azure-native:azurestackhci/v20240101:VirtualMachineInstance',
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
        __props__.__dict__["guest_agent_install_status"] = None
        __props__.__dict__["hardware_profile"] = None
        __props__.__dict__["http_proxy_config"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["instance_view"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["os_profile"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_uid"] = None
        __props__.__dict__["security_profile"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_id"] = None
        return VirtualMachineInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="guestAgentInstallStatus")
    def guest_agent_install_status(self) -> pulumi.Output[Optional['outputs.GuestAgentInstallStatusResponse']]:
        """
        Guest agent install status.
        """
        return pulumi.get(self, "guest_agent_install_status")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional['outputs.VirtualMachineInstancePropertiesResponseHardwareProfile']]:
        """
        HardwareProfile - Specifies the hardware settings for the virtual machine instance.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> pulumi.Output[Optional['outputs.HttpProxyConfigurationResponse']]:
        """
        HTTP Proxy configuration for the VM.
        """
        return pulumi.get(self, "http_proxy_config")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output['outputs.VirtualMachineInstanceViewResponse']:
        """
        The virtual machine instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.VirtualMachineInstancePropertiesResponseNetworkProfile']]:
        """
        NetworkProfile - describes the network configuration the virtual machine instance
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional['outputs.VirtualMachineInstancePropertiesResponseOsProfile']]:
        """
        OsProfile - describes the configuration of the operating system and sets login data
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the virtual machine instance.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> pulumi.Output[Optional[str]]:
        """
        Unique identifier defined by ARC to identify the guest of the VM.
        """
        return pulumi.get(self, "resource_uid")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[Optional['outputs.VirtualMachineInstancePropertiesResponseSecurityProfile']]:
        """
        SecurityProfile - Specifies the security settings for the virtual machine instance.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.VirtualMachineInstanceStatusResponse']:
        """
        The observed state of virtual machine instances
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.VirtualMachineInstancePropertiesResponseStorageProfile']]:
        """
        StorageProfile - contains information about the disks and storage information for the virtual machine instance
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

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[str]:
        """
        Unique identifier for the vm resource.
        """
        return pulumi.get(self, "vm_id")

