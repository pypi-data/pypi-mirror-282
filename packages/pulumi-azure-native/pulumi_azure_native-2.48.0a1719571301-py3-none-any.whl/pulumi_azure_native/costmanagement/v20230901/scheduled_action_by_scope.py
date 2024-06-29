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

__all__ = ['ScheduledActionByScopeArgs', 'ScheduledActionByScope']

@pulumi.input_type
class ScheduledActionByScopeArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 notification: pulumi.Input['NotificationPropertiesArgs'],
                 schedule: pulumi.Input['SchedulePropertiesArgs'],
                 scope: pulumi.Input[str],
                 status: pulumi.Input[Union[str, 'ScheduledActionStatus']],
                 view_id: pulumi.Input[str],
                 file_destination: Optional[pulumi.Input['FileDestinationArgs']] = None,
                 kind: Optional[pulumi.Input[Union[str, 'ScheduledActionKind']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_email: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScheduledActionByScope resource.
        :param pulumi.Input[str] display_name: Scheduled action name.
        :param pulumi.Input['NotificationPropertiesArgs'] notification: Notification properties based on scheduled action kind.
        :param pulumi.Input['SchedulePropertiesArgs'] schedule: Schedule of the scheduled action.
        :param pulumi.Input[str] scope: For private scheduled action(Create or Update), scope will be empty.<br /> For shared scheduled action(Create or Update By Scope), Cost Management scope can be 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        :param pulumi.Input[Union[str, 'ScheduledActionStatus']] status: Status of the scheduled action.
        :param pulumi.Input[str] view_id: Cost analysis viewId used for scheduled action. For example, '/providers/Microsoft.CostManagement/views/swaggerExample'
        :param pulumi.Input['FileDestinationArgs'] file_destination: Destination format of the view data. This is optional.
        :param pulumi.Input[Union[str, 'ScheduledActionKind']] kind: Kind of the scheduled action.
        :param pulumi.Input[str] name: Scheduled action name.
        :param pulumi.Input[str] notification_email: Email address of the point of contact that should get the unsubscribe requests and notification emails.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "notification", notification)
        pulumi.set(__self__, "schedule", schedule)
        pulumi.set(__self__, "scope", scope)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "view_id", view_id)
        if file_destination is not None:
            pulumi.set(__self__, "file_destination", file_destination)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_email is not None:
            pulumi.set(__self__, "notification_email", notification_email)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Scheduled action name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def notification(self) -> pulumi.Input['NotificationPropertiesArgs']:
        """
        Notification properties based on scheduled action kind.
        """
        return pulumi.get(self, "notification")

    @notification.setter
    def notification(self, value: pulumi.Input['NotificationPropertiesArgs']):
        pulumi.set(self, "notification", value)

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Input['SchedulePropertiesArgs']:
        """
        Schedule of the scheduled action.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: pulumi.Input['SchedulePropertiesArgs']):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        For private scheduled action(Create or Update), scope will be empty.<br /> For shared scheduled action(Create or Update By Scope), Cost Management scope can be 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[str, 'ScheduledActionStatus']]:
        """
        Status of the scheduled action.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[Union[str, 'ScheduledActionStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> pulumi.Input[str]:
        """
        Cost analysis viewId used for scheduled action. For example, '/providers/Microsoft.CostManagement/views/swaggerExample'
        """
        return pulumi.get(self, "view_id")

    @view_id.setter
    def view_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "view_id", value)

    @property
    @pulumi.getter(name="fileDestination")
    def file_destination(self) -> Optional[pulumi.Input['FileDestinationArgs']]:
        """
        Destination format of the view data. This is optional.
        """
        return pulumi.get(self, "file_destination")

    @file_destination.setter
    def file_destination(self, value: Optional[pulumi.Input['FileDestinationArgs']]):
        pulumi.set(self, "file_destination", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'ScheduledActionKind']]]:
        """
        Kind of the scheduled action.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'ScheduledActionKind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Scheduled action name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the point of contact that should get the unsubscribe requests and notification emails.
        """
        return pulumi.get(self, "notification_email")

    @notification_email.setter
    def notification_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_email", value)


class ScheduledActionByScope(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 file_destination: Optional[pulumi.Input[pulumi.InputType['FileDestinationArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'ScheduledActionKind']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification: Optional[pulumi.Input[pulumi.InputType['NotificationPropertiesArgs']]] = None,
                 notification_email: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['SchedulePropertiesArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'ScheduledActionStatus']]] = None,
                 view_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Scheduled action definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Scheduled action name.
        :param pulumi.Input[pulumi.InputType['FileDestinationArgs']] file_destination: Destination format of the view data. This is optional.
        :param pulumi.Input[Union[str, 'ScheduledActionKind']] kind: Kind of the scheduled action.
        :param pulumi.Input[str] name: Scheduled action name.
        :param pulumi.Input[pulumi.InputType['NotificationPropertiesArgs']] notification: Notification properties based on scheduled action kind.
        :param pulumi.Input[str] notification_email: Email address of the point of contact that should get the unsubscribe requests and notification emails.
        :param pulumi.Input[pulumi.InputType['SchedulePropertiesArgs']] schedule: Schedule of the scheduled action.
        :param pulumi.Input[str] scope: For private scheduled action(Create or Update), scope will be empty.<br /> For shared scheduled action(Create or Update By Scope), Cost Management scope can be 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        :param pulumi.Input[Union[str, 'ScheduledActionStatus']] status: Status of the scheduled action.
        :param pulumi.Input[str] view_id: Cost analysis viewId used for scheduled action. For example, '/providers/Microsoft.CostManagement/views/swaggerExample'
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduledActionByScopeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Scheduled action definition.

        :param str resource_name: The name of the resource.
        :param ScheduledActionByScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduledActionByScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 file_destination: Optional[pulumi.Input[pulumi.InputType['FileDestinationArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'ScheduledActionKind']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification: Optional[pulumi.Input[pulumi.InputType['NotificationPropertiesArgs']]] = None,
                 notification_email: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['SchedulePropertiesArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'ScheduledActionStatus']]] = None,
                 view_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduledActionByScopeArgs.__new__(ScheduledActionByScopeArgs)

            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["file_destination"] = file_destination
            __props__.__dict__["kind"] = kind
            __props__.__dict__["name"] = name
            if notification is None and not opts.urn:
                raise TypeError("Missing required property 'notification'")
            __props__.__dict__["notification"] = notification
            __props__.__dict__["notification_email"] = notification_email
            if schedule is None and not opts.urn:
                raise TypeError("Missing required property 'schedule'")
            __props__.__dict__["schedule"] = schedule
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            if view_id is None and not opts.urn:
                raise TypeError("Missing required property 'view_id'")
            __props__.__dict__["view_id"] = view_id
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20220401preview:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20220601preview:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20221001:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230301:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230401preview:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230701preview:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230801:ScheduledActionByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20231101:ScheduledActionByScope")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScheduledActionByScope, __self__).__init__(
            'azure-native:costmanagement/v20230901:ScheduledActionByScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScheduledActionByScope':
        """
        Get an existing ScheduledActionByScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduledActionByScopeArgs.__new__(ScheduledActionByScopeArgs)

        __props__.__dict__["display_name"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["file_destination"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification"] = None
        __props__.__dict__["notification_email"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["view_id"] = None
        return ScheduledActionByScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Scheduled action name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        Resource Etag. For update calls, eTag is optional and can be specified to achieve optimistic concurrency. Fetch the resource's eTag by doing a 'GET' call first and then including the latest eTag as part of the request body or 'If-Match' header while performing the update. For create calls, eTag is not required.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="fileDestination")
    def file_destination(self) -> pulumi.Output[Optional['outputs.FileDestinationResponse']]:
        """
        Destination format of the view data. This is optional.
        """
        return pulumi.get(self, "file_destination")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of the scheduled action.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notification(self) -> pulumi.Output['outputs.NotificationPropertiesResponse']:
        """
        Notification properties based on scheduled action kind.
        """
        return pulumi.get(self, "notification")

    @property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> pulumi.Output[Optional[str]]:
        """
        Email address of the point of contact that should get the unsubscribe requests and notification emails.
        """
        return pulumi.get(self, "notification_email")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output['outputs.SchedulePropertiesResponse']:
        """
        Schedule of the scheduled action.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        For private scheduled action(Create or Update), scope will be empty.<br /> For shared scheduled action(Create or Update By Scope), Cost Management scope can be 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the scheduled action.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Kind of the scheduled action.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> pulumi.Output[str]:
        """
        Cost analysis viewId used for scheduled action. For example, '/providers/Microsoft.CostManagement/views/swaggerExample'
        """
        return pulumi.get(self, "view_id")

