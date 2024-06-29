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

__all__ = ['RosettaNetProcessConfigurationArgs', 'RosettaNetProcessConfiguration']

@pulumi.input_type
class RosettaNetProcessConfigurationArgs:
    def __init__(__self__, *,
                 activity_settings: pulumi.Input['RosettaNetPipActivitySettingsArgs'],
                 initiator_role_settings: pulumi.Input['RosettaNetPipRoleSettingsArgs'],
                 integration_account_name: pulumi.Input[str],
                 process_code: pulumi.Input[str],
                 process_name: pulumi.Input[str],
                 process_version: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 responder_role_settings: pulumi.Input['RosettaNetPipRoleSettingsArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 rosetta_net_process_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RosettaNetProcessConfiguration resource.
        :param pulumi.Input['RosettaNetPipActivitySettingsArgs'] activity_settings: The RosettaNet process configuration activity settings.
        :param pulumi.Input['RosettaNetPipRoleSettingsArgs'] initiator_role_settings: The RosettaNet initiator role settings.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] process_code: The integration account RosettaNet process code.
        :param pulumi.Input[str] process_name: The integration account RosettaNet process name.
        :param pulumi.Input[str] process_version: The integration account RosettaNet process version.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input['RosettaNetPipRoleSettingsArgs'] responder_role_settings: The RosettaNet responder role settings.
        :param pulumi.Input[str] description: The integration account RosettaNet ProcessConfiguration properties.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: The metadata.
        :param pulumi.Input[str] rosetta_net_process_configuration_name: The integration account RosettaNet ProcessConfiguration name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "activity_settings", activity_settings)
        pulumi.set(__self__, "initiator_role_settings", initiator_role_settings)
        pulumi.set(__self__, "integration_account_name", integration_account_name)
        pulumi.set(__self__, "process_code", process_code)
        pulumi.set(__self__, "process_name", process_name)
        pulumi.set(__self__, "process_version", process_version)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "responder_role_settings", responder_role_settings)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if rosetta_net_process_configuration_name is not None:
            pulumi.set(__self__, "rosetta_net_process_configuration_name", rosetta_net_process_configuration_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="activitySettings")
    def activity_settings(self) -> pulumi.Input['RosettaNetPipActivitySettingsArgs']:
        """
        The RosettaNet process configuration activity settings.
        """
        return pulumi.get(self, "activity_settings")

    @activity_settings.setter
    def activity_settings(self, value: pulumi.Input['RosettaNetPipActivitySettingsArgs']):
        pulumi.set(self, "activity_settings", value)

    @property
    @pulumi.getter(name="initiatorRoleSettings")
    def initiator_role_settings(self) -> pulumi.Input['RosettaNetPipRoleSettingsArgs']:
        """
        The RosettaNet initiator role settings.
        """
        return pulumi.get(self, "initiator_role_settings")

    @initiator_role_settings.setter
    def initiator_role_settings(self, value: pulumi.Input['RosettaNetPipRoleSettingsArgs']):
        pulumi.set(self, "initiator_role_settings", value)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[str]:
        """
        The integration account name.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="processCode")
    def process_code(self) -> pulumi.Input[str]:
        """
        The integration account RosettaNet process code.
        """
        return pulumi.get(self, "process_code")

    @process_code.setter
    def process_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "process_code", value)

    @property
    @pulumi.getter(name="processName")
    def process_name(self) -> pulumi.Input[str]:
        """
        The integration account RosettaNet process name.
        """
        return pulumi.get(self, "process_name")

    @process_name.setter
    def process_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "process_name", value)

    @property
    @pulumi.getter(name="processVersion")
    def process_version(self) -> pulumi.Input[str]:
        """
        The integration account RosettaNet process version.
        """
        return pulumi.get(self, "process_version")

    @process_version.setter
    def process_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "process_version", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="responderRoleSettings")
    def responder_role_settings(self) -> pulumi.Input['RosettaNetPipRoleSettingsArgs']:
        """
        The RosettaNet responder role settings.
        """
        return pulumi.get(self, "responder_role_settings")

    @responder_role_settings.setter
    def responder_role_settings(self, value: pulumi.Input['RosettaNetPipRoleSettingsArgs']):
        pulumi.set(self, "responder_role_settings", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The integration account RosettaNet ProcessConfiguration properties.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="rosettaNetProcessConfigurationName")
    def rosetta_net_process_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The integration account RosettaNet ProcessConfiguration name.
        """
        return pulumi.get(self, "rosetta_net_process_configuration_name")

    @rosetta_net_process_configuration_name.setter
    def rosetta_net_process_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rosetta_net_process_configuration_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class RosettaNetProcessConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activity_settings: Optional[pulumi.Input[pulumi.InputType['RosettaNetPipActivitySettingsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 initiator_role_settings: Optional[pulumi.Input[pulumi.InputType['RosettaNetPipRoleSettingsArgs']]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 process_code: Optional[pulumi.Input[str]] = None,
                 process_name: Optional[pulumi.Input[str]] = None,
                 process_version: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 responder_role_settings: Optional[pulumi.Input[pulumi.InputType['RosettaNetPipRoleSettingsArgs']]] = None,
                 rosetta_net_process_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The integration account RosettaNet process configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RosettaNetPipActivitySettingsArgs']] activity_settings: The RosettaNet process configuration activity settings.
        :param pulumi.Input[str] description: The integration account RosettaNet ProcessConfiguration properties.
        :param pulumi.Input[pulumi.InputType['RosettaNetPipRoleSettingsArgs']] initiator_role_settings: The RosettaNet initiator role settings.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: The metadata.
        :param pulumi.Input[str] process_code: The integration account RosettaNet process code.
        :param pulumi.Input[str] process_name: The integration account RosettaNet process name.
        :param pulumi.Input[str] process_version: The integration account RosettaNet process version.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[pulumi.InputType['RosettaNetPipRoleSettingsArgs']] responder_role_settings: The RosettaNet responder role settings.
        :param pulumi.Input[str] rosetta_net_process_configuration_name: The integration account RosettaNet ProcessConfiguration name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RosettaNetProcessConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The integration account RosettaNet process configuration.

        :param str resource_name: The name of the resource.
        :param RosettaNetProcessConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RosettaNetProcessConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activity_settings: Optional[pulumi.Input[pulumi.InputType['RosettaNetPipActivitySettingsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 initiator_role_settings: Optional[pulumi.Input[pulumi.InputType['RosettaNetPipRoleSettingsArgs']]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 process_code: Optional[pulumi.Input[str]] = None,
                 process_name: Optional[pulumi.Input[str]] = None,
                 process_version: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 responder_role_settings: Optional[pulumi.Input[pulumi.InputType['RosettaNetPipRoleSettingsArgs']]] = None,
                 rosetta_net_process_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RosettaNetProcessConfigurationArgs.__new__(RosettaNetProcessConfigurationArgs)

            if activity_settings is None and not opts.urn:
                raise TypeError("Missing required property 'activity_settings'")
            __props__.__dict__["activity_settings"] = activity_settings
            __props__.__dict__["description"] = description
            if initiator_role_settings is None and not opts.urn:
                raise TypeError("Missing required property 'initiator_role_settings'")
            __props__.__dict__["initiator_role_settings"] = initiator_role_settings
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            if process_code is None and not opts.urn:
                raise TypeError("Missing required property 'process_code'")
            __props__.__dict__["process_code"] = process_code
            if process_name is None and not opts.urn:
                raise TypeError("Missing required property 'process_name'")
            __props__.__dict__["process_name"] = process_name
            if process_version is None and not opts.urn:
                raise TypeError("Missing required property 'process_version'")
            __props__.__dict__["process_version"] = process_version
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if responder_role_settings is None and not opts.urn:
                raise TypeError("Missing required property 'responder_role_settings'")
            __props__.__dict__["responder_role_settings"] = responder_role_settings
            __props__.__dict__["rosetta_net_process_configuration_name"] = rosetta_net_process_configuration_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["changed_time"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic:RosettaNetProcessConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RosettaNetProcessConfiguration, __self__).__init__(
            'azure-native:logic/v20160601:RosettaNetProcessConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RosettaNetProcessConfiguration':
        """
        Get an existing RosettaNetProcessConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RosettaNetProcessConfigurationArgs.__new__(RosettaNetProcessConfigurationArgs)

        __props__.__dict__["activity_settings"] = None
        __props__.__dict__["changed_time"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["initiator_role_settings"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["process_code"] = None
        __props__.__dict__["process_name"] = None
        __props__.__dict__["process_version"] = None
        __props__.__dict__["responder_role_settings"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return RosettaNetProcessConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activitySettings")
    def activity_settings(self) -> pulumi.Output['outputs.RosettaNetPipActivitySettingsResponse']:
        """
        The RosettaNet process configuration activity settings.
        """
        return pulumi.get(self, "activity_settings")

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[str]:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The integration account RosettaNet ProcessConfiguration properties.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="initiatorRoleSettings")
    def initiator_role_settings(self) -> pulumi.Output['outputs.RosettaNetPipRoleSettingsResponse']:
        """
        The RosettaNet initiator role settings.
        """
        return pulumi.get(self, "initiator_role_settings")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="processCode")
    def process_code(self) -> pulumi.Output[str]:
        """
        The integration account RosettaNet process code.
        """
        return pulumi.get(self, "process_code")

    @property
    @pulumi.getter(name="processName")
    def process_name(self) -> pulumi.Output[str]:
        """
        The integration account RosettaNet process name.
        """
        return pulumi.get(self, "process_name")

    @property
    @pulumi.getter(name="processVersion")
    def process_version(self) -> pulumi.Output[str]:
        """
        The integration account RosettaNet process version.
        """
        return pulumi.get(self, "process_version")

    @property
    @pulumi.getter(name="responderRoleSettings")
    def responder_role_settings(self) -> pulumi.Output['outputs.RosettaNetPipRoleSettingsResponse']:
        """
        The RosettaNet responder role settings.
        """
        return pulumi.get(self, "responder_role_settings")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

