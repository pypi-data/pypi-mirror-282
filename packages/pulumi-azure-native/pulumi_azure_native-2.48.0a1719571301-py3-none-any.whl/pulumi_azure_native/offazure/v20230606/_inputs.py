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
    'PrivateLinkServiceConnectionStateArgs',
    'SiteAgentPropertiesArgs',
    'SiteAppliancePropertiesArgs',
    'SiteSpnPropertiesArgs',
]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateLinkServiceConnectionStateStatus']]] = None):
        """
        Service Connection State
        :param pulumi.Input[str] actions_required: actions required
        :param pulumi.Input[str] description: description string
        :param pulumi.Input[Union[str, 'PrivateLinkServiceConnectionStateStatus']] status: state status
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
        actions required
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description string
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateLinkServiceConnectionStateStatus']]]:
        """
        state status
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateLinkServiceConnectionStateStatus']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class SiteAgentPropertiesArgs:
    def __init__(__self__, *,
                 key_vault_id: Optional[pulumi.Input[str]] = None,
                 key_vault_uri: Optional[pulumi.Input[str]] = None):
        """
        Class for site agent properties.
        :param pulumi.Input[str] key_vault_id: Gets or sets the key vault ARM Id.
        :param pulumi.Input[str] key_vault_uri: Gets or sets the key vault URI.
        """
        if key_vault_id is not None:
            pulumi.set(__self__, "key_vault_id", key_vault_id)
        if key_vault_uri is not None:
            pulumi.set(__self__, "key_vault_uri", key_vault_uri)

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the key vault ARM Id.
        """
        return pulumi.get(self, "key_vault_id")

    @key_vault_id.setter
    def key_vault_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_id", value)

    @property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the key vault URI.
        """
        return pulumi.get(self, "key_vault_uri")

    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_uri", value)


@pulumi.input_type
class SiteAppliancePropertiesArgs:
    def __init__(__self__, *,
                 agent_details: Optional[pulumi.Input['SiteAgentPropertiesArgs']] = None,
                 appliance_name: Optional[pulumi.Input[str]] = None,
                 service_principal_identity_details: Optional[pulumi.Input['SiteSpnPropertiesArgs']] = None):
        """
        Class for site appliance properties.
        :param pulumi.Input['SiteAgentPropertiesArgs'] agent_details: Gets or sets the on-premises agent details.
        :param pulumi.Input[str] appliance_name: Gets or sets the Appliance Name.
        :param pulumi.Input['SiteSpnPropertiesArgs'] service_principal_identity_details:  Gets or sets the service principal identity details used by agent for  communication              to the service.  
        """
        if agent_details is not None:
            pulumi.set(__self__, "agent_details", agent_details)
        if appliance_name is not None:
            pulumi.set(__self__, "appliance_name", appliance_name)
        if service_principal_identity_details is not None:
            pulumi.set(__self__, "service_principal_identity_details", service_principal_identity_details)

    @property
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Optional[pulumi.Input['SiteAgentPropertiesArgs']]:
        """
        Gets or sets the on-premises agent details.
        """
        return pulumi.get(self, "agent_details")

    @agent_details.setter
    def agent_details(self, value: Optional[pulumi.Input['SiteAgentPropertiesArgs']]):
        pulumi.set(self, "agent_details", value)

    @property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the Appliance Name.
        """
        return pulumi.get(self, "appliance_name")

    @appliance_name.setter
    def appliance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "appliance_name", value)

    @property
    @pulumi.getter(name="servicePrincipalIdentityDetails")
    def service_principal_identity_details(self) -> Optional[pulumi.Input['SiteSpnPropertiesArgs']]:
        """
         Gets or sets the service principal identity details used by agent for  communication              to the service.  
        """
        return pulumi.get(self, "service_principal_identity_details")

    @service_principal_identity_details.setter
    def service_principal_identity_details(self, value: Optional[pulumi.Input['SiteSpnPropertiesArgs']]):
        pulumi.set(self, "service_principal_identity_details", value)


@pulumi.input_type
class SiteSpnPropertiesArgs:
    def __init__(__self__, *,
                 aad_authority: Optional[pulumi.Input[str]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 audience: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 raw_cert_data: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        Class for site properties.
        :param pulumi.Input[str] aad_authority: Gets or sets the AAD Authority URL which was used to request the token for
               the
                           service principal.
        :param pulumi.Input[str] application_id: Gets or sets the application/client Id for the service principal with which
               the
                           on-premise management/data plane components would communicate
               with our Azure 
                           services.
        :param pulumi.Input[str] audience: Gets or sets the intended audience for the service principal.
        :param pulumi.Input[str] object_id: Gets or sets the object Id of the service principal with which the on-premise
               
                          management/data plane components would communicate with our Azure
               services.
        :param pulumi.Input[str] raw_cert_data: Gets or sets the raw certificate data for building certificate expiry flows.
        :param pulumi.Input[str] tenant_id: Gets or sets the tenant Id for the service principal with which the
               on-premise
                           management/data plane components would communicate with
               our Azure services.
        """
        if aad_authority is not None:
            pulumi.set(__self__, "aad_authority", aad_authority)
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if audience is not None:
            pulumi.set(__self__, "audience", audience)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if raw_cert_data is not None:
            pulumi.set(__self__, "raw_cert_data", raw_cert_data)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the AAD Authority URL which was used to request the token for
        the
                    service principal.
        """
        return pulumi.get(self, "aad_authority")

    @aad_authority.setter
    def aad_authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aad_authority", value)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the application/client Id for the service principal with which
        the
                    on-premise management/data plane components would communicate
        with our Azure 
                    services.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the intended audience for the service principal.
        """
        return pulumi.get(self, "audience")

    @audience.setter
    def audience(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audience", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the object Id of the service principal with which the on-premise

                   management/data plane components would communicate with our Azure
        services.
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter(name="rawCertData")
    def raw_cert_data(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the raw certificate data for building certificate expiry flows.
        """
        return pulumi.get(self, "raw_cert_data")

    @raw_cert_data.setter
    def raw_cert_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raw_cert_data", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the tenant Id for the service principal with which the
        on-premise
                    management/data plane components would communicate with
        our Azure services.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


