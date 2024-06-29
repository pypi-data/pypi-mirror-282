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
    'ResourceReferenceArgs',
    'SkuArgs',
    'WorkflowParameterArgs',
]

@pulumi.input_type
class ResourceReferenceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        The resource reference.
        :param pulumi.Input[str] id: The resource id.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'SkuName']],
                 plan: Optional[pulumi.Input['ResourceReferenceArgs']] = None):
        """
        The sku type.
        :param pulumi.Input[Union[str, 'SkuName']] name: The name.
        :param pulumi.Input['ResourceReferenceArgs'] plan: The reference to plan.
        """
        pulumi.set(__self__, "name", name)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuName']]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        The reference to plan.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "plan", value)


@pulumi.input_type
class WorkflowParameterArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 type: Optional[pulumi.Input[Union[str, 'ParameterType']]] = None,
                 value: Optional[Any] = None):
        """
        The workflow parameters.
        :param pulumi.Input[str] description: The description.
        :param Any metadata: The metadata.
        :param pulumi.Input[Union[str, 'ParameterType']] type: The type.
        :param Any value: The value.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'ParameterType']]]:
        """
        The type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'ParameterType']]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        """
        The value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[Any]):
        pulumi.set(self, "value", value)


