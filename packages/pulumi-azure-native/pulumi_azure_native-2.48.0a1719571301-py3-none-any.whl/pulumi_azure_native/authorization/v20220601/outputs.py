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
from ._enums import *

__all__ = [
    'IdentityResponse',
    'IdentityResponseUserAssignedIdentities',
    'NonComplianceMessageResponse',
    'OverrideResponse',
    'ParameterValuesValueResponse',
    'ResourceSelectorResponse',
    'SelectorResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class IdentityResponse(dict):
    """
    Identity for the resource.  Policy assignments support a maximum of one identity.  That is either a system assigned identity or a single user assigned identity.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.IdentityResponseUserAssignedIdentities']] = None):
        """
        Identity for the resource.  Policy assignments support a maximum of one identity.  That is either a system assigned identity or a single user assigned identity.
        :param str principal_id: The principal ID of the resource identity.  This property will only be provided for a system assigned identity
        :param str tenant_id: The tenant ID of the resource identity.  This property will only be provided for a system assigned identity
        :param str type: The identity type. This is the only required field when adding a system or user assigned identity to a resource.
        :param Mapping[str, 'IdentityResponseUserAssignedIdentities'] user_assigned_identities: The user identity associated with the policy. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of the resource identity.  This property will only be provided for a system assigned identity
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the resource identity.  This property will only be provided for a system assigned identity
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type. This is the only required field when adding a system or user assigned identity to a resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.IdentityResponseUserAssignedIdentities']]:
        """
        The user identity associated with the policy. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class IdentityResponseUserAssignedIdentities(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponseUserAssignedIdentities. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponseUserAssignedIdentities.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponseUserAssignedIdentities.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 principal_id: str):
        """
        :param str client_id: The client id of user assigned identity.
        :param str principal_id: The principal id of user assigned identity.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client id of user assigned identity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal id of user assigned identity.
        """
        return pulumi.get(self, "principal_id")


@pulumi.output_type
class NonComplianceMessageResponse(dict):
    """
    A message that describes why a resource is non-compliant with the policy. This is shown in 'deny' error messages and on resource's non-compliant compliance results.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "policyDefinitionReferenceId":
            suggest = "policy_definition_reference_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NonComplianceMessageResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NonComplianceMessageResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NonComplianceMessageResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 message: str,
                 policy_definition_reference_id: Optional[str] = None):
        """
        A message that describes why a resource is non-compliant with the policy. This is shown in 'deny' error messages and on resource's non-compliant compliance results.
        :param str message: A message that describes why a resource is non-compliant with the policy. This is shown in 'deny' error messages and on resource's non-compliant compliance results.
        :param str policy_definition_reference_id: The policy definition reference ID within a policy set definition the message is intended for. This is only applicable if the policy assignment assigns a policy set definition. If this is not provided the message applies to all policies assigned by this policy assignment.
        """
        pulumi.set(__self__, "message", message)
        if policy_definition_reference_id is not None:
            pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        A message that describes why a resource is non-compliant with the policy. This is shown in 'deny' error messages and on resource's non-compliant compliance results.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[str]:
        """
        The policy definition reference ID within a policy set definition the message is intended for. This is only applicable if the policy assignment assigns a policy set definition. If this is not provided the message applies to all policies assigned by this policy assignment.
        """
        return pulumi.get(self, "policy_definition_reference_id")


@pulumi.output_type
class OverrideResponse(dict):
    """
    The policy property value override.
    """
    def __init__(__self__, *,
                 kind: Optional[str] = None,
                 selectors: Optional[Sequence['outputs.SelectorResponse']] = None,
                 value: Optional[str] = None):
        """
        The policy property value override.
        :param str kind: The override kind.
        :param Sequence['SelectorResponse'] selectors: The list of the selector expressions.
        :param str value: The value to override the policy property.
        """
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if selectors is not None:
            pulumi.set(__self__, "selectors", selectors)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The override kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def selectors(self) -> Optional[Sequence['outputs.SelectorResponse']]:
        """
        The list of the selector expressions.
        """
        return pulumi.get(self, "selectors")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value to override the policy property.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ParameterValuesValueResponse(dict):
    """
    The value of a parameter.
    """
    def __init__(__self__, *,
                 value: Optional[Any] = None):
        """
        The value of a parameter.
        :param Any value: The value of the parameter.
        """
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        """
        The value of the parameter.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ResourceSelectorResponse(dict):
    """
    The resource selector to filter policies by resource properties.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 selectors: Optional[Sequence['outputs.SelectorResponse']] = None):
        """
        The resource selector to filter policies by resource properties.
        :param str name: The name of the resource selector.
        :param Sequence['SelectorResponse'] selectors: The list of the selector expressions.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if selectors is not None:
            pulumi.set(__self__, "selectors", selectors)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource selector.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def selectors(self) -> Optional[Sequence['outputs.SelectorResponse']]:
        """
        The list of the selector expressions.
        """
        return pulumi.get(self, "selectors")


@pulumi.output_type
class SelectorResponse(dict):
    """
    The selector expression.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "in":
            suggest = "in_"
        elif key == "notIn":
            suggest = "not_in"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SelectorResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SelectorResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SelectorResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 in_: Optional[Sequence[str]] = None,
                 kind: Optional[str] = None,
                 not_in: Optional[Sequence[str]] = None):
        """
        The selector expression.
        :param Sequence[str] in_: The list of values to filter in.
        :param str kind: The selector kind.
        :param Sequence[str] not_in: The list of values to filter out.
        """
        if in_ is not None:
            pulumi.set(__self__, "in_", in_)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if not_in is not None:
            pulumi.set(__self__, "not_in", not_in)

    @property
    @pulumi.getter(name="in")
    def in_(self) -> Optional[Sequence[str]]:
        """
        The list of values to filter in.
        """
        return pulumi.get(self, "in_")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The selector kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="notIn")
    def not_in(self) -> Optional[Sequence[str]]:
        """
        The list of values to filter out.
        """
        return pulumi.get(self, "not_in")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


