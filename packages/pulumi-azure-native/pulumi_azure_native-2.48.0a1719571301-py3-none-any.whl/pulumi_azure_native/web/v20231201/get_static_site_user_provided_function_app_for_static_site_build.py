# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult',
    'AwaitableGetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult',
    'get_static_site_user_provided_function_app_for_static_site_build',
    'get_static_site_user_provided_function_app_for_static_site_build_output',
]

@pulumi.output_type
class GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult:
    """
    Static Site User Provided Function App ARM resource.
    """
    def __init__(__self__, created_on=None, function_app_region=None, function_app_resource_id=None, id=None, kind=None, name=None, type=None):
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if function_app_region and not isinstance(function_app_region, str):
            raise TypeError("Expected argument 'function_app_region' to be a str")
        pulumi.set(__self__, "function_app_region", function_app_region)
        if function_app_resource_id and not isinstance(function_app_resource_id, str):
            raise TypeError("Expected argument 'function_app_resource_id' to be a str")
        pulumi.set(__self__, "function_app_resource_id", function_app_resource_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        """
        The date and time on which the function app was registered with the static site.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="functionAppRegion")
    def function_app_region(self) -> Optional[str]:
        """
        The region of the function app registered with the static site
        """
        return pulumi.get(self, "function_app_region")

    @property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> Optional[str]:
        """
        The resource id of the function app registered with the static site
        """
        return pulumi.get(self, "function_app_resource_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult(GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult(
            created_on=self.created_on,
            function_app_region=self.function_app_region,
            function_app_resource_id=self.function_app_resource_id,
            id=self.id,
            kind=self.kind,
            name=self.name,
            type=self.type)


def get_static_site_user_provided_function_app_for_static_site_build(environment_name: Optional[str] = None,
                                                                     function_app_name: Optional[str] = None,
                                                                     name: Optional[str] = None,
                                                                     resource_group_name: Optional[str] = None,
                                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult:
    """
    Description for Gets the details of the user provided function app registered with a static site build


    :param str environment_name: The stage site identifier.
    :param str function_app_name: Name of the function app registered with the static site build.
    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['functionAppName'] = function_app_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20231201:getStaticSiteUserProvidedFunctionAppForStaticSiteBuild', __args__, opts=opts, typ=GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult).value

    return AwaitableGetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult(
        created_on=pulumi.get(__ret__, 'created_on'),
        function_app_region=pulumi.get(__ret__, 'function_app_region'),
        function_app_resource_id=pulumi.get(__ret__, 'function_app_resource_id'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_static_site_user_provided_function_app_for_static_site_build)
def get_static_site_user_provided_function_app_for_static_site_build_output(environment_name: Optional[pulumi.Input[str]] = None,
                                                                            function_app_name: Optional[pulumi.Input[str]] = None,
                                                                            name: Optional[pulumi.Input[str]] = None,
                                                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult]:
    """
    Description for Gets the details of the user provided function app registered with a static site build


    :param str environment_name: The stage site identifier.
    :param str function_app_name: Name of the function app registered with the static site build.
    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
