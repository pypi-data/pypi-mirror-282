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
    'GetExtensionResult',
    'AwaitableGetExtensionResult',
    'get_extension',
    'get_extension_output',
]

@pulumi.output_type
class GetExtensionResult:
    """
    Extension resource.
    """
    def __init__(__self__, additional_api_properties=None, e_tag=None, extension_api_docs_link=None, extension_auth_link=None, extension_category=None, extension_id=None, id=None, installed_extension_version=None, name=None, system_data=None, type=None):
        if additional_api_properties and not isinstance(additional_api_properties, dict):
            raise TypeError("Expected argument 'additional_api_properties' to be a dict")
        pulumi.set(__self__, "additional_api_properties", additional_api_properties)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if extension_api_docs_link and not isinstance(extension_api_docs_link, str):
            raise TypeError("Expected argument 'extension_api_docs_link' to be a str")
        pulumi.set(__self__, "extension_api_docs_link", extension_api_docs_link)
        if extension_auth_link and not isinstance(extension_auth_link, str):
            raise TypeError("Expected argument 'extension_auth_link' to be a str")
        pulumi.set(__self__, "extension_auth_link", extension_auth_link)
        if extension_category and not isinstance(extension_category, str):
            raise TypeError("Expected argument 'extension_category' to be a str")
        pulumi.set(__self__, "extension_category", extension_category)
        if extension_id and not isinstance(extension_id, str):
            raise TypeError("Expected argument 'extension_id' to be a str")
        pulumi.set(__self__, "extension_id", extension_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if installed_extension_version and not isinstance(installed_extension_version, str):
            raise TypeError("Expected argument 'installed_extension_version' to be a str")
        pulumi.set(__self__, "installed_extension_version", installed_extension_version)
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
    @pulumi.getter(name="additionalApiProperties")
    def additional_api_properties(self) -> Mapping[str, 'outputs.ApiPropertiesResponse']:
        """
        Additional api properties.
        """
        return pulumi.get(self, "additional_api_properties")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        The ETag value to implement optimistic concurrency.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="extensionApiDocsLink")
    def extension_api_docs_link(self) -> str:
        """
        Extension api docs link.
        """
        return pulumi.get(self, "extension_api_docs_link")

    @property
    @pulumi.getter(name="extensionAuthLink")
    def extension_auth_link(self) -> str:
        """
        Extension auth link.
        """
        return pulumi.get(self, "extension_auth_link")

    @property
    @pulumi.getter(name="extensionCategory")
    def extension_category(self) -> str:
        """
        Extension category. e.g. weather/sensor/satellite.
        """
        return pulumi.get(self, "extension_category")

    @property
    @pulumi.getter(name="extensionId")
    def extension_id(self) -> str:
        """
        Extension Id.
        """
        return pulumi.get(self, "extension_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="installedExtensionVersion")
    def installed_extension_version(self) -> str:
        """
        Installed extension version.
        """
        return pulumi.get(self, "installed_extension_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetExtensionResult(GetExtensionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExtensionResult(
            additional_api_properties=self.additional_api_properties,
            e_tag=self.e_tag,
            extension_api_docs_link=self.extension_api_docs_link,
            extension_auth_link=self.extension_auth_link,
            extension_category=self.extension_category,
            extension_id=self.extension_id,
            id=self.id,
            installed_extension_version=self.installed_extension_version,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_extension(extension_id: Optional[str] = None,
                  farm_beats_resource_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExtensionResult:
    """
    Get installed extension details by extension id.


    :param str extension_id: Id of extension resource.
    :param str farm_beats_resource_name: FarmBeats resource name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['extensionId'] = extension_id
    __args__['farmBeatsResourceName'] = farm_beats_resource_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:agfoodplatform/v20210901preview:getExtension', __args__, opts=opts, typ=GetExtensionResult).value

    return AwaitableGetExtensionResult(
        additional_api_properties=pulumi.get(__ret__, 'additional_api_properties'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        extension_api_docs_link=pulumi.get(__ret__, 'extension_api_docs_link'),
        extension_auth_link=pulumi.get(__ret__, 'extension_auth_link'),
        extension_category=pulumi.get(__ret__, 'extension_category'),
        extension_id=pulumi.get(__ret__, 'extension_id'),
        id=pulumi.get(__ret__, 'id'),
        installed_extension_version=pulumi.get(__ret__, 'installed_extension_version'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_extension)
def get_extension_output(extension_id: Optional[pulumi.Input[str]] = None,
                         farm_beats_resource_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExtensionResult]:
    """
    Get installed extension details by extension id.


    :param str extension_id: Id of extension resource.
    :param str farm_beats_resource_name: FarmBeats resource name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
