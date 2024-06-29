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
from ._enums import *

__all__ = [
    'CustomerManagedKeyEncryptionPropertiesResponse',
    'CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity',
    'EncryptionPropertiesResponse',
    'FluidRelayEndpointsResponse',
    'IdentityResponse',
    'IdentityResponseUserAssignedIdentities',
    'SystemDataResponse',
]

@pulumi.output_type
class CustomerManagedKeyEncryptionPropertiesResponse(dict):
    """
    All Customer-managed key encryption properties for the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyEncryptionKeyIdentity":
            suggest = "key_encryption_key_identity"
        elif key == "keyEncryptionKeyUrl":
            suggest = "key_encryption_key_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomerManagedKeyEncryptionPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomerManagedKeyEncryptionPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomerManagedKeyEncryptionPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_encryption_key_identity: Optional['outputs.CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity'] = None,
                 key_encryption_key_url: Optional[str] = None):
        """
        All Customer-managed key encryption properties for the resource.
        :param 'CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity' key_encryption_key_identity: All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param str key_encryption_key_url: key encryption key Url, with or without a version. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek. Key auto rotation is enabled by providing a key uri without version. Otherwise, customer is responsible for rotating the key. The keyEncryptionKeyIdentity(either SystemAssigned or UserAssigned) should have permission to access this key url.
        """
        if key_encryption_key_identity is not None:
            pulumi.set(__self__, "key_encryption_key_identity", key_encryption_key_identity)
        if key_encryption_key_url is not None:
            pulumi.set(__self__, "key_encryption_key_url", key_encryption_key_url)

    @property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(self) -> Optional['outputs.CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity']:
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        return pulumi.get(self, "key_encryption_key_identity")

    @property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[str]:
        """
        key encryption key Url, with or without a version. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek. Key auto rotation is enabled by providing a key uri without version. Otherwise, customer is responsible for rotating the key. The keyEncryptionKeyIdentity(either SystemAssigned or UserAssigned) should have permission to access this key url.
        """
        return pulumi.get(self, "key_encryption_key_url")


@pulumi.output_type
class CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity(dict):
    """
    All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "identityType":
            suggest = "identity_type"
        elif key == "userAssignedIdentityResourceId":
            suggest = "user_assigned_identity_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identity_type: Optional[str] = None,
                 user_assigned_identity_resource_id: Optional[str] = None):
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param str identity_type: Values can be SystemAssigned or UserAssigned
        :param str user_assigned_identity_resource_id: user assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId. Mutually exclusive with identityType systemAssignedIdentity.
        """
        if identity_type is not None:
            pulumi.set(__self__, "identity_type", identity_type)
        if user_assigned_identity_resource_id is not None:
            pulumi.set(__self__, "user_assigned_identity_resource_id", user_assigned_identity_resource_id)

    @property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[str]:
        """
        Values can be SystemAssigned or UserAssigned
        """
        return pulumi.get(self, "identity_type")

    @property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[str]:
        """
        user assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId. Mutually exclusive with identityType systemAssignedIdentity.
        """
        return pulumi.get(self, "user_assigned_identity_resource_id")


@pulumi.output_type
class EncryptionPropertiesResponse(dict):
    """
    All encryption configuration for a resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customerManagedKeyEncryption":
            suggest = "customer_managed_key_encryption"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EncryptionPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EncryptionPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EncryptionPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 customer_managed_key_encryption: Optional['outputs.CustomerManagedKeyEncryptionPropertiesResponse'] = None):
        """
        All encryption configuration for a resource.
        :param 'CustomerManagedKeyEncryptionPropertiesResponse' customer_managed_key_encryption: All Customer-managed key encryption properties for the resource.
        """
        if customer_managed_key_encryption is not None:
            pulumi.set(__self__, "customer_managed_key_encryption", customer_managed_key_encryption)

    @property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(self) -> Optional['outputs.CustomerManagedKeyEncryptionPropertiesResponse']:
        """
        All Customer-managed key encryption properties for the resource.
        """
        return pulumi.get(self, "customer_managed_key_encryption")


@pulumi.output_type
class FluidRelayEndpointsResponse(dict):
    """
    The Fluid Relay endpoints for this server
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ordererEndpoints":
            suggest = "orderer_endpoints"
        elif key == "serviceEndpoints":
            suggest = "service_endpoints"
        elif key == "storageEndpoints":
            suggest = "storage_endpoints"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FluidRelayEndpointsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FluidRelayEndpointsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FluidRelayEndpointsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 orderer_endpoints: Sequence[str],
                 service_endpoints: Sequence[str],
                 storage_endpoints: Sequence[str]):
        """
        The Fluid Relay endpoints for this server
        :param Sequence[str] orderer_endpoints: The Fluid Relay Orderer endpoints.
        :param Sequence[str] service_endpoints: The Fluid Relay service endpoints.
        :param Sequence[str] storage_endpoints: The Fluid Relay storage endpoints.
        """
        pulumi.set(__self__, "orderer_endpoints", orderer_endpoints)
        pulumi.set(__self__, "service_endpoints", service_endpoints)
        pulumi.set(__self__, "storage_endpoints", storage_endpoints)

    @property
    @pulumi.getter(name="ordererEndpoints")
    def orderer_endpoints(self) -> Sequence[str]:
        """
        The Fluid Relay Orderer endpoints.
        """
        return pulumi.get(self, "orderer_endpoints")

    @property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> Sequence[str]:
        """
        The Fluid Relay service endpoints.
        """
        return pulumi.get(self, "service_endpoints")

    @property
    @pulumi.getter(name="storageEndpoints")
    def storage_endpoints(self) -> Sequence[str]:
        """
        The Fluid Relay storage endpoints.
        """
        return pulumi.get(self, "storage_endpoints")


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
                 type: Optional[str] = None,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.IdentityResponseUserAssignedIdentities']] = None):
        """
        Identity for the resource.
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        :param Mapping[str, 'IdentityResponseUserAssignedIdentities'] user_assigned_identities: The list of user identities associated with the resource.
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
    def type(self) -> Optional[str]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.IdentityResponseUserAssignedIdentities']]:
        """
        The list of user identities associated with the resource.
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


