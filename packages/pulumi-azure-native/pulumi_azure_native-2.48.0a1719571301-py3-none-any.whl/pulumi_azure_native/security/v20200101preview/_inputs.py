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
    'AwAssumeRoleAuthenticationDetailsPropertiesArgs',
    'AwsCredsAuthenticationDetailsPropertiesArgs',
    'GcpCredentialsDetailsPropertiesArgs',
    'HybridComputeSettingsPropertiesArgs',
    'ProxyServerPropertiesArgs',
    'SecurityContactPropertiesAlertNotificationsArgs',
    'SecurityContactPropertiesNotificationsByRoleArgs',
    'ServicePrincipalPropertiesArgs',
]

@pulumi.input_type
class AwAssumeRoleAuthenticationDetailsPropertiesArgs:
    def __init__(__self__, *,
                 authentication_type: pulumi.Input[str],
                 aws_assume_role_arn: pulumi.Input[str],
                 aws_external_id: pulumi.Input[str]):
        """
        AWS cloud account connector based assume role, the role enables delegating access to your AWS resources. The role is composed of role Amazon Resource Name (ARN) and external ID. For more details, refer to <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html">Creating a Role to Delegate Permissions to an IAM User (write only)</a>
        :param pulumi.Input[str] authentication_type: Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
               Expected value is 'awsAssumeRole'.
        :param pulumi.Input[str] aws_assume_role_arn: Assumed role ID is an identifier that you can use to create temporary security credentials.
        :param pulumi.Input[str] aws_external_id: A unique identifier that is required when you assume a role in another account.
        """
        pulumi.set(__self__, "authentication_type", 'awsAssumeRole')
        pulumi.set(__self__, "aws_assume_role_arn", aws_assume_role_arn)
        pulumi.set(__self__, "aws_external_id", aws_external_id)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[str]:
        """
        Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
        Expected value is 'awsAssumeRole'.
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="awsAssumeRoleArn")
    def aws_assume_role_arn(self) -> pulumi.Input[str]:
        """
        Assumed role ID is an identifier that you can use to create temporary security credentials.
        """
        return pulumi.get(self, "aws_assume_role_arn")

    @aws_assume_role_arn.setter
    def aws_assume_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_assume_role_arn", value)

    @property
    @pulumi.getter(name="awsExternalId")
    def aws_external_id(self) -> pulumi.Input[str]:
        """
        A unique identifier that is required when you assume a role in another account.
        """
        return pulumi.get(self, "aws_external_id")

    @aws_external_id.setter
    def aws_external_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_external_id", value)


@pulumi.input_type
class AwsCredsAuthenticationDetailsPropertiesArgs:
    def __init__(__self__, *,
                 authentication_type: pulumi.Input[str],
                 aws_access_key_id: pulumi.Input[str],
                 aws_secret_access_key: pulumi.Input[str]):
        """
        AWS cloud account connector based credentials, the credentials is composed of access key ID and secret key, for more details, refer to <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html">Creating an IAM User in Your AWS Account (write only)</a>
        :param pulumi.Input[str] authentication_type: Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
               Expected value is 'awsCreds'.
        :param pulumi.Input[str] aws_access_key_id: Public key element of the AWS credential object (write only)
        :param pulumi.Input[str] aws_secret_access_key: Secret key element of the AWS credential object (write only)
        """
        pulumi.set(__self__, "authentication_type", 'awsCreds')
        pulumi.set(__self__, "aws_access_key_id", aws_access_key_id)
        pulumi.set(__self__, "aws_secret_access_key", aws_secret_access_key)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[str]:
        """
        Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
        Expected value is 'awsCreds'.
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="awsAccessKeyId")
    def aws_access_key_id(self) -> pulumi.Input[str]:
        """
        Public key element of the AWS credential object (write only)
        """
        return pulumi.get(self, "aws_access_key_id")

    @aws_access_key_id.setter
    def aws_access_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_access_key_id", value)

    @property
    @pulumi.getter(name="awsSecretAccessKey")
    def aws_secret_access_key(self) -> pulumi.Input[str]:
        """
        Secret key element of the AWS credential object (write only)
        """
        return pulumi.get(self, "aws_secret_access_key")

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_secret_access_key", value)


@pulumi.input_type
class GcpCredentialsDetailsPropertiesArgs:
    def __init__(__self__, *,
                 auth_provider_x509_cert_url: pulumi.Input[str],
                 auth_uri: pulumi.Input[str],
                 authentication_type: pulumi.Input[str],
                 client_email: pulumi.Input[str],
                 client_id: pulumi.Input[str],
                 client_x509_cert_url: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 private_key: pulumi.Input[str],
                 private_key_id: pulumi.Input[str],
                 project_id: pulumi.Input[str],
                 token_uri: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        GCP cloud account connector based service to service credentials, the credentials are composed of the organization ID and a JSON API key (write only)
        :param pulumi.Input[str] auth_provider_x509_cert_url: Auth provider x509 certificate URL field of the API key (write only)
        :param pulumi.Input[str] auth_uri: Auth URI field of the API key (write only)
        :param pulumi.Input[str] authentication_type: Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
               Expected value is 'gcpCredentials'.
        :param pulumi.Input[str] client_email: Client email field of the API key (write only)
        :param pulumi.Input[str] client_id: Client ID field of the API key (write only)
        :param pulumi.Input[str] client_x509_cert_url: Client x509 certificate URL field of the API key (write only)
        :param pulumi.Input[str] organization_id: The organization ID of the GCP cloud account
        :param pulumi.Input[str] private_key: Private key field of the API key (write only)
        :param pulumi.Input[str] private_key_id: Private key ID field of the API key (write only)
        :param pulumi.Input[str] project_id: Project ID field of the API key (write only)
        :param pulumi.Input[str] token_uri: Token URI field of the API key (write only)
        :param pulumi.Input[str] type: Type field of the API key (write only)
        """
        pulumi.set(__self__, "auth_provider_x509_cert_url", auth_provider_x509_cert_url)
        pulumi.set(__self__, "auth_uri", auth_uri)
        pulumi.set(__self__, "authentication_type", 'gcpCredentials')
        pulumi.set(__self__, "client_email", client_email)
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_x509_cert_url", client_x509_cert_url)
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "private_key", private_key)
        pulumi.set(__self__, "private_key_id", private_key_id)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "token_uri", token_uri)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="authProviderX509CertUrl")
    def auth_provider_x509_cert_url(self) -> pulumi.Input[str]:
        """
        Auth provider x509 certificate URL field of the API key (write only)
        """
        return pulumi.get(self, "auth_provider_x509_cert_url")

    @auth_provider_x509_cert_url.setter
    def auth_provider_x509_cert_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_provider_x509_cert_url", value)

    @property
    @pulumi.getter(name="authUri")
    def auth_uri(self) -> pulumi.Input[str]:
        """
        Auth URI field of the API key (write only)
        """
        return pulumi.get(self, "auth_uri")

    @auth_uri.setter
    def auth_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_uri", value)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[str]:
        """
        Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
        Expected value is 'gcpCredentials'.
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> pulumi.Input[str]:
        """
        Client email field of the API key (write only)
        """
        return pulumi.get(self, "client_email")

    @client_email.setter
    def client_email(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_email", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        Client ID field of the API key (write only)
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientX509CertUrl")
    def client_x509_cert_url(self) -> pulumi.Input[str]:
        """
        Client x509 certificate URL field of the API key (write only)
        """
        return pulumi.get(self, "client_x509_cert_url")

    @client_x509_cert_url.setter
    def client_x509_cert_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_x509_cert_url", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        """
        The organization ID of the GCP cloud account
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[str]:
        """
        Private key field of the API key (write only)
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="privateKeyId")
    def private_key_id(self) -> pulumi.Input[str]:
        """
        Private key ID field of the API key (write only)
        """
        return pulumi.get(self, "private_key_id")

    @private_key_id.setter
    def private_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        Project ID field of the API key (write only)
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="tokenUri")
    def token_uri(self) -> pulumi.Input[str]:
        """
        Token URI field of the API key (write only)
        """
        return pulumi.get(self, "token_uri")

    @token_uri.setter
    def token_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "token_uri", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type field of the API key (write only)
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class HybridComputeSettingsPropertiesArgs:
    def __init__(__self__, *,
                 auto_provision: pulumi.Input[Union[str, 'AutoProvision']],
                 proxy_server: Optional[pulumi.Input['ProxyServerPropertiesArgs']] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_principal: Optional[pulumi.Input['ServicePrincipalPropertiesArgs']] = None):
        """
        Settings for hybrid compute management
        :param pulumi.Input[Union[str, 'AutoProvision']] auto_provision: Whether or not to automatically install Azure Arc (hybrid compute) agents on machines
        :param pulumi.Input['ProxyServerPropertiesArgs'] proxy_server: For a non-Azure machine that is not connected directly to the internet, specify a proxy server that the non-Azure machine can use.
        :param pulumi.Input[str] region: The location where the metadata of machines will be stored
        :param pulumi.Input[str] resource_group_name: The name of the resource group where Arc (Hybrid Compute) connectors are connected.
        :param pulumi.Input['ServicePrincipalPropertiesArgs'] service_principal: An object to access resources that are secured by an Azure AD tenant.
        """
        pulumi.set(__self__, "auto_provision", auto_provision)
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
    def auto_provision(self) -> pulumi.Input[Union[str, 'AutoProvision']]:
        """
        Whether or not to automatically install Azure Arc (hybrid compute) agents on machines
        """
        return pulumi.get(self, "auto_provision")

    @auto_provision.setter
    def auto_provision(self, value: pulumi.Input[Union[str, 'AutoProvision']]):
        pulumi.set(self, "auto_provision", value)

    @property
    @pulumi.getter(name="proxyServer")
    def proxy_server(self) -> Optional[pulumi.Input['ProxyServerPropertiesArgs']]:
        """
        For a non-Azure machine that is not connected directly to the internet, specify a proxy server that the non-Azure machine can use.
        """
        return pulumi.get(self, "proxy_server")

    @proxy_server.setter
    def proxy_server(self, value: Optional[pulumi.Input['ProxyServerPropertiesArgs']]):
        pulumi.set(self, "proxy_server", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the metadata of machines will be stored
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group where Arc (Hybrid Compute) connectors are connected.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional[pulumi.Input['ServicePrincipalPropertiesArgs']]:
        """
        An object to access resources that are secured by an Azure AD tenant.
        """
        return pulumi.get(self, "service_principal")

    @service_principal.setter
    def service_principal(self, value: Optional[pulumi.Input['ServicePrincipalPropertiesArgs']]):
        pulumi.set(self, "service_principal", value)


@pulumi.input_type
class ProxyServerPropertiesArgs:
    def __init__(__self__, *,
                 ip: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None):
        """
        For a non-Azure machine that is not connected directly to the internet, specify a proxy server that the non-Azure machine can use.
        :param pulumi.Input[str] ip: Proxy server IP
        :param pulumi.Input[str] port: Proxy server port
        """
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        Proxy server IP
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        Proxy server port
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)


@pulumi.input_type
class SecurityContactPropertiesAlertNotificationsArgs:
    def __init__(__self__, *,
                 minimal_severity: Optional[pulumi.Input[Union[str, 'MinimalSeverity']]] = None,
                 state: Optional[pulumi.Input[Union[str, 'State']]] = None):
        """
        Defines whether to send email notifications about new security alerts
        :param pulumi.Input[Union[str, 'MinimalSeverity']] minimal_severity: Defines the minimal alert severity which will be sent as email notifications
        :param pulumi.Input[Union[str, 'State']] state: Defines if email notifications will be sent about new security alerts
        """
        if minimal_severity is not None:
            pulumi.set(__self__, "minimal_severity", minimal_severity)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="minimalSeverity")
    def minimal_severity(self) -> Optional[pulumi.Input[Union[str, 'MinimalSeverity']]]:
        """
        Defines the minimal alert severity which will be sent as email notifications
        """
        return pulumi.get(self, "minimal_severity")

    @minimal_severity.setter
    def minimal_severity(self, value: Optional[pulumi.Input[Union[str, 'MinimalSeverity']]]):
        pulumi.set(self, "minimal_severity", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'State']]]:
        """
        Defines if email notifications will be sent about new security alerts
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'State']]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class SecurityContactPropertiesNotificationsByRoleArgs:
    def __init__(__self__, *,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Roles']]]]] = None,
                 state: Optional[pulumi.Input[Union[str, 'State']]] = None):
        """
        Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'Roles']]]] roles: Defines which RBAC roles will get email notifications from Microsoft Defender for Cloud. List of allowed RBAC roles: 
        :param pulumi.Input[Union[str, 'State']] state: Defines whether to send email notifications from AMicrosoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        """
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Roles']]]]]:
        """
        Defines which RBAC roles will get email notifications from Microsoft Defender for Cloud. List of allowed RBAC roles: 
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Roles']]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'State']]]:
        """
        Defines whether to send email notifications from AMicrosoft Defender for Cloud to persons with specific RBAC roles on the subscription.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'State']]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class ServicePrincipalPropertiesArgs:
    def __init__(__self__, *,
                 application_id: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None):
        """
        Details of the service principal.
        :param pulumi.Input[str] application_id: Application ID of service principal.
        :param pulumi.Input[str] secret: A secret string that the application uses to prove its identity, also can be referred to as application password (write only).
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        Application ID of service principal.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        """
        A secret string that the application uses to prove its identity, also can be referred to as application password (write only).
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)


