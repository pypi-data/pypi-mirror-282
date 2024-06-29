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
    'CapabilityArgs',
    'HostingEnvironmentProfileArgs',
    'SkuCapacityArgs',
    'SkuDescriptionArgs',
]

@pulumi.input_type
class CapabilityArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Describes the capabilities/features allowed for a specific SKU.
        :param pulumi.Input[str] name: Name of the SKU capability.
        :param pulumi.Input[str] reason: Reason of the SKU capability.
        :param pulumi.Input[str] value: Value of the SKU capability.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if reason is not None:
            pulumi.set(__self__, "reason", reason)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SKU capability.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[str]]:
        """
        Reason of the SKU capability.
        """
        return pulumi.get(self, "reason")

    @reason.setter
    def reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reason", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Value of the SKU capability.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class HostingEnvironmentProfileArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Specification for an App Service Environment to use for this resource.
        :param pulumi.Input[str] id: Resource ID of the App Service Environment.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID of the App Service Environment.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class SkuCapacityArgs:
    def __init__(__self__, *,
                 default: Optional[pulumi.Input[int]] = None,
                 maximum: Optional[pulumi.Input[int]] = None,
                 minimum: Optional[pulumi.Input[int]] = None,
                 scale_type: Optional[pulumi.Input[str]] = None):
        """
        Description of the App Service plan scale options.
        :param pulumi.Input[int] default: Default number of workers for this App Service plan SKU.
        :param pulumi.Input[int] maximum: Maximum number of workers for this App Service plan SKU.
        :param pulumi.Input[int] minimum: Minimum number of workers for this App Service plan SKU.
        :param pulumi.Input[str] scale_type: Available scale configurations for an App Service plan.
        """
        if default is not None:
            pulumi.set(__self__, "default", default)
        if maximum is not None:
            pulumi.set(__self__, "maximum", maximum)
        if minimum is not None:
            pulumi.set(__self__, "minimum", minimum)
        if scale_type is not None:
            pulumi.set(__self__, "scale_type", scale_type)

    @property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[int]]:
        """
        Default number of workers for this App Service plan SKU.
        """
        return pulumi.get(self, "default")

    @default.setter
    def default(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default", value)

    @property
    @pulumi.getter
    def maximum(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of workers for this App Service plan SKU.
        """
        return pulumi.get(self, "maximum")

    @maximum.setter
    def maximum(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum", value)

    @property
    @pulumi.getter
    def minimum(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of workers for this App Service plan SKU.
        """
        return pulumi.get(self, "minimum")

    @minimum.setter
    def minimum(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minimum", value)

    @property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> Optional[pulumi.Input[str]]:
        """
        Available scale configurations for an App Service plan.
        """
        return pulumi.get(self, "scale_type")

    @scale_type.setter
    def scale_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scale_type", value)


@pulumi.input_type
class SkuDescriptionArgs:
    def __init__(__self__, *,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input['CapabilityArgs']]]] = None,
                 capacity: Optional[pulumi.Input[int]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 sku_capacity: Optional[pulumi.Input['SkuCapacityArgs']] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        Description of a SKU for a scalable resource.
        :param pulumi.Input[Sequence[pulumi.Input['CapabilityArgs']]] capabilities: Capabilities of the SKU, e.g., is traffic manager enabled?
        :param pulumi.Input[int] capacity: Current number of instances assigned to the resource.
        :param pulumi.Input[str] family: Family code of the resource SKU.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: Locations of the SKU.
        :param pulumi.Input[str] name: Name of the resource SKU.
        :param pulumi.Input[str] size: Size specifier of the resource SKU.
        :param pulumi.Input['SkuCapacityArgs'] sku_capacity: Min, max, and default scale values of the SKU.
        :param pulumi.Input[str] tier: Service tier of the resource SKU.
        """
        if capabilities is not None:
            pulumi.set(__self__, "capabilities", capabilities)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if locations is not None:
            pulumi.set(__self__, "locations", locations)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if sku_capacity is not None:
            pulumi.set(__self__, "sku_capacity", sku_capacity)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CapabilityArgs']]]]:
        """
        Capabilities of the SKU, e.g., is traffic manager enabled?
        """
        return pulumi.get(self, "capabilities")

    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CapabilityArgs']]]]):
        pulumi.set(self, "capabilities", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        Current number of instances assigned to the resource.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        """
        Family code of the resource SKU.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Locations of the SKU.
        """
        return pulumi.get(self, "locations")

    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "locations", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource SKU.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        Size specifier of the resource SKU.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="skuCapacity")
    def sku_capacity(self) -> Optional[pulumi.Input['SkuCapacityArgs']]:
        """
        Min, max, and default scale values of the SKU.
        """
        return pulumi.get(self, "sku_capacity")

    @sku_capacity.setter
    def sku_capacity(self, value: Optional[pulumi.Input['SkuCapacityArgs']]):
        pulumi.set(self, "sku_capacity", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        Service tier of the resource SKU.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


