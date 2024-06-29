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
    'SystemAssignedServiceIdentityArgs',
]

@pulumi.input_type
class SystemAssignedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'SystemAssignedServiceIdentityType']]):
        """
        Managed service identity (either system assigned, or none)
        :param pulumi.Input[Union[str, 'SystemAssignedServiceIdentityType']] type: Type of managed service identity (either system assigned, or none).
        """
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'SystemAssignedServiceIdentityType']]:
        """
        Type of managed service identity (either system assigned, or none).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'SystemAssignedServiceIdentityType']]):
        pulumi.set(self, "type", value)


