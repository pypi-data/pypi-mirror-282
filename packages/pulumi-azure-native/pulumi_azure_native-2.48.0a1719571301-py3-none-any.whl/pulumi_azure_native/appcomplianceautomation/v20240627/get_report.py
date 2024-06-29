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
    'GetReportResult',
    'AwaitableGetReportResult',
    'get_report',
    'get_report_output',
]

@pulumi.output_type
class GetReportResult:
    """
    A class represent an AppComplianceAutomation report resource.
    """
    def __init__(__self__, cert_records=None, compliance_status=None, errors=None, id=None, last_trigger_time=None, name=None, next_trigger_time=None, offer_guid=None, provisioning_state=None, resources=None, status=None, storage_info=None, subscriptions=None, system_data=None, tenant_id=None, time_zone=None, trigger_time=None, type=None):
        if cert_records and not isinstance(cert_records, list):
            raise TypeError("Expected argument 'cert_records' to be a list")
        pulumi.set(__self__, "cert_records", cert_records)
        if compliance_status and not isinstance(compliance_status, dict):
            raise TypeError("Expected argument 'compliance_status' to be a dict")
        pulumi.set(__self__, "compliance_status", compliance_status)
        if errors and not isinstance(errors, list):
            raise TypeError("Expected argument 'errors' to be a list")
        pulumi.set(__self__, "errors", errors)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_trigger_time and not isinstance(last_trigger_time, str):
            raise TypeError("Expected argument 'last_trigger_time' to be a str")
        pulumi.set(__self__, "last_trigger_time", last_trigger_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if next_trigger_time and not isinstance(next_trigger_time, str):
            raise TypeError("Expected argument 'next_trigger_time' to be a str")
        pulumi.set(__self__, "next_trigger_time", next_trigger_time)
        if offer_guid and not isinstance(offer_guid, str):
            raise TypeError("Expected argument 'offer_guid' to be a str")
        pulumi.set(__self__, "offer_guid", offer_guid)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resources and not isinstance(resources, list):
            raise TypeError("Expected argument 'resources' to be a list")
        pulumi.set(__self__, "resources", resources)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if storage_info and not isinstance(storage_info, dict):
            raise TypeError("Expected argument 'storage_info' to be a dict")
        pulumi.set(__self__, "storage_info", storage_info)
        if subscriptions and not isinstance(subscriptions, list):
            raise TypeError("Expected argument 'subscriptions' to be a list")
        pulumi.set(__self__, "subscriptions", subscriptions)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if trigger_time and not isinstance(trigger_time, str):
            raise TypeError("Expected argument 'trigger_time' to be a str")
        pulumi.set(__self__, "trigger_time", trigger_time)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="certRecords")
    def cert_records(self) -> Sequence['outputs.CertSyncRecordResponse']:
        """
        List of synchronized certification records.
        """
        return pulumi.get(self, "cert_records")

    @property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> 'outputs.ReportComplianceStatusResponse':
        """
        Report compliance status.
        """
        return pulumi.get(self, "compliance_status")

    @property
    @pulumi.getter
    def errors(self) -> Sequence[str]:
        """
        List of report error codes.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextTriggerTime")
    def next_trigger_time(self) -> str:
        """
        Report next collection trigger time.
        """
        return pulumi.get(self, "next_trigger_time")

    @property
    @pulumi.getter(name="offerGuid")
    def offer_guid(self) -> Optional[str]:
        """
        A list of comma-separated offerGuids indicates a series of offerGuids that map to the report. For example, "00000000-0000-0000-0000-000000000001,00000000-0000-0000-0000-000000000002" and "00000000-0000-0000-0000-000000000003".
        """
        return pulumi.get(self, "offer_guid")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

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
    @pulumi.getter(name="storageInfo")
    def storage_info(self) -> Optional['outputs.StorageInfoResponse']:
        """
        The information of 'bring your own storage' binding to the report
        """
        return pulumi.get(self, "storage_info")

    @property
    @pulumi.getter
    def subscriptions(self) -> Sequence[str]:
        """
        List of subscription Ids.
        """
        return pulumi.get(self, "subscriptions")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetReportResult(GetReportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReportResult(
            cert_records=self.cert_records,
            compliance_status=self.compliance_status,
            errors=self.errors,
            id=self.id,
            last_trigger_time=self.last_trigger_time,
            name=self.name,
            next_trigger_time=self.next_trigger_time,
            offer_guid=self.offer_guid,
            provisioning_state=self.provisioning_state,
            resources=self.resources,
            status=self.status,
            storage_info=self.storage_info,
            subscriptions=self.subscriptions,
            system_data=self.system_data,
            tenant_id=self.tenant_id,
            time_zone=self.time_zone,
            trigger_time=self.trigger_time,
            type=self.type)


def get_report(report_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReportResult:
    """
    Get the AppComplianceAutomation report and its properties.


    :param str report_name: Report Name.
    """
    __args__ = dict()
    __args__['reportName'] = report_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appcomplianceautomation/v20240627:getReport', __args__, opts=opts, typ=GetReportResult).value

    return AwaitableGetReportResult(
        cert_records=pulumi.get(__ret__, 'cert_records'),
        compliance_status=pulumi.get(__ret__, 'compliance_status'),
        errors=pulumi.get(__ret__, 'errors'),
        id=pulumi.get(__ret__, 'id'),
        last_trigger_time=pulumi.get(__ret__, 'last_trigger_time'),
        name=pulumi.get(__ret__, 'name'),
        next_trigger_time=pulumi.get(__ret__, 'next_trigger_time'),
        offer_guid=pulumi.get(__ret__, 'offer_guid'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resources=pulumi.get(__ret__, 'resources'),
        status=pulumi.get(__ret__, 'status'),
        storage_info=pulumi.get(__ret__, 'storage_info'),
        subscriptions=pulumi.get(__ret__, 'subscriptions'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        time_zone=pulumi.get(__ret__, 'time_zone'),
        trigger_time=pulumi.get(__ret__, 'trigger_time'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_report)
def get_report_output(report_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReportResult]:
    """
    Get the AppComplianceAutomation report and its properties.


    :param str report_name: Report Name.
    """
    ...
