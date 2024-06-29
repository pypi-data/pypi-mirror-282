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
    'OverviewStatusResponse',
    'ReportComplianceStatusResponse',
    'ReportPropertiesResponse',
    'ResourceMetadataResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class OverviewStatusResponse(dict):
    """
    The overview of the compliance result for one report.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "failedCount":
            suggest = "failed_count"
        elif key == "manualCount":
            suggest = "manual_count"
        elif key == "passedCount":
            suggest = "passed_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OverviewStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OverviewStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OverviewStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 failed_count: Optional[int] = None,
                 manual_count: Optional[int] = None,
                 passed_count: Optional[int] = None):
        """
        The overview of the compliance result for one report.
        :param int failed_count: The count of all failed full automation control.
        :param int manual_count: The count of all manual control.
        :param int passed_count: The count of all passed full automation control.
        """
        if failed_count is not None:
            pulumi.set(__self__, "failed_count", failed_count)
        if manual_count is not None:
            pulumi.set(__self__, "manual_count", manual_count)
        if passed_count is not None:
            pulumi.set(__self__, "passed_count", passed_count)

    @property
    @pulumi.getter(name="failedCount")
    def failed_count(self) -> Optional[int]:
        """
        The count of all failed full automation control.
        """
        return pulumi.get(self, "failed_count")

    @property
    @pulumi.getter(name="manualCount")
    def manual_count(self) -> Optional[int]:
        """
        The count of all manual control.
        """
        return pulumi.get(self, "manual_count")

    @property
    @pulumi.getter(name="passedCount")
    def passed_count(self) -> Optional[int]:
        """
        The count of all passed full automation control.
        """
        return pulumi.get(self, "passed_count")


@pulumi.output_type
class ReportComplianceStatusResponse(dict):
    """
    A list which includes all the compliance result for one report.
    """
    def __init__(__self__, *,
                 m365: Optional['outputs.OverviewStatusResponse'] = None):
        """
        A list which includes all the compliance result for one report.
        :param 'OverviewStatusResponse' m365: The Microsoft 365 certification name.
        """
        if m365 is not None:
            pulumi.set(__self__, "m365", m365)

    @property
    @pulumi.getter
    def m365(self) -> Optional['outputs.OverviewStatusResponse']:
        """
        The Microsoft 365 certification name.
        """
        return pulumi.get(self, "m365")


@pulumi.output_type
class ReportPropertiesResponse(dict):
    """
    Report's properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "complianceStatus":
            suggest = "compliance_status"
        elif key == "lastTriggerTime":
            suggest = "last_trigger_time"
        elif key == "nextTriggerTime":
            suggest = "next_trigger_time"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "reportName":
            suggest = "report_name"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "timeZone":
            suggest = "time_zone"
        elif key == "triggerTime":
            suggest = "trigger_time"
        elif key == "offerGuid":
            suggest = "offer_guid"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReportPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReportPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReportPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 compliance_status: 'outputs.ReportComplianceStatusResponse',
                 id: str,
                 last_trigger_time: str,
                 next_trigger_time: str,
                 provisioning_state: str,
                 report_name: str,
                 resources: Sequence['outputs.ResourceMetadataResponse'],
                 status: str,
                 subscriptions: Sequence[str],
                 tenant_id: str,
                 time_zone: str,
                 trigger_time: str,
                 offer_guid: Optional[str] = None):
        """
        Report's properties.
        :param 'ReportComplianceStatusResponse' compliance_status: Report compliance status.
        :param str id: Report id in database.
        :param str last_trigger_time: Report last collection trigger time.
        :param str next_trigger_time: Report next collection trigger time.
        :param str provisioning_state: Azure lifecycle management
        :param str report_name: Report name.
        :param Sequence['ResourceMetadataResponse'] resources: List of resource data.
        :param str status: Report status.
        :param Sequence[str] subscriptions: List of subscription Ids.
        :param str tenant_id: Report's tenant id.
        :param str time_zone: Report collection trigger time's time zone, the available list can be obtained by executing "Get-TimeZone -ListAvailable" in PowerShell.
               An example of valid timezone id is "Pacific Standard Time".
        :param str trigger_time: Report collection trigger time.
        :param str offer_guid: Report offer Guid.
        """
        pulumi.set(__self__, "compliance_status", compliance_status)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "last_trigger_time", last_trigger_time)
        pulumi.set(__self__, "next_trigger_time", next_trigger_time)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "report_name", report_name)
        pulumi.set(__self__, "resources", resources)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "subscriptions", subscriptions)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "time_zone", time_zone)
        pulumi.set(__self__, "trigger_time", trigger_time)
        if offer_guid is not None:
            pulumi.set(__self__, "offer_guid", offer_guid)

    @property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> 'outputs.ReportComplianceStatusResponse':
        """
        Report compliance status.
        """
        return pulumi.get(self, "compliance_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Report id in database.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastTriggerTime")
    def last_trigger_time(self) -> str:
        """
        Report last collection trigger time.
        """
        return pulumi.get(self, "last_trigger_time")

    @property
    @pulumi.getter(name="nextTriggerTime")
    def next_trigger_time(self) -> str:
        """
        Report next collection trigger time.
        """
        return pulumi.get(self, "next_trigger_time")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reportName")
    def report_name(self) -> str:
        """
        Report name.
        """
        return pulumi.get(self, "report_name")

    @property
    @pulumi.getter
    def resources(self) -> Sequence['outputs.ResourceMetadataResponse']:
        """
        List of resource data.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Report status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subscriptions(self) -> Sequence[str]:
        """
        List of subscription Ids.
        """
        return pulumi.get(self, "subscriptions")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        Report's tenant id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        Report collection trigger time's time zone, the available list can be obtained by executing "Get-TimeZone -ListAvailable" in PowerShell.
        An example of valid timezone id is "Pacific Standard Time".
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter(name="triggerTime")
    def trigger_time(self) -> str:
        """
        Report collection trigger time.
        """
        return pulumi.get(self, "trigger_time")

    @property
    @pulumi.getter(name="offerGuid")
    def offer_guid(self) -> Optional[str]:
        """
        Report offer Guid.
        """
        return pulumi.get(self, "offer_guid")


@pulumi.output_type
class ResourceMetadataResponse(dict):
    """
    Single resource Id's metadata.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceId":
            suggest = "resource_id"
        elif key == "resourceKind":
            suggest = "resource_kind"
        elif key == "resourceName":
            suggest = "resource_name"
        elif key == "resourceType":
            suggest = "resource_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceMetadataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceMetadataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceMetadataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_id: str,
                 resource_kind: Optional[str] = None,
                 resource_name: Optional[str] = None,
                 resource_type: Optional[str] = None,
                 tags: Optional[Mapping[str, str]] = None):
        """
        Single resource Id's metadata.
        :param str resource_id: Resource Id - e.g. "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1".
        :param str resource_kind: Resource kind.
        :param str resource_name: Resource name.
        :param str resource_type: Resource type.
        :param Mapping[str, str] tags: Resource's tag type.
        """
        pulumi.set(__self__, "resource_id", resource_id)
        if resource_kind is not None:
            pulumi.set(__self__, "resource_kind", resource_kind)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        Resource Id - e.g. "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1".
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[str]:
        """
        Resource kind.
        """
        return pulumi.get(self, "resource_kind")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource's tag type.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


