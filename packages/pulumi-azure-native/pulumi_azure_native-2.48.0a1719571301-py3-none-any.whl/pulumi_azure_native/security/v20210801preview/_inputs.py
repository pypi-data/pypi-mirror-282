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
    'AssignedComponentItemArgs',
    'AssignedStandardItemArgs',
    'AssignmentPropertiesAdditionalDataArgs',
    'StandardComponentPropertiesArgs',
]

@pulumi.input_type
class AssignedComponentItemArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None):
        """
        describe the properties of a security assessment object reference (by key)
        :param pulumi.Input[str] key: unique key to a security assessment object
        """
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        unique key to a security assessment object
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


@pulumi.input_type
class AssignedStandardItemArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        describe the properties of a of a security standard object reference
        :param pulumi.Input[str] id: full resourceId of the Microsoft.Security/standard object
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        full resourceId of the Microsoft.Security/standard object
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class AssignmentPropertiesAdditionalDataArgs:
    def __init__(__self__, *,
                 exemption_category: Optional[pulumi.Input[str]] = None):
        """
        Additional data about the assignment
        :param pulumi.Input[str] exemption_category: Exemption category of this assignment
        """
        if exemption_category is not None:
            pulumi.set(__self__, "exemption_category", exemption_category)

    @property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> Optional[pulumi.Input[str]]:
        """
        Exemption category of this assignment
        """
        return pulumi.get(self, "exemption_category")

    @exemption_category.setter
    def exemption_category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exemption_category", value)


@pulumi.input_type
class StandardComponentPropertiesArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None):
        """
        Describes properties of an component as related to the standard
        :param pulumi.Input[str] key: Component Key matching componentMetadata
        """
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Component Key matching componentMetadata
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


