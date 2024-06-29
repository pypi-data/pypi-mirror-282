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
    'GetNspAssociationResult',
    'AwaitableGetNspAssociationResult',
    'get_nsp_association',
    'get_nsp_association_output',
]

@pulumi.output_type
class GetNspAssociationResult:
    """
    The NSP resource association resource
    """
    def __init__(__self__, access_mode=None, has_provisioning_issues=None, id=None, location=None, name=None, private_link_resource=None, profile=None, provisioning_state=None, tags=None, type=None):
        if access_mode and not isinstance(access_mode, str):
            raise TypeError("Expected argument 'access_mode' to be a str")
        pulumi.set(__self__, "access_mode", access_mode)
        if has_provisioning_issues and not isinstance(has_provisioning_issues, str):
            raise TypeError("Expected argument 'has_provisioning_issues' to be a str")
        pulumi.set(__self__, "has_provisioning_issues", has_provisioning_issues)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_link_resource and not isinstance(private_link_resource, dict):
            raise TypeError("Expected argument 'private_link_resource' to be a dict")
        pulumi.set(__self__, "private_link_resource", private_link_resource)
        if profile and not isinstance(profile, dict):
            raise TypeError("Expected argument 'profile' to be a dict")
        pulumi.set(__self__, "profile", profile)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[str]:
        """
        Access mode on the association.
        """
        return pulumi.get(self, "access_mode")

    @property
    @pulumi.getter(name="hasProvisioningIssues")
    def has_provisioning_issues(self) -> str:
        """
        Specifies if there are provisioning issues
        """
        return pulumi.get(self, "has_provisioning_issues")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkResource")
    def private_link_resource(self) -> Optional['outputs.SubResourceResponse']:
        """
        The PaaS resource to be associated.
        """
        return pulumi.get(self, "private_link_resource")

    @property
    @pulumi.getter
    def profile(self) -> Optional['outputs.SubResourceResponse']:
        """
        Profile id to which the PaaS resource is associated.
        """
        return pulumi.get(self, "profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource  association resource.
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
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetNspAssociationResult(GetNspAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNspAssociationResult(
            access_mode=self.access_mode,
            has_provisioning_issues=self.has_provisioning_issues,
            id=self.id,
            location=self.location,
            name=self.name,
            private_link_resource=self.private_link_resource,
            profile=self.profile,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type)


def get_nsp_association(association_name: Optional[str] = None,
                        network_security_perimeter_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNspAssociationResult:
    """
    Gets the specified NSP association by name.
    Azure REST API version: 2021-02-01-preview.

    Other available API versions: 2023-07-01-preview, 2023-08-01-preview.


    :param str association_name: The name of the NSP association.
    :param str network_security_perimeter_name: The name of the network security perimeter.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['associationName'] = association_name
    __args__['networkSecurityPerimeterName'] = network_security_perimeter_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getNspAssociation', __args__, opts=opts, typ=GetNspAssociationResult).value

    return AwaitableGetNspAssociationResult(
        access_mode=pulumi.get(__ret__, 'access_mode'),
        has_provisioning_issues=pulumi.get(__ret__, 'has_provisioning_issues'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        private_link_resource=pulumi.get(__ret__, 'private_link_resource'),
        profile=pulumi.get(__ret__, 'profile'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_nsp_association)
def get_nsp_association_output(association_name: Optional[pulumi.Input[str]] = None,
                               network_security_perimeter_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNspAssociationResult]:
    """
    Gets the specified NSP association by name.
    Azure REST API version: 2021-02-01-preview.

    Other available API versions: 2023-07-01-preview, 2023-08-01-preview.


    :param str association_name: The name of the NSP association.
    :param str network_security_perimeter_name: The name of the network security perimeter.
    :param str resource_group_name: The name of the resource group.
    """
    ...
