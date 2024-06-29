# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetWebhookCallbackConfigResult',
    'AwaitableGetWebhookCallbackConfigResult',
    'get_webhook_callback_config',
    'get_webhook_callback_config_output',
]

@pulumi.output_type
class GetWebhookCallbackConfigResult:
    """
    The configuration of service URI and custom headers for the webhook.
    """
    def __init__(__self__, custom_headers=None, service_uri=None):
        if custom_headers and not isinstance(custom_headers, dict):
            raise TypeError("Expected argument 'custom_headers' to be a dict")
        pulumi.set(__self__, "custom_headers", custom_headers)
        if service_uri and not isinstance(service_uri, str):
            raise TypeError("Expected argument 'service_uri' to be a str")
        pulumi.set(__self__, "service_uri", service_uri)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[Mapping[str, str]]:
        """
        Custom headers that will be added to the webhook notifications.
        """
        return pulumi.get(self, "custom_headers")

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> str:
        """
        The service URI for the webhook to post notifications.
        """
        return pulumi.get(self, "service_uri")


class AwaitableGetWebhookCallbackConfigResult(GetWebhookCallbackConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebhookCallbackConfigResult(
            custom_headers=self.custom_headers,
            service_uri=self.service_uri)


def get_webhook_callback_config(registry_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                webhook_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebhookCallbackConfigResult:
    """
    Gets the configuration of service URI and custom headers for the webhook.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str webhook_name: The name of the webhook.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['webhookName'] = webhook_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20230701:getWebhookCallbackConfig', __args__, opts=opts, typ=GetWebhookCallbackConfigResult).value

    return AwaitableGetWebhookCallbackConfigResult(
        custom_headers=pulumi.get(__ret__, 'custom_headers'),
        service_uri=pulumi.get(__ret__, 'service_uri'))


@_utilities.lift_output_func(get_webhook_callback_config)
def get_webhook_callback_config_output(registry_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       webhook_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebhookCallbackConfigResult]:
    """
    Gets the configuration of service URI and custom headers for the webhook.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str webhook_name: The name of the webhook.
    """
    ...
