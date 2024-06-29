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
from ._inputs import *

__all__ = ['NotificationHubArgs', 'NotificationHub']

@pulumi.input_type
class NotificationHubArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 adm_credential: Optional[pulumi.Input['AdmCredentialArgs']] = None,
                 apns_credential: Optional[pulumi.Input['ApnsCredentialArgs']] = None,
                 baidu_credential: Optional[pulumi.Input['BaiduCredentialArgs']] = None,
                 browser_credential: Optional[pulumi.Input['BrowserCredentialArgs']] = None,
                 fcm_v1_credential: Optional[pulumi.Input['FcmV1CredentialArgs']] = None,
                 gcm_credential: Optional[pulumi.Input['GcmCredentialArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mpns_credential: Optional[pulumi.Input['MpnsCredentialArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_hub_name: Optional[pulumi.Input[str]] = None,
                 registration_ttl: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 wns_credential: Optional[pulumi.Input['WnsCredentialArgs']] = None,
                 xiaomi_credential: Optional[pulumi.Input['XiaomiCredentialArgs']] = None):
        """
        The set of arguments for constructing a NotificationHub resource.
        :param pulumi.Input[str] namespace_name: Namespace name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['AdmCredentialArgs'] adm_credential: Description of a NotificationHub AdmCredential.
        :param pulumi.Input['ApnsCredentialArgs'] apns_credential: Description of a NotificationHub ApnsCredential.
        :param pulumi.Input['BaiduCredentialArgs'] baidu_credential: Description of a NotificationHub BaiduCredential.
        :param pulumi.Input['BrowserCredentialArgs'] browser_credential: Description of a NotificationHub BrowserCredential.
        :param pulumi.Input['FcmV1CredentialArgs'] fcm_v1_credential: Description of a NotificationHub FcmV1Credential.
        :param pulumi.Input['GcmCredentialArgs'] gcm_credential: Description of a NotificationHub GcmCredential.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['MpnsCredentialArgs'] mpns_credential: Description of a NotificationHub MpnsCredential.
        :param pulumi.Input[str] name: Gets or sets the NotificationHub name.
        :param pulumi.Input[str] notification_hub_name: Notification Hub name
        :param pulumi.Input[str] registration_ttl: Gets or sets the RegistrationTtl of the created NotificationHub
        :param pulumi.Input['SkuArgs'] sku: The Sku description for a namespace
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['WnsCredentialArgs'] wns_credential: Description of a NotificationHub WnsCredential.
        :param pulumi.Input['XiaomiCredentialArgs'] xiaomi_credential: Description of a NotificationHub XiaomiCredential.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if adm_credential is not None:
            pulumi.set(__self__, "adm_credential", adm_credential)
        if apns_credential is not None:
            pulumi.set(__self__, "apns_credential", apns_credential)
        if baidu_credential is not None:
            pulumi.set(__self__, "baidu_credential", baidu_credential)
        if browser_credential is not None:
            pulumi.set(__self__, "browser_credential", browser_credential)
        if fcm_v1_credential is not None:
            pulumi.set(__self__, "fcm_v1_credential", fcm_v1_credential)
        if gcm_credential is not None:
            pulumi.set(__self__, "gcm_credential", gcm_credential)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mpns_credential is not None:
            pulumi.set(__self__, "mpns_credential", mpns_credential)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_hub_name is not None:
            pulumi.set(__self__, "notification_hub_name", notification_hub_name)
        if registration_ttl is not None:
            pulumi.set(__self__, "registration_ttl", registration_ttl)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if wns_credential is not None:
            pulumi.set(__self__, "wns_credential", wns_credential)
        if xiaomi_credential is not None:
            pulumi.set(__self__, "xiaomi_credential", xiaomi_credential)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        Namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> Optional[pulumi.Input['AdmCredentialArgs']]:
        """
        Description of a NotificationHub AdmCredential.
        """
        return pulumi.get(self, "adm_credential")

    @adm_credential.setter
    def adm_credential(self, value: Optional[pulumi.Input['AdmCredentialArgs']]):
        pulumi.set(self, "adm_credential", value)

    @property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> Optional[pulumi.Input['ApnsCredentialArgs']]:
        """
        Description of a NotificationHub ApnsCredential.
        """
        return pulumi.get(self, "apns_credential")

    @apns_credential.setter
    def apns_credential(self, value: Optional[pulumi.Input['ApnsCredentialArgs']]):
        pulumi.set(self, "apns_credential", value)

    @property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> Optional[pulumi.Input['BaiduCredentialArgs']]:
        """
        Description of a NotificationHub BaiduCredential.
        """
        return pulumi.get(self, "baidu_credential")

    @baidu_credential.setter
    def baidu_credential(self, value: Optional[pulumi.Input['BaiduCredentialArgs']]):
        pulumi.set(self, "baidu_credential", value)

    @property
    @pulumi.getter(name="browserCredential")
    def browser_credential(self) -> Optional[pulumi.Input['BrowserCredentialArgs']]:
        """
        Description of a NotificationHub BrowserCredential.
        """
        return pulumi.get(self, "browser_credential")

    @browser_credential.setter
    def browser_credential(self, value: Optional[pulumi.Input['BrowserCredentialArgs']]):
        pulumi.set(self, "browser_credential", value)

    @property
    @pulumi.getter(name="fcmV1Credential")
    def fcm_v1_credential(self) -> Optional[pulumi.Input['FcmV1CredentialArgs']]:
        """
        Description of a NotificationHub FcmV1Credential.
        """
        return pulumi.get(self, "fcm_v1_credential")

    @fcm_v1_credential.setter
    def fcm_v1_credential(self, value: Optional[pulumi.Input['FcmV1CredentialArgs']]):
        pulumi.set(self, "fcm_v1_credential", value)

    @property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> Optional[pulumi.Input['GcmCredentialArgs']]:
        """
        Description of a NotificationHub GcmCredential.
        """
        return pulumi.get(self, "gcm_credential")

    @gcm_credential.setter
    def gcm_credential(self, value: Optional[pulumi.Input['GcmCredentialArgs']]):
        pulumi.set(self, "gcm_credential", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> Optional[pulumi.Input['MpnsCredentialArgs']]:
        """
        Description of a NotificationHub MpnsCredential.
        """
        return pulumi.get(self, "mpns_credential")

    @mpns_credential.setter
    def mpns_credential(self, value: Optional[pulumi.Input['MpnsCredentialArgs']]):
        pulumi.set(self, "mpns_credential", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the NotificationHub name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationHubName")
    def notification_hub_name(self) -> Optional[pulumi.Input[str]]:
        """
        Notification Hub name
        """
        return pulumi.get(self, "notification_hub_name")

    @notification_hub_name.setter
    def notification_hub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_hub_name", value)

    @property
    @pulumi.getter(name="registrationTtl")
    def registration_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the RegistrationTtl of the created NotificationHub
        """
        return pulumi.get(self, "registration_ttl")

    @registration_ttl.setter
    def registration_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registration_ttl", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The Sku description for a namespace
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> Optional[pulumi.Input['WnsCredentialArgs']]:
        """
        Description of a NotificationHub WnsCredential.
        """
        return pulumi.get(self, "wns_credential")

    @wns_credential.setter
    def wns_credential(self, value: Optional[pulumi.Input['WnsCredentialArgs']]):
        pulumi.set(self, "wns_credential", value)

    @property
    @pulumi.getter(name="xiaomiCredential")
    def xiaomi_credential(self) -> Optional[pulumi.Input['XiaomiCredentialArgs']]:
        """
        Description of a NotificationHub XiaomiCredential.
        """
        return pulumi.get(self, "xiaomi_credential")

    @xiaomi_credential.setter
    def xiaomi_credential(self, value: Optional[pulumi.Input['XiaomiCredentialArgs']]):
        pulumi.set(self, "xiaomi_credential", value)


class NotificationHub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adm_credential: Optional[pulumi.Input[pulumi.InputType['AdmCredentialArgs']]] = None,
                 apns_credential: Optional[pulumi.Input[pulumi.InputType['ApnsCredentialArgs']]] = None,
                 baidu_credential: Optional[pulumi.Input[pulumi.InputType['BaiduCredentialArgs']]] = None,
                 browser_credential: Optional[pulumi.Input[pulumi.InputType['BrowserCredentialArgs']]] = None,
                 fcm_v1_credential: Optional[pulumi.Input[pulumi.InputType['FcmV1CredentialArgs']]] = None,
                 gcm_credential: Optional[pulumi.Input[pulumi.InputType['GcmCredentialArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mpns_credential: Optional[pulumi.Input[pulumi.InputType['MpnsCredentialArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 notification_hub_name: Optional[pulumi.Input[str]] = None,
                 registration_ttl: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 wns_credential: Optional[pulumi.Input[pulumi.InputType['WnsCredentialArgs']]] = None,
                 xiaomi_credential: Optional[pulumi.Input[pulumi.InputType['XiaomiCredentialArgs']]] = None,
                 __props__=None):
        """
        Notification Hub Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AdmCredentialArgs']] adm_credential: Description of a NotificationHub AdmCredential.
        :param pulumi.Input[pulumi.InputType['ApnsCredentialArgs']] apns_credential: Description of a NotificationHub ApnsCredential.
        :param pulumi.Input[pulumi.InputType['BaiduCredentialArgs']] baidu_credential: Description of a NotificationHub BaiduCredential.
        :param pulumi.Input[pulumi.InputType['BrowserCredentialArgs']] browser_credential: Description of a NotificationHub BrowserCredential.
        :param pulumi.Input[pulumi.InputType['FcmV1CredentialArgs']] fcm_v1_credential: Description of a NotificationHub FcmV1Credential.
        :param pulumi.Input[pulumi.InputType['GcmCredentialArgs']] gcm_credential: Description of a NotificationHub GcmCredential.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['MpnsCredentialArgs']] mpns_credential: Description of a NotificationHub MpnsCredential.
        :param pulumi.Input[str] name: Gets or sets the NotificationHub name.
        :param pulumi.Input[str] namespace_name: Namespace name
        :param pulumi.Input[str] notification_hub_name: Notification Hub name
        :param pulumi.Input[str] registration_ttl: Gets or sets the RegistrationTtl of the created NotificationHub
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The Sku description for a namespace
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['WnsCredentialArgs']] wns_credential: Description of a NotificationHub WnsCredential.
        :param pulumi.Input[pulumi.InputType['XiaomiCredentialArgs']] xiaomi_credential: Description of a NotificationHub XiaomiCredential.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationHubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Notification Hub Resource.

        :param str resource_name: The name of the resource.
        :param NotificationHubArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationHubArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adm_credential: Optional[pulumi.Input[pulumi.InputType['AdmCredentialArgs']]] = None,
                 apns_credential: Optional[pulumi.Input[pulumi.InputType['ApnsCredentialArgs']]] = None,
                 baidu_credential: Optional[pulumi.Input[pulumi.InputType['BaiduCredentialArgs']]] = None,
                 browser_credential: Optional[pulumi.Input[pulumi.InputType['BrowserCredentialArgs']]] = None,
                 fcm_v1_credential: Optional[pulumi.Input[pulumi.InputType['FcmV1CredentialArgs']]] = None,
                 gcm_credential: Optional[pulumi.Input[pulumi.InputType['GcmCredentialArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mpns_credential: Optional[pulumi.Input[pulumi.InputType['MpnsCredentialArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 notification_hub_name: Optional[pulumi.Input[str]] = None,
                 registration_ttl: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 wns_credential: Optional[pulumi.Input[pulumi.InputType['WnsCredentialArgs']]] = None,
                 xiaomi_credential: Optional[pulumi.Input[pulumi.InputType['XiaomiCredentialArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationHubArgs.__new__(NotificationHubArgs)

            __props__.__dict__["adm_credential"] = adm_credential
            __props__.__dict__["apns_credential"] = apns_credential
            __props__.__dict__["baidu_credential"] = baidu_credential
            __props__.__dict__["browser_credential"] = browser_credential
            __props__.__dict__["fcm_v1_credential"] = fcm_v1_credential
            __props__.__dict__["gcm_credential"] = gcm_credential
            __props__.__dict__["location"] = location
            __props__.__dict__["mpns_credential"] = mpns_credential
            __props__.__dict__["name"] = name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["notification_hub_name"] = notification_hub_name
            __props__.__dict__["registration_ttl"] = registration_ttl
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["wns_credential"] = wns_credential
            __props__.__dict__["xiaomi_credential"] = xiaomi_credential
            __props__.__dict__["authorization_rules"] = None
            __props__.__dict__["daily_max_active_devices"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:notificationhubs:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20140901:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20160301:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20170401:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20230101preview:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20230901:NotificationHub")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NotificationHub, __self__).__init__(
            'azure-native:notificationhubs/v20231001preview:NotificationHub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NotificationHub':
        """
        Get an existing NotificationHub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NotificationHubArgs.__new__(NotificationHubArgs)

        __props__.__dict__["adm_credential"] = None
        __props__.__dict__["apns_credential"] = None
        __props__.__dict__["authorization_rules"] = None
        __props__.__dict__["baidu_credential"] = None
        __props__.__dict__["browser_credential"] = None
        __props__.__dict__["daily_max_active_devices"] = None
        __props__.__dict__["fcm_v1_credential"] = None
        __props__.__dict__["gcm_credential"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mpns_credential"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["registration_ttl"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["wns_credential"] = None
        __props__.__dict__["xiaomi_credential"] = None
        return NotificationHub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> pulumi.Output[Optional['outputs.AdmCredentialResponse']]:
        """
        Description of a NotificationHub AdmCredential.
        """
        return pulumi.get(self, "adm_credential")

    @property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> pulumi.Output[Optional['outputs.ApnsCredentialResponse']]:
        """
        Description of a NotificationHub ApnsCredential.
        """
        return pulumi.get(self, "apns_credential")

    @property
    @pulumi.getter(name="authorizationRules")
    def authorization_rules(self) -> pulumi.Output[Sequence['outputs.SharedAccessAuthorizationRulePropertiesResponse']]:
        """
        Gets or sets the AuthorizationRules of the created NotificationHub
        """
        return pulumi.get(self, "authorization_rules")

    @property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> pulumi.Output[Optional['outputs.BaiduCredentialResponse']]:
        """
        Description of a NotificationHub BaiduCredential.
        """
        return pulumi.get(self, "baidu_credential")

    @property
    @pulumi.getter(name="browserCredential")
    def browser_credential(self) -> pulumi.Output[Optional['outputs.BrowserCredentialResponse']]:
        """
        Description of a NotificationHub BrowserCredential.
        """
        return pulumi.get(self, "browser_credential")

    @property
    @pulumi.getter(name="dailyMaxActiveDevices")
    def daily_max_active_devices(self) -> pulumi.Output[float]:
        return pulumi.get(self, "daily_max_active_devices")

    @property
    @pulumi.getter(name="fcmV1Credential")
    def fcm_v1_credential(self) -> pulumi.Output[Optional['outputs.FcmV1CredentialResponse']]:
        """
        Description of a NotificationHub FcmV1Credential.
        """
        return pulumi.get(self, "fcm_v1_credential")

    @property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> pulumi.Output[Optional['outputs.GcmCredentialResponse']]:
        """
        Description of a NotificationHub GcmCredential.
        """
        return pulumi.get(self, "gcm_credential")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> pulumi.Output[Optional['outputs.MpnsCredentialResponse']]:
        """
        Description of a NotificationHub MpnsCredential.
        """
        return pulumi.get(self, "mpns_credential")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="registrationTtl")
    def registration_ttl(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the RegistrationTtl of the created NotificationHub
        """
        return pulumi.get(self, "registration_ttl")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The Sku description for a namespace
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> pulumi.Output[Optional['outputs.WnsCredentialResponse']]:
        """
        Description of a NotificationHub WnsCredential.
        """
        return pulumi.get(self, "wns_credential")

    @property
    @pulumi.getter(name="xiaomiCredential")
    def xiaomi_credential(self) -> pulumi.Output[Optional['outputs.XiaomiCredentialResponse']]:
        """
        Description of a NotificationHub XiaomiCredential.
        """
        return pulumi.get(self, "xiaomi_credential")

