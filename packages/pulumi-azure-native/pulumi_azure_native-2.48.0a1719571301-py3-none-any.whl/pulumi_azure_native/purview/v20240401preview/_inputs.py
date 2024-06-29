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
    'AccountSkuArgs',
    'CredentialsArgs',
    'IdentityArgs',
    'IngestionStorageArgs',
    'PrivateEndpointArgs',
    'PrivateLinkServiceConnectionStateArgs',
]

@pulumi.input_type
class AccountSkuArgs:
    def __init__(__self__, *,
                 capacity: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[Union[str, 'AccountSkuName']]] = None):
        """
        Gets or sets the Sku.
        :param pulumi.Input[int] capacity: Gets or sets the sku capacity.
        :param pulumi.Input[Union[str, 'AccountSkuName']] name: Gets or sets the sku name.
        """
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        Gets or sets the sku capacity.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[str, 'AccountSkuName']]]:
        """
        Gets or sets the sku name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[str, 'AccountSkuName']]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class CredentialsArgs:
    def __init__(__self__, *,
                 identity_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'KafkaConfigurationIdentityType']]] = None):
        """
        Credentials to access the event streaming service attached to the purview account.
        :param pulumi.Input[str] identity_id: Identity identifier for UserAssign type.
        :param pulumi.Input[Union[str, 'KafkaConfigurationIdentityType']] type: Identity Type.
        """
        if identity_id is not None:
            pulumi.set(__self__, "identity_id", identity_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identity identifier for UserAssign type.
        """
        return pulumi.get(self, "identity_id")

    @identity_id.setter
    def identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'KafkaConfigurationIdentityType']]]:
        """
        Identity Type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'KafkaConfigurationIdentityType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]] = None,
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The Managed Identity of the resource
        :param pulumi.Input[Union[str, 'ManagedIdentityType']] type: Identity Type
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: User Assigned Identities
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]]:
        """
        Identity Type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        User Assigned Identities
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class IngestionStorageArgs:
    def __init__(__self__, *,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None):
        """
        Ingestion Storage Account Info
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Gets or sets the public network access setting
        """
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        Gets or sets the public network access setting
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)


@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        A private endpoint class.
        :param pulumi.Input[str] id: The private endpoint identifier.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The private endpoint identifier.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointConnectionStatus']]] = None):
        """
        The private link service connection state.
        :param pulumi.Input[str] actions_required: The required actions.
        :param pulumi.Input[str] description: The description.
        :param pulumi.Input[Union[str, 'PrivateEndpointConnectionStatus']] status: The status.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        The required actions.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointConnectionStatus']]]:
        """
        The status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointConnectionStatus']]]):
        pulumi.set(self, "status", value)


