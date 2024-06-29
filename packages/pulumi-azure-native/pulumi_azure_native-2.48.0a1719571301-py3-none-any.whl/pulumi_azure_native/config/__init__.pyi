# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

auxiliaryTenantIds: Optional[str]
"""
Any additional Tenant IDs which should be used for authentication.
"""

clientCertificatePassword: Optional[str]
"""
The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate
"""

clientCertificatePath: Optional[str]
"""
The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate.
"""

clientId: Optional[str]
"""
The Client ID which should be used.
"""

clientSecret: Optional[str]
"""
The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.
"""

disablePulumiPartnerId: Optional[bool]
"""
This will disable the Pulumi Partner ID which is used if a custom `partnerId` isn't specified.
"""

environment: Optional[str]
"""
The Cloud Environment which should be used. Possible values are public, usgovernment, and china. Defaults to public.
"""

location: Optional[str]
"""
The location to use. ResourceGroups will consult this property for a default location, if one was not supplied explicitly when defining the resource.
"""

metadataHost: Optional[str]
"""
The Hostname of the Azure Metadata Service.
"""

msiEndpoint: Optional[str]
"""
The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically.
"""

oidcRequestToken: Optional[str]
"""
Your cloud service or provider's bearer token to exchange for an OIDC ID token.
"""

oidcRequestUrl: Optional[str]
"""
The URL to initiate the OIDC token exchange. 
"""

oidcToken: Optional[str]
"""
The OIDC token to exchange for an Azure token.
"""

oidcTokenFilePath: Optional[str]
"""
The path to a file containing an OIDC token to exchange for an Azure token.
"""

partnerId: Optional[str]
"""
A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.
"""

subscriptionId: Optional[str]
"""
The Subscription ID which should be used.
"""

tenantId: Optional[str]
"""
The Tenant ID which should be used.
"""

useMsi: Optional[bool]
"""
Allow Managed Service Identity be used for Authentication.
"""

useOidc: Optional[bool]
"""
Allow OpenID Connect (OIDC) to be used for Authentication.
"""

