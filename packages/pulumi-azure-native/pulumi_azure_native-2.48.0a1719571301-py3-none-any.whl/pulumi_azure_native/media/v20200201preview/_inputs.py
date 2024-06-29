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
    'MediaGraphAssetSinkArgs',
    'MediaGraphClearEndpointArgs',
    'MediaGraphPemCertificateListArgs',
    'MediaGraphRtspSourceArgs',
    'MediaGraphTlsEndpointArgs',
    'MediaGraphTlsValidationOptionsArgs',
    'MediaGraphUsernamePasswordCredentialsArgs',
]

@pulumi.input_type
class MediaGraphAssetSinkArgs:
    def __init__(__self__, *,
                 asset_name: pulumi.Input[str],
                 inputs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: pulumi.Input[str],
                 odata_type: pulumi.Input[str]):
        """
        Asset sink.
        :param pulumi.Input[str] asset_name: Asset name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inputs: Sink inputs.
        :param pulumi.Input[str] name: Sink name.
        :param pulumi.Input[str] odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphAssetSink'.
        """
        pulumi.set(__self__, "asset_name", asset_name)
        pulumi.set(__self__, "inputs", inputs)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphAssetSink')

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> pulumi.Input[str]:
        """
        Asset name.
        """
        return pulumi.get(self, "asset_name")

    @asset_name.setter
    def asset_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "asset_name", value)

    @property
    @pulumi.getter
    def inputs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Sink inputs.
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Sink name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphAssetSink'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)


@pulumi.input_type
class MediaGraphClearEndpointArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 url: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs']] = None):
        """
        An endpoint to connect to with no encryption in transit.
        :param pulumi.Input[str] odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphClearEndpoint'.
        :param pulumi.Input[str] url: Url for the endpoint.
        :param pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs'] credentials: Polymorphic credentials to present to the endpoint.
        """
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphClearEndpoint')
        pulumi.set(__self__, "url", url)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphClearEndpoint'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        Url for the endpoint.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs']]:
        """
        Polymorphic credentials to present to the endpoint.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs']]):
        pulumi.set(self, "credentials", value)


@pulumi.input_type
class MediaGraphPemCertificateListArgs:
    def __init__(__self__, *,
                 certificates: pulumi.Input[Sequence[pulumi.Input[str]]],
                 odata_type: pulumi.Input[str]):
        """
        A list of PEM formatted certificates.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] certificates: PEM formatted public certificates, one per entry.
        :param pulumi.Input[str] odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphPemCertificateList'.
        """
        pulumi.set(__self__, "certificates", certificates)
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphPemCertificateList')

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        PEM formatted public certificates, one per entry.
        """
        return pulumi.get(self, "certificates")

    @certificates.setter
    def certificates(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "certificates", value)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphPemCertificateList'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)


@pulumi.input_type
class MediaGraphRtspSourceArgs:
    def __init__(__self__, *,
                 endpoint: pulumi.Input[Union['MediaGraphClearEndpointArgs', 'MediaGraphTlsEndpointArgs']],
                 name: pulumi.Input[str],
                 odata_type: pulumi.Input[str],
                 transport: pulumi.Input[Union[str, 'MediaGraphRtspTransport']]):
        """
        RTSP source.
        :param pulumi.Input[Union['MediaGraphClearEndpointArgs', 'MediaGraphTlsEndpointArgs']] endpoint: RTSP endpoint of the stream being connected to.
        :param pulumi.Input[str] name: Source name.
        :param pulumi.Input[str] odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphRtspSource'.
        :param pulumi.Input[Union[str, 'MediaGraphRtspTransport']] transport: Underlying RTSP transport. This can be used to enable or disable HTTP tunneling.
        """
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphRtspSource')
        pulumi.set(__self__, "transport", transport)

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[Union['MediaGraphClearEndpointArgs', 'MediaGraphTlsEndpointArgs']]:
        """
        RTSP endpoint of the stream being connected to.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: pulumi.Input[Union['MediaGraphClearEndpointArgs', 'MediaGraphTlsEndpointArgs']]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Source name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphRtspSource'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def transport(self) -> pulumi.Input[Union[str, 'MediaGraphRtspTransport']]:
        """
        Underlying RTSP transport. This can be used to enable or disable HTTP tunneling.
        """
        return pulumi.get(self, "transport")

    @transport.setter
    def transport(self, value: pulumi.Input[Union[str, 'MediaGraphRtspTransport']]):
        pulumi.set(self, "transport", value)


@pulumi.input_type
class MediaGraphTlsEndpointArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 url: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs']] = None,
                 trusted_certificates: Optional[pulumi.Input['MediaGraphPemCertificateListArgs']] = None,
                 validation_options: Optional[pulumi.Input['MediaGraphTlsValidationOptionsArgs']] = None):
        """
        An endpoint which must be connected over TLS/SSL.
        :param pulumi.Input[str] odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphTlsEndpoint'.
        :param pulumi.Input[str] url: Url for the endpoint.
        :param pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs'] credentials: Polymorphic credentials to present to the endpoint.
        :param pulumi.Input['MediaGraphPemCertificateListArgs'] trusted_certificates: What certificates should be trusted when authenticating a TLS connection. Null designates that Azure Media's source of trust should be used.
        :param pulumi.Input['MediaGraphTlsValidationOptionsArgs'] validation_options: Validation options to use when authenticating a TLS connection. By default, strict validation is used.
        """
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphTlsEndpoint')
        pulumi.set(__self__, "url", url)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if trusted_certificates is not None:
            pulumi.set(__self__, "trusted_certificates", trusted_certificates)
        if validation_options is not None:
            pulumi.set(__self__, "validation_options", validation_options)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphTlsEndpoint'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        Url for the endpoint.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs']]:
        """
        Polymorphic credentials to present to the endpoint.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['MediaGraphUsernamePasswordCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="trustedCertificates")
    def trusted_certificates(self) -> Optional[pulumi.Input['MediaGraphPemCertificateListArgs']]:
        """
        What certificates should be trusted when authenticating a TLS connection. Null designates that Azure Media's source of trust should be used.
        """
        return pulumi.get(self, "trusted_certificates")

    @trusted_certificates.setter
    def trusted_certificates(self, value: Optional[pulumi.Input['MediaGraphPemCertificateListArgs']]):
        pulumi.set(self, "trusted_certificates", value)

    @property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> Optional[pulumi.Input['MediaGraphTlsValidationOptionsArgs']]:
        """
        Validation options to use when authenticating a TLS connection. By default, strict validation is used.
        """
        return pulumi.get(self, "validation_options")

    @validation_options.setter
    def validation_options(self, value: Optional[pulumi.Input['MediaGraphTlsValidationOptionsArgs']]):
        pulumi.set(self, "validation_options", value)


@pulumi.input_type
class MediaGraphTlsValidationOptionsArgs:
    def __init__(__self__, *,
                 ignore_hostname: pulumi.Input[bool],
                 ignore_signature: pulumi.Input[bool]):
        """
        Options for controlling the authentication of TLS endpoints.
        :param pulumi.Input[bool] ignore_hostname: Ignore the host name (common name) during validation.
        :param pulumi.Input[bool] ignore_signature: Ignore the integrity of the certificate chain at the current time.
        """
        pulumi.set(__self__, "ignore_hostname", ignore_hostname)
        pulumi.set(__self__, "ignore_signature", ignore_signature)

    @property
    @pulumi.getter(name="ignoreHostname")
    def ignore_hostname(self) -> pulumi.Input[bool]:
        """
        Ignore the host name (common name) during validation.
        """
        return pulumi.get(self, "ignore_hostname")

    @ignore_hostname.setter
    def ignore_hostname(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ignore_hostname", value)

    @property
    @pulumi.getter(name="ignoreSignature")
    def ignore_signature(self) -> pulumi.Input[bool]:
        """
        Ignore the integrity of the certificate chain at the current time.
        """
        return pulumi.get(self, "ignore_signature")

    @ignore_signature.setter
    def ignore_signature(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ignore_signature", value)


@pulumi.input_type
class MediaGraphUsernamePasswordCredentialsArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        Username/password credential pair.
        :param pulumi.Input[str] odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphUsernamePasswordCredentials'.
        :param pulumi.Input[str] password: Password for a username/password pair.
        :param pulumi.Input[str] username: Username for a username/password pair.
        """
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphUsernamePasswordCredentials')
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphUsernamePasswordCredentials'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        Password for a username/password pair.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        Username for a username/password pair.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


