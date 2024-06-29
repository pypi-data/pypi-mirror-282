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
    'GetContainerAppResult',
    'AwaitableGetContainerAppResult',
    'get_container_app',
    'get_container_app_output',
]

@pulumi.output_type
class GetContainerAppResult:
    """
    Container App.
    """
    def __init__(__self__, configuration=None, id=None, kind=None, kube_environment_id=None, latest_revision_fqdn=None, latest_revision_name=None, location=None, name=None, provisioning_state=None, tags=None, template=None, type=None):
        if configuration and not isinstance(configuration, dict):
            raise TypeError("Expected argument 'configuration' to be a dict")
        pulumi.set(__self__, "configuration", configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if kube_environment_id and not isinstance(kube_environment_id, str):
            raise TypeError("Expected argument 'kube_environment_id' to be a str")
        pulumi.set(__self__, "kube_environment_id", kube_environment_id)
        if latest_revision_fqdn and not isinstance(latest_revision_fqdn, str):
            raise TypeError("Expected argument 'latest_revision_fqdn' to be a str")
        pulumi.set(__self__, "latest_revision_fqdn", latest_revision_fqdn)
        if latest_revision_name and not isinstance(latest_revision_name, str):
            raise TypeError("Expected argument 'latest_revision_name' to be a str")
        pulumi.set(__self__, "latest_revision_name", latest_revision_name)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template and not isinstance(template, dict):
            raise TypeError("Expected argument 'template' to be a dict")
        pulumi.set(__self__, "template", template)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def configuration(self) -> Optional['outputs.ConfigurationResponse']:
        """
        Non versioned Container App configuration properties.
        """
        return pulumi.get(self, "configuration")

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
    @pulumi.getter(name="kubeEnvironmentId")
    def kube_environment_id(self) -> Optional[str]:
        """
        Resource ID of the Container App's KubeEnvironment.
        """
        return pulumi.get(self, "kube_environment_id")

    @property
    @pulumi.getter(name="latestRevisionFqdn")
    def latest_revision_fqdn(self) -> str:
        """
        Fully Qualified Domain Name of the latest revision of the Container App.
        """
        return pulumi.get(self, "latest_revision_fqdn")

    @property
    @pulumi.getter(name="latestRevisionName")
    def latest_revision_name(self) -> str:
        """
        Name of the latest revision of the Container App.
        """
        return pulumi.get(self, "latest_revision_name")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Container App.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> Optional['outputs.TemplateResponse']:
        """
        Container App versioned application definition.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetContainerAppResult(GetContainerAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerAppResult(
            configuration=self.configuration,
            id=self.id,
            kind=self.kind,
            kube_environment_id=self.kube_environment_id,
            latest_revision_fqdn=self.latest_revision_fqdn,
            latest_revision_name=self.latest_revision_name,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            template=self.template,
            type=self.type)


def get_container_app(name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerAppResult:
    """
    Container App.


    :param str name: Name of the Container App.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20231201:getContainerApp', __args__, opts=opts, typ=GetContainerAppResult).value

    return AwaitableGetContainerAppResult(
        configuration=pulumi.get(__ret__, 'configuration'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        kube_environment_id=pulumi.get(__ret__, 'kube_environment_id'),
        latest_revision_fqdn=pulumi.get(__ret__, 'latest_revision_fqdn'),
        latest_revision_name=pulumi.get(__ret__, 'latest_revision_name'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        tags=pulumi.get(__ret__, 'tags'),
        template=pulumi.get(__ret__, 'template'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_container_app)
def get_container_app_output(name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerAppResult]:
    """
    Container App.


    :param str name: Name of the Container App.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
