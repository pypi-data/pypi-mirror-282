# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetWorkspaceApiResult',
    'AwaitableGetWorkspaceApiResult',
    'get_workspace_api',
    'get_workspace_api_output',
]

@pulumi.output_type
class GetWorkspaceApiResult:
    """
    API details.
    """
    def __init__(__self__, api_revision=None, api_revision_description=None, api_type=None, api_version=None, api_version_description=None, api_version_set=None, api_version_set_id=None, authentication_settings=None, contact=None, description=None, display_name=None, id=None, is_current=None, is_online=None, license=None, name=None, path=None, protocols=None, service_url=None, source_api_id=None, subscription_key_parameter_names=None, subscription_required=None, terms_of_service_url=None, type=None):
        if api_revision and not isinstance(api_revision, str):
            raise TypeError("Expected argument 'api_revision' to be a str")
        pulumi.set(__self__, "api_revision", api_revision)
        if api_revision_description and not isinstance(api_revision_description, str):
            raise TypeError("Expected argument 'api_revision_description' to be a str")
        pulumi.set(__self__, "api_revision_description", api_revision_description)
        if api_type and not isinstance(api_type, str):
            raise TypeError("Expected argument 'api_type' to be a str")
        pulumi.set(__self__, "api_type", api_type)
        if api_version and not isinstance(api_version, str):
            raise TypeError("Expected argument 'api_version' to be a str")
        pulumi.set(__self__, "api_version", api_version)
        if api_version_description and not isinstance(api_version_description, str):
            raise TypeError("Expected argument 'api_version_description' to be a str")
        pulumi.set(__self__, "api_version_description", api_version_description)
        if api_version_set and not isinstance(api_version_set, dict):
            raise TypeError("Expected argument 'api_version_set' to be a dict")
        pulumi.set(__self__, "api_version_set", api_version_set)
        if api_version_set_id and not isinstance(api_version_set_id, str):
            raise TypeError("Expected argument 'api_version_set_id' to be a str")
        pulumi.set(__self__, "api_version_set_id", api_version_set_id)
        if authentication_settings and not isinstance(authentication_settings, dict):
            raise TypeError("Expected argument 'authentication_settings' to be a dict")
        pulumi.set(__self__, "authentication_settings", authentication_settings)
        if contact and not isinstance(contact, dict):
            raise TypeError("Expected argument 'contact' to be a dict")
        pulumi.set(__self__, "contact", contact)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_current and not isinstance(is_current, bool):
            raise TypeError("Expected argument 'is_current' to be a bool")
        pulumi.set(__self__, "is_current", is_current)
        if is_online and not isinstance(is_online, bool):
            raise TypeError("Expected argument 'is_online' to be a bool")
        pulumi.set(__self__, "is_online", is_online)
        if license and not isinstance(license, dict):
            raise TypeError("Expected argument 'license' to be a dict")
        pulumi.set(__self__, "license", license)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if protocols and not isinstance(protocols, list):
            raise TypeError("Expected argument 'protocols' to be a list")
        pulumi.set(__self__, "protocols", protocols)
        if service_url and not isinstance(service_url, str):
            raise TypeError("Expected argument 'service_url' to be a str")
        pulumi.set(__self__, "service_url", service_url)
        if source_api_id and not isinstance(source_api_id, str):
            raise TypeError("Expected argument 'source_api_id' to be a str")
        pulumi.set(__self__, "source_api_id", source_api_id)
        if subscription_key_parameter_names and not isinstance(subscription_key_parameter_names, dict):
            raise TypeError("Expected argument 'subscription_key_parameter_names' to be a dict")
        pulumi.set(__self__, "subscription_key_parameter_names", subscription_key_parameter_names)
        if subscription_required and not isinstance(subscription_required, bool):
            raise TypeError("Expected argument 'subscription_required' to be a bool")
        pulumi.set(__self__, "subscription_required", subscription_required)
        if terms_of_service_url and not isinstance(terms_of_service_url, str):
            raise TypeError("Expected argument 'terms_of_service_url' to be a str")
        pulumi.set(__self__, "terms_of_service_url", terms_of_service_url)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="apiRevision")
    def api_revision(self) -> Optional[str]:
        """
        Describes the revision of the API. If no value is provided, default revision 1 is created
        """
        return pulumi.get(self, "api_revision")

    @property
    @pulumi.getter(name="apiRevisionDescription")
    def api_revision_description(self) -> Optional[str]:
        """
        Description of the API Revision.
        """
        return pulumi.get(self, "api_revision_description")

    @property
    @pulumi.getter(name="apiType")
    def api_type(self) -> Optional[str]:
        """
        Type of API.
        """
        return pulumi.get(self, "api_type")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        Indicates the version identifier of the API if the API is versioned
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter(name="apiVersionDescription")
    def api_version_description(self) -> Optional[str]:
        """
        Description of the API Version.
        """
        return pulumi.get(self, "api_version_description")

    @property
    @pulumi.getter(name="apiVersionSet")
    def api_version_set(self) -> Optional['outputs.ApiVersionSetContractDetailsResponse']:
        """
        Version set details
        """
        return pulumi.get(self, "api_version_set")

    @property
    @pulumi.getter(name="apiVersionSetId")
    def api_version_set_id(self) -> Optional[str]:
        """
        A resource identifier for the related ApiVersionSet.
        """
        return pulumi.get(self, "api_version_set_id")

    @property
    @pulumi.getter(name="authenticationSettings")
    def authentication_settings(self) -> Optional['outputs.AuthenticationSettingsContractResponse']:
        """
        Collection of authentication settings included into this API.
        """
        return pulumi.get(self, "authentication_settings")

    @property
    @pulumi.getter
    def contact(self) -> Optional['outputs.ApiContactInformationResponse']:
        """
        Contact information for the API.
        """
        return pulumi.get(self, "contact")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the API. May include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        API name. Must be 1 to 300 characters long.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isCurrent")
    def is_current(self) -> Optional[bool]:
        """
        Indicates if API revision is current api revision.
        """
        return pulumi.get(self, "is_current")

    @property
    @pulumi.getter(name="isOnline")
    def is_online(self) -> bool:
        """
        Indicates if API revision is accessible via the gateway.
        """
        return pulumi.get(self, "is_online")

    @property
    @pulumi.getter
    def license(self) -> Optional['outputs.ApiLicenseInformationResponse']:
        """
        License information for the API.
        """
        return pulumi.get(self, "license")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[str]]:
        """
        Describes on which protocols the operations in this API can be invoked.
        """
        return pulumi.get(self, "protocols")

    @property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> Optional[str]:
        """
        Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.
        """
        return pulumi.get(self, "service_url")

    @property
    @pulumi.getter(name="sourceApiId")
    def source_api_id(self) -> Optional[str]:
        """
        API identifier of the source API.
        """
        return pulumi.get(self, "source_api_id")

    @property
    @pulumi.getter(name="subscriptionKeyParameterNames")
    def subscription_key_parameter_names(self) -> Optional['outputs.SubscriptionKeyParameterNamesContractResponse']:
        """
        Protocols over which API is made available.
        """
        return pulumi.get(self, "subscription_key_parameter_names")

    @property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> Optional[bool]:
        """
        Specifies whether an API or Product subscription is required for accessing the API.
        """
        return pulumi.get(self, "subscription_required")

    @property
    @pulumi.getter(name="termsOfServiceUrl")
    def terms_of_service_url(self) -> Optional[str]:
        """
         A URL to the Terms of Service for the API. MUST be in the format of a URL.
        """
        return pulumi.get(self, "terms_of_service_url")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceApiResult(GetWorkspaceApiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceApiResult(
            api_revision=self.api_revision,
            api_revision_description=self.api_revision_description,
            api_type=self.api_type,
            api_version=self.api_version,
            api_version_description=self.api_version_description,
            api_version_set=self.api_version_set,
            api_version_set_id=self.api_version_set_id,
            authentication_settings=self.authentication_settings,
            contact=self.contact,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            is_current=self.is_current,
            is_online=self.is_online,
            license=self.license,
            name=self.name,
            path=self.path,
            protocols=self.protocols,
            service_url=self.service_url,
            source_api_id=self.source_api_id,
            subscription_key_parameter_names=self.subscription_key_parameter_names,
            subscription_required=self.subscription_required,
            terms_of_service_url=self.terms_of_service_url,
            type=self.type)


def get_workspace_api(api_id: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      service_name: Optional[str] = None,
                      workspace_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceApiResult:
    """
    Gets the details of the API specified by its identifier.
    Azure REST API version: 2022-09-01-preview.

    Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:getWorkspaceApi', __args__, opts=opts, typ=GetWorkspaceApiResult).value

    return AwaitableGetWorkspaceApiResult(
        api_revision=pulumi.get(__ret__, 'api_revision'),
        api_revision_description=pulumi.get(__ret__, 'api_revision_description'),
        api_type=pulumi.get(__ret__, 'api_type'),
        api_version=pulumi.get(__ret__, 'api_version'),
        api_version_description=pulumi.get(__ret__, 'api_version_description'),
        api_version_set=pulumi.get(__ret__, 'api_version_set'),
        api_version_set_id=pulumi.get(__ret__, 'api_version_set_id'),
        authentication_settings=pulumi.get(__ret__, 'authentication_settings'),
        contact=pulumi.get(__ret__, 'contact'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        is_current=pulumi.get(__ret__, 'is_current'),
        is_online=pulumi.get(__ret__, 'is_online'),
        license=pulumi.get(__ret__, 'license'),
        name=pulumi.get(__ret__, 'name'),
        path=pulumi.get(__ret__, 'path'),
        protocols=pulumi.get(__ret__, 'protocols'),
        service_url=pulumi.get(__ret__, 'service_url'),
        source_api_id=pulumi.get(__ret__, 'source_api_id'),
        subscription_key_parameter_names=pulumi.get(__ret__, 'subscription_key_parameter_names'),
        subscription_required=pulumi.get(__ret__, 'subscription_required'),
        terms_of_service_url=pulumi.get(__ret__, 'terms_of_service_url'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_api)
def get_workspace_api_output(api_id: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             service_name: Optional[pulumi.Input[str]] = None,
                             workspace_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceApiResult]:
    """
    Gets the details of the API specified by its identifier.
    Azure REST API version: 2022-09-01-preview.

    Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    ...
