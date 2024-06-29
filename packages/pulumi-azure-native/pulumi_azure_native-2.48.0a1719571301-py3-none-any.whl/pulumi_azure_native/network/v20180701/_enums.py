# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DhGroup',
    'IPAllocationMethod',
    'IPVersion',
    'IkeEncryption',
    'IkeIntegrity',
    'IpsecEncryption',
    'IpsecIntegrity',
    'PfsGroup',
    'PublicIPAddressSkuName',
    'RouteNextHopType',
    'SecurityRuleAccess',
    'SecurityRuleDirection',
    'SecurityRuleProtocol',
    'TransportProtocol',
]


class DhGroup(str, Enum):
    """
    The DH Groups used in IKE Phase 1 for initial SA.
    """
    NONE = "None"
    DH_GROUP1 = "DHGroup1"
    DH_GROUP2 = "DHGroup2"
    DH_GROUP14 = "DHGroup14"
    DH_GROUP2048 = "DHGroup2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    DH_GROUP24 = "DHGroup24"


class IPAllocationMethod(str, Enum):
    """
    The public IP allocation method. Possible values are: 'Static' and 'Dynamic'.
    """
    STATIC = "Static"
    DYNAMIC = "Dynamic"


class IPVersion(str, Enum):
    """
    The public IP address version. Possible values are: 'IPv4' and 'IPv6'.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class IkeEncryption(str, Enum):
    """
    The IKE encryption algorithm (IKE phase 2).
    """
    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IkeIntegrity(str, Enum):
    """
    The IKE integrity algorithm (IKE phase 2).
    """
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IpsecEncryption(str, Enum):
    """
    The IPSec encryption algorithm (IKE phase 1).
    """
    NONE = "None"
    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class IpsecIntegrity(str, Enum):
    """
    The IPSec integrity algorithm (IKE phase 1).
    """
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class PfsGroup(str, Enum):
    """
    The Pfs Groups used in IKE Phase 2 for new child SA.
    """
    NONE = "None"
    PFS1 = "PFS1"
    PFS2 = "PFS2"
    PFS2048 = "PFS2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    PFS24 = "PFS24"
    PFS14 = "PFS14"
    PFSMM = "PFSMM"


class PublicIPAddressSkuName(str, Enum):
    """
    Name of a public IP address SKU.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class RouteNextHopType(str, Enum):
    """
    The type of Azure hop the packet should be sent to. Possible values are: 'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'VirtualAppliance', and 'None'
    """
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    NONE = "None"


class SecurityRuleAccess(str, Enum):
    """
    The network traffic is allowed or denied. Possible values are: 'Allow' and 'Deny'.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class SecurityRuleDirection(str, Enum):
    """
    The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are: 'Inbound' and 'Outbound'.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityRuleProtocol(str, Enum):
    """
    Network protocol this rule applies to. Possible values are 'Tcp', 'Udp', and '*'.
    """
    TCP = "Tcp"
    UDP = "Udp"
    ASTERISK = "*"


class TransportProtocol(str, Enum):
    """
    The transport protocol for the endpoint. Possible values are 'Udp' or 'Tcp' or 'All'.
    """
    UDP = "Udp"
    TCP = "Tcp"
    ALL = "All"
