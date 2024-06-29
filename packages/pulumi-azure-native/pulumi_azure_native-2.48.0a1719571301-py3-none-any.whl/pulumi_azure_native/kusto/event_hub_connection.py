# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['EventHubConnectionArgs', 'EventHubConnection']

@pulumi.input_type
class EventHubConnectionArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 consumer_group: pulumi.Input[str],
                 database_name: pulumi.Input[str],
                 event_hub_resource_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 data_format: Optional[pulumi.Input[Union[str, 'DataFormat']]] = None,
                 event_hub_connection_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EventHubConnection resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] consumer_group: The event hub consumer group.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto cluster.
        :param pulumi.Input[str] event_hub_resource_id: The resource ID of the event hub to be used to create a data connection.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[Union[str, 'DataFormat']] data_format: The data format of the message. Optionally the data format can be added to each message.
        :param pulumi.Input[str] event_hub_connection_name: The name of the event hub connection.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mapping_rule_name: The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        :param pulumi.Input[str] table_name: The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "consumer_group", consumer_group)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "event_hub_resource_id", event_hub_resource_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_format is not None:
            pulumi.set(__self__, "data_format", data_format)
        if event_hub_connection_name is not None:
            pulumi.set(__self__, "event_hub_connection_name", event_hub_connection_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mapping_rule_name is not None:
            pulumi.set(__self__, "mapping_rule_name", mapping_rule_name)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Input[str]:
        """
        The event hub consumer group.
        """
        return pulumi.get(self, "consumer_group")

    @consumer_group.setter
    def consumer_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "consumer_group", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database in the Kusto cluster.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the event hub to be used to create a data connection.
        """
        return pulumi.get(self, "event_hub_resource_id")

    @event_hub_resource_id.setter
    def event_hub_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_hub_resource_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the Kusto cluster.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[Union[str, 'DataFormat']]]:
        """
        The data format of the message. Optionally the data format can be added to each message.
        """
        return pulumi.get(self, "data_format")

    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[Union[str, 'DataFormat']]]):
        pulumi.set(self, "data_format", value)

    @property
    @pulumi.getter(name="eventHubConnectionName")
    def event_hub_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the event hub connection.
        """
        return pulumi.get(self, "event_hub_connection_name")

    @event_hub_connection_name.setter
    def event_hub_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_hub_connection_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        """
        return pulumi.get(self, "mapping_rule_name")

    @mapping_rule_name.setter
    def mapping_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mapping_rule_name", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)


class EventHubConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 consumer_group: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'DataFormat']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 event_hub_connection_name: Optional[pulumi.Input[str]] = None,
                 event_hub_resource_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing an event hub connection.
        Azure REST API version: 2018-09-07-preview. Prior API version in Azure Native 1.x: 2018-09-07-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] consumer_group: The event hub consumer group.
        :param pulumi.Input[Union[str, 'DataFormat']] data_format: The data format of the message. Optionally the data format can be added to each message.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto cluster.
        :param pulumi.Input[str] event_hub_connection_name: The name of the event hub connection.
        :param pulumi.Input[str] event_hub_resource_id: The resource ID of the event hub to be used to create a data connection.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mapping_rule_name: The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[str] table_name: The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventHubConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing an event hub connection.
        Azure REST API version: 2018-09-07-preview. Prior API version in Azure Native 1.x: 2018-09-07-preview.

        :param str resource_name: The name of the resource.
        :param EventHubConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventHubConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 consumer_group: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'DataFormat']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 event_hub_connection_name: Optional[pulumi.Input[str]] = None,
                 event_hub_resource_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventHubConnectionArgs.__new__(EventHubConnectionArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if consumer_group is None and not opts.urn:
                raise TypeError("Missing required property 'consumer_group'")
            __props__.__dict__["consumer_group"] = consumer_group
            __props__.__dict__["data_format"] = data_format
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["event_hub_connection_name"] = event_hub_connection_name
            if event_hub_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'event_hub_resource_id'")
            __props__.__dict__["event_hub_resource_id"] = event_hub_resource_id
            __props__.__dict__["location"] = location
            __props__.__dict__["mapping_rule_name"] = mapping_rule_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kusto/v20170907privatepreview:EventHubConnection"), pulumi.Alias(type_="azure-native:kusto/v20180907preview:EventHubConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EventHubConnection, __self__).__init__(
            'azure-native:kusto:EventHubConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventHubConnection':
        """
        Get an existing EventHubConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventHubConnectionArgs.__new__(EventHubConnectionArgs)

        __props__.__dict__["consumer_group"] = None
        __props__.__dict__["data_format"] = None
        __props__.__dict__["event_hub_resource_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mapping_rule_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["type"] = None
        return EventHubConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Output[str]:
        """
        The event hub consumer group.
        """
        return pulumi.get(self, "consumer_group")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[Optional[str]]:
        """
        The data format of the message. Optionally the data format can be added to each message.
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the event hub to be used to create a data connection.
        """
        return pulumi.get(self, "event_hub_resource_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        """
        return pulumi.get(self, "mapping_rule_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[str]]:
        """
        The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

