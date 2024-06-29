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
    'GetApplicationGatewayPrivateEndpointConnectionResult',
    'AwaitableGetApplicationGatewayPrivateEndpointConnectionResult',
    'get_application_gateway_private_endpoint_connection',
    'get_application_gateway_private_endpoint_connection_output',
]

@pulumi.output_type
class GetApplicationGatewayPrivateEndpointConnectionResult:
    """
    Private Endpoint connection on an application gateway.
    """
    def __init__(__self__, etag=None, id=None, link_identifier=None, name=None, private_endpoint=None, private_link_service_connection_state=None, provisioning_state=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if link_identifier and not isinstance(link_identifier, str):
            raise TypeError("Expected argument 'link_identifier' to be a str")
        pulumi.set(__self__, "link_identifier", link_identifier)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint and not isinstance(private_endpoint, dict):
            raise TypeError("Expected argument 'private_endpoint' to be a dict")
        pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state and not isinstance(private_link_service_connection_state, dict):
            raise TypeError("Expected argument 'private_link_service_connection_state' to be a dict")
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> str:
        """
        The consumer link id.
        """
        return pulumi.get(self, "link_identifier")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the private endpoint connection on an application gateway.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> 'outputs.PrivateEndpointResponse':
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional['outputs.PrivateLinkServiceConnectionStateResponse']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the application gateway private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetApplicationGatewayPrivateEndpointConnectionResult(GetApplicationGatewayPrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationGatewayPrivateEndpointConnectionResult(
            etag=self.etag,
            id=self.id,
            link_identifier=self.link_identifier,
            name=self.name,
            private_endpoint=self.private_endpoint,
            private_link_service_connection_state=self.private_link_service_connection_state,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_application_gateway_private_endpoint_connection(application_gateway_name: Optional[str] = None,
                                                        connection_name: Optional[str] = None,
                                                        resource_group_name: Optional[str] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationGatewayPrivateEndpointConnectionResult:
    """
    Gets the specified private endpoint connection on application gateway.


    :param str application_gateway_name: The name of the application gateway.
    :param str connection_name: The name of the application gateway private endpoint connection.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['applicationGatewayName'] = application_gateway_name
    __args__['connectionName'] = connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230501:getApplicationGatewayPrivateEndpointConnection', __args__, opts=opts, typ=GetApplicationGatewayPrivateEndpointConnectionResult).value

    return AwaitableGetApplicationGatewayPrivateEndpointConnectionResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        link_identifier=pulumi.get(__ret__, 'link_identifier'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint=pulumi.get(__ret__, 'private_endpoint'),
        private_link_service_connection_state=pulumi.get(__ret__, 'private_link_service_connection_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_application_gateway_private_endpoint_connection)
def get_application_gateway_private_endpoint_connection_output(application_gateway_name: Optional[pulumi.Input[str]] = None,
                                                               connection_name: Optional[pulumi.Input[str]] = None,
                                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationGatewayPrivateEndpointConnectionResult]:
    """
    Gets the specified private endpoint connection on application gateway.


    :param str application_gateway_name: The name of the application gateway.
    :param str connection_name: The name of the application gateway private endpoint connection.
    :param str resource_group_name: The name of the resource group.
    """
    ...
