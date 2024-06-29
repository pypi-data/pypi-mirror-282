# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetWebhookResult',
    'AwaitableGetWebhookResult',
    'get_webhook',
    'get_webhook_output',
]

@pulumi.output_type
class GetWebhookResult:
    """
    A class represent an AppComplianceAutomation webhook resource.
    """
    def __init__(__self__, content_type=None, delivery_status=None, enable_ssl_verification=None, events=None, id=None, name=None, payload_url=None, provisioning_state=None, send_all_events=None, status=None, system_data=None, tenant_id=None, type=None, update_webhook_key=None, webhook_id=None, webhook_key=None, webhook_key_enabled=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if delivery_status and not isinstance(delivery_status, str):
            raise TypeError("Expected argument 'delivery_status' to be a str")
        pulumi.set(__self__, "delivery_status", delivery_status)
        if enable_ssl_verification and not isinstance(enable_ssl_verification, str):
            raise TypeError("Expected argument 'enable_ssl_verification' to be a str")
        pulumi.set(__self__, "enable_ssl_verification", enable_ssl_verification)
        if events and not isinstance(events, list):
            raise TypeError("Expected argument 'events' to be a list")
        pulumi.set(__self__, "events", events)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if payload_url and not isinstance(payload_url, str):
            raise TypeError("Expected argument 'payload_url' to be a str")
        pulumi.set(__self__, "payload_url", payload_url)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if send_all_events and not isinstance(send_all_events, str):
            raise TypeError("Expected argument 'send_all_events' to be a str")
        pulumi.set(__self__, "send_all_events", send_all_events)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if update_webhook_key and not isinstance(update_webhook_key, str):
            raise TypeError("Expected argument 'update_webhook_key' to be a str")
        pulumi.set(__self__, "update_webhook_key", update_webhook_key)
        if webhook_id and not isinstance(webhook_id, str):
            raise TypeError("Expected argument 'webhook_id' to be a str")
        pulumi.set(__self__, "webhook_id", webhook_id)
        if webhook_key and not isinstance(webhook_key, str):
            raise TypeError("Expected argument 'webhook_key' to be a str")
        pulumi.set(__self__, "webhook_key", webhook_key)
        if webhook_key_enabled and not isinstance(webhook_key_enabled, str):
            raise TypeError("Expected argument 'webhook_key_enabled' to be a str")
        pulumi.set(__self__, "webhook_key_enabled", webhook_key_enabled)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        content type
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="deliveryStatus")
    def delivery_status(self) -> str:
        """
        webhook deliveryStatus
        """
        return pulumi.get(self, "delivery_status")

    @property
    @pulumi.getter(name="enableSslVerification")
    def enable_ssl_verification(self) -> Optional[str]:
        """
        whether to enable ssl verification
        """
        return pulumi.get(self, "enable_ssl_verification")

    @property
    @pulumi.getter
    def events(self) -> Optional[Sequence[str]]:
        """
        under which event notification should be sent.
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> Optional[str]:
        """
        webhook payload url
        """
        return pulumi.get(self, "payload_url")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure Resource Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sendAllEvents")
    def send_all_events(self) -> Optional[str]:
        """
        whether to send notification under any event.
        """
        return pulumi.get(self, "send_all_events")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Webhook status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        Tenant id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateWebhookKey")
    def update_webhook_key(self) -> Optional[str]:
        """
        whether to update webhookKey.
        """
        return pulumi.get(self, "update_webhook_key")

    @property
    @pulumi.getter(name="webhookId")
    def webhook_id(self) -> str:
        """
        Webhook id in database.
        """
        return pulumi.get(self, "webhook_id")

    @property
    @pulumi.getter(name="webhookKey")
    def webhook_key(self) -> Optional[str]:
        """
        webhook secret token. If not set, this field value is null; otherwise, please set a string value.
        """
        return pulumi.get(self, "webhook_key")

    @property
    @pulumi.getter(name="webhookKeyEnabled")
    def webhook_key_enabled(self) -> str:
        """
        whether webhookKey is enabled.
        """
        return pulumi.get(self, "webhook_key_enabled")


class AwaitableGetWebhookResult(GetWebhookResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebhookResult(
            content_type=self.content_type,
            delivery_status=self.delivery_status,
            enable_ssl_verification=self.enable_ssl_verification,
            events=self.events,
            id=self.id,
            name=self.name,
            payload_url=self.payload_url,
            provisioning_state=self.provisioning_state,
            send_all_events=self.send_all_events,
            status=self.status,
            system_data=self.system_data,
            tenant_id=self.tenant_id,
            type=self.type,
            update_webhook_key=self.update_webhook_key,
            webhook_id=self.webhook_id,
            webhook_key=self.webhook_key,
            webhook_key_enabled=self.webhook_key_enabled)


def get_webhook(report_name: Optional[str] = None,
                webhook_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebhookResult:
    """
    Get the AppComplianceAutomation webhook and its properties.


    :param str report_name: Report Name.
    :param str webhook_name: Webhook Name.
    """
    __args__ = dict()
    __args__['reportName'] = report_name
    __args__['webhookName'] = webhook_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appcomplianceautomation/v20240627:getWebhook', __args__, opts=opts, typ=GetWebhookResult).value

    return AwaitableGetWebhookResult(
        content_type=pulumi.get(__ret__, 'content_type'),
        delivery_status=pulumi.get(__ret__, 'delivery_status'),
        enable_ssl_verification=pulumi.get(__ret__, 'enable_ssl_verification'),
        events=pulumi.get(__ret__, 'events'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        payload_url=pulumi.get(__ret__, 'payload_url'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        send_all_events=pulumi.get(__ret__, 'send_all_events'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'),
        update_webhook_key=pulumi.get(__ret__, 'update_webhook_key'),
        webhook_id=pulumi.get(__ret__, 'webhook_id'),
        webhook_key=pulumi.get(__ret__, 'webhook_key'),
        webhook_key_enabled=pulumi.get(__ret__, 'webhook_key_enabled'))


@_utilities.lift_output_func(get_webhook)
def get_webhook_output(report_name: Optional[pulumi.Input[str]] = None,
                       webhook_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebhookResult]:
    """
    Get the AppComplianceAutomation webhook and its properties.


    :param str report_name: Report Name.
    :param str webhook_name: Webhook Name.
    """
    ...
