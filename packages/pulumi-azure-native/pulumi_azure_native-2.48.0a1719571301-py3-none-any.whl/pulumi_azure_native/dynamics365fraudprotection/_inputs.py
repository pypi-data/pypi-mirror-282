# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DFPInstanceAdministratorsArgs',
]

@pulumi.input_type
class DFPInstanceAdministratorsArgs:
    def __init__(__self__, *,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        An array of administrator user identities
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: An array of administrator user identities.
        """
        if members is not None:
            pulumi.set(__self__, "members", members)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of administrator user identities.
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)


