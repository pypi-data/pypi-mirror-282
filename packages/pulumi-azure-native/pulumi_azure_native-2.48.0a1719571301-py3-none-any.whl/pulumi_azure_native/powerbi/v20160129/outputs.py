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
    'AzureSkuResponse',
]

@pulumi.output_type
class AzureSkuResponse(dict):
    def __init__(__self__, *,
                 name: str,
                 tier: str):
        """
        :param str name: SKU name
        :param str tier: SKU tier
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        SKU name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        SKU tier
        """
        return pulumi.get(self, "tier")


