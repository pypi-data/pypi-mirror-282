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
    'DataPointArgs',
    'EventArgs',
    'ExtendedLocationArgs',
    'OwnCertificateArgs',
    'TransportAuthenticationArgs',
    'UserAuthenticationArgs',
    'UsernamePasswordCredentialsArgs',
    'X509CredentialsArgs',
]

@pulumi.input_type
class DataPointArgs:
    def __init__(__self__, *,
                 data_source: pulumi.Input[str],
                 capability_id: Optional[pulumi.Input[str]] = None,
                 data_point_configuration: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 observability_mode: Optional[pulumi.Input[Union[str, 'DataPointsObservabilityMode']]] = None):
        """
        Defines the data point properties.
        :param pulumi.Input[str] data_source: The address of the source of the data in the asset (e.g. URL) so that a client can access the data source on the asset.
        :param pulumi.Input[str] capability_id: The path to the type definition of the capability (e.g. DTMI, OPC UA information model node id, etc.), for example dtmi:com:example:Robot:_contents:__prop1;1.
        :param pulumi.Input[str] data_point_configuration: Protocol-specific configuration for the data point. For OPC UA, this could include configuration like, publishingInterval, samplingInterval, and queueSize.
        :param pulumi.Input[str] name: The name of the data point.
        :param pulumi.Input[Union[str, 'DataPointsObservabilityMode']] observability_mode: An indication of how the data point should be mapped to OpenTelemetry.
        """
        pulumi.set(__self__, "data_source", data_source)
        if capability_id is not None:
            pulumi.set(__self__, "capability_id", capability_id)
        if data_point_configuration is not None:
            pulumi.set(__self__, "data_point_configuration", data_point_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if observability_mode is None:
            observability_mode = 'none'
        if observability_mode is not None:
            pulumi.set(__self__, "observability_mode", observability_mode)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[str]:
        """
        The address of the source of the data in the asset (e.g. URL) so that a client can access the data source on the asset.
        """
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_source", value)

    @property
    @pulumi.getter(name="capabilityId")
    def capability_id(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the type definition of the capability (e.g. DTMI, OPC UA information model node id, etc.), for example dtmi:com:example:Robot:_contents:__prop1;1.
        """
        return pulumi.get(self, "capability_id")

    @capability_id.setter
    def capability_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capability_id", value)

    @property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[pulumi.Input[str]]:
        """
        Protocol-specific configuration for the data point. For OPC UA, this could include configuration like, publishingInterval, samplingInterval, and queueSize.
        """
        return pulumi.get(self, "data_point_configuration")

    @data_point_configuration.setter
    def data_point_configuration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_point_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data point.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(self) -> Optional[pulumi.Input[Union[str, 'DataPointsObservabilityMode']]]:
        """
        An indication of how the data point should be mapped to OpenTelemetry.
        """
        return pulumi.get(self, "observability_mode")

    @observability_mode.setter
    def observability_mode(self, value: Optional[pulumi.Input[Union[str, 'DataPointsObservabilityMode']]]):
        pulumi.set(self, "observability_mode", value)


@pulumi.input_type
class EventArgs:
    def __init__(__self__, *,
                 event_notifier: pulumi.Input[str],
                 capability_id: Optional[pulumi.Input[str]] = None,
                 event_configuration: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 observability_mode: Optional[pulumi.Input[Union[str, 'EventsObservabilityMode']]] = None):
        """
        Defines the event properties.
        :param pulumi.Input[str] event_notifier: The address of the notifier of the event in the asset (e.g. URL) so that a client can access the event on the asset.
        :param pulumi.Input[str] capability_id: The path to the type definition of the capability (e.g. DTMI, OPC UA information model node id, etc.), for example dtmi:com:example:Robot:_contents:__prop1;1.
        :param pulumi.Input[str] event_configuration: Protocol-specific configuration for the event. For OPC UA, this could include configuration like, publishingInterval, samplingInterval, and queueSize.
        :param pulumi.Input[str] name: The name of the event.
        :param pulumi.Input[Union[str, 'EventsObservabilityMode']] observability_mode: An indication of how the event should be mapped to OpenTelemetry.
        """
        pulumi.set(__self__, "event_notifier", event_notifier)
        if capability_id is not None:
            pulumi.set(__self__, "capability_id", capability_id)
        if event_configuration is not None:
            pulumi.set(__self__, "event_configuration", event_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if observability_mode is None:
            observability_mode = 'none'
        if observability_mode is not None:
            pulumi.set(__self__, "observability_mode", observability_mode)

    @property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> pulumi.Input[str]:
        """
        The address of the notifier of the event in the asset (e.g. URL) so that a client can access the event on the asset.
        """
        return pulumi.get(self, "event_notifier")

    @event_notifier.setter
    def event_notifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_notifier", value)

    @property
    @pulumi.getter(name="capabilityId")
    def capability_id(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the type definition of the capability (e.g. DTMI, OPC UA information model node id, etc.), for example dtmi:com:example:Robot:_contents:__prop1;1.
        """
        return pulumi.get(self, "capability_id")

    @capability_id.setter
    def capability_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capability_id", value)

    @property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[pulumi.Input[str]]:
        """
        Protocol-specific configuration for the event. For OPC UA, this could include configuration like, publishingInterval, samplingInterval, and queueSize.
        """
        return pulumi.get(self, "event_configuration")

    @event_configuration.setter
    def event_configuration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the event.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(self) -> Optional[pulumi.Input[Union[str, 'EventsObservabilityMode']]]:
        """
        An indication of how the event should be mapped to OpenTelemetry.
        """
        return pulumi.get(self, "observability_mode")

    @observability_mode.setter
    def observability_mode(self, value: Optional[pulumi.Input[Union[str, 'EventsObservabilityMode']]]):
        pulumi.set(self, "observability_mode", value)


@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        The extended location.
        :param pulumi.Input[str] name: The extended location name.
        :param pulumi.Input[str] type: The extended location type.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The extended location name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The extended location type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class OwnCertificateArgs:
    def __init__(__self__, *,
                 cert_password_reference: Optional[pulumi.Input[str]] = None,
                 cert_secret_reference: Optional[pulumi.Input[str]] = None,
                 cert_thumbprint: Optional[pulumi.Input[str]] = None):
        """
        Certificate or private key that can be used by the southbound connector connecting to the shop floor/OT device. The accepted extensions are .der for certificates and .pfx/.pem for private keys.
        :param pulumi.Input[str] cert_password_reference: Secret Reference Name (Pfx or Pem password).
        :param pulumi.Input[str] cert_secret_reference: Secret Reference name (cert and private key).
        :param pulumi.Input[str] cert_thumbprint: Certificate thumbprint.
        """
        if cert_password_reference is not None:
            pulumi.set(__self__, "cert_password_reference", cert_password_reference)
        if cert_secret_reference is not None:
            pulumi.set(__self__, "cert_secret_reference", cert_secret_reference)
        if cert_thumbprint is not None:
            pulumi.set(__self__, "cert_thumbprint", cert_thumbprint)

    @property
    @pulumi.getter(name="certPasswordReference")
    def cert_password_reference(self) -> Optional[pulumi.Input[str]]:
        """
        Secret Reference Name (Pfx or Pem password).
        """
        return pulumi.get(self, "cert_password_reference")

    @cert_password_reference.setter
    def cert_password_reference(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_password_reference", value)

    @property
    @pulumi.getter(name="certSecretReference")
    def cert_secret_reference(self) -> Optional[pulumi.Input[str]]:
        """
        Secret Reference name (cert and private key).
        """
        return pulumi.get(self, "cert_secret_reference")

    @cert_secret_reference.setter
    def cert_secret_reference(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_secret_reference", value)

    @property
    @pulumi.getter(name="certThumbprint")
    def cert_thumbprint(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate thumbprint.
        """
        return pulumi.get(self, "cert_thumbprint")

    @cert_thumbprint.setter
    def cert_thumbprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_thumbprint", value)


@pulumi.input_type
class TransportAuthenticationArgs:
    def __init__(__self__, *,
                 own_certificates: pulumi.Input[Sequence[pulumi.Input['OwnCertificateArgs']]]):
        """
        Definition of the authentication mechanism for the southbound connector.
        :param pulumi.Input[Sequence[pulumi.Input['OwnCertificateArgs']]] own_certificates: Defines a reference to a secret which contains all certificates and private keys that can be used by the southbound connector connecting to the shop floor/OT device. The accepted extensions are .der for certificates and .pfx/.pem for private keys.
        """
        pulumi.set(__self__, "own_certificates", own_certificates)

    @property
    @pulumi.getter(name="ownCertificates")
    def own_certificates(self) -> pulumi.Input[Sequence[pulumi.Input['OwnCertificateArgs']]]:
        """
        Defines a reference to a secret which contains all certificates and private keys that can be used by the southbound connector connecting to the shop floor/OT device. The accepted extensions are .der for certificates and .pfx/.pem for private keys.
        """
        return pulumi.get(self, "own_certificates")

    @own_certificates.setter
    def own_certificates(self, value: pulumi.Input[Sequence[pulumi.Input['OwnCertificateArgs']]]):
        pulumi.set(self, "own_certificates", value)


@pulumi.input_type
class UserAuthenticationArgs:
    def __init__(__self__, *,
                 mode: Optional[pulumi.Input[Union[str, 'UserAuthenticationMode']]] = None,
                 username_password_credentials: Optional[pulumi.Input['UsernamePasswordCredentialsArgs']] = None,
                 x509_credentials: Optional[pulumi.Input['X509CredentialsArgs']] = None):
        """
        Definition of the client authentication mechanism to the server.
        :param pulumi.Input[Union[str, 'UserAuthenticationMode']] mode: Defines the mode to authenticate the user of the client at the server.
        :param pulumi.Input['UsernamePasswordCredentialsArgs'] username_password_credentials: Defines the username and password references when UsernamePassword user authentication mode is selected.
        :param pulumi.Input['X509CredentialsArgs'] x509_credentials: Defines the certificate reference when Certificate user authentication mode is selected.
        """
        if mode is None:
            mode = 'Certificate'
        pulumi.set(__self__, "mode", mode)
        if username_password_credentials is not None:
            pulumi.set(__self__, "username_password_credentials", username_password_credentials)
        if x509_credentials is not None:
            pulumi.set(__self__, "x509_credentials", x509_credentials)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[str, 'UserAuthenticationMode']]:
        """
        Defines the mode to authenticate the user of the client at the server.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[Union[str, 'UserAuthenticationMode']]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(self) -> Optional[pulumi.Input['UsernamePasswordCredentialsArgs']]:
        """
        Defines the username and password references when UsernamePassword user authentication mode is selected.
        """
        return pulumi.get(self, "username_password_credentials")

    @username_password_credentials.setter
    def username_password_credentials(self, value: Optional[pulumi.Input['UsernamePasswordCredentialsArgs']]):
        pulumi.set(self, "username_password_credentials", value)

    @property
    @pulumi.getter(name="x509Credentials")
    def x509_credentials(self) -> Optional[pulumi.Input['X509CredentialsArgs']]:
        """
        Defines the certificate reference when Certificate user authentication mode is selected.
        """
        return pulumi.get(self, "x509_credentials")

    @x509_credentials.setter
    def x509_credentials(self, value: Optional[pulumi.Input['X509CredentialsArgs']]):
        pulumi.set(self, "x509_credentials", value)


@pulumi.input_type
class UsernamePasswordCredentialsArgs:
    def __init__(__self__, *,
                 password_reference: pulumi.Input[str],
                 username_reference: pulumi.Input[str]):
        """
        The credentials for authentication mode UsernamePassword.
        :param pulumi.Input[str] password_reference: A reference to secret containing the password.
        :param pulumi.Input[str] username_reference: A reference to secret containing the username.
        """
        pulumi.set(__self__, "password_reference", password_reference)
        pulumi.set(__self__, "username_reference", username_reference)

    @property
    @pulumi.getter(name="passwordReference")
    def password_reference(self) -> pulumi.Input[str]:
        """
        A reference to secret containing the password.
        """
        return pulumi.get(self, "password_reference")

    @password_reference.setter
    def password_reference(self, value: pulumi.Input[str]):
        pulumi.set(self, "password_reference", value)

    @property
    @pulumi.getter(name="usernameReference")
    def username_reference(self) -> pulumi.Input[str]:
        """
        A reference to secret containing the username.
        """
        return pulumi.get(self, "username_reference")

    @username_reference.setter
    def username_reference(self, value: pulumi.Input[str]):
        pulumi.set(self, "username_reference", value)


@pulumi.input_type
class X509CredentialsArgs:
    def __init__(__self__, *,
                 certificate_reference: pulumi.Input[str]):
        """
        The x509 certificate for authentication mode Certificate.
        :param pulumi.Input[str] certificate_reference: A reference to secret containing the certificate and private key (e.g. stored as .der/.pem or .der/.pfx).
        """
        pulumi.set(__self__, "certificate_reference", certificate_reference)

    @property
    @pulumi.getter(name="certificateReference")
    def certificate_reference(self) -> pulumi.Input[str]:
        """
        A reference to secret containing the certificate and private key (e.g. stored as .der/.pem or .der/.pfx).
        """
        return pulumi.get(self, "certificate_reference")

    @certificate_reference.setter
    def certificate_reference(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_reference", value)


