# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AzureHybridBenefitPropertiesArgs',
    'DatabaseInstancePropertiesArgs',
    'DomainControllerPropertiesArgs',
    'DomainUserCredentialsArgs',
    'GmsaDetailsArgs',
    'ManagedIdentityArgs',
    'MonitoringInstancePropertiesArgs',
]

@pulumi.input_type
class AzureHybridBenefitPropertiesArgs:
    def __init__(__self__, *,
                 scom_license_type: Optional[pulumi.Input[Union[str, 'HybridLicenseType']]] = None,
                 sql_server_license_type: Optional[pulumi.Input[Union[str, 'HybridLicenseType']]] = None,
                 windows_server_license_type: Optional[pulumi.Input[Union[str, 'HybridLicenseType']]] = None):
        """
        The properties to maximize savings by using Azure Hybrid Benefit
        :param pulumi.Input[Union[str, 'HybridLicenseType']] scom_license_type: SCOM license type. Maximize savings by using license you already own
        :param pulumi.Input[Union[str, 'HybridLicenseType']] sql_server_license_type: SQL Server license type. Maximize savings by using Azure Hybrid Benefit for SQL Server with license you already own
        :param pulumi.Input[Union[str, 'HybridLicenseType']] windows_server_license_type: Specifies that the image or disk that is being used was licensed on-premises. <br><br> For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
        """
        if scom_license_type is not None:
            pulumi.set(__self__, "scom_license_type", scom_license_type)
        if sql_server_license_type is not None:
            pulumi.set(__self__, "sql_server_license_type", sql_server_license_type)
        if windows_server_license_type is not None:
            pulumi.set(__self__, "windows_server_license_type", windows_server_license_type)

    @property
    @pulumi.getter(name="scomLicenseType")
    def scom_license_type(self) -> Optional[pulumi.Input[Union[str, 'HybridLicenseType']]]:
        """
        SCOM license type. Maximize savings by using license you already own
        """
        return pulumi.get(self, "scom_license_type")

    @scom_license_type.setter
    def scom_license_type(self, value: Optional[pulumi.Input[Union[str, 'HybridLicenseType']]]):
        pulumi.set(self, "scom_license_type", value)

    @property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[pulumi.Input[Union[str, 'HybridLicenseType']]]:
        """
        SQL Server license type. Maximize savings by using Azure Hybrid Benefit for SQL Server with license you already own
        """
        return pulumi.get(self, "sql_server_license_type")

    @sql_server_license_type.setter
    def sql_server_license_type(self, value: Optional[pulumi.Input[Union[str, 'HybridLicenseType']]]):
        pulumi.set(self, "sql_server_license_type", value)

    @property
    @pulumi.getter(name="windowsServerLicenseType")
    def windows_server_license_type(self) -> Optional[pulumi.Input[Union[str, 'HybridLicenseType']]]:
        """
        Specifies that the image or disk that is being used was licensed on-premises. <br><br> For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
        """
        return pulumi.get(self, "windows_server_license_type")

    @windows_server_license_type.setter
    def windows_server_license_type(self, value: Optional[pulumi.Input[Union[str, 'HybridLicenseType']]]):
        pulumi.set(self, "windows_server_license_type", value)


@pulumi.input_type
class DatabaseInstancePropertiesArgs:
    def __init__(__self__, *,
                 database_instance_id: Optional[pulumi.Input[str]] = None):
        """
        The properties of database instance
        :param pulumi.Input[str] database_instance_id: Resource Id of existing database instance
        """
        if database_instance_id is not None:
            pulumi.set(__self__, "database_instance_id", database_instance_id)

    @property
    @pulumi.getter(name="databaseInstanceId")
    def database_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id of existing database instance
        """
        return pulumi.get(self, "database_instance_id")

    @database_instance_id.setter
    def database_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_instance_id", value)


@pulumi.input_type
class DomainControllerPropertiesArgs:
    def __init__(__self__, *,
                 dns_server: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 ou_path: Optional[pulumi.Input[str]] = None):
        """
        The properties of domain controller to which SCOM and SQL servers join for AuthN/AuthZ.
        :param pulumi.Input[str] dns_server: IP address of DNS server 
        :param pulumi.Input[str] domain_name: Fully qualified domain name
        :param pulumi.Input[str] ou_path: Organizational Unit path in which the SCOM servers will be present
        """
        if dns_server is not None:
            pulumi.set(__self__, "dns_server", dns_server)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if ou_path is None:
            ou_path = ''
        if ou_path is not None:
            pulumi.set(__self__, "ou_path", ou_path)

    @property
    @pulumi.getter(name="dnsServer")
    def dns_server(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of DNS server 
        """
        return pulumi.get(self, "dns_server")

    @dns_server.setter
    def dns_server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_server", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Fully qualified domain name
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="ouPath")
    def ou_path(self) -> Optional[pulumi.Input[str]]:
        """
        Organizational Unit path in which the SCOM servers will be present
        """
        return pulumi.get(self, "ou_path")

    @ou_path.setter
    def ou_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ou_path", value)


@pulumi.input_type
class DomainUserCredentialsArgs:
    def __init__(__self__, *,
                 key_vault_url: Optional[pulumi.Input[str]] = None,
                 password_secret: Optional[pulumi.Input[str]] = None,
                 user_name_secret: Optional[pulumi.Input[str]] = None):
        """
        Get Domain user name and password from key vault
        :param pulumi.Input[str] key_vault_url: Key vault url to get the domain username and password
        :param pulumi.Input[str] password_secret: Domain Password secret 
        :param pulumi.Input[str] user_name_secret: Domain user name secret 
        """
        if key_vault_url is not None:
            pulumi.set(__self__, "key_vault_url", key_vault_url)
        if password_secret is not None:
            pulumi.set(__self__, "password_secret", password_secret)
        if user_name_secret is not None:
            pulumi.set(__self__, "user_name_secret", user_name_secret)

    @property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[pulumi.Input[str]]:
        """
        Key vault url to get the domain username and password
        """
        return pulumi.get(self, "key_vault_url")

    @key_vault_url.setter
    def key_vault_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_url", value)

    @property
    @pulumi.getter(name="passwordSecret")
    def password_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Domain Password secret 
        """
        return pulumi.get(self, "password_secret")

    @password_secret.setter
    def password_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_secret", value)

    @property
    @pulumi.getter(name="userNameSecret")
    def user_name_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Domain user name secret 
        """
        return pulumi.get(self, "user_name_secret")

    @user_name_secret.setter
    def user_name_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name_secret", value)


@pulumi.input_type
class GmsaDetailsArgs:
    def __init__(__self__, *,
                 dns_name: Optional[pulumi.Input[str]] = None,
                 gmsa_account: Optional[pulumi.Input[str]] = None,
                 load_balancer_ip: Optional[pulumi.Input[str]] = None,
                 management_server_group_name: Optional[pulumi.Input[str]] = None):
        """
        Gmsa Details
        :param pulumi.Input[str] dns_name: Frontend DNS name for Load Balancer which will be used by Agents to initiate communication
        :param pulumi.Input[str] gmsa_account: gMSA account under which context all Management Server services will run
        :param pulumi.Input[str] load_balancer_ip: Frontend IP configuration for Load Balancer, which should be an available IP in customer VNet
        :param pulumi.Input[str] management_server_group_name: OnPrem AD Computer Group where we will join VMs for ease of management
        """
        if dns_name is not None:
            pulumi.set(__self__, "dns_name", dns_name)
        if gmsa_account is not None:
            pulumi.set(__self__, "gmsa_account", gmsa_account)
        if load_balancer_ip is not None:
            pulumi.set(__self__, "load_balancer_ip", load_balancer_ip)
        if management_server_group_name is not None:
            pulumi.set(__self__, "management_server_group_name", management_server_group_name)

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[str]]:
        """
        Frontend DNS name for Load Balancer which will be used by Agents to initiate communication
        """
        return pulumi.get(self, "dns_name")

    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_name", value)

    @property
    @pulumi.getter(name="gmsaAccount")
    def gmsa_account(self) -> Optional[pulumi.Input[str]]:
        """
        gMSA account under which context all Management Server services will run
        """
        return pulumi.get(self, "gmsa_account")

    @gmsa_account.setter
    def gmsa_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gmsa_account", value)

    @property
    @pulumi.getter(name="loadBalancerIP")
    def load_balancer_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Frontend IP configuration for Load Balancer, which should be an available IP in customer VNet
        """
        return pulumi.get(self, "load_balancer_ip")

    @load_balancer_ip.setter
    def load_balancer_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "load_balancer_ip", value)

    @property
    @pulumi.getter(name="managementServerGroupName")
    def management_server_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        OnPrem AD Computer Group where we will join VMs for ease of management
        """
        return pulumi.get(self, "management_server_group_name")

    @management_server_group_name.setter
    def management_server_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_server_group_name", value)


@pulumi.input_type
class ManagedIdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]] = None,
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Azure Active Directory identity configuration for a resource.
        :param pulumi.Input[Union[str, 'ManagedIdentityType']] type: The identity type
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The resource ids of the user assigned identities to use
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]]:
        """
        The identity type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The resource ids of the user assigned identities to use
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class MonitoringInstancePropertiesArgs:
    def __init__(__self__, *,
                 azure_hybrid_benefit: Optional[pulumi.Input['AzureHybridBenefitPropertiesArgs']] = None,
                 database_instance: Optional[pulumi.Input['DatabaseInstancePropertiesArgs']] = None,
                 domain_controller: Optional[pulumi.Input['DomainControllerPropertiesArgs']] = None,
                 domain_user_credentials: Optional[pulumi.Input['DomainUserCredentialsArgs']] = None,
                 gmsa_details: Optional[pulumi.Input['GmsaDetailsArgs']] = None,
                 v_net_subnet_id: Optional[pulumi.Input[str]] = None):
        """
        The properties of a SCOM instance resource
        :param pulumi.Input['AzureHybridBenefitPropertiesArgs'] azure_hybrid_benefit: The properties to enable Azure Hybrid benefit for various SCOM infrastructure license.
        :param pulumi.Input['DatabaseInstancePropertiesArgs'] database_instance: The database instance where the SCOM Operational and Warehouse databases will be stored.
        :param pulumi.Input['DomainControllerPropertiesArgs'] domain_controller: Domain controller details
        :param pulumi.Input['DomainUserCredentialsArgs'] domain_user_credentials: Domain user which will be used to join VMs to domain and login to VMs.
        :param pulumi.Input['GmsaDetailsArgs'] gmsa_details: Gmsa Details for load balancer and vmss
        :param pulumi.Input[str] v_net_subnet_id: Virtual Network subnet id on which Aquila instance will be provisioned
        """
        if azure_hybrid_benefit is not None:
            pulumi.set(__self__, "azure_hybrid_benefit", azure_hybrid_benefit)
        if database_instance is not None:
            pulumi.set(__self__, "database_instance", database_instance)
        if domain_controller is not None:
            pulumi.set(__self__, "domain_controller", domain_controller)
        if domain_user_credentials is not None:
            pulumi.set(__self__, "domain_user_credentials", domain_user_credentials)
        if gmsa_details is not None:
            pulumi.set(__self__, "gmsa_details", gmsa_details)
        if v_net_subnet_id is not None:
            pulumi.set(__self__, "v_net_subnet_id", v_net_subnet_id)

    @property
    @pulumi.getter(name="azureHybridBenefit")
    def azure_hybrid_benefit(self) -> Optional[pulumi.Input['AzureHybridBenefitPropertiesArgs']]:
        """
        The properties to enable Azure Hybrid benefit for various SCOM infrastructure license.
        """
        return pulumi.get(self, "azure_hybrid_benefit")

    @azure_hybrid_benefit.setter
    def azure_hybrid_benefit(self, value: Optional[pulumi.Input['AzureHybridBenefitPropertiesArgs']]):
        pulumi.set(self, "azure_hybrid_benefit", value)

    @property
    @pulumi.getter(name="databaseInstance")
    def database_instance(self) -> Optional[pulumi.Input['DatabaseInstancePropertiesArgs']]:
        """
        The database instance where the SCOM Operational and Warehouse databases will be stored.
        """
        return pulumi.get(self, "database_instance")

    @database_instance.setter
    def database_instance(self, value: Optional[pulumi.Input['DatabaseInstancePropertiesArgs']]):
        pulumi.set(self, "database_instance", value)

    @property
    @pulumi.getter(name="domainController")
    def domain_controller(self) -> Optional[pulumi.Input['DomainControllerPropertiesArgs']]:
        """
        Domain controller details
        """
        return pulumi.get(self, "domain_controller")

    @domain_controller.setter
    def domain_controller(self, value: Optional[pulumi.Input['DomainControllerPropertiesArgs']]):
        pulumi.set(self, "domain_controller", value)

    @property
    @pulumi.getter(name="domainUserCredentials")
    def domain_user_credentials(self) -> Optional[pulumi.Input['DomainUserCredentialsArgs']]:
        """
        Domain user which will be used to join VMs to domain and login to VMs.
        """
        return pulumi.get(self, "domain_user_credentials")

    @domain_user_credentials.setter
    def domain_user_credentials(self, value: Optional[pulumi.Input['DomainUserCredentialsArgs']]):
        pulumi.set(self, "domain_user_credentials", value)

    @property
    @pulumi.getter(name="gmsaDetails")
    def gmsa_details(self) -> Optional[pulumi.Input['GmsaDetailsArgs']]:
        """
        Gmsa Details for load balancer and vmss
        """
        return pulumi.get(self, "gmsa_details")

    @gmsa_details.setter
    def gmsa_details(self, value: Optional[pulumi.Input['GmsaDetailsArgs']]):
        pulumi.set(self, "gmsa_details", value)

    @property
    @pulumi.getter(name="vNetSubnetId")
    def v_net_subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        Virtual Network subnet id on which Aquila instance will be provisioned
        """
        return pulumi.get(self, "v_net_subnet_id")

    @v_net_subnet_id.setter
    def v_net_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "v_net_subnet_id", value)


