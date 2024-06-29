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
    'EndpointPropertiesArgs',
]

@pulumi.input_type
class EndpointPropertiesArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'Type']],
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        Endpoint details
        :param pulumi.Input[Union[str, 'Type']] type: The type of endpoint.
        :param pulumi.Input[str] resource_id: The resource Id of the connectivity endpoint (optional).
        """
        pulumi.set(__self__, "type", type)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'Type']]:
        """
        The type of endpoint.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'Type']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource Id of the connectivity endpoint (optional).
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


