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
    'GetDiagnosticServiceResult',
    'AwaitableGetDiagnosticServiceResult',
    'get_diagnostic_service',
    'get_diagnostic_service_output',
]

@pulumi.output_type
class GetDiagnosticServiceResult:
    """
    MQ diagnostic services resource
    """
    def __init__(__self__, data_export_frequency_seconds=None, extended_location=None, id=None, image=None, location=None, log_format=None, log_level=None, max_data_storage_size=None, metrics_port=None, name=None, open_telemetry_traces_collector_addr=None, provisioning_state=None, stale_data_timeout_seconds=None, system_data=None, tags=None, type=None):
        if data_export_frequency_seconds and not isinstance(data_export_frequency_seconds, int):
            raise TypeError("Expected argument 'data_export_frequency_seconds' to be a int")
        pulumi.set(__self__, "data_export_frequency_seconds", data_export_frequency_seconds)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image and not isinstance(image, dict):
            raise TypeError("Expected argument 'image' to be a dict")
        pulumi.set(__self__, "image", image)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if log_format and not isinstance(log_format, str):
            raise TypeError("Expected argument 'log_format' to be a str")
        pulumi.set(__self__, "log_format", log_format)
        if log_level and not isinstance(log_level, str):
            raise TypeError("Expected argument 'log_level' to be a str")
        pulumi.set(__self__, "log_level", log_level)
        if max_data_storage_size and not isinstance(max_data_storage_size, float):
            raise TypeError("Expected argument 'max_data_storage_size' to be a float")
        pulumi.set(__self__, "max_data_storage_size", max_data_storage_size)
        if metrics_port and not isinstance(metrics_port, int):
            raise TypeError("Expected argument 'metrics_port' to be a int")
        pulumi.set(__self__, "metrics_port", metrics_port)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if open_telemetry_traces_collector_addr and not isinstance(open_telemetry_traces_collector_addr, str):
            raise TypeError("Expected argument 'open_telemetry_traces_collector_addr' to be a str")
        pulumi.set(__self__, "open_telemetry_traces_collector_addr", open_telemetry_traces_collector_addr)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if stale_data_timeout_seconds and not isinstance(stale_data_timeout_seconds, int):
            raise TypeError("Expected argument 'stale_data_timeout_seconds' to be a int")
        pulumi.set(__self__, "stale_data_timeout_seconds", stale_data_timeout_seconds)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataExportFrequencySeconds")
    def data_export_frequency_seconds(self) -> Optional[int]:
        """
        The frequency at which the data will be exported.
        """
        return pulumi.get(self, "data_export_frequency_seconds")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationPropertyResponse':
        """
        Extended Location
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def image(self) -> 'outputs.ContainerImageResponse':
        """
        The details of Diagnostic Service Docker Image.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> Optional[str]:
        """
        The format for the logs generated.
        """
        return pulumi.get(self, "log_format")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[str]:
        """
        The format for the logs generated.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter(name="maxDataStorageSize")
    def max_data_storage_size(self) -> Optional[float]:
        """
        The maximum data stored in MiB.
        """
        return pulumi.get(self, "max_data_storage_size")

    @property
    @pulumi.getter(name="metricsPort")
    def metrics_port(self) -> Optional[int]:
        """
        The port at which metrics is exposed.
        """
        return pulumi.get(self, "metrics_port")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openTelemetryTracesCollectorAddr")
    def open_telemetry_traces_collector_addr(self) -> Optional[str]:
        """
        The destination to collect traces. Diagnostic service will push traces to this endpoint
        """
        return pulumi.get(self, "open_telemetry_traces_collector_addr")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="staleDataTimeoutSeconds")
    def stale_data_timeout_seconds(self) -> Optional[int]:
        """
        Metric inactivity timeout.
        """
        return pulumi.get(self, "stale_data_timeout_seconds")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDiagnosticServiceResult(GetDiagnosticServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiagnosticServiceResult(
            data_export_frequency_seconds=self.data_export_frequency_seconds,
            extended_location=self.extended_location,
            id=self.id,
            image=self.image,
            location=self.location,
            log_format=self.log_format,
            log_level=self.log_level,
            max_data_storage_size=self.max_data_storage_size,
            metrics_port=self.metrics_port,
            name=self.name,
            open_telemetry_traces_collector_addr=self.open_telemetry_traces_collector_addr,
            provisioning_state=self.provisioning_state,
            stale_data_timeout_seconds=self.stale_data_timeout_seconds,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_diagnostic_service(diagnostic_service_name: Optional[str] = None,
                           mq_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiagnosticServiceResult:
    """
    Get a DiagnosticServiceResource


    :param str diagnostic_service_name: Name of MQ diagnostic resource
    :param str mq_name: Name of MQ resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['diagnosticServiceName'] = diagnostic_service_name
    __args__['mqName'] = mq_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iotoperationsmq/v20231004preview:getDiagnosticService', __args__, opts=opts, typ=GetDiagnosticServiceResult).value

    return AwaitableGetDiagnosticServiceResult(
        data_export_frequency_seconds=pulumi.get(__ret__, 'data_export_frequency_seconds'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        image=pulumi.get(__ret__, 'image'),
        location=pulumi.get(__ret__, 'location'),
        log_format=pulumi.get(__ret__, 'log_format'),
        log_level=pulumi.get(__ret__, 'log_level'),
        max_data_storage_size=pulumi.get(__ret__, 'max_data_storage_size'),
        metrics_port=pulumi.get(__ret__, 'metrics_port'),
        name=pulumi.get(__ret__, 'name'),
        open_telemetry_traces_collector_addr=pulumi.get(__ret__, 'open_telemetry_traces_collector_addr'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        stale_data_timeout_seconds=pulumi.get(__ret__, 'stale_data_timeout_seconds'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_diagnostic_service)
def get_diagnostic_service_output(diagnostic_service_name: Optional[pulumi.Input[str]] = None,
                                  mq_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiagnosticServiceResult]:
    """
    Get a DiagnosticServiceResource


    :param str diagnostic_service_name: Name of MQ diagnostic resource
    :param str mq_name: Name of MQ resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
