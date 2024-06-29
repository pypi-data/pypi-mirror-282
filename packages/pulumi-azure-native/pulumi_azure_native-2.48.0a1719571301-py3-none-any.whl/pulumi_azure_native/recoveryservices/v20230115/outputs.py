# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'WorkloadCrrAccessTokenResponse',
]

@pulumi.output_type
class WorkloadCrrAccessTokenResponse(dict):
    def __init__(__self__, *,
                 object_type: str,
                 access_token_string: Optional[str] = None,
                 b_ms_active_region: Optional[str] = None,
                 backup_management_type: Optional[str] = None,
                 container_id: Optional[str] = None,
                 container_name: Optional[str] = None,
                 container_type: Optional[str] = None,
                 coordinator_service_stamp_id: Optional[str] = None,
                 coordinator_service_stamp_uri: Optional[str] = None,
                 datasource_container_name: Optional[str] = None,
                 datasource_id: Optional[str] = None,
                 datasource_name: Optional[str] = None,
                 datasource_type: Optional[str] = None,
                 policy_id: Optional[str] = None,
                 policy_name: Optional[str] = None,
                 protectable_object_container_host_os_name: Optional[str] = None,
                 protectable_object_friendly_name: Optional[str] = None,
                 protectable_object_parent_logical_container_name: Optional[str] = None,
                 protectable_object_protection_state: Optional[str] = None,
                 protectable_object_unique_name: Optional[str] = None,
                 protectable_object_workload_type: Optional[str] = None,
                 protection_container_id: Optional[float] = None,
                 protection_service_stamp_id: Optional[str] = None,
                 protection_service_stamp_uri: Optional[str] = None,
                 recovery_point_id: Optional[str] = None,
                 recovery_point_time: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 resource_id: Optional[str] = None,
                 resource_name: Optional[str] = None,
                 rp_is_managed_virtual_machine: Optional[bool] = None,
                 rp_original_sa_option: Optional[bool] = None,
                 rp_tier_information: Optional[Mapping[str, str]] = None,
                 rp_vm_size_description: Optional[str] = None,
                 subscription_id: Optional[str] = None,
                 token_extended_information: Optional[str] = None):
        """
        :param str object_type: Type of the specific object - used for deserializing
               Expected value is 'WorkloadCrrAccessToken'.
        :param str access_token_string: Access token used for authentication
        :param str b_ms_active_region: Active region name of BMS Stamp
        :param str backup_management_type: Backup Management Type
        :param str container_id: Container Id
        :param str container_name: Container Unique name
        :param str container_type: Container Type
        :param str coordinator_service_stamp_id: CoordinatorServiceStampId to be used by BCM in restore call
        :param str coordinator_service_stamp_uri: CoordinatorServiceStampUri to be used by BCM in restore call
        :param str datasource_container_name: Datasource Container Unique Name
        :param str datasource_id: Datasource Id
        :param str datasource_name: Datasource Friendly Name
        :param str datasource_type: Datasource Type
        :param str policy_id: Policy Id
        :param str policy_name: Policy Name
        :param float protection_container_id: Protected item container id
        :param str protection_service_stamp_id: ProtectionServiceStampId to be used by BCM in restore call
        :param str protection_service_stamp_uri: ProtectionServiceStampUri to be used by BCM in restore call
        :param str recovery_point_id: Recovery Point Id
        :param str recovery_point_time: Recovery Point Time
        :param str resource_group_name: Resource Group name of the source vault
        :param str resource_id: Resource Id of the source vault
        :param str resource_name: Resource Name of the source vault
        :param bool rp_is_managed_virtual_machine: Recovery point information: Managed virtual machine
        :param bool rp_original_sa_option: Recovery point information: Original SA option
        :param Mapping[str, str] rp_tier_information: Recovery point Tier Information
        :param str rp_vm_size_description: Recovery point information: VM size description
        :param str subscription_id: Subscription Id of the source vault
        :param str token_extended_information: Extended Information about the token like FileSpec etc.
        """
        pulumi.set(__self__, "object_type", 'WorkloadCrrAccessToken')
        if access_token_string is not None:
            pulumi.set(__self__, "access_token_string", access_token_string)
        if b_ms_active_region is not None:
            pulumi.set(__self__, "b_ms_active_region", b_ms_active_region)
        if backup_management_type is not None:
            pulumi.set(__self__, "backup_management_type", backup_management_type)
        if container_id is not None:
            pulumi.set(__self__, "container_id", container_id)
        if container_name is not None:
            pulumi.set(__self__, "container_name", container_name)
        if container_type is not None:
            pulumi.set(__self__, "container_type", container_type)
        if coordinator_service_stamp_id is not None:
            pulumi.set(__self__, "coordinator_service_stamp_id", coordinator_service_stamp_id)
        if coordinator_service_stamp_uri is not None:
            pulumi.set(__self__, "coordinator_service_stamp_uri", coordinator_service_stamp_uri)
        if datasource_container_name is not None:
            pulumi.set(__self__, "datasource_container_name", datasource_container_name)
        if datasource_id is not None:
            pulumi.set(__self__, "datasource_id", datasource_id)
        if datasource_name is not None:
            pulumi.set(__self__, "datasource_name", datasource_name)
        if datasource_type is not None:
            pulumi.set(__self__, "datasource_type", datasource_type)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if protectable_object_container_host_os_name is not None:
            pulumi.set(__self__, "protectable_object_container_host_os_name", protectable_object_container_host_os_name)
        if protectable_object_friendly_name is not None:
            pulumi.set(__self__, "protectable_object_friendly_name", protectable_object_friendly_name)
        if protectable_object_parent_logical_container_name is not None:
            pulumi.set(__self__, "protectable_object_parent_logical_container_name", protectable_object_parent_logical_container_name)
        if protectable_object_protection_state is not None:
            pulumi.set(__self__, "protectable_object_protection_state", protectable_object_protection_state)
        if protectable_object_unique_name is not None:
            pulumi.set(__self__, "protectable_object_unique_name", protectable_object_unique_name)
        if protectable_object_workload_type is not None:
            pulumi.set(__self__, "protectable_object_workload_type", protectable_object_workload_type)
        if protection_container_id is not None:
            pulumi.set(__self__, "protection_container_id", protection_container_id)
        if protection_service_stamp_id is not None:
            pulumi.set(__self__, "protection_service_stamp_id", protection_service_stamp_id)
        if protection_service_stamp_uri is not None:
            pulumi.set(__self__, "protection_service_stamp_uri", protection_service_stamp_uri)
        if recovery_point_id is not None:
            pulumi.set(__self__, "recovery_point_id", recovery_point_id)
        if recovery_point_time is not None:
            pulumi.set(__self__, "recovery_point_time", recovery_point_time)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if rp_is_managed_virtual_machine is not None:
            pulumi.set(__self__, "rp_is_managed_virtual_machine", rp_is_managed_virtual_machine)
        if rp_original_sa_option is not None:
            pulumi.set(__self__, "rp_original_sa_option", rp_original_sa_option)
        if rp_tier_information is not None:
            pulumi.set(__self__, "rp_tier_information", rp_tier_information)
        if rp_vm_size_description is not None:
            pulumi.set(__self__, "rp_vm_size_description", rp_vm_size_description)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if token_extended_information is not None:
            pulumi.set(__self__, "token_extended_information", token_extended_information)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> str:
        """
        Type of the specific object - used for deserializing
        Expected value is 'WorkloadCrrAccessToken'.
        """
        return pulumi.get(self, "object_type")

    @property
    @pulumi.getter(name="accessTokenString")
    def access_token_string(self) -> Optional[str]:
        """
        Access token used for authentication
        """
        return pulumi.get(self, "access_token_string")

    @property
    @pulumi.getter(name="bMSActiveRegion")
    def b_ms_active_region(self) -> Optional[str]:
        """
        Active region name of BMS Stamp
        """
        return pulumi.get(self, "b_ms_active_region")

    @property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[str]:
        """
        Backup Management Type
        """
        return pulumi.get(self, "backup_management_type")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[str]:
        """
        Container Id
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[str]:
        """
        Container Unique name
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="containerType")
    def container_type(self) -> Optional[str]:
        """
        Container Type
        """
        return pulumi.get(self, "container_type")

    @property
    @pulumi.getter(name="coordinatorServiceStampId")
    def coordinator_service_stamp_id(self) -> Optional[str]:
        """
        CoordinatorServiceStampId to be used by BCM in restore call
        """
        return pulumi.get(self, "coordinator_service_stamp_id")

    @property
    @pulumi.getter(name="coordinatorServiceStampUri")
    def coordinator_service_stamp_uri(self) -> Optional[str]:
        """
        CoordinatorServiceStampUri to be used by BCM in restore call
        """
        return pulumi.get(self, "coordinator_service_stamp_uri")

    @property
    @pulumi.getter(name="datasourceContainerName")
    def datasource_container_name(self) -> Optional[str]:
        """
        Datasource Container Unique Name
        """
        return pulumi.get(self, "datasource_container_name")

    @property
    @pulumi.getter(name="datasourceId")
    def datasource_id(self) -> Optional[str]:
        """
        Datasource Id
        """
        return pulumi.get(self, "datasource_id")

    @property
    @pulumi.getter(name="datasourceName")
    def datasource_name(self) -> Optional[str]:
        """
        Datasource Friendly Name
        """
        return pulumi.get(self, "datasource_name")

    @property
    @pulumi.getter(name="datasourceType")
    def datasource_type(self) -> Optional[str]:
        """
        Datasource Type
        """
        return pulumi.get(self, "datasource_type")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[str]:
        """
        Policy Id
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[str]:
        """
        Policy Name
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="protectableObjectContainerHostOsName")
    def protectable_object_container_host_os_name(self) -> Optional[str]:
        return pulumi.get(self, "protectable_object_container_host_os_name")

    @property
    @pulumi.getter(name="protectableObjectFriendlyName")
    def protectable_object_friendly_name(self) -> Optional[str]:
        return pulumi.get(self, "protectable_object_friendly_name")

    @property
    @pulumi.getter(name="protectableObjectParentLogicalContainerName")
    def protectable_object_parent_logical_container_name(self) -> Optional[str]:
        return pulumi.get(self, "protectable_object_parent_logical_container_name")

    @property
    @pulumi.getter(name="protectableObjectProtectionState")
    def protectable_object_protection_state(self) -> Optional[str]:
        return pulumi.get(self, "protectable_object_protection_state")

    @property
    @pulumi.getter(name="protectableObjectUniqueName")
    def protectable_object_unique_name(self) -> Optional[str]:
        return pulumi.get(self, "protectable_object_unique_name")

    @property
    @pulumi.getter(name="protectableObjectWorkloadType")
    def protectable_object_workload_type(self) -> Optional[str]:
        return pulumi.get(self, "protectable_object_workload_type")

    @property
    @pulumi.getter(name="protectionContainerId")
    def protection_container_id(self) -> Optional[float]:
        """
        Protected item container id
        """
        return pulumi.get(self, "protection_container_id")

    @property
    @pulumi.getter(name="protectionServiceStampId")
    def protection_service_stamp_id(self) -> Optional[str]:
        """
        ProtectionServiceStampId to be used by BCM in restore call
        """
        return pulumi.get(self, "protection_service_stamp_id")

    @property
    @pulumi.getter(name="protectionServiceStampUri")
    def protection_service_stamp_uri(self) -> Optional[str]:
        """
        ProtectionServiceStampUri to be used by BCM in restore call
        """
        return pulumi.get(self, "protection_service_stamp_uri")

    @property
    @pulumi.getter(name="recoveryPointId")
    def recovery_point_id(self) -> Optional[str]:
        """
        Recovery Point Id
        """
        return pulumi.get(self, "recovery_point_id")

    @property
    @pulumi.getter(name="recoveryPointTime")
    def recovery_point_time(self) -> Optional[str]:
        """
        Recovery Point Time
        """
        return pulumi.get(self, "recovery_point_time")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[str]:
        """
        Resource Group name of the source vault
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Resource Id of the source vault
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[str]:
        """
        Resource Name of the source vault
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="rpIsManagedVirtualMachine")
    def rp_is_managed_virtual_machine(self) -> Optional[bool]:
        """
        Recovery point information: Managed virtual machine
        """
        return pulumi.get(self, "rp_is_managed_virtual_machine")

    @property
    @pulumi.getter(name="rpOriginalSAOption")
    def rp_original_sa_option(self) -> Optional[bool]:
        """
        Recovery point information: Original SA option
        """
        return pulumi.get(self, "rp_original_sa_option")

    @property
    @pulumi.getter(name="rpTierInformation")
    def rp_tier_information(self) -> Optional[Mapping[str, str]]:
        """
        Recovery point Tier Information
        """
        return pulumi.get(self, "rp_tier_information")

    @property
    @pulumi.getter(name="rpVMSizeDescription")
    def rp_vm_size_description(self) -> Optional[str]:
        """
        Recovery point information: VM size description
        """
        return pulumi.get(self, "rp_vm_size_description")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[str]:
        """
        Subscription Id of the source vault
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="tokenExtendedInformation")
    def token_extended_information(self) -> Optional[str]:
        """
        Extended Information about the token like FileSpec etc.
        """
        return pulumi.get(self, "token_extended_information")


