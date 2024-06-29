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
    'GetPacketCaptureResult',
    'AwaitableGetPacketCaptureResult',
    'get_packet_capture',
    'get_packet_capture_output',
]

@pulumi.output_type
class GetPacketCaptureResult:
    """
    Packet capture session resource.
    """
    def __init__(__self__, bytes_to_capture_per_packet=None, capture_start_time=None, id=None, name=None, network_interfaces=None, output_files=None, provisioning_state=None, reason=None, status=None, system_data=None, time_limit_in_seconds=None, total_bytes_per_session=None, type=None):
        if bytes_to_capture_per_packet and not isinstance(bytes_to_capture_per_packet, float):
            raise TypeError("Expected argument 'bytes_to_capture_per_packet' to be a float")
        pulumi.set(__self__, "bytes_to_capture_per_packet", bytes_to_capture_per_packet)
        if capture_start_time and not isinstance(capture_start_time, str):
            raise TypeError("Expected argument 'capture_start_time' to be a str")
        pulumi.set(__self__, "capture_start_time", capture_start_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_interfaces and not isinstance(network_interfaces, list):
            raise TypeError("Expected argument 'network_interfaces' to be a list")
        pulumi.set(__self__, "network_interfaces", network_interfaces)
        if output_files and not isinstance(output_files, list):
            raise TypeError("Expected argument 'output_files' to be a list")
        pulumi.set(__self__, "output_files", output_files)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if reason and not isinstance(reason, str):
            raise TypeError("Expected argument 'reason' to be a str")
        pulumi.set(__self__, "reason", reason)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time_limit_in_seconds and not isinstance(time_limit_in_seconds, int):
            raise TypeError("Expected argument 'time_limit_in_seconds' to be a int")
        pulumi.set(__self__, "time_limit_in_seconds", time_limit_in_seconds)
        if total_bytes_per_session and not isinstance(total_bytes_per_session, float):
            raise TypeError("Expected argument 'total_bytes_per_session' to be a float")
        pulumi.set(__self__, "total_bytes_per_session", total_bytes_per_session)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(self) -> Optional[float]:
        """
        Number of bytes captured per packet, the remaining bytes are truncated. The default "0" means the entire packet is captured.
        """
        return pulumi.get(self, "bytes_to_capture_per_packet")

    @property
    @pulumi.getter(name="captureStartTime")
    def capture_start_time(self) -> str:
        """
        The start time of the packet capture session.
        """
        return pulumi.get(self, "capture_start_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[str]]:
        """
        List of network interfaces to capture on.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="outputFiles")
    def output_files(self) -> Sequence[str]:
        """
        The list of output files of a packet capture session.
        """
        return pulumi.get(self, "output_files")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the packet capture session resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def reason(self) -> str:
        """
        The reason the current packet capture session state.
        """
        return pulumi.get(self, "reason")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the packet capture session.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> Optional[int]:
        """
        Maximum duration of the capture session in seconds.
        """
        return pulumi.get(self, "time_limit_in_seconds")

    @property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> Optional[float]:
        """
        Maximum size of the capture output.
        """
        return pulumi.get(self, "total_bytes_per_session")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetPacketCaptureResult(GetPacketCaptureResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPacketCaptureResult(
            bytes_to_capture_per_packet=self.bytes_to_capture_per_packet,
            capture_start_time=self.capture_start_time,
            id=self.id,
            name=self.name,
            network_interfaces=self.network_interfaces,
            output_files=self.output_files,
            provisioning_state=self.provisioning_state,
            reason=self.reason,
            status=self.status,
            system_data=self.system_data,
            time_limit_in_seconds=self.time_limit_in_seconds,
            total_bytes_per_session=self.total_bytes_per_session,
            type=self.type)


def get_packet_capture(packet_capture_name: Optional[str] = None,
                       packet_core_control_plane_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPacketCaptureResult:
    """
    Gets information about the specified packet capture session.


    :param str packet_capture_name: The name of the packet capture session.
    :param str packet_core_control_plane_name: The name of the packet core control plane.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['packetCaptureName'] = packet_capture_name
    __args__['packetCoreControlPlaneName'] = packet_core_control_plane_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilenetwork/v20230901:getPacketCapture', __args__, opts=opts, typ=GetPacketCaptureResult).value

    return AwaitableGetPacketCaptureResult(
        bytes_to_capture_per_packet=pulumi.get(__ret__, 'bytes_to_capture_per_packet'),
        capture_start_time=pulumi.get(__ret__, 'capture_start_time'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network_interfaces=pulumi.get(__ret__, 'network_interfaces'),
        output_files=pulumi.get(__ret__, 'output_files'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        reason=pulumi.get(__ret__, 'reason'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_limit_in_seconds=pulumi.get(__ret__, 'time_limit_in_seconds'),
        total_bytes_per_session=pulumi.get(__ret__, 'total_bytes_per_session'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_packet_capture)
def get_packet_capture_output(packet_capture_name: Optional[pulumi.Input[str]] = None,
                              packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPacketCaptureResult]:
    """
    Gets information about the specified packet capture session.


    :param str packet_capture_name: The name of the packet capture session.
    :param str packet_core_control_plane_name: The name of the packet core control plane.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
