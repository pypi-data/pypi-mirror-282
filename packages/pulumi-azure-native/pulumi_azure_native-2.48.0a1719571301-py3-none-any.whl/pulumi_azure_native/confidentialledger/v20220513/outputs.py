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
    'AADBasedSecurityPrincipalResponse',
    'CertBasedSecurityPrincipalResponse',
    'LedgerPropertiesResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class AADBasedSecurityPrincipalResponse(dict):
    """
    AAD based security principal with associated Ledger RoleName
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ledgerRoleName":
            suggest = "ledger_role_name"
        elif key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AADBasedSecurityPrincipalResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AADBasedSecurityPrincipalResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AADBasedSecurityPrincipalResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ledger_role_name: Optional[str] = None,
                 principal_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        AAD based security principal with associated Ledger RoleName
        :param str ledger_role_name: LedgerRole associated with the Security Principal of Ledger
        :param str principal_id: UUID/GUID based Principal Id of the Security Principal
        :param str tenant_id: UUID/GUID based Tenant Id of the Security Principal
        """
        if ledger_role_name is not None:
            pulumi.set(__self__, "ledger_role_name", ledger_role_name)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> Optional[str]:
        """
        LedgerRole associated with the Security Principal of Ledger
        """
        return pulumi.get(self, "ledger_role_name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        UUID/GUID based Principal Id of the Security Principal
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        UUID/GUID based Tenant Id of the Security Principal
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class CertBasedSecurityPrincipalResponse(dict):
    """
    Cert based security principal with Ledger RoleName
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ledgerRoleName":
            suggest = "ledger_role_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CertBasedSecurityPrincipalResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CertBasedSecurityPrincipalResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CertBasedSecurityPrincipalResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cert: Optional[str] = None,
                 ledger_role_name: Optional[str] = None):
        """
        Cert based security principal with Ledger RoleName
        :param str cert: Public key of the user cert (.pem or .cer)
        :param str ledger_role_name: LedgerRole associated with the Security Principal of Ledger
        """
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if ledger_role_name is not None:
            pulumi.set(__self__, "ledger_role_name", ledger_role_name)

    @property
    @pulumi.getter
    def cert(self) -> Optional[str]:
        """
        Public key of the user cert (.pem or .cer)
        """
        return pulumi.get(self, "cert")

    @property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> Optional[str]:
        """
        LedgerRole associated with the Security Principal of Ledger
        """
        return pulumi.get(self, "ledger_role_name")


@pulumi.output_type
class LedgerPropertiesResponse(dict):
    """
    Additional Confidential Ledger properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "identityServiceUri":
            suggest = "identity_service_uri"
        elif key == "ledgerInternalNamespace":
            suggest = "ledger_internal_namespace"
        elif key == "ledgerName":
            suggest = "ledger_name"
        elif key == "ledgerUri":
            suggest = "ledger_uri"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "aadBasedSecurityPrincipals":
            suggest = "aad_based_security_principals"
        elif key == "certBasedSecurityPrincipals":
            suggest = "cert_based_security_principals"
        elif key == "ledgerType":
            suggest = "ledger_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LedgerPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LedgerPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LedgerPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identity_service_uri: str,
                 ledger_internal_namespace: str,
                 ledger_name: str,
                 ledger_uri: str,
                 provisioning_state: str,
                 aad_based_security_principals: Optional[Sequence['outputs.AADBasedSecurityPrincipalResponse']] = None,
                 cert_based_security_principals: Optional[Sequence['outputs.CertBasedSecurityPrincipalResponse']] = None,
                 ledger_type: Optional[str] = None):
        """
        Additional Confidential Ledger properties.
        :param str identity_service_uri: Endpoint for accessing network identity.
        :param str ledger_internal_namespace: Internal namespace for the Ledger
        :param str ledger_name: Unique name for the Confidential Ledger.
        :param str ledger_uri: Endpoint for calling Ledger Service.
        :param str provisioning_state: Provisioning state of Ledger Resource
        :param Sequence['AADBasedSecurityPrincipalResponse'] aad_based_security_principals: Array of all AAD based Security Principals.
        :param Sequence['CertBasedSecurityPrincipalResponse'] cert_based_security_principals: Array of all cert based Security Principals.
        :param str ledger_type: Type of Confidential Ledger
        """
        pulumi.set(__self__, "identity_service_uri", identity_service_uri)
        pulumi.set(__self__, "ledger_internal_namespace", ledger_internal_namespace)
        pulumi.set(__self__, "ledger_name", ledger_name)
        pulumi.set(__self__, "ledger_uri", ledger_uri)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if aad_based_security_principals is not None:
            pulumi.set(__self__, "aad_based_security_principals", aad_based_security_principals)
        if cert_based_security_principals is not None:
            pulumi.set(__self__, "cert_based_security_principals", cert_based_security_principals)
        if ledger_type is not None:
            pulumi.set(__self__, "ledger_type", ledger_type)

    @property
    @pulumi.getter(name="identityServiceUri")
    def identity_service_uri(self) -> str:
        """
        Endpoint for accessing network identity.
        """
        return pulumi.get(self, "identity_service_uri")

    @property
    @pulumi.getter(name="ledgerInternalNamespace")
    def ledger_internal_namespace(self) -> str:
        """
        Internal namespace for the Ledger
        """
        return pulumi.get(self, "ledger_internal_namespace")

    @property
    @pulumi.getter(name="ledgerName")
    def ledger_name(self) -> str:
        """
        Unique name for the Confidential Ledger.
        """
        return pulumi.get(self, "ledger_name")

    @property
    @pulumi.getter(name="ledgerUri")
    def ledger_uri(self) -> str:
        """
        Endpoint for calling Ledger Service.
        """
        return pulumi.get(self, "ledger_uri")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of Ledger Resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="aadBasedSecurityPrincipals")
    def aad_based_security_principals(self) -> Optional[Sequence['outputs.AADBasedSecurityPrincipalResponse']]:
        """
        Array of all AAD based Security Principals.
        """
        return pulumi.get(self, "aad_based_security_principals")

    @property
    @pulumi.getter(name="certBasedSecurityPrincipals")
    def cert_based_security_principals(self) -> Optional[Sequence['outputs.CertBasedSecurityPrincipalResponse']]:
        """
        Array of all cert based Security Principals.
        """
        return pulumi.get(self, "cert_based_security_principals")

    @property
    @pulumi.getter(name="ledgerType")
    def ledger_type(self) -> Optional[str]:
        """
        Type of Confidential Ledger
        """
        return pulumi.get(self, "ledger_type")


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


