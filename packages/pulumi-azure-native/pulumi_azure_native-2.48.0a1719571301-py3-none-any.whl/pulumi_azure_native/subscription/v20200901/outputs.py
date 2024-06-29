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
    'PutAliasResponsePropertiesResponse',
]

@pulumi.output_type
class PutAliasResponsePropertiesResponse(dict):
    """
    Put subscription creation result properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subscriptionId":
            suggest = "subscription_id"
        elif key == "provisioningState":
            suggest = "provisioning_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PutAliasResponsePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PutAliasResponsePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PutAliasResponsePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subscription_id: str,
                 provisioning_state: Optional[str] = None):
        """
        Put subscription creation result properties.
        :param str subscription_id: Newly created subscription Id.
        :param str provisioning_state: The provisioning state of the resource.
        """
        pulumi.set(__self__, "subscription_id", subscription_id)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        Newly created subscription Id.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")


