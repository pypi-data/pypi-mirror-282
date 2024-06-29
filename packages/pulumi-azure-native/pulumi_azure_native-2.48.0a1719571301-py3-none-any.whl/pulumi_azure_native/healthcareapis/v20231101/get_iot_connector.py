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
    'GetIotConnectorResult',
    'AwaitableGetIotConnectorResult',
    'get_iot_connector',
    'get_iot_connector_output',
]

@pulumi.output_type
class GetIotConnectorResult:
    """
    IoT Connector definition.
    """
    def __init__(__self__, device_mapping=None, etag=None, id=None, identity=None, ingestion_endpoint_configuration=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if device_mapping and not isinstance(device_mapping, dict):
            raise TypeError("Expected argument 'device_mapping' to be a dict")
        pulumi.set(__self__, "device_mapping", device_mapping)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if ingestion_endpoint_configuration and not isinstance(ingestion_endpoint_configuration, dict):
            raise TypeError("Expected argument 'ingestion_endpoint_configuration' to be a dict")
        pulumi.set(__self__, "ingestion_endpoint_configuration", ingestion_endpoint_configuration)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="deviceMapping")
    def device_mapping(self) -> Optional['outputs.IotMappingPropertiesResponse']:
        """
        Device Mappings.
        """
        return pulumi.get(self, "device_mapping")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        An etag associated with the resource, used for optimistic concurrency when editing it.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ServiceManagedIdentityResponseIdentity']:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="ingestionEndpointConfiguration")
    def ingestion_endpoint_configuration(self) -> Optional['outputs.IotEventHubIngestionEndpointConfigurationResponse']:
        """
        Source configuration.
        """
        return pulumi.get(self, "ingestion_endpoint_configuration")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIotConnectorResult(GetIotConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIotConnectorResult(
            device_mapping=self.device_mapping,
            etag=self.etag,
            id=self.id,
            identity=self.identity,
            ingestion_endpoint_configuration=self.ingestion_endpoint_configuration,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_iot_connector(iot_connector_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      workspace_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIotConnectorResult:
    """
    Gets the properties of the specified IoT Connector.


    :param str iot_connector_name: The name of IoT Connector resource.
    :param str resource_group_name: The name of the resource group that contains the service instance.
    :param str workspace_name: The name of workspace resource.
    """
    __args__ = dict()
    __args__['iotConnectorName'] = iot_connector_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:healthcareapis/v20231101:getIotConnector', __args__, opts=opts, typ=GetIotConnectorResult).value

    return AwaitableGetIotConnectorResult(
        device_mapping=pulumi.get(__ret__, 'device_mapping'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        ingestion_endpoint_configuration=pulumi.get(__ret__, 'ingestion_endpoint_configuration'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_iot_connector)
def get_iot_connector_output(iot_connector_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             workspace_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIotConnectorResult]:
    """
    Gets the properties of the specified IoT Connector.


    :param str iot_connector_name: The name of IoT Connector resource.
    :param str resource_group_name: The name of the resource group that contains the service instance.
    :param str workspace_name: The name of workspace resource.
    """
    ...
