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
    'GetKafkaConfigurationResult',
    'AwaitableGetKafkaConfigurationResult',
    'get_kafka_configuration',
    'get_kafka_configuration_output',
]

@pulumi.output_type
class GetKafkaConfigurationResult:
    """
    The configuration of the event streaming service resource attached to the Purview account for kafka notifications.
    """
    def __init__(__self__, consumer_group=None, credentials=None, event_hub_partition_id=None, event_hub_resource_id=None, event_hub_type=None, event_streaming_state=None, event_streaming_type=None, id=None, name=None, system_data=None, type=None):
        if consumer_group and not isinstance(consumer_group, str):
            raise TypeError("Expected argument 'consumer_group' to be a str")
        pulumi.set(__self__, "consumer_group", consumer_group)
        if credentials and not isinstance(credentials, dict):
            raise TypeError("Expected argument 'credentials' to be a dict")
        pulumi.set(__self__, "credentials", credentials)
        if event_hub_partition_id and not isinstance(event_hub_partition_id, str):
            raise TypeError("Expected argument 'event_hub_partition_id' to be a str")
        pulumi.set(__self__, "event_hub_partition_id", event_hub_partition_id)
        if event_hub_resource_id and not isinstance(event_hub_resource_id, str):
            raise TypeError("Expected argument 'event_hub_resource_id' to be a str")
        pulumi.set(__self__, "event_hub_resource_id", event_hub_resource_id)
        if event_hub_type and not isinstance(event_hub_type, str):
            raise TypeError("Expected argument 'event_hub_type' to be a str")
        pulumi.set(__self__, "event_hub_type", event_hub_type)
        if event_streaming_state and not isinstance(event_streaming_state, str):
            raise TypeError("Expected argument 'event_streaming_state' to be a str")
        pulumi.set(__self__, "event_streaming_state", event_streaming_state)
        if event_streaming_type and not isinstance(event_streaming_type, str):
            raise TypeError("Expected argument 'event_streaming_type' to be a str")
        pulumi.set(__self__, "event_streaming_type", event_streaming_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[str]:
        """
        Consumer group for hook event hub.
        """
        return pulumi.get(self, "consumer_group")

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.CredentialsResponse']:
        """
        Credentials to access event hub.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="eventHubPartitionId")
    def event_hub_partition_id(self) -> Optional[str]:
        """
        Optional partition Id for notification event hub. If not set, all partitions will be leveraged.
        """
        return pulumi.get(self, "event_hub_partition_id")

    @property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> Optional[str]:
        return pulumi.get(self, "event_hub_resource_id")

    @property
    @pulumi.getter(name="eventHubType")
    def event_hub_type(self) -> Optional[str]:
        """
        The event hub type.
        """
        return pulumi.get(self, "event_hub_type")

    @property
    @pulumi.getter(name="eventStreamingState")
    def event_streaming_state(self) -> Optional[str]:
        """
        The state of the event streaming service
        """
        return pulumi.get(self, "event_streaming_state")

    @property
    @pulumi.getter(name="eventStreamingType")
    def event_streaming_type(self) -> Optional[str]:
        """
        The event streaming service type
        """
        return pulumi.get(self, "event_streaming_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Gets or sets the identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets or sets the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.ProxyResourceResponseSystemData':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets or sets the type.
        """
        return pulumi.get(self, "type")


class AwaitableGetKafkaConfigurationResult(GetKafkaConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaConfigurationResult(
            consumer_group=self.consumer_group,
            credentials=self.credentials,
            event_hub_partition_id=self.event_hub_partition_id,
            event_hub_resource_id=self.event_hub_resource_id,
            event_hub_type=self.event_hub_type,
            event_streaming_state=self.event_streaming_state,
            event_streaming_type=self.event_streaming_type,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_kafka_configuration(account_name: Optional[str] = None,
                            kafka_configuration_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaConfigurationResult:
    """
    Gets the kafka configuration for the account


    :param str account_name: The name of the account.
    :param str kafka_configuration_name: Name of kafka configuration.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['kafkaConfigurationName'] = kafka_configuration_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:purview/v20211201:getKafkaConfiguration', __args__, opts=opts, typ=GetKafkaConfigurationResult).value

    return AwaitableGetKafkaConfigurationResult(
        consumer_group=pulumi.get(__ret__, 'consumer_group'),
        credentials=pulumi.get(__ret__, 'credentials'),
        event_hub_partition_id=pulumi.get(__ret__, 'event_hub_partition_id'),
        event_hub_resource_id=pulumi.get(__ret__, 'event_hub_resource_id'),
        event_hub_type=pulumi.get(__ret__, 'event_hub_type'),
        event_streaming_state=pulumi.get(__ret__, 'event_streaming_state'),
        event_streaming_type=pulumi.get(__ret__, 'event_streaming_type'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_kafka_configuration)
def get_kafka_configuration_output(account_name: Optional[pulumi.Input[str]] = None,
                                   kafka_configuration_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaConfigurationResult]:
    """
    Gets the kafka configuration for the account


    :param str account_name: The name of the account.
    :param str kafka_configuration_name: Name of kafka configuration.
    :param str resource_group_name: The resource group name.
    """
    ...
