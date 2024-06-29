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
from ._enums import *

__all__ = ['WebhookArgs', 'Webhook']

@pulumi.input_type
class WebhookArgs:
    def __init__(__self__, *,
                 report_name: pulumi.Input[str],
                 content_type: Optional[pulumi.Input[Union[str, 'ContentType']]] = None,
                 enable_ssl_verification: Optional[pulumi.Input[Union[str, 'EnableSslVerification']]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NotificationEvent']]]]] = None,
                 payload_url: Optional[pulumi.Input[str]] = None,
                 send_all_events: Optional[pulumi.Input[Union[str, 'SendAllEvents']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'WebhookStatus']]] = None,
                 update_webhook_key: Optional[pulumi.Input[Union[str, 'UpdateWebhookKey']]] = None,
                 webhook_key: Optional[pulumi.Input[str]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Webhook resource.
        :param pulumi.Input[str] report_name: Report Name.
        :param pulumi.Input[Union[str, 'ContentType']] content_type: content type
        :param pulumi.Input[Union[str, 'EnableSslVerification']] enable_ssl_verification: whether to enable ssl verification
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'NotificationEvent']]]] events: under which event notification should be sent.
        :param pulumi.Input[str] payload_url: webhook payload url
        :param pulumi.Input[Union[str, 'SendAllEvents']] send_all_events: whether to send notification under any event.
        :param pulumi.Input[Union[str, 'WebhookStatus']] status: Webhook status.
        :param pulumi.Input[Union[str, 'UpdateWebhookKey']] update_webhook_key: whether to update webhookKey.
        :param pulumi.Input[str] webhook_key: webhook secret token. If not set, this field value is null; otherwise, please set a string value.
        :param pulumi.Input[str] webhook_name: Webhook Name.
        """
        pulumi.set(__self__, "report_name", report_name)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if enable_ssl_verification is not None:
            pulumi.set(__self__, "enable_ssl_verification", enable_ssl_verification)
        if events is not None:
            pulumi.set(__self__, "events", events)
        if payload_url is not None:
            pulumi.set(__self__, "payload_url", payload_url)
        if send_all_events is not None:
            pulumi.set(__self__, "send_all_events", send_all_events)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if update_webhook_key is not None:
            pulumi.set(__self__, "update_webhook_key", update_webhook_key)
        if webhook_key is not None:
            pulumi.set(__self__, "webhook_key", webhook_key)
        if webhook_name is not None:
            pulumi.set(__self__, "webhook_name", webhook_name)

    @property
    @pulumi.getter(name="reportName")
    def report_name(self) -> pulumi.Input[str]:
        """
        Report Name.
        """
        return pulumi.get(self, "report_name")

    @report_name.setter
    def report_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "report_name", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[Union[str, 'ContentType']]]:
        """
        content type
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[Union[str, 'ContentType']]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="enableSslVerification")
    def enable_ssl_verification(self) -> Optional[pulumi.Input[Union[str, 'EnableSslVerification']]]:
        """
        whether to enable ssl verification
        """
        return pulumi.get(self, "enable_ssl_verification")

    @enable_ssl_verification.setter
    def enable_ssl_verification(self, value: Optional[pulumi.Input[Union[str, 'EnableSslVerification']]]):
        pulumi.set(self, "enable_ssl_verification", value)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NotificationEvent']]]]]:
        """
        under which event notification should be sent.
        """
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NotificationEvent']]]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> Optional[pulumi.Input[str]]:
        """
        webhook payload url
        """
        return pulumi.get(self, "payload_url")

    @payload_url.setter
    def payload_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payload_url", value)

    @property
    @pulumi.getter(name="sendAllEvents")
    def send_all_events(self) -> Optional[pulumi.Input[Union[str, 'SendAllEvents']]]:
        """
        whether to send notification under any event.
        """
        return pulumi.get(self, "send_all_events")

    @send_all_events.setter
    def send_all_events(self, value: Optional[pulumi.Input[Union[str, 'SendAllEvents']]]):
        pulumi.set(self, "send_all_events", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'WebhookStatus']]]:
        """
        Webhook status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'WebhookStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="updateWebhookKey")
    def update_webhook_key(self) -> Optional[pulumi.Input[Union[str, 'UpdateWebhookKey']]]:
        """
        whether to update webhookKey.
        """
        return pulumi.get(self, "update_webhook_key")

    @update_webhook_key.setter
    def update_webhook_key(self, value: Optional[pulumi.Input[Union[str, 'UpdateWebhookKey']]]):
        pulumi.set(self, "update_webhook_key", value)

    @property
    @pulumi.getter(name="webhookKey")
    def webhook_key(self) -> Optional[pulumi.Input[str]]:
        """
        webhook secret token. If not set, this field value is null; otherwise, please set a string value.
        """
        return pulumi.get(self, "webhook_key")

    @webhook_key.setter
    def webhook_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_key", value)

    @property
    @pulumi.getter(name="webhookName")
    def webhook_name(self) -> Optional[pulumi.Input[str]]:
        """
        Webhook Name.
        """
        return pulumi.get(self, "webhook_name")

    @webhook_name.setter
    def webhook_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_name", value)


class Webhook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[Union[str, 'ContentType']]] = None,
                 enable_ssl_verification: Optional[pulumi.Input[Union[str, 'EnableSslVerification']]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NotificationEvent']]]]] = None,
                 payload_url: Optional[pulumi.Input[str]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 send_all_events: Optional[pulumi.Input[Union[str, 'SendAllEvents']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'WebhookStatus']]] = None,
                 update_webhook_key: Optional[pulumi.Input[Union[str, 'UpdateWebhookKey']]] = None,
                 webhook_key: Optional[pulumi.Input[str]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A class represent an AppComplianceAutomation webhook resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'ContentType']] content_type: content type
        :param pulumi.Input[Union[str, 'EnableSslVerification']] enable_ssl_verification: whether to enable ssl verification
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'NotificationEvent']]]] events: under which event notification should be sent.
        :param pulumi.Input[str] payload_url: webhook payload url
        :param pulumi.Input[str] report_name: Report Name.
        :param pulumi.Input[Union[str, 'SendAllEvents']] send_all_events: whether to send notification under any event.
        :param pulumi.Input[Union[str, 'WebhookStatus']] status: Webhook status.
        :param pulumi.Input[Union[str, 'UpdateWebhookKey']] update_webhook_key: whether to update webhookKey.
        :param pulumi.Input[str] webhook_key: webhook secret token. If not set, this field value is null; otherwise, please set a string value.
        :param pulumi.Input[str] webhook_name: Webhook Name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebhookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A class represent an AppComplianceAutomation webhook resource.

        :param str resource_name: The name of the resource.
        :param WebhookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebhookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[Union[str, 'ContentType']]] = None,
                 enable_ssl_verification: Optional[pulumi.Input[Union[str, 'EnableSslVerification']]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NotificationEvent']]]]] = None,
                 payload_url: Optional[pulumi.Input[str]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 send_all_events: Optional[pulumi.Input[Union[str, 'SendAllEvents']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'WebhookStatus']]] = None,
                 update_webhook_key: Optional[pulumi.Input[Union[str, 'UpdateWebhookKey']]] = None,
                 webhook_key: Optional[pulumi.Input[str]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebhookArgs.__new__(WebhookArgs)

            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["enable_ssl_verification"] = enable_ssl_verification
            __props__.__dict__["events"] = events
            __props__.__dict__["payload_url"] = payload_url
            if report_name is None and not opts.urn:
                raise TypeError("Missing required property 'report_name'")
            __props__.__dict__["report_name"] = report_name
            __props__.__dict__["send_all_events"] = send_all_events
            __props__.__dict__["status"] = status
            __props__.__dict__["update_webhook_key"] = update_webhook_key
            __props__.__dict__["webhook_key"] = webhook_key
            __props__.__dict__["webhook_name"] = webhook_name
            __props__.__dict__["delivery_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["webhook_id"] = None
            __props__.__dict__["webhook_key_enabled"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appcomplianceautomation:Webhook")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Webhook, __self__).__init__(
            'azure-native:appcomplianceautomation/v20240627:Webhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Webhook':
        """
        Get an existing Webhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebhookArgs.__new__(WebhookArgs)

        __props__.__dict__["content_type"] = None
        __props__.__dict__["delivery_status"] = None
        __props__.__dict__["enable_ssl_verification"] = None
        __props__.__dict__["events"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["payload_url"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["send_all_events"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["update_webhook_key"] = None
        __props__.__dict__["webhook_id"] = None
        __props__.__dict__["webhook_key"] = None
        __props__.__dict__["webhook_key_enabled"] = None
        return Webhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        """
        content type
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="deliveryStatus")
    def delivery_status(self) -> pulumi.Output[str]:
        """
        webhook deliveryStatus
        """
        return pulumi.get(self, "delivery_status")

    @property
    @pulumi.getter(name="enableSslVerification")
    def enable_ssl_verification(self) -> pulumi.Output[Optional[str]]:
        """
        whether to enable ssl verification
        """
        return pulumi.get(self, "enable_ssl_verification")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        under which event notification should be sent.
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> pulumi.Output[Optional[str]]:
        """
        webhook payload url
        """
        return pulumi.get(self, "payload_url")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Azure Resource Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sendAllEvents")
    def send_all_events(self) -> pulumi.Output[Optional[str]]:
        """
        whether to send notification under any event.
        """
        return pulumi.get(self, "send_all_events")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Webhook status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Tenant id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateWebhookKey")
    def update_webhook_key(self) -> pulumi.Output[Optional[str]]:
        """
        whether to update webhookKey.
        """
        return pulumi.get(self, "update_webhook_key")

    @property
    @pulumi.getter(name="webhookId")
    def webhook_id(self) -> pulumi.Output[str]:
        """
        Webhook id in database.
        """
        return pulumi.get(self, "webhook_id")

    @property
    @pulumi.getter(name="webhookKey")
    def webhook_key(self) -> pulumi.Output[Optional[str]]:
        """
        webhook secret token. If not set, this field value is null; otherwise, please set a string value.
        """
        return pulumi.get(self, "webhook_key")

    @property
    @pulumi.getter(name="webhookKeyEnabled")
    def webhook_key_enabled(self) -> pulumi.Output[str]:
        """
        whether webhookKey is enabled.
        """
        return pulumi.get(self, "webhook_key_enabled")

