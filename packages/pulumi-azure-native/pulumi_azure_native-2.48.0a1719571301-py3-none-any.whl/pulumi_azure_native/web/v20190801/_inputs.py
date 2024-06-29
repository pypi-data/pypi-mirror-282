# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'NameValuePairArgs',
    'NetworkAccessControlEntryArgs',
    'VirtualNetworkProfileArgs',
    'WorkerPoolArgs',
]

@pulumi.input_type
class NameValuePairArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Name value pair.
        :param pulumi.Input[str] name: Pair name.
        :param pulumi.Input[str] value: Pair value.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Pair name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Pair value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class NetworkAccessControlEntryArgs:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input['AccessControlEntryAction']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 remote_subnet: Optional[pulumi.Input[str]] = None):
        """
        Network access control entry.
        :param pulumi.Input['AccessControlEntryAction'] action: Action object.
        :param pulumi.Input[str] description: Description of network access control entry.
        :param pulumi.Input[int] order: Order of precedence.
        :param pulumi.Input[str] remote_subnet: Remote subnet.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if remote_subnet is not None:
            pulumi.set(__self__, "remote_subnet", remote_subnet)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input['AccessControlEntryAction']]:
        """
        Action object.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input['AccessControlEntryAction']]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of network access control entry.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        Order of precedence.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="remoteSubnet")
    def remote_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        Remote subnet.
        """
        return pulumi.get(self, "remote_subnet")

    @remote_subnet.setter
    def remote_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_subnet", value)


@pulumi.input_type
class VirtualNetworkProfileArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[str]] = None):
        """
        Specification for using a Virtual Network.
        :param pulumi.Input[str] id: Resource id of the Virtual Network.
        :param pulumi.Input[str] subnet: Subnet within the Virtual Network.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource id of the Virtual Network.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[str]]:
        """
        Subnet within the Virtual Network.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet", value)


@pulumi.input_type
class WorkerPoolArgs:
    def __init__(__self__, *,
                 compute_mode: Optional[pulumi.Input['ComputeModeOptions']] = None,
                 worker_count: Optional[pulumi.Input[int]] = None,
                 worker_size: Optional[pulumi.Input[str]] = None,
                 worker_size_id: Optional[pulumi.Input[int]] = None):
        """
        Worker pool of an App Service Environment.
        :param pulumi.Input['ComputeModeOptions'] compute_mode: Shared or dedicated app hosting.
        :param pulumi.Input[int] worker_count: Number of instances in the worker pool.
        :param pulumi.Input[str] worker_size: VM size of the worker pool instances.
        :param pulumi.Input[int] worker_size_id: Worker size ID for referencing this worker pool.
        """
        if compute_mode is not None:
            pulumi.set(__self__, "compute_mode", compute_mode)
        if worker_count is not None:
            pulumi.set(__self__, "worker_count", worker_count)
        if worker_size is not None:
            pulumi.set(__self__, "worker_size", worker_size)
        if worker_size_id is not None:
            pulumi.set(__self__, "worker_size_id", worker_size_id)

    @property
    @pulumi.getter(name="computeMode")
    def compute_mode(self) -> Optional[pulumi.Input['ComputeModeOptions']]:
        """
        Shared or dedicated app hosting.
        """
        return pulumi.get(self, "compute_mode")

    @compute_mode.setter
    def compute_mode(self, value: Optional[pulumi.Input['ComputeModeOptions']]):
        pulumi.set(self, "compute_mode", value)

    @property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of instances in the worker pool.
        """
        return pulumi.get(self, "worker_count")

    @worker_count.setter
    def worker_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "worker_count", value)

    @property
    @pulumi.getter(name="workerSize")
    def worker_size(self) -> Optional[pulumi.Input[str]]:
        """
        VM size of the worker pool instances.
        """
        return pulumi.get(self, "worker_size")

    @worker_size.setter
    def worker_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "worker_size", value)

    @property
    @pulumi.getter(name="workerSizeId")
    def worker_size_id(self) -> Optional[pulumi.Input[int]]:
        """
        Worker size ID for referencing this worker pool.
        """
        return pulumi.get(self, "worker_size_id")

    @worker_size_id.setter
    def worker_size_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "worker_size_id", value)


