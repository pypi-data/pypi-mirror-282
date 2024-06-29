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

__all__ = ['UpdateSummaryArgs', 'UpdateSummary']

@pulumi.input_type
class UpdateSummaryArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 current_version: Optional[pulumi.Input[str]] = None,
                 hardware_model: Optional[pulumi.Input[str]] = None,
                 health_check_date: Optional[pulumi.Input[str]] = None,
                 last_checked: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 oem_family: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UpdateSummariesPropertiesState']]] = None):
        """
        The set of arguments for constructing a UpdateSummary resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] current_version: Current Solution Bundle version of the stamp.
        :param pulumi.Input[str] hardware_model: Name of the hardware model.
        :param pulumi.Input[str] health_check_date: Last time the package-specific checks were run.
        :param pulumi.Input[str] last_checked: Last time the update service successfully checked for updates
        :param pulumi.Input[str] last_updated: Last time an update installation completed successfully.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] oem_family: OEM family name.
        :param pulumi.Input[Union[str, 'UpdateSummariesPropertiesState']] state: Overall update state of the stamp.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if current_version is not None:
            pulumi.set(__self__, "current_version", current_version)
        if hardware_model is not None:
            pulumi.set(__self__, "hardware_model", hardware_model)
        if health_check_date is not None:
            pulumi.set(__self__, "health_check_date", health_check_date)
        if last_checked is not None:
            pulumi.set(__self__, "last_checked", last_checked)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if oem_family is not None:
            pulumi.set(__self__, "oem_family", oem_family)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

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
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[pulumi.Input[str]]:
        """
        Current Solution Bundle version of the stamp.
        """
        return pulumi.get(self, "current_version")

    @current_version.setter
    def current_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "current_version", value)

    @property
    @pulumi.getter(name="hardwareModel")
    def hardware_model(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the hardware model.
        """
        return pulumi.get(self, "hardware_model")

    @hardware_model.setter
    def hardware_model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hardware_model", value)

    @property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> Optional[pulumi.Input[str]]:
        """
        Last time the package-specific checks were run.
        """
        return pulumi.get(self, "health_check_date")

    @health_check_date.setter
    def health_check_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_date", value)

    @property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> Optional[pulumi.Input[str]]:
        """
        Last time the update service successfully checked for updates
        """
        return pulumi.get(self, "last_checked")

    @last_checked.setter
    def last_checked(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_checked", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        """
        Last time an update installation completed successfully.
        """
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)

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
    @pulumi.getter(name="oemFamily")
    def oem_family(self) -> Optional[pulumi.Input[str]]:
        """
        OEM family name.
        """
        return pulumi.get(self, "oem_family")

    @oem_family.setter
    def oem_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oem_family", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'UpdateSummariesPropertiesState']]]:
        """
        Overall update state of the stamp.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'UpdateSummariesPropertiesState']]]):
        pulumi.set(self, "state", value)


class UpdateSummary(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 current_version: Optional[pulumi.Input[str]] = None,
                 hardware_model: Optional[pulumi.Input[str]] = None,
                 health_check_date: Optional[pulumi.Input[str]] = None,
                 last_checked: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 oem_family: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UpdateSummariesPropertiesState']]] = None,
                 __props__=None):
        """
        Get the update summaries for the cluster

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] current_version: Current Solution Bundle version of the stamp.
        :param pulumi.Input[str] hardware_model: Name of the hardware model.
        :param pulumi.Input[str] health_check_date: Last time the package-specific checks were run.
        :param pulumi.Input[str] last_checked: Last time the update service successfully checked for updates
        :param pulumi.Input[str] last_updated: Last time an update installation completed successfully.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] oem_family: OEM family name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'UpdateSummariesPropertiesState']] state: Overall update state of the stamp.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UpdateSummaryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Get the update summaries for the cluster

        :param str resource_name: The name of the resource.
        :param UpdateSummaryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UpdateSummaryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 current_version: Optional[pulumi.Input[str]] = None,
                 hardware_model: Optional[pulumi.Input[str]] = None,
                 health_check_date: Optional[pulumi.Input[str]] = None,
                 last_checked: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 oem_family: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UpdateSummariesPropertiesState']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UpdateSummaryArgs.__new__(UpdateSummaryArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["current_version"] = current_version
            __props__.__dict__["hardware_model"] = hardware_model
            __props__.__dict__["health_check_date"] = health_check_date
            __props__.__dict__["last_checked"] = last_checked
            __props__.__dict__["last_updated"] = last_updated
            __props__.__dict__["location"] = location
            __props__.__dict__["oem_family"] = oem_family
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["state"] = state
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20221201:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20230201:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20230301:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20230601:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20230801preview:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20231101preview:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20240215preview:UpdateSummary"), pulumi.Alias(type_="azure-native:azurestackhci/v20240401:UpdateSummary")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(UpdateSummary, __self__).__init__(
            'azure-native:azurestackhci/v20230801:UpdateSummary',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UpdateSummary':
        """
        Get an existing UpdateSummary resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UpdateSummaryArgs.__new__(UpdateSummaryArgs)

        __props__.__dict__["current_version"] = None
        __props__.__dict__["hardware_model"] = None
        __props__.__dict__["health_check_date"] = None
        __props__.__dict__["last_checked"] = None
        __props__.__dict__["last_updated"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["oem_family"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return UpdateSummary(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> pulumi.Output[Optional[str]]:
        """
        Current Solution Bundle version of the stamp.
        """
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter(name="hardwareModel")
    def hardware_model(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the hardware model.
        """
        return pulumi.get(self, "hardware_model")

    @property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> pulumi.Output[Optional[str]]:
        """
        Last time the package-specific checks were run.
        """
        return pulumi.get(self, "health_check_date")

    @property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> pulumi.Output[Optional[str]]:
        """
        Last time the update service successfully checked for updates
        """
        return pulumi.get(self, "last_checked")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[Optional[str]]:
        """
        Last time an update installation completed successfully.
        """
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oemFamily")
    def oem_family(self) -> pulumi.Output[Optional[str]]:
        """
        OEM family name.
        """
        return pulumi.get(self, "oem_family")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the UpdateSummaries proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Overall update state of the stamp.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

