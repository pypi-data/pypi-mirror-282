# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationGatewayCookieBasedAffinity',
    'ApplicationGatewayCustomErrorStatusCode',
    'ApplicationGatewayFirewallMode',
    'ApplicationGatewayProtocol',
    'ApplicationGatewayRedirectType',
    'ApplicationGatewayRequestRoutingRuleType',
    'ApplicationGatewaySkuName',
    'ApplicationGatewaySslCipherSuite',
    'ApplicationGatewaySslPolicyName',
    'ApplicationGatewaySslPolicyType',
    'ApplicationGatewaySslProtocol',
    'ApplicationGatewayTier',
    'AuthorizationUseStatus',
    'DdosSettingsProtectionCoverage',
    'ExpressRouteCircuitPeeringAdvertisedPublicPrefixState',
    'ExpressRouteCircuitPeeringState',
    'ExpressRouteCircuitSkuFamily',
    'ExpressRouteCircuitSkuTier',
    'ExpressRoutePeeringState',
    'ExpressRoutePeeringType',
    'IPAllocationMethod',
    'IPVersion',
    'LoadBalancerOutboundRuleProtocol',
    'LoadBalancerSkuName',
    'LoadDistribution',
    'NatGatewaySkuName',
    'ProbeProtocol',
    'PublicIPAddressSkuName',
    'PublicIPPrefixSkuName',
    'ResourceIdentityType',
    'RouteNextHopType',
    'SecurityRuleAccess',
    'SecurityRuleDirection',
    'SecurityRuleProtocol',
    'ServiceProviderProvisioningState',
    'TransportProtocol',
    'VirtualNetworkPeeringState',
]


class ApplicationGatewayCookieBasedAffinity(str, Enum):
    """
    Cookie based affinity.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ApplicationGatewayCustomErrorStatusCode(str, Enum):
    """
    Status code of the application gateway customer error.
    """
    HTTP_STATUS403 = "HttpStatus403"
    HTTP_STATUS502 = "HttpStatus502"


class ApplicationGatewayFirewallMode(str, Enum):
    """
    Web application firewall mode.
    """
    DETECTION = "Detection"
    PREVENTION = "Prevention"


class ApplicationGatewayProtocol(str, Enum):
    """
    The protocol used for the probe.
    """
    HTTP = "Http"
    HTTPS = "Https"


class ApplicationGatewayRedirectType(str, Enum):
    """
    HTTP redirection type.
    """
    PERMANENT = "Permanent"
    FOUND = "Found"
    SEE_OTHER = "SeeOther"
    TEMPORARY = "Temporary"


class ApplicationGatewayRequestRoutingRuleType(str, Enum):
    """
    Rule type.
    """
    BASIC = "Basic"
    PATH_BASED_ROUTING = "PathBasedRouting"


class ApplicationGatewaySkuName(str, Enum):
    """
    Name of an application gateway SKU.
    """
    STANDARD_SMALL = "Standard_Small"
    STANDARD_MEDIUM = "Standard_Medium"
    STANDARD_LARGE = "Standard_Large"
    WA_F_MEDIUM = "WAF_Medium"
    WA_F_LARGE = "WAF_Large"
    STANDARD_V2 = "Standard_v2"
    WA_F_V2 = "WAF_v2"


class ApplicationGatewaySslCipherSuite(str, Enum):
    """
    Ssl cipher suites enums.
    """
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_256_CB_C_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"
    TL_S_DH_E_RS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384"
    TL_S_DH_E_RS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256"
    TL_S_DH_E_RS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_DHE_RSA_WITH_AES_256_CBC_SHA"
    TL_S_DH_E_RS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_DHE_RSA_WITH_AES_128_CBC_SHA"
    TL_S_RS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_RSA_WITH_AES_256_GCM_SHA384"
    TL_S_RS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_RSA_WITH_AES_128_GCM_SHA256"
    TL_S_RS_A_WIT_H_AE_S_256_CB_C_SHA256 = "TLS_RSA_WITH_AES_256_CBC_SHA256"
    TL_S_RS_A_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_RSA_WITH_AES_128_CBC_SHA256"
    TL_S_RS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_RSA_WITH_AES_256_CBC_SHA"
    TL_S_RS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_RSA_WITH_AES_128_CBC_SHA"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_256_CB_C_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_256_CB_C_SHA = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA"
    TL_S_ECDH_E_ECDS_A_WIT_H_AE_S_128_CB_C_SHA = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA"
    TL_S_DH_E_DS_S_WIT_H_AE_S_256_CB_C_SHA256 = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256"
    TL_S_DH_E_DS_S_WIT_H_AE_S_128_CB_C_SHA256 = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256"
    TL_S_DH_E_DS_S_WIT_H_AE_S_256_CB_C_SHA = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA"
    TL_S_DH_E_DS_S_WIT_H_AE_S_128_CB_C_SHA = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA"
    TL_S_RS_A_WIT_H_3_DE_S_ED_E_CB_C_SHA = "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
    TL_S_DH_E_DS_S_WIT_H_3_DE_S_ED_E_CB_C_SHA = "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_128_GC_M_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
    TL_S_ECDH_E_RS_A_WIT_H_AE_S_256_GC_M_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"


class ApplicationGatewaySslPolicyName(str, Enum):
    """
    Name of Ssl predefined policy.
    """
    APP_GW_SSL_POLICY20150501 = "AppGwSslPolicy20150501"
    APP_GW_SSL_POLICY20170401 = "AppGwSslPolicy20170401"
    APP_GW_SSL_POLICY20170401_S = "AppGwSslPolicy20170401S"


class ApplicationGatewaySslPolicyType(str, Enum):
    """
    Type of Ssl Policy.
    """
    PREDEFINED = "Predefined"
    CUSTOM = "Custom"


class ApplicationGatewaySslProtocol(str, Enum):
    """
    Minimum version of Ssl protocol to be supported on application gateway.
    """
    TL_SV1_0 = "TLSv1_0"
    TL_SV1_1 = "TLSv1_1"
    TL_SV1_2 = "TLSv1_2"


class ApplicationGatewayTier(str, Enum):
    """
    Tier of an application gateway.
    """
    STANDARD = "Standard"
    WAF = "WAF"
    STANDARD_V2 = "Standard_v2"
    WA_F_V2 = "WAF_v2"


class AuthorizationUseStatus(str, Enum):
    """
    The authorization use status.
    """
    AVAILABLE = "Available"
    IN_USE = "InUse"


class DdosSettingsProtectionCoverage(str, Enum):
    """
    The DDoS protection policy customizability of the public IP. Only standard coverage will have the ability to be customized.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(str, Enum):
    """
    The advertised public prefix state of the Peering resource.
    """
    NOT_CONFIGURED = "NotConfigured"
    CONFIGURING = "Configuring"
    CONFIGURED = "Configured"
    VALIDATION_NEEDED = "ValidationNeeded"


class ExpressRouteCircuitPeeringState(str, Enum):
    """
    The state of peering.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRouteCircuitSkuFamily(str, Enum):
    """
    The family of the SKU.
    """
    UNLIMITED_DATA = "UnlimitedData"
    METERED_DATA = "MeteredData"


class ExpressRouteCircuitSkuTier(str, Enum):
    """
    The tier of the SKU.
    """
    STANDARD = "Standard"
    PREMIUM = "Premium"
    BASIC = "Basic"
    LOCAL = "Local"


class ExpressRoutePeeringState(str, Enum):
    """
    The peering state.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRoutePeeringType(str, Enum):
    """
    The peering type.
    """
    AZURE_PUBLIC_PEERING = "AzurePublicPeering"
    AZURE_PRIVATE_PEERING = "AzurePrivatePeering"
    MICROSOFT_PEERING = "MicrosoftPeering"


class IPAllocationMethod(str, Enum):
    """
    The public IP address allocation method.
    """
    STATIC = "Static"
    DYNAMIC = "Dynamic"


class IPVersion(str, Enum):
    """
    The public IP address version.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class LoadBalancerOutboundRuleProtocol(str, Enum):
    """
    The protocol for the outbound rule in load balancer.
    """
    TCP = "Tcp"
    UDP = "Udp"
    ALL = "All"


class LoadBalancerSkuName(str, Enum):
    """
    Name of a load balancer SKU.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class LoadDistribution(str, Enum):
    """
    The load distribution policy for this rule.
    """
    DEFAULT = "Default"
    SOURCE_IP = "SourceIP"
    SOURCE_IP_PROTOCOL = "SourceIPProtocol"


class NatGatewaySkuName(str, Enum):
    """
    Name of Nat Gateway SKU.
    """
    STANDARD = "Standard"


class ProbeProtocol(str, Enum):
    """
    The protocol of the end point. If 'Tcp' is specified, a received ACK is required for the probe to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI is required for the probe to be successful.
    """
    HTTP = "Http"
    TCP = "Tcp"
    HTTPS = "Https"


class PublicIPAddressSkuName(str, Enum):
    """
    Name of a public IP address SKU.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class PublicIPPrefixSkuName(str, Enum):
    """
    Name of a public IP prefix SKU.
    """
    STANDARD = "Standard"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the virtual machine.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class RouteNextHopType(str, Enum):
    """
    The type of Azure hop the packet should be sent to.
    """
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    NONE = "None"


class SecurityRuleAccess(str, Enum):
    """
    The network traffic is allowed or denied.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class SecurityRuleDirection(str, Enum):
    """
    The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityRuleProtocol(str, Enum):
    """
    Network protocol this rule applies to.
    """
    TCP = "Tcp"
    UDP = "Udp"
    ICMP = "Icmp"
    ESP = "Esp"
    ASTERISK = "*"


class ServiceProviderProvisioningState(str, Enum):
    """
    The ServiceProviderProvisioningState state of the resource.
    """
    NOT_PROVISIONED = "NotProvisioned"
    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    DEPROVISIONING = "Deprovisioning"


class TransportProtocol(str, Enum):
    """
    The reference to the transport protocol used by the load balancing rule.
    """
    UDP = "Udp"
    TCP = "Tcp"
    ALL = "All"


class VirtualNetworkPeeringState(str, Enum):
    """
    The status of the virtual network peering.
    """
    INITIATED = "Initiated"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
