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
    'GetOfferAccessTokenResult',
    'AwaitableGetOfferAccessTokenResult',
    'get_offer_access_token',
    'get_offer_access_token_output',
]

@pulumi.output_type
class GetOfferAccessTokenResult:
    """
    The disk access token
    """
    def __init__(__self__, access_token=None, disk_id=None, status=None):
        if access_token and not isinstance(access_token, str):
            raise TypeError("Expected argument 'access_token' to be a str")
        pulumi.set(__self__, "access_token", access_token)
        if disk_id and not isinstance(disk_id, str):
            raise TypeError("Expected argument 'disk_id' to be a str")
        pulumi.set(__self__, "disk_id", disk_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> str:
        """
        The access token.
        """
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[str]:
        """
        The disk id.
        """
        return pulumi.get(self, "disk_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The access token creation status.
        """
        return pulumi.get(self, "status")


class AwaitableGetOfferAccessTokenResult(GetOfferAccessTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOfferAccessTokenResult(
            access_token=self.access_token,
            disk_id=self.disk_id,
            status=self.status)


def get_offer_access_token(offer_id: Optional[str] = None,
                           request_id: Optional[str] = None,
                           resource_uri: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOfferAccessTokenResult:
    """
    get access token.
    Azure REST API version: 2023-08-01-preview.

    Other available API versions: 2023-08-01.


    :param str offer_id: Id of the offer
    :param str request_id: The name of the publisher.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    """
    __args__ = dict()
    __args__['offerId'] = offer_id
    __args__['requestId'] = request_id
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:edgemarketplace:getOfferAccessToken', __args__, opts=opts, typ=GetOfferAccessTokenResult).value

    return AwaitableGetOfferAccessTokenResult(
        access_token=pulumi.get(__ret__, 'access_token'),
        disk_id=pulumi.get(__ret__, 'disk_id'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_offer_access_token)
def get_offer_access_token_output(offer_id: Optional[pulumi.Input[str]] = None,
                                  request_id: Optional[pulumi.Input[str]] = None,
                                  resource_uri: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOfferAccessTokenResult]:
    """
    get access token.
    Azure REST API version: 2023-08-01-preview.

    Other available API versions: 2023-08-01.


    :param str offer_id: Id of the offer
    :param str request_id: The name of the publisher.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    """
    ...
