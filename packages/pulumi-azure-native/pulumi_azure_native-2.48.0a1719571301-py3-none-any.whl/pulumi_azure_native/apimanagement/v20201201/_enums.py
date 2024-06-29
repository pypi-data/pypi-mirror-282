# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApiType',
    'BearerTokenSendingMethods',
    'ContentFormat',
    'Protocol',
    'SoapApiType',
]


class ApiType(str, Enum):
    """
    Type of API.
    """
    HTTP = "http"
    SOAP = "soap"


class BearerTokenSendingMethods(str, Enum):
    """
    Form of an authorization grant, which the client uses to request the access token.
    """
    AUTHORIZATION_HEADER = "authorizationHeader"
    """
    Access token will be transmitted in the Authorization header using Bearer schema
    """
    QUERY = "query"
    """
    Access token will be transmitted as query parameters.
    """


class ContentFormat(str, Enum):
    """
    Format of the Content in which the API is getting imported.
    """
    WADL_XML = "wadl-xml"
    """
    The contents are inline and Content type is a WADL document.
    """
    WADL_LINK_JSON = "wadl-link-json"
    """
    The WADL document is hosted on a publicly accessible internet address.
    """
    SWAGGER_JSON = "swagger-json"
    """
    The contents are inline and Content Type is a OpenAPI 2.0 JSON Document.
    """
    SWAGGER_LINK_JSON = "swagger-link-json"
    """
    The OpenAPI 2.0 JSON document is hosted on a publicly accessible internet address.
    """
    WSDL = "wsdl"
    """
    The contents are inline and the document is a WSDL/Soap document.
    """
    WSDL_LINK = "wsdl-link"
    """
    The WSDL document is hosted on a publicly accessible internet address.
    """
    OPENAPI = "openapi"
    """
    The contents are inline and Content Type is a OpenAPI 3.0 YAML Document.
    """
    OPENAPI_JSON = "openapi+json"
    """
    The contents are inline and Content Type is a OpenAPI 3.0 JSON Document.
    """
    OPENAPI_LINK = "openapi-link"
    """
    The OpenAPI 3.0 YAML document is hosted on a publicly accessible internet address.
    """
    OPENAPI_JSON_LINK = "openapi+json-link"
    """
    The OpenAPI 3.0 JSON document is hosted on a publicly accessible internet address.
    """


class Protocol(str, Enum):
    HTTP = "http"
    HTTPS = "https"


class SoapApiType(str, Enum):
    """
    Type of Api to create. 
     * `http` creates a SOAP to REST API 
     * `soap` creates a SOAP pass-through API .
    """
    SOAP_TO_REST = "http"
    """
    Imports a SOAP API having a RESTful front end.
    """
    SOAP_PASS_THROUGH = "soap"
    """
    Imports the Soap API having a SOAP front end.
    """
