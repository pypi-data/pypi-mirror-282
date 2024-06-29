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
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter
    def properties(self) -> 'outputs.ReportPropertiesResponse':
        """
        Report property.
        """
        return pulumi.get(self, "properties")

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


class AwaitableGetReportResult(GetReportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReportResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
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
    __ret__ = pulumi.runtime.invoke('azure-native:appcomplianceautomation/v20221116preview:getReport', __args__, opts=opts, typ=GetReportResult).value

    return AwaitableGetReportResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_report)
def get_report_output(report_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReportResult]:
    """
    Get the AppComplianceAutomation report and its properties.


    :param str report_name: Report Name.
    """
    ...
