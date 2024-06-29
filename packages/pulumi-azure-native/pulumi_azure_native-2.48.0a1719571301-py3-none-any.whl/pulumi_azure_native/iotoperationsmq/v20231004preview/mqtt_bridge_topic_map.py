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

__all__ = ['MqttBridgeTopicMapArgs', 'MqttBridgeTopicMap']

@pulumi.input_type
class MqttBridgeTopicMapArgs:
    def __init__(__self__, *,
                 extended_location: pulumi.Input['ExtendedLocationPropertyArgs'],
                 mq_name: pulumi.Input[str],
                 mqtt_bridge_connector_name: pulumi.Input[str],
                 mqtt_bridge_connector_ref: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input['MqttBridgeRoutesArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_map_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MqttBridgeTopicMap resource.
        :param pulumi.Input['ExtendedLocationPropertyArgs'] extended_location: Extended Location
        :param pulumi.Input[str] mq_name: Name of MQ resource
        :param pulumi.Input[str] mqtt_bridge_connector_name: Name of MQ mqttBridgeConnector resource
        :param pulumi.Input[str] mqtt_bridge_connector_ref: The MqttBridgeConnector CRD it refers to.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input['MqttBridgeRoutesArgs']]] routes: The route details for MqttBridge connector.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] topic_map_name: Name of MQ mqttBridgeTopicMap resource
        """
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "mq_name", mq_name)
        pulumi.set(__self__, "mqtt_bridge_connector_name", mqtt_bridge_connector_name)
        pulumi.set(__self__, "mqtt_bridge_connector_ref", mqtt_bridge_connector_ref)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if routes is not None:
            pulumi.set(__self__, "routes", routes)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if topic_map_name is not None:
            pulumi.set(__self__, "topic_map_name", topic_map_name)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationPropertyArgs']:
        """
        Extended Location
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationPropertyArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="mqName")
    def mq_name(self) -> pulumi.Input[str]:
        """
        Name of MQ resource
        """
        return pulumi.get(self, "mq_name")

    @mq_name.setter
    def mq_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mq_name", value)

    @property
    @pulumi.getter(name="mqttBridgeConnectorName")
    def mqtt_bridge_connector_name(self) -> pulumi.Input[str]:
        """
        Name of MQ mqttBridgeConnector resource
        """
        return pulumi.get(self, "mqtt_bridge_connector_name")

    @mqtt_bridge_connector_name.setter
    def mqtt_bridge_connector_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mqtt_bridge_connector_name", value)

    @property
    @pulumi.getter(name="mqttBridgeConnectorRef")
    def mqtt_bridge_connector_ref(self) -> pulumi.Input[str]:
        """
        The MqttBridgeConnector CRD it refers to.
        """
        return pulumi.get(self, "mqtt_bridge_connector_ref")

    @mqtt_bridge_connector_ref.setter
    def mqtt_bridge_connector_ref(self, value: pulumi.Input[str]):
        pulumi.set(self, "mqtt_bridge_connector_ref", value)

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
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MqttBridgeRoutesArgs']]]]:
        """
        The route details for MqttBridge connector.
        """
        return pulumi.get(self, "routes")

    @routes.setter
    def routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MqttBridgeRoutesArgs']]]]):
        pulumi.set(self, "routes", value)

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
    @pulumi.getter(name="topicMapName")
    def topic_map_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of MQ mqttBridgeTopicMap resource
        """
        return pulumi.get(self, "topic_map_name")

    @topic_map_name.setter
    def topic_map_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_map_name", value)


class MqttBridgeTopicMap(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationPropertyArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mq_name: Optional[pulumi.Input[str]] = None,
                 mqtt_bridge_connector_name: Optional[pulumi.Input[str]] = None,
                 mqtt_bridge_connector_ref: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MqttBridgeRoutesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_map_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        MQ mqttBridgeTopicMap resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationPropertyArgs']] extended_location: Extended Location
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mq_name: Name of MQ resource
        :param pulumi.Input[str] mqtt_bridge_connector_name: Name of MQ mqttBridgeConnector resource
        :param pulumi.Input[str] mqtt_bridge_connector_ref: The MqttBridgeConnector CRD it refers to.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MqttBridgeRoutesArgs']]]] routes: The route details for MqttBridge connector.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] topic_map_name: Name of MQ mqttBridgeTopicMap resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MqttBridgeTopicMapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        MQ mqttBridgeTopicMap resource

        :param str resource_name: The name of the resource.
        :param MqttBridgeTopicMapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MqttBridgeTopicMapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationPropertyArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mq_name: Optional[pulumi.Input[str]] = None,
                 mqtt_bridge_connector_name: Optional[pulumi.Input[str]] = None,
                 mqtt_bridge_connector_ref: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MqttBridgeRoutesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_map_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MqttBridgeTopicMapArgs.__new__(MqttBridgeTopicMapArgs)

            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            if mq_name is None and not opts.urn:
                raise TypeError("Missing required property 'mq_name'")
            __props__.__dict__["mq_name"] = mq_name
            if mqtt_bridge_connector_name is None and not opts.urn:
                raise TypeError("Missing required property 'mqtt_bridge_connector_name'")
            __props__.__dict__["mqtt_bridge_connector_name"] = mqtt_bridge_connector_name
            if mqtt_bridge_connector_ref is None and not opts.urn:
                raise TypeError("Missing required property 'mqtt_bridge_connector_ref'")
            __props__.__dict__["mqtt_bridge_connector_ref"] = mqtt_bridge_connector_ref
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["routes"] = routes
            __props__.__dict__["tags"] = tags
            __props__.__dict__["topic_map_name"] = topic_map_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:iotoperationsmq:MqttBridgeTopicMap")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MqttBridgeTopicMap, __self__).__init__(
            'azure-native:iotoperationsmq/v20231004preview:MqttBridgeTopicMap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MqttBridgeTopicMap':
        """
        Get an existing MqttBridgeTopicMap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MqttBridgeTopicMapArgs.__new__(MqttBridgeTopicMapArgs)

        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mqtt_bridge_connector_ref"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["routes"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return MqttBridgeTopicMap(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationPropertyResponse']:
        """
        Extended Location
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mqttBridgeConnectorRef")
    def mqtt_bridge_connector_ref(self) -> pulumi.Output[str]:
        """
        The MqttBridgeConnector CRD it refers to.
        """
        return pulumi.get(self, "mqtt_bridge_connector_ref")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Optional[Sequence['outputs.MqttBridgeRoutesResponse']]]:
        """
        The route details for MqttBridge connector.
        """
        return pulumi.get(self, "routes")

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

