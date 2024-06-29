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
    'GetDataCollectionEndpointResult',
    'AwaitableGetDataCollectionEndpointResult',
    'get_data_collection_endpoint',
    'get_data_collection_endpoint_output',
]

@pulumi.output_type
class GetDataCollectionEndpointResult:
    """
    Definition of ARM tracked top level resource.
    """
    def __init__(__self__, configuration_access=None, description=None, etag=None, failover_configuration=None, id=None, identity=None, immutable_id=None, kind=None, location=None, logs_ingestion=None, metadata=None, metrics_ingestion=None, name=None, network_acls=None, private_link_scoped_resources=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if configuration_access and not isinstance(configuration_access, dict):
            raise TypeError("Expected argument 'configuration_access' to be a dict")
        pulumi.set(__self__, "configuration_access", configuration_access)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if failover_configuration and not isinstance(failover_configuration, dict):
            raise TypeError("Expected argument 'failover_configuration' to be a dict")
        pulumi.set(__self__, "failover_configuration", failover_configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if immutable_id and not isinstance(immutable_id, str):
            raise TypeError("Expected argument 'immutable_id' to be a str")
        pulumi.set(__self__, "immutable_id", immutable_id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if logs_ingestion and not isinstance(logs_ingestion, dict):
            raise TypeError("Expected argument 'logs_ingestion' to be a dict")
        pulumi.set(__self__, "logs_ingestion", logs_ingestion)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if metrics_ingestion and not isinstance(metrics_ingestion, dict):
            raise TypeError("Expected argument 'metrics_ingestion' to be a dict")
        pulumi.set(__self__, "metrics_ingestion", metrics_ingestion)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_acls and not isinstance(network_acls, dict):
            raise TypeError("Expected argument 'network_acls' to be a dict")
        pulumi.set(__self__, "network_acls", network_acls)
        if private_link_scoped_resources and not isinstance(private_link_scoped_resources, list):
            raise TypeError("Expected argument 'private_link_scoped_resources' to be a list")
        pulumi.set(__self__, "private_link_scoped_resources", private_link_scoped_resources)
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
    @pulumi.getter(name="configurationAccess")
    def configuration_access(self) -> Optional['outputs.DataCollectionEndpointResponseConfigurationAccess']:
        """
        The endpoint used by clients to access their configuration.
        """
        return pulumi.get(self, "configuration_access")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the data collection endpoint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource entity tag (ETag).
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="failoverConfiguration")
    def failover_configuration(self) -> 'outputs.DataCollectionEndpointResponseFailoverConfiguration':
        """
        Failover configuration on this endpoint. This property is READ-ONLY.
        """
        return pulumi.get(self, "failover_configuration")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.DataCollectionEndpointResourceResponseIdentity']:
        """
        Managed service identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> Optional[str]:
        """
        The immutable ID of this data collection endpoint resource. This property is READ-ONLY.
        """
        return pulumi.get(self, "immutable_id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logsIngestion")
    def logs_ingestion(self) -> Optional['outputs.DataCollectionEndpointResponseLogsIngestion']:
        """
        The endpoint used by clients to ingest logs.
        """
        return pulumi.get(self, "logs_ingestion")

    @property
    @pulumi.getter
    def metadata(self) -> 'outputs.DataCollectionEndpointResponseMetadata':
        """
        Metadata for the resource. This property is READ-ONLY.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="metricsIngestion")
    def metrics_ingestion(self) -> Optional['outputs.DataCollectionEndpointResponseMetricsIngestion']:
        """
        The endpoint used by clients to ingest metrics.
        """
        return pulumi.get(self, "metrics_ingestion")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional['outputs.DataCollectionEndpointResponseNetworkAcls']:
        """
        Network access control rules for the endpoints.
        """
        return pulumi.get(self, "network_acls")

    @property
    @pulumi.getter(name="privateLinkScopedResources")
    def private_link_scoped_resources(self) -> Sequence['outputs.PrivateLinkScopedResourceResponse']:
        """
        List of Azure Monitor Private Link Scope Resources to which this data collection endpoint resource is associated. This property is READ-ONLY.
        """
        return pulumi.get(self, "private_link_scoped_resources")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The resource provisioning state. This property is READ-ONLY.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.DataCollectionEndpointResourceResponseSystemData':
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
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetDataCollectionEndpointResult(GetDataCollectionEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataCollectionEndpointResult(
            configuration_access=self.configuration_access,
            description=self.description,
            etag=self.etag,
            failover_configuration=self.failover_configuration,
            id=self.id,
            identity=self.identity,
            immutable_id=self.immutable_id,
            kind=self.kind,
            location=self.location,
            logs_ingestion=self.logs_ingestion,
            metadata=self.metadata,
            metrics_ingestion=self.metrics_ingestion,
            name=self.name,
            network_acls=self.network_acls,
            private_link_scoped_resources=self.private_link_scoped_resources,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_data_collection_endpoint(data_collection_endpoint_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataCollectionEndpointResult:
    """
    Definition of ARM tracked top level resource.


    :param str data_collection_endpoint_name: The name of the data collection endpoint. The name is case insensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['dataCollectionEndpointName'] = data_collection_endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20220601:getDataCollectionEndpoint', __args__, opts=opts, typ=GetDataCollectionEndpointResult).value

    return AwaitableGetDataCollectionEndpointResult(
        configuration_access=pulumi.get(__ret__, 'configuration_access'),
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        failover_configuration=pulumi.get(__ret__, 'failover_configuration'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        immutable_id=pulumi.get(__ret__, 'immutable_id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        logs_ingestion=pulumi.get(__ret__, 'logs_ingestion'),
        metadata=pulumi.get(__ret__, 'metadata'),
        metrics_ingestion=pulumi.get(__ret__, 'metrics_ingestion'),
        name=pulumi.get(__ret__, 'name'),
        network_acls=pulumi.get(__ret__, 'network_acls'),
        private_link_scoped_resources=pulumi.get(__ret__, 'private_link_scoped_resources'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_data_collection_endpoint)
def get_data_collection_endpoint_output(data_collection_endpoint_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataCollectionEndpointResult]:
    """
    Definition of ARM tracked top level resource.


    :param str data_collection_endpoint_name: The name of the data collection endpoint. The name is case insensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
