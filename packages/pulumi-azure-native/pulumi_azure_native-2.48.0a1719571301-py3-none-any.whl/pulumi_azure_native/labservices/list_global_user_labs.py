# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ListGlobalUserLabsResult',
    'AwaitableListGlobalUserLabsResult',
    'list_global_user_labs',
    'list_global_user_labs_output',
]

@pulumi.output_type
class ListGlobalUserLabsResult:
    """
    Lists the labs owned by a user
    """
    def __init__(__self__, labs=None):
        if labs and not isinstance(labs, list):
            raise TypeError("Expected argument 'labs' to be a list")
        pulumi.set(__self__, "labs", labs)

    @property
    @pulumi.getter
    def labs(self) -> Optional[Sequence['outputs.LabDetailsResponse']]:
        """
        List of all the labs
        """
        return pulumi.get(self, "labs")


class AwaitableListGlobalUserLabsResult(ListGlobalUserLabsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGlobalUserLabsResult(
            labs=self.labs)


def list_global_user_labs(user_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGlobalUserLabsResult:
    """
    List labs for the user.
    Azure REST API version: 2018-10-15.


    :param str user_name: The name of the user.
    """
    __args__ = dict()
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices:listGlobalUserLabs', __args__, opts=opts, typ=ListGlobalUserLabsResult).value

    return AwaitableListGlobalUserLabsResult(
        labs=pulumi.get(__ret__, 'labs'))


@_utilities.lift_output_func(list_global_user_labs)
def list_global_user_labs_output(user_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGlobalUserLabsResult]:
    """
    List labs for the user.
    Azure REST API version: 2018-10-15.


    :param str user_name: The name of the user.
    """
    ...
