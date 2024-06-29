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

__all__ = ['PacketCaptureArgs', 'PacketCapture']

@pulumi.input_type
class PacketCaptureArgs:
    def __init__(__self__, *,
                 network_watcher_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_location: pulumi.Input['PacketCaptureStorageLocationArgs'],
                 target: pulumi.Input[str],
                 bytes_to_capture_per_packet: Optional[pulumi.Input[float]] = None,
                 capture_settings: Optional[pulumi.Input['PacketCaptureSettingsArgs']] = None,
                 continuous_capture: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input['PacketCaptureFilterArgs']]]] = None,
                 packet_capture_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['PacketCaptureMachineScopeArgs']] = None,
                 target_type: Optional[pulumi.Input['PacketCaptureTargetType']] = None,
                 time_limit_in_seconds: Optional[pulumi.Input[int]] = None,
                 total_bytes_per_session: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a PacketCapture resource.
        :param pulumi.Input[str] network_watcher_name: The name of the network watcher.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['PacketCaptureStorageLocationArgs'] storage_location: The storage location for a packet capture session.
        :param pulumi.Input[str] target: The ID of the targeted resource, only AzureVM and AzureVMSS as target type are currently supported.
        :param pulumi.Input[float] bytes_to_capture_per_packet: Number of bytes captured per packet, the remaining bytes are truncated.
        :param pulumi.Input['PacketCaptureSettingsArgs'] capture_settings: The capture setting holds the 'FileCount', 'FileSizeInBytes', 'SessionTimeLimitInSeconds' values.
        :param pulumi.Input[bool] continuous_capture: This continuous capture is a nullable boolean, which can hold 'null', 'true' or 'false' value. If we do not pass this parameter, it would be consider as 'null', default value is 'null'.
        :param pulumi.Input[Sequence[pulumi.Input['PacketCaptureFilterArgs']]] filters: A list of packet capture filters.
        :param pulumi.Input[str] packet_capture_name: The name of the packet capture session.
        :param pulumi.Input['PacketCaptureMachineScopeArgs'] scope: A list of AzureVMSS instances which can be included or excluded to run packet capture. If both included and excluded are empty, then the packet capture will run on all instances of AzureVMSS.
        :param pulumi.Input['PacketCaptureTargetType'] target_type: Target type of the resource provided.
        :param pulumi.Input[int] time_limit_in_seconds: Maximum duration of the capture session in seconds.
        :param pulumi.Input[float] total_bytes_per_session: Maximum size of the capture output.
        """
        pulumi.set(__self__, "network_watcher_name", network_watcher_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_location", storage_location)
        pulumi.set(__self__, "target", target)
        if bytes_to_capture_per_packet is None:
            bytes_to_capture_per_packet = 0
        if bytes_to_capture_per_packet is not None:
            pulumi.set(__self__, "bytes_to_capture_per_packet", bytes_to_capture_per_packet)
        if capture_settings is not None:
            pulumi.set(__self__, "capture_settings", capture_settings)
        if continuous_capture is not None:
            pulumi.set(__self__, "continuous_capture", continuous_capture)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if packet_capture_name is not None:
            pulumi.set(__self__, "packet_capture_name", packet_capture_name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if target_type is not None:
            pulumi.set(__self__, "target_type", target_type)
        if time_limit_in_seconds is None:
            time_limit_in_seconds = 18000
        if time_limit_in_seconds is not None:
            pulumi.set(__self__, "time_limit_in_seconds", time_limit_in_seconds)
        if total_bytes_per_session is None:
            total_bytes_per_session = 1073741824
        if total_bytes_per_session is not None:
            pulumi.set(__self__, "total_bytes_per_session", total_bytes_per_session)

    @property
    @pulumi.getter(name="networkWatcherName")
    def network_watcher_name(self) -> pulumi.Input[str]:
        """
        The name of the network watcher.
        """
        return pulumi.get(self, "network_watcher_name")

    @network_watcher_name.setter
    def network_watcher_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_watcher_name", value)

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
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Input['PacketCaptureStorageLocationArgs']:
        """
        The storage location for a packet capture session.
        """
        return pulumi.get(self, "storage_location")

    @storage_location.setter
    def storage_location(self, value: pulumi.Input['PacketCaptureStorageLocationArgs']):
        pulumi.set(self, "storage_location", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        """
        The ID of the targeted resource, only AzureVM and AzureVMSS as target type are currently supported.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(self) -> Optional[pulumi.Input[float]]:
        """
        Number of bytes captured per packet, the remaining bytes are truncated.
        """
        return pulumi.get(self, "bytes_to_capture_per_packet")

    @bytes_to_capture_per_packet.setter
    def bytes_to_capture_per_packet(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "bytes_to_capture_per_packet", value)

    @property
    @pulumi.getter(name="captureSettings")
    def capture_settings(self) -> Optional[pulumi.Input['PacketCaptureSettingsArgs']]:
        """
        The capture setting holds the 'FileCount', 'FileSizeInBytes', 'SessionTimeLimitInSeconds' values.
        """
        return pulumi.get(self, "capture_settings")

    @capture_settings.setter
    def capture_settings(self, value: Optional[pulumi.Input['PacketCaptureSettingsArgs']]):
        pulumi.set(self, "capture_settings", value)

    @property
    @pulumi.getter(name="continuousCapture")
    def continuous_capture(self) -> Optional[pulumi.Input[bool]]:
        """
        This continuous capture is a nullable boolean, which can hold 'null', 'true' or 'false' value. If we do not pass this parameter, it would be consider as 'null', default value is 'null'.
        """
        return pulumi.get(self, "continuous_capture")

    @continuous_capture.setter
    def continuous_capture(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "continuous_capture", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PacketCaptureFilterArgs']]]]:
        """
        A list of packet capture filters.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PacketCaptureFilterArgs']]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="packetCaptureName")
    def packet_capture_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the packet capture session.
        """
        return pulumi.get(self, "packet_capture_name")

    @packet_capture_name.setter
    def packet_capture_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "packet_capture_name", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input['PacketCaptureMachineScopeArgs']]:
        """
        A list of AzureVMSS instances which can be included or excluded to run packet capture. If both included and excluded are empty, then the packet capture will run on all instances of AzureVMSS.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input['PacketCaptureMachineScopeArgs']]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input['PacketCaptureTargetType']]:
        """
        Target type of the resource provided.
        """
        return pulumi.get(self, "target_type")

    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input['PacketCaptureTargetType']]):
        pulumi.set(self, "target_type", value)

    @property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum duration of the capture session in seconds.
        """
        return pulumi.get(self, "time_limit_in_seconds")

    @time_limit_in_seconds.setter
    def time_limit_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "time_limit_in_seconds", value)

    @property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> Optional[pulumi.Input[float]]:
        """
        Maximum size of the capture output.
        """
        return pulumi.get(self, "total_bytes_per_session")

    @total_bytes_per_session.setter
    def total_bytes_per_session(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "total_bytes_per_session", value)


class PacketCapture(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bytes_to_capture_per_packet: Optional[pulumi.Input[float]] = None,
                 capture_settings: Optional[pulumi.Input[pulumi.InputType['PacketCaptureSettingsArgs']]] = None,
                 continuous_capture: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketCaptureFilterArgs']]]]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 packet_capture_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['PacketCaptureMachineScopeArgs']]] = None,
                 storage_location: Optional[pulumi.Input[pulumi.InputType['PacketCaptureStorageLocationArgs']]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input['PacketCaptureTargetType']] = None,
                 time_limit_in_seconds: Optional[pulumi.Input[int]] = None,
                 total_bytes_per_session: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        Information about packet capture session.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] bytes_to_capture_per_packet: Number of bytes captured per packet, the remaining bytes are truncated.
        :param pulumi.Input[pulumi.InputType['PacketCaptureSettingsArgs']] capture_settings: The capture setting holds the 'FileCount', 'FileSizeInBytes', 'SessionTimeLimitInSeconds' values.
        :param pulumi.Input[bool] continuous_capture: This continuous capture is a nullable boolean, which can hold 'null', 'true' or 'false' value. If we do not pass this parameter, it would be consider as 'null', default value is 'null'.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketCaptureFilterArgs']]]] filters: A list of packet capture filters.
        :param pulumi.Input[str] network_watcher_name: The name of the network watcher.
        :param pulumi.Input[str] packet_capture_name: The name of the packet capture session.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['PacketCaptureMachineScopeArgs']] scope: A list of AzureVMSS instances which can be included or excluded to run packet capture. If both included and excluded are empty, then the packet capture will run on all instances of AzureVMSS.
        :param pulumi.Input[pulumi.InputType['PacketCaptureStorageLocationArgs']] storage_location: The storage location for a packet capture session.
        :param pulumi.Input[str] target: The ID of the targeted resource, only AzureVM and AzureVMSS as target type are currently supported.
        :param pulumi.Input['PacketCaptureTargetType'] target_type: Target type of the resource provided.
        :param pulumi.Input[int] time_limit_in_seconds: Maximum duration of the capture session in seconds.
        :param pulumi.Input[float] total_bytes_per_session: Maximum size of the capture output.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PacketCaptureArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Information about packet capture session.

        :param str resource_name: The name of the resource.
        :param PacketCaptureArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PacketCaptureArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bytes_to_capture_per_packet: Optional[pulumi.Input[float]] = None,
                 capture_settings: Optional[pulumi.Input[pulumi.InputType['PacketCaptureSettingsArgs']]] = None,
                 continuous_capture: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PacketCaptureFilterArgs']]]]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 packet_capture_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['PacketCaptureMachineScopeArgs']]] = None,
                 storage_location: Optional[pulumi.Input[pulumi.InputType['PacketCaptureStorageLocationArgs']]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input['PacketCaptureTargetType']] = None,
                 time_limit_in_seconds: Optional[pulumi.Input[int]] = None,
                 total_bytes_per_session: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PacketCaptureArgs.__new__(PacketCaptureArgs)

            if bytes_to_capture_per_packet is None:
                bytes_to_capture_per_packet = 0
            __props__.__dict__["bytes_to_capture_per_packet"] = bytes_to_capture_per_packet
            __props__.__dict__["capture_settings"] = capture_settings
            __props__.__dict__["continuous_capture"] = continuous_capture
            __props__.__dict__["filters"] = filters
            if network_watcher_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__.__dict__["network_watcher_name"] = network_watcher_name
            __props__.__dict__["packet_capture_name"] = packet_capture_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope"] = scope
            if storage_location is None and not opts.urn:
                raise TypeError("Missing required property 'storage_location'")
            __props__.__dict__["storage_location"] = storage_location
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            __props__.__dict__["target_type"] = target_type
            if time_limit_in_seconds is None:
                time_limit_in_seconds = 18000
            __props__.__dict__["time_limit_in_seconds"] = time_limit_in_seconds
            if total_bytes_per_session is None:
                total_bytes_per_session = 1073741824
            __props__.__dict__["total_bytes_per_session"] = total_bytes_per_session
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20160901:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20161201:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20170301:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20170601:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20170801:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20170901:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20171001:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20171101:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20180101:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20180201:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20180401:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20180601:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20180701:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20180801:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20181001:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20181101:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20181201:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20190201:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20190401:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20190601:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20190701:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20190801:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20190901:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20191101:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20191201:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20200301:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20200401:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20200501:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20200601:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20200701:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20200801:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20201101:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20210201:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20210301:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20210501:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20210801:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20220101:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20220501:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20220701:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20220901:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20221101:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20230201:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20230401:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20230501:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20230601:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20230901:PacketCapture"), pulumi.Alias(type_="azure-native:network/v20240101:PacketCapture")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PacketCapture, __self__).__init__(
            'azure-native:network/v20231101:PacketCapture',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PacketCapture':
        """
        Get an existing PacketCapture resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PacketCaptureArgs.__new__(PacketCaptureArgs)

        __props__.__dict__["bytes_to_capture_per_packet"] = None
        __props__.__dict__["capture_settings"] = None
        __props__.__dict__["continuous_capture"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["filters"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["storage_location"] = None
        __props__.__dict__["target"] = None
        __props__.__dict__["target_type"] = None
        __props__.__dict__["time_limit_in_seconds"] = None
        __props__.__dict__["total_bytes_per_session"] = None
        return PacketCapture(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(self) -> pulumi.Output[Optional[float]]:
        """
        Number of bytes captured per packet, the remaining bytes are truncated.
        """
        return pulumi.get(self, "bytes_to_capture_per_packet")

    @property
    @pulumi.getter(name="captureSettings")
    def capture_settings(self) -> pulumi.Output[Optional['outputs.PacketCaptureSettingsResponse']]:
        """
        The capture setting holds the 'FileCount', 'FileSizeInBytes', 'SessionTimeLimitInSeconds' values.
        """
        return pulumi.get(self, "capture_settings")

    @property
    @pulumi.getter(name="continuousCapture")
    def continuous_capture(self) -> pulumi.Output[Optional[bool]]:
        """
        This continuous capture is a nullable boolean, which can hold 'null', 'true' or 'false' value. If we do not pass this parameter, it would be consider as 'null', default value is 'null'.
        """
        return pulumi.get(self, "continuous_capture")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional[Sequence['outputs.PacketCaptureFilterResponse']]]:
        """
        A list of packet capture filters.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the packet capture session.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the packet capture session.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional['outputs.PacketCaptureMachineScopeResponse']]:
        """
        A list of AzureVMSS instances which can be included or excluded to run packet capture. If both included and excluded are empty, then the packet capture will run on all instances of AzureVMSS.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output['outputs.PacketCaptureStorageLocationResponse']:
        """
        The storage location for a packet capture session.
        """
        return pulumi.get(self, "storage_location")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[str]:
        """
        The ID of the targeted resource, only AzureVM and AzureVMSS as target type are currently supported.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[Optional[str]]:
        """
        Target type of the resource provided.
        """
        return pulumi.get(self, "target_type")

    @property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum duration of the capture session in seconds.
        """
        return pulumi.get(self, "time_limit_in_seconds")

    @property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> pulumi.Output[Optional[float]]:
        """
        Maximum size of the capture output.
        """
        return pulumi.get(self, "total_bytes_per_session")

