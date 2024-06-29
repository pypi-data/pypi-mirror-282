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
    'GetApiManagementServiceResult',
    'AwaitableGetApiManagementServiceResult',
    'get_api_management_service',
    'get_api_management_service_output',
]

@pulumi.output_type
class GetApiManagementServiceResult:
    """
    A single API Management service resource in List or Get response.
    """
    def __init__(__self__, additional_locations=None, addresser_email=None, created_at_utc=None, custom_properties=None, etag=None, hostname_configurations=None, id=None, location=None, management_api_url=None, name=None, portal_url=None, provisioning_state=None, publisher_email=None, publisher_name=None, runtime_url=None, scm_url=None, sku=None, static_ips=None, tags=None, target_provisioning_state=None, type=None, vpn_type=None, vpnconfiguration=None):
        if additional_locations and not isinstance(additional_locations, list):
            raise TypeError("Expected argument 'additional_locations' to be a list")
        pulumi.set(__self__, "additional_locations", additional_locations)
        if addresser_email and not isinstance(addresser_email, str):
            raise TypeError("Expected argument 'addresser_email' to be a str")
        pulumi.set(__self__, "addresser_email", addresser_email)
        if created_at_utc and not isinstance(created_at_utc, str):
            raise TypeError("Expected argument 'created_at_utc' to be a str")
        pulumi.set(__self__, "created_at_utc", created_at_utc)
        if custom_properties and not isinstance(custom_properties, dict):
            raise TypeError("Expected argument 'custom_properties' to be a dict")
        pulumi.set(__self__, "custom_properties", custom_properties)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if hostname_configurations and not isinstance(hostname_configurations, list):
            raise TypeError("Expected argument 'hostname_configurations' to be a list")
        pulumi.set(__self__, "hostname_configurations", hostname_configurations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if management_api_url and not isinstance(management_api_url, str):
            raise TypeError("Expected argument 'management_api_url' to be a str")
        pulumi.set(__self__, "management_api_url", management_api_url)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if portal_url and not isinstance(portal_url, str):
            raise TypeError("Expected argument 'portal_url' to be a str")
        pulumi.set(__self__, "portal_url", portal_url)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if publisher_email and not isinstance(publisher_email, str):
            raise TypeError("Expected argument 'publisher_email' to be a str")
        pulumi.set(__self__, "publisher_email", publisher_email)
        if publisher_name and not isinstance(publisher_name, str):
            raise TypeError("Expected argument 'publisher_name' to be a str")
        pulumi.set(__self__, "publisher_name", publisher_name)
        if runtime_url and not isinstance(runtime_url, str):
            raise TypeError("Expected argument 'runtime_url' to be a str")
        pulumi.set(__self__, "runtime_url", runtime_url)
        if scm_url and not isinstance(scm_url, str):
            raise TypeError("Expected argument 'scm_url' to be a str")
        pulumi.set(__self__, "scm_url", scm_url)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if static_ips and not isinstance(static_ips, list):
            raise TypeError("Expected argument 'static_ips' to be a list")
        pulumi.set(__self__, "static_ips", static_ips)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_provisioning_state and not isinstance(target_provisioning_state, str):
            raise TypeError("Expected argument 'target_provisioning_state' to be a str")
        pulumi.set(__self__, "target_provisioning_state", target_provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vpn_type and not isinstance(vpn_type, str):
            raise TypeError("Expected argument 'vpn_type' to be a str")
        pulumi.set(__self__, "vpn_type", vpn_type)
        if vpnconfiguration and not isinstance(vpnconfiguration, dict):
            raise TypeError("Expected argument 'vpnconfiguration' to be a dict")
        pulumi.set(__self__, "vpnconfiguration", vpnconfiguration)

    @property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Optional[Sequence['outputs.AdditionalRegionResponse']]:
        """
        Additional datacenter locations of the API Management service.
        """
        return pulumi.get(self, "additional_locations")

    @property
    @pulumi.getter(name="addresserEmail")
    def addresser_email(self) -> Optional[str]:
        """
        Addresser email.
        """
        return pulumi.get(self, "addresser_email")

    @property
    @pulumi.getter(name="createdAtUtc")
    def created_at_utc(self) -> str:
        """
        Creation UTC date of the API Management service.The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "created_at_utc")

    @property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Mapping[str, str]]:
        """
        Custom properties of the API Management service, like disabling TLS 1.0.
        """
        return pulumi.get(self, "custom_properties")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hostnameConfigurations")
    def hostname_configurations(self) -> Optional[Sequence['outputs.HostnameConfigurationResponse']]:
        """
        Custom hostname configuration of the API Management service.
        """
        return pulumi.get(self, "hostname_configurations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementApiUrl")
    def management_api_url(self) -> str:
        """
        Management API endpoint URL of the API Management service.
        """
        return pulumi.get(self, "management_api_url")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portalUrl")
    def portal_url(self) -> str:
        """
        Publisher portal endpoint Url of the API Management service.
        """
        return pulumi.get(self, "portal_url")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publisherEmail")
    def publisher_email(self) -> str:
        """
        Publisher email.
        """
        return pulumi.get(self, "publisher_email")

    @property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> str:
        """
        Publisher name.
        """
        return pulumi.get(self, "publisher_name")

    @property
    @pulumi.getter(name="runtimeUrl")
    def runtime_url(self) -> str:
        """
        Proxy endpoint URL of the API Management service.
        """
        return pulumi.get(self, "runtime_url")

    @property
    @pulumi.getter(name="scmUrl")
    def scm_url(self) -> str:
        """
        SCM endpoint URL of the API Management service.
        """
        return pulumi.get(self, "scm_url")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.ApiManagementServiceSkuPropertiesResponse':
        """
        SKU properties of the API Management service.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="staticIPs")
    def static_ips(self) -> Sequence[str]:
        """
        Static IP addresses of the API Management service virtual machines. Available only for Standard and Premium SKU.
        """
        return pulumi.get(self, "static_ips")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetProvisioningState")
    def target_provisioning_state(self) -> str:
        """
        The provisioning state of the API Management service, which is targeted by the long running operation started on the service.
        """
        return pulumi.get(self, "target_provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource is set to Microsoft.ApiManagement.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vpnType")
    def vpn_type(self) -> Optional[str]:
        """
        The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.
        """
        return pulumi.get(self, "vpn_type")

    @property
    @pulumi.getter
    def vpnconfiguration(self) -> Optional['outputs.VirtualNetworkConfigurationResponse']:
        """
        Virtual network configuration of the API Management service.
        """
        return pulumi.get(self, "vpnconfiguration")


class AwaitableGetApiManagementServiceResult(GetApiManagementServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiManagementServiceResult(
            additional_locations=self.additional_locations,
            addresser_email=self.addresser_email,
            created_at_utc=self.created_at_utc,
            custom_properties=self.custom_properties,
            etag=self.etag,
            hostname_configurations=self.hostname_configurations,
            id=self.id,
            location=self.location,
            management_api_url=self.management_api_url,
            name=self.name,
            portal_url=self.portal_url,
            provisioning_state=self.provisioning_state,
            publisher_email=self.publisher_email,
            publisher_name=self.publisher_name,
            runtime_url=self.runtime_url,
            scm_url=self.scm_url,
            sku=self.sku,
            static_ips=self.static_ips,
            tags=self.tags,
            target_provisioning_state=self.target_provisioning_state,
            type=self.type,
            vpn_type=self.vpn_type,
            vpnconfiguration=self.vpnconfiguration)


def get_api_management_service(resource_group_name: Optional[str] = None,
                               service_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiManagementServiceResult:
    """
    Gets an API Management service resource description.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20161010:getApiManagementService', __args__, opts=opts, typ=GetApiManagementServiceResult).value

    return AwaitableGetApiManagementServiceResult(
        additional_locations=pulumi.get(__ret__, 'additional_locations'),
        addresser_email=pulumi.get(__ret__, 'addresser_email'),
        created_at_utc=pulumi.get(__ret__, 'created_at_utc'),
        custom_properties=pulumi.get(__ret__, 'custom_properties'),
        etag=pulumi.get(__ret__, 'etag'),
        hostname_configurations=pulumi.get(__ret__, 'hostname_configurations'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        management_api_url=pulumi.get(__ret__, 'management_api_url'),
        name=pulumi.get(__ret__, 'name'),
        portal_url=pulumi.get(__ret__, 'portal_url'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        publisher_email=pulumi.get(__ret__, 'publisher_email'),
        publisher_name=pulumi.get(__ret__, 'publisher_name'),
        runtime_url=pulumi.get(__ret__, 'runtime_url'),
        scm_url=pulumi.get(__ret__, 'scm_url'),
        sku=pulumi.get(__ret__, 'sku'),
        static_ips=pulumi.get(__ret__, 'static_ips'),
        tags=pulumi.get(__ret__, 'tags'),
        target_provisioning_state=pulumi.get(__ret__, 'target_provisioning_state'),
        type=pulumi.get(__ret__, 'type'),
        vpn_type=pulumi.get(__ret__, 'vpn_type'),
        vpnconfiguration=pulumi.get(__ret__, 'vpnconfiguration'))


@_utilities.lift_output_func(get_api_management_service)
def get_api_management_service_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                      service_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiManagementServiceResult]:
    """
    Gets an API Management service resource description.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
