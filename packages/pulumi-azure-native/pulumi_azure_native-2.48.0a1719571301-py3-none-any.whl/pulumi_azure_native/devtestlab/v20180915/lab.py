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

__all__ = ['LabArgs', 'Lab']

@pulumi.input_type
class LabArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 announcement: Optional[pulumi.Input['LabAnnouncementPropertiesArgs']] = None,
                 environment_permission: Optional[pulumi.Input[Union[str, 'EnvironmentPermission']]] = None,
                 extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lab_storage_type: Optional[pulumi.Input[Union[str, 'StorageType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mandatory_artifacts_resource_ids_linux: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mandatory_artifacts_resource_ids_windows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 premium_data_disks: Optional[pulumi.Input[Union[str, 'PremiumDataDisk']]] = None,
                 support: Optional[pulumi.Input['LabSupportPropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Lab resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['LabAnnouncementPropertiesArgs'] announcement: The properties of any lab announcement associated with this lab
        :param pulumi.Input[Union[str, 'EnvironmentPermission']] environment_permission: The access rights to be granted to the user when provisioning an environment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] extended_properties: Extended properties of the lab used for experimental features
        :param pulumi.Input[Union[str, 'StorageType']] lab_storage_type: Type of storage used by the lab. It can be either Premium or Standard. Default is Premium.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mandatory_artifacts_resource_ids_linux: The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mandatory_artifacts_resource_ids_windows: The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.
        :param pulumi.Input[str] name: The name of the lab.
        :param pulumi.Input[Union[str, 'PremiumDataDisk']] premium_data_disks: The setting to enable usage of premium data disks.
               When its value is 'Enabled', creation of standard or premium data disks is allowed.
               When its value is 'Disabled', only creation of standard data disks is allowed.
        :param pulumi.Input['LabSupportPropertiesArgs'] support: The properties of any lab support message associated with this lab
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if announcement is not None:
            pulumi.set(__self__, "announcement", announcement)
        if environment_permission is not None:
            pulumi.set(__self__, "environment_permission", environment_permission)
        if extended_properties is not None:
            pulumi.set(__self__, "extended_properties", extended_properties)
        if lab_storage_type is None:
            lab_storage_type = 'Premium'
        if lab_storage_type is not None:
            pulumi.set(__self__, "lab_storage_type", lab_storage_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mandatory_artifacts_resource_ids_linux is not None:
            pulumi.set(__self__, "mandatory_artifacts_resource_ids_linux", mandatory_artifacts_resource_ids_linux)
        if mandatory_artifacts_resource_ids_windows is not None:
            pulumi.set(__self__, "mandatory_artifacts_resource_ids_windows", mandatory_artifacts_resource_ids_windows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if premium_data_disks is not None:
            pulumi.set(__self__, "premium_data_disks", premium_data_disks)
        if support is not None:
            pulumi.set(__self__, "support", support)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def announcement(self) -> Optional[pulumi.Input['LabAnnouncementPropertiesArgs']]:
        """
        The properties of any lab announcement associated with this lab
        """
        return pulumi.get(self, "announcement")

    @announcement.setter
    def announcement(self, value: Optional[pulumi.Input['LabAnnouncementPropertiesArgs']]):
        pulumi.set(self, "announcement", value)

    @property
    @pulumi.getter(name="environmentPermission")
    def environment_permission(self) -> Optional[pulumi.Input[Union[str, 'EnvironmentPermission']]]:
        """
        The access rights to be granted to the user when provisioning an environment
        """
        return pulumi.get(self, "environment_permission")

    @environment_permission.setter
    def environment_permission(self, value: Optional[pulumi.Input[Union[str, 'EnvironmentPermission']]]):
        pulumi.set(self, "environment_permission", value)

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Extended properties of the lab used for experimental features
        """
        return pulumi.get(self, "extended_properties")

    @extended_properties.setter
    def extended_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "extended_properties", value)

    @property
    @pulumi.getter(name="labStorageType")
    def lab_storage_type(self) -> Optional[pulumi.Input[Union[str, 'StorageType']]]:
        """
        Type of storage used by the lab. It can be either Premium or Standard. Default is Premium.
        """
        return pulumi.get(self, "lab_storage_type")

    @lab_storage_type.setter
    def lab_storage_type(self, value: Optional[pulumi.Input[Union[str, 'StorageType']]]):
        pulumi.set(self, "lab_storage_type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsLinux")
    def mandatory_artifacts_resource_ids_linux(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.
        """
        return pulumi.get(self, "mandatory_artifacts_resource_ids_linux")

    @mandatory_artifacts_resource_ids_linux.setter
    def mandatory_artifacts_resource_ids_linux(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "mandatory_artifacts_resource_ids_linux", value)

    @property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsWindows")
    def mandatory_artifacts_resource_ids_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.
        """
        return pulumi.get(self, "mandatory_artifacts_resource_ids_windows")

    @mandatory_artifacts_resource_ids_windows.setter
    def mandatory_artifacts_resource_ids_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "mandatory_artifacts_resource_ids_windows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="premiumDataDisks")
    def premium_data_disks(self) -> Optional[pulumi.Input[Union[str, 'PremiumDataDisk']]]:
        """
        The setting to enable usage of premium data disks.
        When its value is 'Enabled', creation of standard or premium data disks is allowed.
        When its value is 'Disabled', only creation of standard data disks is allowed.
        """
        return pulumi.get(self, "premium_data_disks")

    @premium_data_disks.setter
    def premium_data_disks(self, value: Optional[pulumi.Input[Union[str, 'PremiumDataDisk']]]):
        pulumi.set(self, "premium_data_disks", value)

    @property
    @pulumi.getter
    def support(self) -> Optional[pulumi.Input['LabSupportPropertiesArgs']]:
        """
        The properties of any lab support message associated with this lab
        """
        return pulumi.get(self, "support")

    @support.setter
    def support(self, value: Optional[pulumi.Input['LabSupportPropertiesArgs']]):
        pulumi.set(self, "support", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Lab(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 announcement: Optional[pulumi.Input[pulumi.InputType['LabAnnouncementPropertiesArgs']]] = None,
                 environment_permission: Optional[pulumi.Input[Union[str, 'EnvironmentPermission']]] = None,
                 extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lab_storage_type: Optional[pulumi.Input[Union[str, 'StorageType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mandatory_artifacts_resource_ids_linux: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mandatory_artifacts_resource_ids_windows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 premium_data_disks: Optional[pulumi.Input[Union[str, 'PremiumDataDisk']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 support: Optional[pulumi.Input[pulumi.InputType['LabSupportPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A lab.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LabAnnouncementPropertiesArgs']] announcement: The properties of any lab announcement associated with this lab
        :param pulumi.Input[Union[str, 'EnvironmentPermission']] environment_permission: The access rights to be granted to the user when provisioning an environment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] extended_properties: Extended properties of the lab used for experimental features
        :param pulumi.Input[Union[str, 'StorageType']] lab_storage_type: Type of storage used by the lab. It can be either Premium or Standard. Default is Premium.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mandatory_artifacts_resource_ids_linux: The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mandatory_artifacts_resource_ids_windows: The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.
        :param pulumi.Input[str] name: The name of the lab.
        :param pulumi.Input[Union[str, 'PremiumDataDisk']] premium_data_disks: The setting to enable usage of premium data disks.
               When its value is 'Enabled', creation of standard or premium data disks is allowed.
               When its value is 'Disabled', only creation of standard data disks is allowed.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['LabSupportPropertiesArgs']] support: The properties of any lab support message associated with this lab
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LabArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A lab.

        :param str resource_name: The name of the resource.
        :param LabArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LabArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 announcement: Optional[pulumi.Input[pulumi.InputType['LabAnnouncementPropertiesArgs']]] = None,
                 environment_permission: Optional[pulumi.Input[Union[str, 'EnvironmentPermission']]] = None,
                 extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lab_storage_type: Optional[pulumi.Input[Union[str, 'StorageType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mandatory_artifacts_resource_ids_linux: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mandatory_artifacts_resource_ids_windows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 premium_data_disks: Optional[pulumi.Input[Union[str, 'PremiumDataDisk']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 support: Optional[pulumi.Input[pulumi.InputType['LabSupportPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LabArgs.__new__(LabArgs)

            __props__.__dict__["announcement"] = announcement
            __props__.__dict__["environment_permission"] = environment_permission
            __props__.__dict__["extended_properties"] = extended_properties
            if lab_storage_type is None:
                lab_storage_type = 'Premium'
            __props__.__dict__["lab_storage_type"] = lab_storage_type
            __props__.__dict__["location"] = location
            __props__.__dict__["mandatory_artifacts_resource_ids_linux"] = mandatory_artifacts_resource_ids_linux
            __props__.__dict__["mandatory_artifacts_resource_ids_windows"] = mandatory_artifacts_resource_ids_windows
            __props__.__dict__["name"] = name
            __props__.__dict__["premium_data_disks"] = premium_data_disks
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["support"] = support
            __props__.__dict__["tags"] = tags
            __props__.__dict__["artifacts_storage_account"] = None
            __props__.__dict__["created_date"] = None
            __props__.__dict__["default_premium_storage_account"] = None
            __props__.__dict__["default_storage_account"] = None
            __props__.__dict__["load_balancer_id"] = None
            __props__.__dict__["network_security_group_id"] = None
            __props__.__dict__["premium_data_disk_storage_account"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["public_ip_id"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["unique_identifier"] = None
            __props__.__dict__["vault_name"] = None
            __props__.__dict__["vm_creation_resource_group"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devtestlab:Lab"), pulumi.Alias(type_="azure-native:devtestlab/v20150521preview:Lab"), pulumi.Alias(type_="azure-native:devtestlab/v20160515:Lab")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Lab, __self__).__init__(
            'azure-native:devtestlab/v20180915:Lab',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Lab':
        """
        Get an existing Lab resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LabArgs.__new__(LabArgs)

        __props__.__dict__["announcement"] = None
        __props__.__dict__["artifacts_storage_account"] = None
        __props__.__dict__["created_date"] = None
        __props__.__dict__["default_premium_storage_account"] = None
        __props__.__dict__["default_storage_account"] = None
        __props__.__dict__["environment_permission"] = None
        __props__.__dict__["extended_properties"] = None
        __props__.__dict__["lab_storage_type"] = None
        __props__.__dict__["load_balancer_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mandatory_artifacts_resource_ids_linux"] = None
        __props__.__dict__["mandatory_artifacts_resource_ids_windows"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_security_group_id"] = None
        __props__.__dict__["premium_data_disk_storage_account"] = None
        __props__.__dict__["premium_data_disks"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_ip_id"] = None
        __props__.__dict__["support"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unique_identifier"] = None
        __props__.__dict__["vault_name"] = None
        __props__.__dict__["vm_creation_resource_group"] = None
        return Lab(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def announcement(self) -> pulumi.Output[Optional['outputs.LabAnnouncementPropertiesResponse']]:
        """
        The properties of any lab announcement associated with this lab
        """
        return pulumi.get(self, "announcement")

    @property
    @pulumi.getter(name="artifactsStorageAccount")
    def artifacts_storage_account(self) -> pulumi.Output[str]:
        """
        The lab's artifact storage account.
        """
        return pulumi.get(self, "artifacts_storage_account")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        The creation date of the lab.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="defaultPremiumStorageAccount")
    def default_premium_storage_account(self) -> pulumi.Output[str]:
        """
        The lab's default premium storage account.
        """
        return pulumi.get(self, "default_premium_storage_account")

    @property
    @pulumi.getter(name="defaultStorageAccount")
    def default_storage_account(self) -> pulumi.Output[str]:
        """
        The lab's default storage account.
        """
        return pulumi.get(self, "default_storage_account")

    @property
    @pulumi.getter(name="environmentPermission")
    def environment_permission(self) -> pulumi.Output[Optional[str]]:
        """
        The access rights to be granted to the user when provisioning an environment
        """
        return pulumi.get(self, "environment_permission")

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Extended properties of the lab used for experimental features
        """
        return pulumi.get(self, "extended_properties")

    @property
    @pulumi.getter(name="labStorageType")
    def lab_storage_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of storage used by the lab. It can be either Premium or Standard. Default is Premium.
        """
        return pulumi.get(self, "lab_storage_type")

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> pulumi.Output[str]:
        """
        The load balancer used to for lab VMs that use shared IP address.
        """
        return pulumi.get(self, "load_balancer_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsLinux")
    def mandatory_artifacts_resource_ids_linux(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.
        """
        return pulumi.get(self, "mandatory_artifacts_resource_ids_linux")

    @property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsWindows")
    def mandatory_artifacts_resource_ids_windows(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.
        """
        return pulumi.get(self, "mandatory_artifacts_resource_ids_windows")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSecurityGroupId")
    def network_security_group_id(self) -> pulumi.Output[str]:
        """
        The Network Security Group attached to the lab VMs Network interfaces to restrict open ports.
        """
        return pulumi.get(self, "network_security_group_id")

    @property
    @pulumi.getter(name="premiumDataDiskStorageAccount")
    def premium_data_disk_storage_account(self) -> pulumi.Output[str]:
        """
        The lab's premium data disk storage account.
        """
        return pulumi.get(self, "premium_data_disk_storage_account")

    @property
    @pulumi.getter(name="premiumDataDisks")
    def premium_data_disks(self) -> pulumi.Output[Optional[str]]:
        """
        The setting to enable usage of premium data disks.
        When its value is 'Enabled', creation of standard or premium data disks is allowed.
        When its value is 'Disabled', only creation of standard data disks is allowed.
        """
        return pulumi.get(self, "premium_data_disks")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> pulumi.Output[str]:
        """
        The public IP address for the lab's load balancer.
        """
        return pulumi.get(self, "public_ip_id")

    @property
    @pulumi.getter
    def support(self) -> pulumi.Output[Optional['outputs.LabSupportPropertiesResponse']]:
        """
        The properties of any lab support message associated with this lab
        """
        return pulumi.get(self, "support")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> pulumi.Output[str]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Output[str]:
        """
        The lab's Key vault.
        """
        return pulumi.get(self, "vault_name")

    @property
    @pulumi.getter(name="vmCreationResourceGroup")
    def vm_creation_resource_group(self) -> pulumi.Output[str]:
        """
        The resource group in which all new lab virtual machines will be created. To let DevTest Labs manage resource group creation, set this value to null.
        """
        return pulumi.get(self, "vm_creation_resource_group")

