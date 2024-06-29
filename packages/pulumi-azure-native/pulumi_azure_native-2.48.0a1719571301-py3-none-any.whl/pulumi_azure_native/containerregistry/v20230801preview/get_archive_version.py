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
    'GetArchiveVersionResult',
    'AwaitableGetArchiveVersionResult',
    'get_archive_version',
    'get_archive_version_output',
]

@pulumi.output_type
class GetArchiveVersionResult:
    """
    An object that represents an export pipeline for a container registry.
    """
    def __init__(__self__, archive_version_error_message=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if archive_version_error_message and not isinstance(archive_version_error_message, str):
            raise TypeError("Expected argument 'archive_version_error_message' to be a str")
        pulumi.set(__self__, "archive_version_error_message", archive_version_error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="archiveVersionErrorMessage")
    def archive_version_error_message(self) -> Optional[str]:
        """
        The detailed error message for the archive version in the case of failure.
        """
        return pulumi.get(self, "archive_version_error_message")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the archive at the time the operation was called.
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
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetArchiveVersionResult(GetArchiveVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArchiveVersionResult(
            archive_version_error_message=self.archive_version_error_message,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_archive_version(archive_name: Optional[str] = None,
                        archive_version_name: Optional[str] = None,
                        package_type: Optional[str] = None,
                        registry_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArchiveVersionResult:
    """
    Gets the properties of the archive version.


    :param str archive_name: The name of the archive resource.
    :param str archive_version_name: The name of the archive version resource.
    :param str package_type: The type of the package resource.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['archiveName'] = archive_name
    __args__['archiveVersionName'] = archive_version_name
    __args__['packageType'] = package_type
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20230801preview:getArchiveVersion', __args__, opts=opts, typ=GetArchiveVersionResult).value

    return AwaitableGetArchiveVersionResult(
        archive_version_error_message=pulumi.get(__ret__, 'archive_version_error_message'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_archive_version)
def get_archive_version_output(archive_name: Optional[pulumi.Input[str]] = None,
                               archive_version_name: Optional[pulumi.Input[str]] = None,
                               package_type: Optional[pulumi.Input[str]] = None,
                               registry_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetArchiveVersionResult]:
    """
    Gets the properties of the archive version.


    :param str archive_name: The name of the archive resource.
    :param str archive_version_name: The name of the archive version resource.
    :param str package_type: The type of the package resource.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
