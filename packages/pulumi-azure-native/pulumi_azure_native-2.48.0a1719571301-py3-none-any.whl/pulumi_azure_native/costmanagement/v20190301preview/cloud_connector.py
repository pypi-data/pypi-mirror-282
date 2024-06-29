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

__all__ = ['CloudConnectorArgs', 'CloudConnector']

@pulumi.input_type
class CloudConnectorArgs:
    def __init__(__self__, *,
                 billing_model: Optional[pulumi.Input[Union[str, 'ConnectorBillingModel']]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 credentials_key: Optional[pulumi.Input[str]] = None,
                 credentials_secret: Optional[pulumi.Input[str]] = None,
                 default_management_group_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 report_id: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CloudConnector resource.
        :param pulumi.Input[Union[str, 'ConnectorBillingModel']] billing_model: Connector billing model
        :param pulumi.Input[str] connector_name: Connector Name.
        :param pulumi.Input[str] credentials_key: Credentials authentication key (eg AWS ARN)
        :param pulumi.Input[str] credentials_secret: Credentials secret (eg AWS ExternalId)
        :param pulumi.Input[str] default_management_group_id: Default ManagementGroupId
        :param pulumi.Input[str] display_name: Connector DisplayName
        :param pulumi.Input[str] kind: Connector kind (eg aws)
        :param pulumi.Input[str] report_id: Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources)
        :param pulumi.Input[str] subscription_id: Billing SubscriptionId
        """
        if billing_model is not None:
            pulumi.set(__self__, "billing_model", billing_model)
        if connector_name is not None:
            pulumi.set(__self__, "connector_name", connector_name)
        if credentials_key is not None:
            pulumi.set(__self__, "credentials_key", credentials_key)
        if credentials_secret is not None:
            pulumi.set(__self__, "credentials_secret", credentials_secret)
        if default_management_group_id is not None:
            pulumi.set(__self__, "default_management_group_id", default_management_group_id)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if report_id is not None:
            pulumi.set(__self__, "report_id", report_id)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> Optional[pulumi.Input[Union[str, 'ConnectorBillingModel']]]:
        """
        Connector billing model
        """
        return pulumi.get(self, "billing_model")

    @billing_model.setter
    def billing_model(self, value: Optional[pulumi.Input[Union[str, 'ConnectorBillingModel']]]):
        pulumi.set(self, "billing_model", value)

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[str]]:
        """
        Connector Name.
        """
        return pulumi.get(self, "connector_name")

    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_name", value)

    @property
    @pulumi.getter(name="credentialsKey")
    def credentials_key(self) -> Optional[pulumi.Input[str]]:
        """
        Credentials authentication key (eg AWS ARN)
        """
        return pulumi.get(self, "credentials_key")

    @credentials_key.setter
    def credentials_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credentials_key", value)

    @property
    @pulumi.getter(name="credentialsSecret")
    def credentials_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Credentials secret (eg AWS ExternalId)
        """
        return pulumi.get(self, "credentials_secret")

    @credentials_secret.setter
    def credentials_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credentials_secret", value)

    @property
    @pulumi.getter(name="defaultManagementGroupId")
    def default_management_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Default ManagementGroupId
        """
        return pulumi.get(self, "default_management_group_id")

    @default_management_group_id.setter
    def default_management_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_management_group_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Connector DisplayName
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Connector kind (eg aws)
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="reportId")
    def report_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources)
        """
        return pulumi.get(self, "report_id")

    @report_id.setter
    def report_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "report_id", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        Billing SubscriptionId
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)


class CloudConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_model: Optional[pulumi.Input[Union[str, 'ConnectorBillingModel']]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 credentials_key: Optional[pulumi.Input[str]] = None,
                 credentials_secret: Optional[pulumi.Input[str]] = None,
                 default_management_group_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 report_id: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Connector model definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'ConnectorBillingModel']] billing_model: Connector billing model
        :param pulumi.Input[str] connector_name: Connector Name.
        :param pulumi.Input[str] credentials_key: Credentials authentication key (eg AWS ARN)
        :param pulumi.Input[str] credentials_secret: Credentials secret (eg AWS ExternalId)
        :param pulumi.Input[str] default_management_group_id: Default ManagementGroupId
        :param pulumi.Input[str] display_name: Connector DisplayName
        :param pulumi.Input[str] kind: Connector kind (eg aws)
        :param pulumi.Input[str] report_id: Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources)
        :param pulumi.Input[str] subscription_id: Billing SubscriptionId
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CloudConnectorArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Connector model definition

        :param str resource_name: The name of the resource.
        :param CloudConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_model: Optional[pulumi.Input[Union[str, 'ConnectorBillingModel']]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 credentials_key: Optional[pulumi.Input[str]] = None,
                 credentials_secret: Optional[pulumi.Input[str]] = None,
                 default_management_group_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 report_id: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudConnectorArgs.__new__(CloudConnectorArgs)

            __props__.__dict__["billing_model"] = billing_model
            __props__.__dict__["connector_name"] = connector_name
            __props__.__dict__["credentials_key"] = credentials_key
            __props__.__dict__["credentials_secret"] = credentials_secret
            __props__.__dict__["default_management_group_id"] = default_management_group_id
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["kind"] = kind
            __props__.__dict__["report_id"] = report_id
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["collection_info"] = None
            __props__.__dict__["created_on"] = None
            __props__.__dict__["days_trial_remaining"] = None
            __props__.__dict__["external_billing_account_id"] = None
            __props__.__dict__["modified_on"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provider_billing_account_display_name"] = None
            __props__.__dict__["provider_billing_account_id"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:CloudConnector"), pulumi.Alias(type_="azure-native:costmanagement/v20180801preview:CloudConnector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CloudConnector, __self__).__init__(
            'azure-native:costmanagement/v20190301preview:CloudConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CloudConnector':
        """
        Get an existing CloudConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CloudConnectorArgs.__new__(CloudConnectorArgs)

        __props__.__dict__["billing_model"] = None
        __props__.__dict__["collection_info"] = None
        __props__.__dict__["created_on"] = None
        __props__.__dict__["credentials_key"] = None
        __props__.__dict__["days_trial_remaining"] = None
        __props__.__dict__["default_management_group_id"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["external_billing_account_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["modified_on"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provider_billing_account_display_name"] = None
        __props__.__dict__["provider_billing_account_id"] = None
        __props__.__dict__["report_id"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subscription_id"] = None
        __props__.__dict__["type"] = None
        return CloudConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> pulumi.Output[Optional[str]]:
        """
        Connector billing model
        """
        return pulumi.get(self, "billing_model")

    @property
    @pulumi.getter(name="collectionInfo")
    def collection_info(self) -> pulumi.Output['outputs.ConnectorCollectionInfoResponse']:
        """
        Collection information
        """
        return pulumi.get(self, "collection_info")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        Connector definition creation datetime
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="credentialsKey")
    def credentials_key(self) -> pulumi.Output[Optional[str]]:
        """
        Credentials authentication key (eg AWS ARN)
        """
        return pulumi.get(self, "credentials_key")

    @property
    @pulumi.getter(name="daysTrialRemaining")
    def days_trial_remaining(self) -> pulumi.Output[int]:
        """
        Number of days remaining of trial
        """
        return pulumi.get(self, "days_trial_remaining")

    @property
    @pulumi.getter(name="defaultManagementGroupId")
    def default_management_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        Default ManagementGroupId
        """
        return pulumi.get(self, "default_management_group_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Connector DisplayName
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalBillingAccountId")
    def external_billing_account_id(self) -> pulumi.Output[str]:
        """
        Associated ExternalBillingAccountId
        """
        return pulumi.get(self, "external_billing_account_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Connector kind (eg aws)
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> pulumi.Output[str]:
        """
        Connector last modified datetime
        """
        return pulumi.get(self, "modified_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Connector name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerBillingAccountDisplayName")
    def provider_billing_account_display_name(self) -> pulumi.Output[str]:
        """
        The display name of the providerBillingAccountId as defined on the external provider
        """
        return pulumi.get(self, "provider_billing_account_display_name")

    @property
    @pulumi.getter(name="providerBillingAccountId")
    def provider_billing_account_id(self) -> pulumi.Output[str]:
        """
        Connector providerBillingAccountId, determined from credentials (eg AWS Consolidated account number)
        """
        return pulumi.get(self, "provider_billing_account_id")

    @property
    @pulumi.getter(name="reportId")
    def report_id(self) -> pulumi.Output[Optional[str]]:
        """
        Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources)
        """
        return pulumi.get(self, "report_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Connector status
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[Optional[str]]:
        """
        Billing SubscriptionId
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Connector type
        """
        return pulumi.get(self, "type")

