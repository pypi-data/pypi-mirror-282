# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ContactArgs',
    'DeploymentServerArgs',
    'EnvironmentServerArgs',
    'ExternalDocumentationArgs',
    'LicenseArgs',
    'ManagedServiceIdentityArgs',
    'MetadataAssignmentArgs',
    'OnboardingArgs',
    'TermsOfServiceArgs',
]

@pulumi.input_type
class ContactArgs:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Contact information
        :param pulumi.Input[str] email: Email address of the contact.
        :param pulumi.Input[str] name: Name of the contact.
        :param pulumi.Input[str] url: URL for the contact.
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the contact.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the contact.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL for the contact.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class DeploymentServerArgs:
    def __init__(__self__, *,
                 runtime_uri: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Server
        :param pulumi.Input[Sequence[pulumi.Input[str]]] runtime_uri: Base runtime URLs for this deployment.
        """
        if runtime_uri is not None:
            pulumi.set(__self__, "runtime_uri", runtime_uri)

    @property
    @pulumi.getter(name="runtimeUri")
    def runtime_uri(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Base runtime URLs for this deployment.
        """
        return pulumi.get(self, "runtime_uri")

    @runtime_uri.setter
    def runtime_uri(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "runtime_uri", value)


@pulumi.input_type
class EnvironmentServerArgs:
    def __init__(__self__, *,
                 management_portal_uri: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[Union[str, 'EnvironmentServerType']]] = None):
        """
        Server information of the environment.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] management_portal_uri: The location of the management portal
        :param pulumi.Input[Union[str, 'EnvironmentServerType']] type: Type of the server that represents the environment.
        """
        if management_portal_uri is not None:
            pulumi.set(__self__, "management_portal_uri", management_portal_uri)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="managementPortalUri")
    def management_portal_uri(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The location of the management portal
        """
        return pulumi.get(self, "management_portal_uri")

    @management_portal_uri.setter
    def management_portal_uri(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "management_portal_uri", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'EnvironmentServerType']]]:
        """
        Type of the server that represents the environment.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'EnvironmentServerType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ExternalDocumentationArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Additional, external documentation for the API.
        :param pulumi.Input[str] url: URL pointing to the documentation.
        :param pulumi.Input[str] description: Description of the documentation.
        :param pulumi.Input[str] title: Title of the documentation.
        """
        pulumi.set(__self__, "url", url)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL pointing to the documentation.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the documentation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Title of the documentation.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class LicenseArgs:
    def __init__(__self__, *,
                 identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The license information for the API.
        :param pulumi.Input[str] identifier: SPDX license information for the API. The identifier field is mutually
               exclusive of the URL field.
        :param pulumi.Input[str] name: Name of the license.
        :param pulumi.Input[str] url: URL pointing to the license details. The URL field is mutually exclusive of the
               identifier field.
        """
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        SPDX license information for the API. The identifier field is mutually
        exclusive of the URL field.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the license.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL pointing to the license details. The URL field is mutually exclusive of the
        identifier field.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[Union[str, 'ManagedServiceIdentityType']] type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ManagedServiceIdentityType']]:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class MetadataAssignmentArgs:
    def __init__(__self__, *,
                 deprecated: Optional[pulumi.Input[bool]] = None,
                 entity: Optional[pulumi.Input[Union[str, 'MetadataAssignmentEntity']]] = None,
                 required: Optional[pulumi.Input[bool]] = None):
        """
        Assignment metadata
        :param pulumi.Input[bool] deprecated: Deprecated assignment
        :param pulumi.Input[Union[str, 'MetadataAssignmentEntity']] entity: The entities this metadata schema component gets applied to.
        :param pulumi.Input[bool] required: Required assignment
        """
        if deprecated is not None:
            pulumi.set(__self__, "deprecated", deprecated)
        if entity is not None:
            pulumi.set(__self__, "entity", entity)
        if required is not None:
            pulumi.set(__self__, "required", required)

    @property
    @pulumi.getter
    def deprecated(self) -> Optional[pulumi.Input[bool]]:
        """
        Deprecated assignment
        """
        return pulumi.get(self, "deprecated")

    @deprecated.setter
    def deprecated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deprecated", value)

    @property
    @pulumi.getter
    def entity(self) -> Optional[pulumi.Input[Union[str, 'MetadataAssignmentEntity']]]:
        """
        The entities this metadata schema component gets applied to.
        """
        return pulumi.get(self, "entity")

    @entity.setter
    def entity(self, value: Optional[pulumi.Input[Union[str, 'MetadataAssignmentEntity']]]):
        pulumi.set(self, "entity", value)

    @property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[bool]]:
        """
        Required assignment
        """
        return pulumi.get(self, "required")

    @required.setter
    def required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "required", value)


@pulumi.input_type
class OnboardingArgs:
    def __init__(__self__, *,
                 developer_portal_uri: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instructions: Optional[pulumi.Input[str]] = None):
        """
        Onboarding information
        :param pulumi.Input[Sequence[pulumi.Input[str]]] developer_portal_uri: The location of the development portal
        :param pulumi.Input[str] instructions: Onboarding guide.
        """
        if developer_portal_uri is not None:
            pulumi.set(__self__, "developer_portal_uri", developer_portal_uri)
        if instructions is not None:
            pulumi.set(__self__, "instructions", instructions)

    @property
    @pulumi.getter(name="developerPortalUri")
    def developer_portal_uri(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The location of the development portal
        """
        return pulumi.get(self, "developer_portal_uri")

    @developer_portal_uri.setter
    def developer_portal_uri(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "developer_portal_uri", value)

    @property
    @pulumi.getter
    def instructions(self) -> Optional[pulumi.Input[str]]:
        """
        Onboarding guide.
        """
        return pulumi.get(self, "instructions")

    @instructions.setter
    def instructions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instructions", value)


@pulumi.input_type
class TermsOfServiceArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str]):
        """
        Terms of service for the API.
        :param pulumi.Input[str] url: URL pointing to the terms of service.
        """
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL pointing to the terms of service.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)


