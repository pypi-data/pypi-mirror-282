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
    'EncryptionPropertyResponse',
    'IdentityResponse',
    'IdentityResponseUserAssignedIdentities',
    'KeyVaultPropertiesResponse',
    'NotebookListCredentialsResultResponse',
    'NotebookPreparationErrorResponse',
    'NotebookResourceInfoResponse',
    'PasswordResponse',
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'RegistryListCredentialsResultResponse',
    'SharedPrivateLinkResourceResponse',
    'SkuResponse',
]

@pulumi.output_type
class EncryptionPropertyResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyVaultProperties":
            suggest = "key_vault_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EncryptionPropertyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EncryptionPropertyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EncryptionPropertyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_vault_properties: 'outputs.KeyVaultPropertiesResponse',
                 status: str):
        """
        :param 'KeyVaultPropertiesResponse' key_vault_properties: Customer Key vault properties.
        :param str status: Indicates whether or not the encryption is enabled for the workspace.
        """
        pulumi.set(__self__, "key_vault_properties", key_vault_properties)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> 'outputs.KeyVaultPropertiesResponse':
        """
        Customer Key vault properties.
        """
        return pulumi.get(self, "key_vault_properties")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Indicates whether or not the encryption is enabled for the workspace.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class IdentityResponse(dict):
    """
    Identity for the resource.
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
                 type: str,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.IdentityResponseUserAssignedIdentities']] = None):
        """
        Identity for the resource.
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        :param Mapping[str, 'IdentityResponseUserAssignedIdentities'] user_assigned_identities: The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.IdentityResponseUserAssignedIdentities']]:
        """
        The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
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
class KeyVaultPropertiesResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyIdentifier":
            suggest = "key_identifier"
        elif key == "keyVaultArmId":
            suggest = "key_vault_arm_id"
        elif key == "identityClientId":
            suggest = "identity_client_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in KeyVaultPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        KeyVaultPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        KeyVaultPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_identifier: str,
                 key_vault_arm_id: str,
                 identity_client_id: Optional[str] = None):
        """
        :param str key_identifier: Key vault uri to access the encryption key.
        :param str key_vault_arm_id: The ArmId of the keyVault where the customer owned encryption key is present.
        :param str identity_client_id: For future use - The client id of the identity which will be used to access key vault.
        """
        pulumi.set(__self__, "key_identifier", key_identifier)
        pulumi.set(__self__, "key_vault_arm_id", key_vault_arm_id)
        if identity_client_id is not None:
            pulumi.set(__self__, "identity_client_id", identity_client_id)

    @property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> str:
        """
        Key vault uri to access the encryption key.
        """
        return pulumi.get(self, "key_identifier")

    @property
    @pulumi.getter(name="keyVaultArmId")
    def key_vault_arm_id(self) -> str:
        """
        The ArmId of the keyVault where the customer owned encryption key is present.
        """
        return pulumi.get(self, "key_vault_arm_id")

    @property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[str]:
        """
        For future use - The client id of the identity which will be used to access key vault.
        """
        return pulumi.get(self, "identity_client_id")


@pulumi.output_type
class NotebookListCredentialsResultResponse(dict):
    def __init__(__self__, *,
                 primary_access_key: Optional[str] = None,
                 secondary_access_key: Optional[str] = None):
        if primary_access_key is not None:
            pulumi.set(__self__, "primary_access_key", primary_access_key)
        if secondary_access_key is not None:
            pulumi.set(__self__, "secondary_access_key", secondary_access_key)

    @property
    @pulumi.getter(name="primaryAccessKey")
    def primary_access_key(self) -> Optional[str]:
        return pulumi.get(self, "primary_access_key")

    @property
    @pulumi.getter(name="secondaryAccessKey")
    def secondary_access_key(self) -> Optional[str]:
        return pulumi.get(self, "secondary_access_key")


@pulumi.output_type
class NotebookPreparationErrorResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "errorMessage":
            suggest = "error_message"
        elif key == "statusCode":
            suggest = "status_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NotebookPreparationErrorResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NotebookPreparationErrorResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NotebookPreparationErrorResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 error_message: Optional[str] = None,
                 status_code: Optional[int] = None):
        if error_message is not None:
            pulumi.set(__self__, "error_message", error_message)
        if status_code is not None:
            pulumi.set(__self__, "status_code", status_code)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[str]:
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[int]:
        return pulumi.get(self, "status_code")


@pulumi.output_type
class NotebookResourceInfoResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "notebookPreparationError":
            suggest = "notebook_preparation_error"
        elif key == "resourceId":
            suggest = "resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NotebookResourceInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NotebookResourceInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NotebookResourceInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fqdn: Optional[str] = None,
                 notebook_preparation_error: Optional['outputs.NotebookPreparationErrorResponse'] = None,
                 resource_id: Optional[str] = None):
        """
        :param 'NotebookPreparationErrorResponse' notebook_preparation_error: The error that occurs when preparing notebook.
        :param str resource_id: the data plane resourceId that used to initialize notebook component
        """
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if notebook_preparation_error is not None:
            pulumi.set(__self__, "notebook_preparation_error", notebook_preparation_error)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[str]:
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="notebookPreparationError")
    def notebook_preparation_error(self) -> Optional['outputs.NotebookPreparationErrorResponse']:
        """
        The error that occurs when preparing notebook.
        """
        return pulumi.get(self, "notebook_preparation_error")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        the data plane resourceId that used to initialize notebook component
        """
        return pulumi.get(self, "resource_id")


@pulumi.output_type
class PasswordResponse(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    The Private Endpoint Connection resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 private_link_service_connection_state: 'outputs.PrivateLinkServiceConnectionStateResponse',
                 provisioning_state: str,
                 type: str,
                 private_endpoint: Optional['outputs.PrivateEndpointResponse'] = None):
        """
        The Private Endpoint Connection resource.
        :param str id: ResourceId of the private endpoint connection.
        :param str name: Friendly name of the private endpoint connection.
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param str provisioning_state: The provisioning state of the private endpoint connection resource.
        :param str type: Resource type of private endpoint connection.
        :param 'PrivateEndpointResponse' private_endpoint: The resource of private end point.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "type", type)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ResourceId of the private endpoint connection.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Friendly name of the private endpoint connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type of private endpoint connection.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointResponse']:
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The Private Endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The Private Endpoint resource.
        :param str id: The ARM identifier for Private Endpoint
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for Private Endpoint
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class RegistryListCredentialsResultResponse(dict):
    def __init__(__self__, *,
                 location: str,
                 username: str,
                 passwords: Optional[Sequence['outputs.PasswordResponse']] = None):
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "username", username)
        if passwords is not None:
            pulumi.set(__self__, "passwords", passwords)

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")

    @property
    @pulumi.getter
    def passwords(self) -> Optional[Sequence['outputs.PasswordResponse']]:
        return pulumi.get(self, "passwords")


@pulumi.output_type
class SharedPrivateLinkResourceResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupId":
            suggest = "group_id"
        elif key == "privateLinkResourceId":
            suggest = "private_link_resource_id"
        elif key == "requestMessage":
            suggest = "request_message"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SharedPrivateLinkResourceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SharedPrivateLinkResourceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SharedPrivateLinkResourceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_id: Optional[str] = None,
                 name: Optional[str] = None,
                 private_link_resource_id: Optional[str] = None,
                 request_message: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str group_id: The private link resource group id.
        :param str name: Unique name of the private link.
        :param str private_link_resource_id: The resource id that private link links to.
        :param str request_message: Request message.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_link_resource_id is not None:
            pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if request_message is not None:
            pulumi.set(__self__, "request_message", request_message)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        """
        The private link resource group id.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Unique name of the private link.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[str]:
        """
        The resource id that private link links to.
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[str]:
        """
        Request message.
        """
        return pulumi.get(self, "request_message")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class SkuResponse(dict):
    """
    Sku of the resource
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        Sku of the resource
        :param str name: Name of the sku
        :param str tier: Tier of the sku like Basic or Enterprise
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the sku
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        Tier of the sku like Basic or Enterprise
        """
        return pulumi.get(self, "tier")


