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
    'SkuArgs',
]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input['SkuName'],
                 capacity: Optional[pulumi.Input[int]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input['SkuTier']] = None):
        """
        The resource model definition representing SKU
        :param pulumi.Input['SkuName'] name: The name of the HealthBot SKU
        :param pulumi.Input[int] capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        :param pulumi.Input[str] family: If the service has different generations of hardware, for the same SKU, then that can be captured here.
        :param pulumi.Input[str] size: The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        :param pulumi.Input['SkuTier'] tier: This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input['SkuName']:
        """
        The name of the HealthBot SKU
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input['SkuName']):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input['SkuTier']]:
        """
        This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input['SkuTier']]):
        pulumi.set(self, "tier", value)


