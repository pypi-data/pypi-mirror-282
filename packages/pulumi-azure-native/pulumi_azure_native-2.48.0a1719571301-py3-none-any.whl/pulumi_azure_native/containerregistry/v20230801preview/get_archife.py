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
    'GetArchifeResult',
    'AwaitableGetArchifeResult',
    'get_archife',
    'get_archife_output',
]

@pulumi.output_type
class GetArchifeResult:
    """
    An object that represents a archive for a container registry.
    """
    def __init__(__self__, id=None, name=None, package_source=None, provisioning_state=None, published_version=None, repository_endpoint=None, repository_endpoint_prefix=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_source and not isinstance(package_source, dict):
            raise TypeError("Expected argument 'package_source' to be a dict")
        pulumi.set(__self__, "package_source", package_source)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if published_version and not isinstance(published_version, str):
            raise TypeError("Expected argument 'published_version' to be a str")
        pulumi.set(__self__, "published_version", published_version)
        if repository_endpoint and not isinstance(repository_endpoint, str):
            raise TypeError("Expected argument 'repository_endpoint' to be a str")
        pulumi.set(__self__, "repository_endpoint", repository_endpoint)
        if repository_endpoint_prefix and not isinstance(repository_endpoint_prefix, str):
            raise TypeError("Expected argument 'repository_endpoint_prefix' to be a str")
        pulumi.set(__self__, "repository_endpoint_prefix", repository_endpoint_prefix)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageSource")
    def package_source(self) -> Optional['outputs.ArchivePackageSourcePropertiesResponse']:
        """
        The package source of the archive.
        """
        return pulumi.get(self, "package_source")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the archive at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publishedVersion")
    def published_version(self) -> Optional[str]:
        """
        The published version of the archive.
        """
        return pulumi.get(self, "published_version")

    @property
    @pulumi.getter(name="repositoryEndpoint")
    def repository_endpoint(self) -> str:
        return pulumi.get(self, "repository_endpoint")

    @property
    @pulumi.getter(name="repositoryEndpointPrefix")
    def repository_endpoint_prefix(self) -> Optional[str]:
        return pulumi.get(self, "repository_endpoint_prefix")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetArchifeResult(GetArchifeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArchifeResult(
            id=self.id,
            name=self.name,
            package_source=self.package_source,
            provisioning_state=self.provisioning_state,
            published_version=self.published_version,
            repository_endpoint=self.repository_endpoint,
            repository_endpoint_prefix=self.repository_endpoint_prefix,
            system_data=self.system_data,
            type=self.type)


def get_archife(archive_name: Optional[str] = None,
                package_type: Optional[str] = None,
                registry_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArchifeResult:
    """
    Gets the properties of the archive.


    :param str archive_name: The name of the archive resource.
    :param str package_type: The type of the package resource.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['archiveName'] = archive_name
    __args__['packageType'] = package_type
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20230801preview:getArchife', __args__, opts=opts, typ=GetArchifeResult).value

    return AwaitableGetArchifeResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        package_source=pulumi.get(__ret__, 'package_source'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        published_version=pulumi.get(__ret__, 'published_version'),
        repository_endpoint=pulumi.get(__ret__, 'repository_endpoint'),
        repository_endpoint_prefix=pulumi.get(__ret__, 'repository_endpoint_prefix'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_archife)
def get_archife_output(archive_name: Optional[pulumi.Input[str]] = None,
                       package_type: Optional[pulumi.Input[str]] = None,
                       registry_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetArchifeResult]:
    """
    Gets the properties of the archive.


    :param str archive_name: The name of the archive resource.
    :param str package_type: The type of the package resource.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
