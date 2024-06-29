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
    'AwAssumeRoleAuthenticationDetailsPropertiesResponse',
    'AwsCredsAuthenticationDetailsPropertiesResponse',
    'GcpCredentialsDetailsPropertiesResponse',
    'HybridComputeSettingsPropertiesResponse',
    'ProxyServerPropertiesResponse',
    'SecurityContactPropertiesResponseAlertNotifications',
    'SecurityContactPropertiesResponseNotificationsByRole',
    'ServicePrincipalPropertiesResponse',
]

@pulumi.output_type
class AwAssumeRoleAuthenticationDetailsPropertiesResponse(dict):
    """
    AWS cloud account connector based assume role, the role enables delegating access to your AWS resources. The role is composed of role Amazon Resource Name (ARN) and external ID. For more details, refer to <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html">Creating a Role to Delegate Permissions to an IAM User (write only)</a>
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accountId":
            suggest = "account_id"
        elif key == "authenticationProvisioningState":
            suggest = "authentication_provisioning_state"
        elif key == "authenticationType":
            suggest = "authentication_type"
        elif key == "awsAssumeRoleArn":
            suggest = "aws_assume_role_arn"
        elif key == "awsExternalId":
            suggest = "aws_external_id"
        elif key == "grantedPermissions":
            suggest = "granted_permissions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AwAssumeRoleAuthenticationDetailsPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AwAssumeRoleAuthenticationDetailsPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AwAssumeRoleAuthenticationDetailsPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 account_id: str,
                 authentication_provisioning_state: str,
                 authentication_type: str,
                 aws_assume_role_arn: str,
                 aws_external_id: str,
                 granted_permissions: Sequence[str]):
        """
        AWS cloud account connector based assume role, the role enables delegating access to your AWS resources. The role is composed of role Amazon Resource Name (ARN) and external ID. For more details, refer to <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html">Creating a Role to Delegate Permissions to an IAM User (write only)</a>
        :param str account_id: The ID of the cloud account
        :param str authentication_provisioning_state: State of the multi-cloud connector
        :param str authentication_type: Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
               Expected value is 'awsAssumeRole'.
        :param str aws_assume_role_arn: Assumed role ID is an identifier that you can use to create temporary security credentials.
        :param str aws_external_id: A unique identifier that is required when you assume a role in another account.
        :param Sequence[str] granted_permissions: The permissions detected in the cloud account.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "authentication_provisioning_state", authentication_provisioning_state)
        pulumi.set(__self__, "authentication_type", 'awsAssumeRole')
        pulumi.set(__self__, "aws_assume_role_arn", aws_assume_role_arn)
        pulumi.set(__self__, "aws_external_id", aws_external_id)
        pulumi.set(__self__, "granted_permissions", granted_permissions)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The ID of the cloud account
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="authenticationProvisioningState")
    def authentication_provisioning_state(self) -> str:
        """
        State of the multi-cloud connector
        """
        return pulumi.get(self, "authentication_provisioning_state")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> str:
        """
        Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
        Expected value is 'awsAssumeRole'.
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="awsAssumeRoleArn")
    def aws_assume_role_arn(self) -> str:
        """
        Assumed role ID is an identifier that you can use to create temporary security credentials.
        """
        return pulumi.get(self, "aws_assume_role_arn")

    @property
    @pulumi.getter(name="awsExternalId")
    def aws_external_id(self) -> str:
        """
        A unique identifier that is required when you assume a role in another account.
        """
        return pulumi.get(self, "aws_external_id")

    @property
    @pulumi.getter(name="grantedPermissions")
    def granted_permissions(self) -> Sequence[str]:
        """
        The permissions detected in the cloud account.
        """
        return pulumi.get(self, "granted_permissions")


@pulumi.output_type
class AwsCredsAuthenticationDetailsPropertiesResponse(dict):
    """
    AWS cloud account connector based credentials, the credentials is composed of access key ID and secret key, for more details, refer to <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html">Creating an IAM User in Your AWS Account (write only)</a>
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accountId":
            suggest = "account_id"
        elif key == "authenticationProvisioningState":
            suggest = "authentication_provisioning_state"
        elif key == "authenticationType":
            suggest = "authentication_type"
        elif key == "awsAccessKeyId":
            suggest = "aws_access_key_id"
        elif key == "awsSecretAccessKey":
            suggest = "aws_secret_access_key"
        elif key == "grantedPermissions":
            suggest = "granted_permissions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AwsCredsAuthenticationDetailsPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AwsCredsAuthenticationDetailsPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AwsCredsAuthenticationDetailsPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 account_id: str,
                 authentication_provisioning_state: str,
                 authentication_type: str,
                 aws_access_key_id: str,
                 aws_secret_access_key: str,
                 granted_permissions: Sequence[str]):
        """
        AWS cloud account connector based credentials, the credentials is composed of access key ID and secret key, for more details, refer to <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html">Creating an IAM User in Your AWS Account (write only)</a>
        :param str account_id: The ID of the cloud account
        :param str authentication_provisioning_state: State of the multi-cloud connector
        :param str authentication_type: Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
               Expected value is 'awsCreds'.
        :param str aws_access_key_id: Public key element of the AWS credential object (write only)
        :param str aws_secret_access_key: Secret key element of the AWS credential object (write only)
        :param Sequence[str] granted_permissions: The permissions detected in the cloud account.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "authentication_provisioning_state", authentication_provisioning_state)
        pulumi.set(__self__, "authentication_type", 'awsCreds')
        pulumi.set(__self__, "aws_access_key_id", aws_access_key_id)
        pulumi.set(__self__, "aws_secret_access_key", aws_secret_access_key)
        pulumi.set(__self__, "granted_permissions", granted_permissions)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The ID of the cloud account
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="authenticationProvisioningState")
    def authentication_provisioning_state(self) -> str:
        """
        State of the multi-cloud connector
        """
        return pulumi.get(self, "authentication_provisioning_state")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> str:
        """
        Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
        Expected value is 'awsCreds'.
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="awsAccessKeyId")
    def aws_access_key_id(self) -> str:
        """
        Public key element of the AWS credential object (write only)
        """
        return pulumi.get(self, "aws_access_key_id")

    @property
    @pulumi.getter(name="awsSecretAccessKey")
    def aws_secret_access_key(self) -> str:
        """
        Secret key element of the AWS credential object (write only)
        """
        return pulumi.get(self, "aws_secret_access_key")

    @property
    @pulumi.getter(name="grantedPermissions")
    def granted_permissions(self) -> Sequence[str]:
        """
        The permissions detected in the cloud account.
        """
        return pulumi.get(self, "granted_permissions")


@pulumi.output_type
class GcpCredentialsDetailsPropertiesResponse(dict):
    """
    GCP cloud account connector based service to service credentials, the credentials are composed of the organization ID and a JSON API key (write only)
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authProviderX509CertUrl":
            suggest = "auth_provider_x509_cert_url"
        elif key == "authUri":
            suggest = "auth_uri"
        elif key == "authenticationProvisioningState":
            suggest = "authentication_provisioning_state"
        elif key == "authenticationType":
            suggest = "authentication_type"
        elif key == "clientEmail":
            suggest = "client_email"
        elif key == "clientId":
            suggest = "client_id"
        elif key == "clientX509CertUrl":
            suggest = "client_x509_cert_url"
        elif key == "grantedPermissions":
            suggest = "granted_permissions"
        elif key == "organizationId":
            suggest = "organization_id"
        elif key == "privateKey":
            suggest = "private_key"
        elif key == "privateKeyId":
            suggest = "private_key_id"
        elif key == "projectId":
            suggest = "project_id"
        elif key == "tokenUri":
            suggest = "token_uri"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GcpCredentialsDetailsPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GcpCredentialsDetailsPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GcpCredentialsDetailsPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auth_provider_x509_cert_url: str,
                 auth_uri: str,
                 authentication_provisioning_state: str,
                 authentication_type: str,
                 client_email: str,
                 client_id: str,
                 client_x509_cert_url: str,
                 granted_permissions: Sequence[str],
                 organization_id: str,
                 private_key: str,
                 private_key_id: str,
                 project_id: str,
                 token_uri: str,
                 type: str):
        """
        GCP cloud account connector based service to service credentials, the credentials are composed of the organization ID and a JSON API key (write only)
        :param str auth_provider_x509_cert_url: Auth provider x509 certificate URL field of the API key (write only)
        :param str auth_uri: Auth URI field of the API key (write only)
        :param str authentication_provisioning_state: State of the multi-cloud connector
        :param str authentication_type: Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
               Expected value is 'gcpCredentials'.
        :param str client_email: Client email field of the API key (write only)
        :param str client_id: Client ID field of the API key (write only)
        :param str client_x509_cert_url: Client x509 certificate URL field of the API key (write only)
        :param Sequence[str] granted_permissions: The permissions detected in the cloud account.
        :param str organization_id: The organization ID of the GCP cloud account
        :param str private_key: Private key field of the API key (write only)
        :param str private_key_id: Private key ID field of the API key (write only)
        :param str project_id: Project ID field of the API key (write only)
        :param str token_uri: Token URI field of the API key (write only)
        :param str type: Type field of the API key (write only)
        """
        pulumi.set(__self__, "auth_provider_x509_cert_url", auth_provider_x509_cert_url)
        pulumi.set(__self__, "auth_uri", auth_uri)
        pulumi.set(__self__, "authentication_provisioning_state", authentication_provisioning_state)
        pulumi.set(__self__, "authentication_type", 'gcpCredentials')
        pulumi.set(__self__, "client_email", client_email)
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_x509_cert_url", client_x509_cert_url)
        pulumi.set(__self__, "granted_permissions", granted_permissions)
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "private_key", private_key)
        pulumi.set(__self__, "private_key_id", private_key_id)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "token_uri", token_uri)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="authProviderX509CertUrl")
    def auth_provider_x509_cert_url(self) -> str:
        """
        Auth provider x509 certificate URL field of the API key (write only)
        """
        return pulumi.get(self, "auth_provider_x509_cert_url")

    @property
    @pulumi.getter(name="authUri")
    def auth_uri(self) -> str:
        """
        Auth URI field of the API key (write only)
        """
        return pulumi.get(self, "auth_uri")

    @property
    @pulumi.getter(name="authenticationProvisioningState")
    def authentication_provisioning_state(self) -> str:
        """
        State of the multi-cloud connector
        """
        return pulumi.get(self, "authentication_provisioning_state")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> str:
        """
        Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
        Expected value is 'gcpCredentials'.
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> str:
        """
        Client email field of the API key (write only)
        """
        return pulumi.get(self, "client_email")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Client ID field of the API key (write only)
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientX509CertUrl")
    def client_x509_cert_url(self) -> str:
        """
        Client x509 certificate URL field of the API key (write only)
        """
        return pulumi.get(self, "client_x509_cert_url")

    @property
    @pulumi.getter(name="grantedPermissions")
    def granted_permissions(self) -> Sequence[str]:
        """
        The permissions detected in the cloud account.
        """
        return pulumi.get(self, "granted_permissions")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The organization ID of the GCP cloud account
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> str:
        """
        Private key field of the API key (write only)
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="privateKeyId")
    def private_key_id(self) -> str:
        """
        Private key ID field of the API key (write only)
        """
        return pulumi.get(self, "private_key_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        Project ID field of the API key (write only)
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="tokenUri")
    def token_uri(self) -> str:
        """
        Token URI field of the API key (write only)
        """
        return pulumi.get(self, "token_uri")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type field of the API key (write only)
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class HybridComputeSettingsPropertiesResponse(dict):
    """
    Settings for hybrid compute management
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "autoProvision":
            suggest = "auto_provision"
        elif key == "hybridComputeProvisioningState":
            suggest = "hybrid_compute_provisioning_state"
        elif key == "proxyServer":
            suggest = "proxy_server"
        elif key == "resourceGroupName":
            suggest = "resource_group_name"
        elif key == "servicePrincipal":
            suggest = "service_principal"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HybridComputeSettingsPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HybridComputeSettingsPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HybridComputeSettingsPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auto_provision: str,
                 hybrid_compute_provisioning_state: str,
                 proxy_server: Optional['outputs.ProxyServerPropertiesResponse'] = None,
                 region: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 service_principal: Optional['outputs.ServicePrincipalPropertiesResponse'] = None):
        """
        Settings for hybrid compute management
        :param str auto_provision: Whether or not to automatically install Azure Arc (hybrid compute) agents on machines
        :param str hybrid_compute_provisioning_state: State of the service principal and its secret
        :param 'ProxyServerPropertiesResponse' proxy_server: For a non-Azure machine that is not connected directly to the internet, specify a proxy server that the non-Azure machine can use.
        :param str region: The location where the metadata of machines will be stored
        :param str resource_group_name: The name of the resource group where Arc (Hybrid Compute) connectors are connected.
        :param 'ServicePrincipalPropertiesResponse' service_principal: An object to access resources that are secured by an Azure AD tenant.
        """
        pulumi.set(__self__, "auto_provision", auto_provision)
        pulumi.set(__self__, "hybrid_compute_provisioning_state", hybrid_compute_provisioning_state)
        if proxy_server is not None:
            pulumi.set(__self__, "proxy_server", proxy_server)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if service_principal is not None:
            pulumi.set(__self__, "service_principal", service_principal)

    @property
    @pulumi.getter(name="autoProvision")
    def auto_provision(self) -> str:
        """
        Whether or not to automatically install Azure Arc (hybrid compute) agents on machines
        """
        return pulumi.get(self, "auto_provision")

    @property
    @pulumi.getter(name="hybridComputeProvisioningState")
    def hybrid_compute_provisioning_state(self) -> str:
        """
        State of the service principal and its secret
        """
        return pulumi.get(self, "hybrid_compute_provisioning_state")

    @property
    @pulumi.getter(name="proxyServer")
    def proxy_server(self) -> Optional['outputs.ProxyServerPropertiesResponse']:
        """
        For a non-Azure machine that is not connected directly to the internet, specify a proxy server that the non-Azure machine can use.
        """
        return pulumi.get(self, "proxy_server")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The location where the metadata of machines will be stored
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[str]:
        """
        The name of the resource group where Arc (Hybrid Compute) connectors are connected.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional['outputs.ServicePrincipalPropertiesResponse']:
        """
        An object to access resources that are secured by an Azure AD tenant.
        """
        return pulumi.get(self, "service_principal")


@pulumi.output_type
class ProxyServerPropertiesResponse(dict):
    """
    For a non-Azure machine that is not connected directly to the internet, specify a proxy server that the non-Azure machine can use.
    """
    def __init__(__self__, *,
                 ip: Optional[str] = None,
                 port: Optional[str] = None):
        """
        For a non-Azure machine that is not connected directly to the internet, specify a proxy server that the non-Azure machine can use.
        :param str ip: Proxy server IP
        :param str port: Proxy server port
        """
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def ip(self) -> Optional[str]:
        """
        Proxy server IP
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        """
        Proxy server port
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class SecurityContactPropertiesResponseAlertNotifications(dict):
    """
    Defines whether to send email notifications about new security alerts
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "minimalSeverity":
            suggest = "minimal_severity"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecurityContactPropertiesResponseAlertNotifications. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecurityContactPropertiesResponseAlertNotifications.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecurityContactPropertiesResponseAlertNotifications.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 minimal_severity: Optional[str] = None,
                 state: Optional[str] = None):
        """
        Defines whether to send email notifications about new security alerts
        :param str minimal_severity: Defines the minimal alert severity which will be sent as email notifications
        :param str state: Defines if email notifications will be sent about new security alerts
        """
        if minimal_severity is not None:
            pulumi.set(__self__, "minimal_severity", minimal_severity)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="minimalSeverity")
    def minimal_severity(self) -> Optional[str]:
        """
        Defines the minimal alert severity which will be sent as email notifications
        """
        return pulumi.get(self, "minimal_severity")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Defines if email notifications will be sent about new security alerts
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class SecurityContactPropertiesResponseNotificationsByRole(dict):
    """
    Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
    """
    def __init__(__self__, *,
                 roles: Optional[Sequence[str]] = None,
                 state: Optional[str] = None):
        """
        Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        :param Sequence[str] roles: Defines which RBAC roles will get email notifications from Microsoft Defender for Cloud. List of allowed RBAC roles: 
        :param str state: Defines whether to send email notifications from AMicrosoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        """
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[str]]:
        """
        Defines which RBAC roles will get email notifications from Microsoft Defender for Cloud. List of allowed RBAC roles: 
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Defines whether to send email notifications from AMicrosoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class ServicePrincipalPropertiesResponse(dict):
    """
    Details of the service principal.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "applicationId":
            suggest = "application_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServicePrincipalPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServicePrincipalPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServicePrincipalPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 application_id: Optional[str] = None,
                 secret: Optional[str] = None):
        """
        Details of the service principal.
        :param str application_id: Application ID of service principal.
        :param str secret: A secret string that the application uses to prove its identity, also can be referred to as application password (write only).
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[str]:
        """
        Application ID of service principal.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def secret(self) -> Optional[str]:
        """
        A secret string that the application uses to prove its identity, also can be referred to as application password (write only).
        """
        return pulumi.get(self, "secret")


