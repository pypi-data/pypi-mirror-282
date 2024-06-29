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
    'GetDiagnosticServiceTokenReadOnlyResult',
    'AwaitableGetDiagnosticServiceTokenReadOnlyResult',
    'get_diagnostic_service_token_read_only',
    'get_diagnostic_service_token_read_only_output',
]

@pulumi.output_type
class GetDiagnosticServiceTokenReadOnlyResult:
    """
    The response to a diagnostic services token query.
    """
    def __init__(__self__, token=None):
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        JWT token for accessing application insights diagnostic service data.
        """
        return pulumi.get(self, "token")


class AwaitableGetDiagnosticServiceTokenReadOnlyResult(GetDiagnosticServiceTokenReadOnlyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiagnosticServiceTokenReadOnlyResult(
            token=self.token)


def get_diagnostic_service_token_read_only(resource_uri: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiagnosticServiceTokenReadOnlyResult:
    """
    Gets an read-only access token for application insights diagnostic service data.
    Azure REST API version: 2021-03-03-preview.


    :param str resource_uri: The identifier of the resource.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights:getDiagnosticServiceTokenReadOnly', __args__, opts=opts, typ=GetDiagnosticServiceTokenReadOnlyResult).value

    return AwaitableGetDiagnosticServiceTokenReadOnlyResult(
        token=pulumi.get(__ret__, 'token'))


@_utilities.lift_output_func(get_diagnostic_service_token_read_only)
def get_diagnostic_service_token_read_only_output(resource_uri: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiagnosticServiceTokenReadOnlyResult]:
    """
    Gets an read-only access token for application insights diagnostic service data.
    Azure REST API version: 2021-03-03-preview.


    :param str resource_uri: The identifier of the resource.
    """
    ...
