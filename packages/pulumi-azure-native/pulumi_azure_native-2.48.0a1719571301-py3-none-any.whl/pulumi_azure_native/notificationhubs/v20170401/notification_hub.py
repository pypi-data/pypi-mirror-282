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
                 authorization_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs']]]] = None,
                 baidu_credential: Optional[pulumi.Input['BaiduCredentialArgs']] = None,
                 gcm_credential: Optional[pulumi.Input['GcmCredentialArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mpns_credential: Optional[pulumi.Input['MpnsCredentialArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_hub_name: Optional[pulumi.Input[str]] = None,
                 registration_ttl: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 wns_credential: Optional[pulumi.Input['WnsCredentialArgs']] = None):
        """
        The set of arguments for constructing a NotificationHub resource.
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['AdmCredentialArgs'] adm_credential: The AdmCredential of the created NotificationHub
        :param pulumi.Input['ApnsCredentialArgs'] apns_credential: The ApnsCredential of the created NotificationHub
        :param pulumi.Input[Sequence[pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs']]] authorization_rules: The AuthorizationRules of the created NotificationHub
        :param pulumi.Input['BaiduCredentialArgs'] baidu_credential: The BaiduCredential of the created NotificationHub
        :param pulumi.Input['GcmCredentialArgs'] gcm_credential: The GcmCredential of the created NotificationHub
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['MpnsCredentialArgs'] mpns_credential: The MpnsCredential of the created NotificationHub
        :param pulumi.Input[str] name: The NotificationHub name.
        :param pulumi.Input[str] notification_hub_name: The notification hub name.
        :param pulumi.Input[str] registration_ttl: The RegistrationTtl of the created NotificationHub
        :param pulumi.Input['SkuArgs'] sku: The sku of the created namespace
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input['WnsCredentialArgs'] wns_credential: The WnsCredential of the created NotificationHub
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if adm_credential is not None:
            pulumi.set(__self__, "adm_credential", adm_credential)
        if apns_credential is not None:
            pulumi.set(__self__, "apns_credential", apns_credential)
        if authorization_rules is not None:
            pulumi.set(__self__, "authorization_rules", authorization_rules)
        if baidu_credential is not None:
            pulumi.set(__self__, "baidu_credential", baidu_credential)
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

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The namespace name.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> Optional[pulumi.Input['AdmCredentialArgs']]:
        """
        The AdmCredential of the created NotificationHub
        """
        return pulumi.get(self, "adm_credential")

    @adm_credential.setter
    def adm_credential(self, value: Optional[pulumi.Input['AdmCredentialArgs']]):
        pulumi.set(self, "adm_credential", value)

    @property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> Optional[pulumi.Input['ApnsCredentialArgs']]:
        """
        The ApnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "apns_credential")

    @apns_credential.setter
    def apns_credential(self, value: Optional[pulumi.Input['ApnsCredentialArgs']]):
        pulumi.set(self, "apns_credential", value)

    @property
    @pulumi.getter(name="authorizationRules")
    def authorization_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs']]]]:
        """
        The AuthorizationRules of the created NotificationHub
        """
        return pulumi.get(self, "authorization_rules")

    @authorization_rules.setter
    def authorization_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs']]]]):
        pulumi.set(self, "authorization_rules", value)

    @property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> Optional[pulumi.Input['BaiduCredentialArgs']]:
        """
        The BaiduCredential of the created NotificationHub
        """
        return pulumi.get(self, "baidu_credential")

    @baidu_credential.setter
    def baidu_credential(self, value: Optional[pulumi.Input['BaiduCredentialArgs']]):
        pulumi.set(self, "baidu_credential", value)

    @property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> Optional[pulumi.Input['GcmCredentialArgs']]:
        """
        The GcmCredential of the created NotificationHub
        """
        return pulumi.get(self, "gcm_credential")

    @gcm_credential.setter
    def gcm_credential(self, value: Optional[pulumi.Input['GcmCredentialArgs']]):
        pulumi.set(self, "gcm_credential", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> Optional[pulumi.Input['MpnsCredentialArgs']]:
        """
        The MpnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "mpns_credential")

    @mpns_credential.setter
    def mpns_credential(self, value: Optional[pulumi.Input['MpnsCredentialArgs']]):
        pulumi.set(self, "mpns_credential", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The NotificationHub name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationHubName")
    def notification_hub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The notification hub name.
        """
        return pulumi.get(self, "notification_hub_name")

    @notification_hub_name.setter
    def notification_hub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_hub_name", value)

    @property
    @pulumi.getter(name="registrationTtl")
    def registration_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        The RegistrationTtl of the created NotificationHub
        """
        return pulumi.get(self, "registration_ttl")

    @registration_ttl.setter
    def registration_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registration_ttl", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> Optional[pulumi.Input['WnsCredentialArgs']]:
        """
        The WnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "wns_credential")

    @wns_credential.setter
    def wns_credential(self, value: Optional[pulumi.Input['WnsCredentialArgs']]):
        pulumi.set(self, "wns_credential", value)


class NotificationHub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adm_credential: Optional[pulumi.Input[pulumi.InputType['AdmCredentialArgs']]] = None,
                 apns_credential: Optional[pulumi.Input[pulumi.InputType['ApnsCredentialArgs']]] = None,
                 authorization_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SharedAccessAuthorizationRulePropertiesArgs']]]]] = None,
                 baidu_credential: Optional[pulumi.Input[pulumi.InputType['BaiduCredentialArgs']]] = None,
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
                 __props__=None):
        """
        Description of a NotificationHub Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AdmCredentialArgs']] adm_credential: The AdmCredential of the created NotificationHub
        :param pulumi.Input[pulumi.InputType['ApnsCredentialArgs']] apns_credential: The ApnsCredential of the created NotificationHub
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SharedAccessAuthorizationRulePropertiesArgs']]]] authorization_rules: The AuthorizationRules of the created NotificationHub
        :param pulumi.Input[pulumi.InputType['BaiduCredentialArgs']] baidu_credential: The BaiduCredential of the created NotificationHub
        :param pulumi.Input[pulumi.InputType['GcmCredentialArgs']] gcm_credential: The GcmCredential of the created NotificationHub
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['MpnsCredentialArgs']] mpns_credential: The MpnsCredential of the created NotificationHub
        :param pulumi.Input[str] name: The NotificationHub name.
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input[str] notification_hub_name: The notification hub name.
        :param pulumi.Input[str] registration_ttl: The RegistrationTtl of the created NotificationHub
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku of the created namespace
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[pulumi.InputType['WnsCredentialArgs']] wns_credential: The WnsCredential of the created NotificationHub
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationHubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of a NotificationHub Resource.

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
                 authorization_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SharedAccessAuthorizationRulePropertiesArgs']]]]] = None,
                 baidu_credential: Optional[pulumi.Input[pulumi.InputType['BaiduCredentialArgs']]] = None,
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
            __props__.__dict__["authorization_rules"] = authorization_rules
            __props__.__dict__["baidu_credential"] = baidu_credential
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
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:notificationhubs:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20140901:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20160301:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20230101preview:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20230901:NotificationHub"), pulumi.Alias(type_="azure-native:notificationhubs/v20231001preview:NotificationHub")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NotificationHub, __self__).__init__(
            'azure-native:notificationhubs/v20170401:NotificationHub',
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
        __props__.__dict__["gcm_credential"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mpns_credential"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["registration_ttl"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["wns_credential"] = None
        return NotificationHub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> pulumi.Output[Optional['outputs.AdmCredentialResponse']]:
        """
        The AdmCredential of the created NotificationHub
        """
        return pulumi.get(self, "adm_credential")

    @property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> pulumi.Output[Optional['outputs.ApnsCredentialResponse']]:
        """
        The ApnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "apns_credential")

    @property
    @pulumi.getter(name="authorizationRules")
    def authorization_rules(self) -> pulumi.Output[Optional[Sequence['outputs.SharedAccessAuthorizationRulePropertiesResponse']]]:
        """
        The AuthorizationRules of the created NotificationHub
        """
        return pulumi.get(self, "authorization_rules")

    @property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> pulumi.Output[Optional['outputs.BaiduCredentialResponse']]:
        """
        The BaiduCredential of the created NotificationHub
        """
        return pulumi.get(self, "baidu_credential")

    @property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> pulumi.Output[Optional['outputs.GcmCredentialResponse']]:
        """
        The GcmCredential of the created NotificationHub
        """
        return pulumi.get(self, "gcm_credential")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> pulumi.Output[Optional['outputs.MpnsCredentialResponse']]:
        """
        The MpnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "mpns_credential")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="registrationTtl")
    def registration_ttl(self) -> pulumi.Output[Optional[str]]:
        """
        The RegistrationTtl of the created NotificationHub
        """
        return pulumi.get(self, "registration_ttl")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> pulumi.Output[Optional['outputs.WnsCredentialResponse']]:
        """
        The WnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "wns_credential")

