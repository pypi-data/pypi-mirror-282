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
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    """
    A project resource
    """
    def __init__(__self__, azure_authentication_info=None, creation_time=None, databases_info=None, etag=None, id=None, location=None, name=None, provisioning_state=None, source_connection_info=None, source_platform=None, system_data=None, tags=None, target_connection_info=None, target_platform=None, type=None):
        if azure_authentication_info and not isinstance(azure_authentication_info, dict):
            raise TypeError("Expected argument 'azure_authentication_info' to be a dict")
        pulumi.set(__self__, "azure_authentication_info", azure_authentication_info)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if databases_info and not isinstance(databases_info, list):
            raise TypeError("Expected argument 'databases_info' to be a list")
        pulumi.set(__self__, "databases_info", databases_info)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source_connection_info and not isinstance(source_connection_info, dict):
            raise TypeError("Expected argument 'source_connection_info' to be a dict")
        pulumi.set(__self__, "source_connection_info", source_connection_info)
        if source_platform and not isinstance(source_platform, str):
            raise TypeError("Expected argument 'source_platform' to be a str")
        pulumi.set(__self__, "source_platform", source_platform)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_connection_info and not isinstance(target_connection_info, dict):
            raise TypeError("Expected argument 'target_connection_info' to be a dict")
        pulumi.set(__self__, "target_connection_info", target_connection_info)
        if target_platform and not isinstance(target_platform, str):
            raise TypeError("Expected argument 'target_platform' to be a str")
        pulumi.set(__self__, "target_platform", target_platform)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="azureAuthenticationInfo")
    def azure_authentication_info(self) -> Optional['outputs.AzureActiveDirectoryAppResponse']:
        """
        Field that defines the Azure active directory application info, used to connect to the target Azure resource
        """
        return pulumi.get(self, "azure_authentication_info")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        UTC Date and time when project was created
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="databasesInfo")
    def databases_info(self) -> Optional[Sequence['outputs.DatabaseInfoResponse']]:
        """
        List of DatabaseInfo
        """
        return pulumi.get(self, "databases_info")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        HTTP strong entity tag value. This is ignored if submitted.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The project's provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> Optional[Any]:
        """
        Information for connecting to source
        """
        return pulumi.get(self, "source_connection_info")

    @property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> str:
        """
        Source platform for the project
        """
        return pulumi.get(self, "source_platform")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> Optional[Any]:
        """
        Information for connecting to target
        """
        return pulumi.get(self, "target_connection_info")

    @property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> str:
        """
        Target platform for the project
        """
        return pulumi.get(self, "target_platform")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            azure_authentication_info=self.azure_authentication_info,
            creation_time=self.creation_time,
            databases_info=self.databases_info,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            source_connection_info=self.source_connection_info,
            source_platform=self.source_platform,
            system_data=self.system_data,
            tags=self.tags,
            target_connection_info=self.target_connection_info,
            target_platform=self.target_platform,
            type=self.type)


def get_project(group_name: Optional[str] = None,
                project_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.


    :param str group_name: Name of the resource group
    :param str project_name: Name of the project
    :param str service_name: Name of the service
    """
    __args__ = dict()
    __args__['groupName'] = group_name
    __args__['projectName'] = project_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datamigration/v20220330preview:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        azure_authentication_info=pulumi.get(__ret__, 'azure_authentication_info'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        databases_info=pulumi.get(__ret__, 'databases_info'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        source_connection_info=pulumi.get(__ret__, 'source_connection_info'),
        source_platform=pulumi.get(__ret__, 'source_platform'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        target_connection_info=pulumi.get(__ret__, 'target_connection_info'),
        target_platform=pulumi.get(__ret__, 'target_platform'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_project)
def get_project_output(group_name: Optional[pulumi.Input[str]] = None,
                       project_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.


    :param str group_name: Name of the resource group
    :param str project_name: Name of the project
    :param str service_name: Name of the service
    """
    ...
