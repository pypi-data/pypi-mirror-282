# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'CustomerSecretArgs',
    'ScheduleArgs',
    'SkuArgs',
]

@pulumi.input_type
class CustomerSecretArgs:
    def __init__(__self__, *,
                 algorithm: pulumi.Input['SupportedAlgorithm'],
                 key_identifier: pulumi.Input[str],
                 key_value: pulumi.Input[str]):
        """
        The pair of customer secret.
        :param pulumi.Input['SupportedAlgorithm'] algorithm: The encryption algorithm used to encrypt data.
        :param pulumi.Input[str] key_identifier: The identifier to the data service input object which this secret corresponds to.
        :param pulumi.Input[str] key_value: It contains the encrypted customer secret.
        """
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "key_identifier", key_identifier)
        pulumi.set(__self__, "key_value", key_value)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input['SupportedAlgorithm']:
        """
        The encryption algorithm used to encrypt data.
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: pulumi.Input['SupportedAlgorithm']):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> pulumi.Input[str]:
        """
        The identifier to the data service input object which this secret corresponds to.
        """
        return pulumi.get(self, "key_identifier")

    @key_identifier.setter
    def key_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_identifier", value)

    @property
    @pulumi.getter(name="keyValue")
    def key_value(self) -> pulumi.Input[str]:
        """
        It contains the encrypted customer secret.
        """
        return pulumi.get(self, "key_value")

    @key_value.setter
    def key_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_value", value)


@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Schedule for the job run.
        :param pulumi.Input[str] name: Name of the schedule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_list: A list of repetition intervals in ISO 8601 format.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_list is not None:
            pulumi.set(__self__, "policy_list", policy_list)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the schedule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyList")
    def policy_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of repetition intervals in ISO 8601 format.
        """
        return pulumi.get(self, "policy_list")

    @policy_list.setter
    def policy_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policy_list", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        The sku type.
        :param pulumi.Input[str] name: The sku name. Required for data manager creation, optional for update.
        :param pulumi.Input[str] tier: The sku tier. This is based on the SKU name.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The sku name. Required for data manager creation, optional for update.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        The sku tier. This is based on the SKU name.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


