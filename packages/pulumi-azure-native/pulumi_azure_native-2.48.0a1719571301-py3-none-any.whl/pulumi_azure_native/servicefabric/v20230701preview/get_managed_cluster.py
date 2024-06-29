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

__all__ = [
    'GetManagedClusterResult',
    'AwaitableGetManagedClusterResult',
    'get_managed_cluster',
    'get_managed_cluster_output',
]

@pulumi.output_type
class GetManagedClusterResult:
    """
    The managed cluster resource
    """
    def __init__(__self__, addon_features=None, admin_password=None, admin_user_name=None, allow_rdp_access=None, application_type_versions_cleanup_policy=None, auxiliary_subnets=None, azure_active_directory=None, client_connection_port=None, clients=None, cluster_certificate_thumbprints=None, cluster_code_version=None, cluster_id=None, cluster_state=None, cluster_upgrade_cadence=None, cluster_upgrade_mode=None, ddos_protection_plan_id=None, dns_name=None, enable_auto_os_upgrade=None, enable_ipv6=None, enable_service_public_ip=None, etag=None, fabric_settings=None, fqdn=None, http_gateway_connection_port=None, id=None, ip_tags=None, ipv4_address=None, ipv6_address=None, load_balancing_rules=None, location=None, name=None, network_security_rules=None, provisioning_state=None, public_ip_prefix_id=None, service_endpoints=None, sku=None, subnet_id=None, system_data=None, tags=None, type=None, use_custom_vnet=None, zonal_resiliency=None, zonal_update_mode=None):
        if addon_features and not isinstance(addon_features, list):
            raise TypeError("Expected argument 'addon_features' to be a list")
        pulumi.set(__self__, "addon_features", addon_features)
        if admin_password and not isinstance(admin_password, str):
            raise TypeError("Expected argument 'admin_password' to be a str")
        pulumi.set(__self__, "admin_password", admin_password)
        if admin_user_name and not isinstance(admin_user_name, str):
            raise TypeError("Expected argument 'admin_user_name' to be a str")
        pulumi.set(__self__, "admin_user_name", admin_user_name)
        if allow_rdp_access and not isinstance(allow_rdp_access, bool):
            raise TypeError("Expected argument 'allow_rdp_access' to be a bool")
        pulumi.set(__self__, "allow_rdp_access", allow_rdp_access)
        if application_type_versions_cleanup_policy and not isinstance(application_type_versions_cleanup_policy, dict):
            raise TypeError("Expected argument 'application_type_versions_cleanup_policy' to be a dict")
        pulumi.set(__self__, "application_type_versions_cleanup_policy", application_type_versions_cleanup_policy)
        if auxiliary_subnets and not isinstance(auxiliary_subnets, list):
            raise TypeError("Expected argument 'auxiliary_subnets' to be a list")
        pulumi.set(__self__, "auxiliary_subnets", auxiliary_subnets)
        if azure_active_directory and not isinstance(azure_active_directory, dict):
            raise TypeError("Expected argument 'azure_active_directory' to be a dict")
        pulumi.set(__self__, "azure_active_directory", azure_active_directory)
        if client_connection_port and not isinstance(client_connection_port, int):
            raise TypeError("Expected argument 'client_connection_port' to be a int")
        pulumi.set(__self__, "client_connection_port", client_connection_port)
        if clients and not isinstance(clients, list):
            raise TypeError("Expected argument 'clients' to be a list")
        pulumi.set(__self__, "clients", clients)
        if cluster_certificate_thumbprints and not isinstance(cluster_certificate_thumbprints, list):
            raise TypeError("Expected argument 'cluster_certificate_thumbprints' to be a list")
        pulumi.set(__self__, "cluster_certificate_thumbprints", cluster_certificate_thumbprints)
        if cluster_code_version and not isinstance(cluster_code_version, str):
            raise TypeError("Expected argument 'cluster_code_version' to be a str")
        pulumi.set(__self__, "cluster_code_version", cluster_code_version)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_state and not isinstance(cluster_state, str):
            raise TypeError("Expected argument 'cluster_state' to be a str")
        pulumi.set(__self__, "cluster_state", cluster_state)
        if cluster_upgrade_cadence and not isinstance(cluster_upgrade_cadence, str):
            raise TypeError("Expected argument 'cluster_upgrade_cadence' to be a str")
        pulumi.set(__self__, "cluster_upgrade_cadence", cluster_upgrade_cadence)
        if cluster_upgrade_mode and not isinstance(cluster_upgrade_mode, str):
            raise TypeError("Expected argument 'cluster_upgrade_mode' to be a str")
        pulumi.set(__self__, "cluster_upgrade_mode", cluster_upgrade_mode)
        if ddos_protection_plan_id and not isinstance(ddos_protection_plan_id, str):
            raise TypeError("Expected argument 'ddos_protection_plan_id' to be a str")
        pulumi.set(__self__, "ddos_protection_plan_id", ddos_protection_plan_id)
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        pulumi.set(__self__, "dns_name", dns_name)
        if enable_auto_os_upgrade and not isinstance(enable_auto_os_upgrade, bool):
            raise TypeError("Expected argument 'enable_auto_os_upgrade' to be a bool")
        pulumi.set(__self__, "enable_auto_os_upgrade", enable_auto_os_upgrade)
        if enable_ipv6 and not isinstance(enable_ipv6, bool):
            raise TypeError("Expected argument 'enable_ipv6' to be a bool")
        pulumi.set(__self__, "enable_ipv6", enable_ipv6)
        if enable_service_public_ip and not isinstance(enable_service_public_ip, bool):
            raise TypeError("Expected argument 'enable_service_public_ip' to be a bool")
        pulumi.set(__self__, "enable_service_public_ip", enable_service_public_ip)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if fabric_settings and not isinstance(fabric_settings, list):
            raise TypeError("Expected argument 'fabric_settings' to be a list")
        pulumi.set(__self__, "fabric_settings", fabric_settings)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if http_gateway_connection_port and not isinstance(http_gateway_connection_port, int):
            raise TypeError("Expected argument 'http_gateway_connection_port' to be a int")
        pulumi.set(__self__, "http_gateway_connection_port", http_gateway_connection_port)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_tags and not isinstance(ip_tags, list):
            raise TypeError("Expected argument 'ip_tags' to be a list")
        pulumi.set(__self__, "ip_tags", ip_tags)
        if ipv4_address and not isinstance(ipv4_address, str):
            raise TypeError("Expected argument 'ipv4_address' to be a str")
        pulumi.set(__self__, "ipv4_address", ipv4_address)
        if ipv6_address and not isinstance(ipv6_address, str):
            raise TypeError("Expected argument 'ipv6_address' to be a str")
        pulumi.set(__self__, "ipv6_address", ipv6_address)
        if load_balancing_rules and not isinstance(load_balancing_rules, list):
            raise TypeError("Expected argument 'load_balancing_rules' to be a list")
        pulumi.set(__self__, "load_balancing_rules", load_balancing_rules)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_security_rules and not isinstance(network_security_rules, list):
            raise TypeError("Expected argument 'network_security_rules' to be a list")
        pulumi.set(__self__, "network_security_rules", network_security_rules)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_ip_prefix_id and not isinstance(public_ip_prefix_id, str):
            raise TypeError("Expected argument 'public_ip_prefix_id' to be a str")
        pulumi.set(__self__, "public_ip_prefix_id", public_ip_prefix_id)
        if service_endpoints and not isinstance(service_endpoints, list):
            raise TypeError("Expected argument 'service_endpoints' to be a list")
        pulumi.set(__self__, "service_endpoints", service_endpoints)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if use_custom_vnet and not isinstance(use_custom_vnet, bool):
            raise TypeError("Expected argument 'use_custom_vnet' to be a bool")
        pulumi.set(__self__, "use_custom_vnet", use_custom_vnet)
        if zonal_resiliency and not isinstance(zonal_resiliency, bool):
            raise TypeError("Expected argument 'zonal_resiliency' to be a bool")
        pulumi.set(__self__, "zonal_resiliency", zonal_resiliency)
        if zonal_update_mode and not isinstance(zonal_update_mode, str):
            raise TypeError("Expected argument 'zonal_update_mode' to be a str")
        pulumi.set(__self__, "zonal_update_mode", zonal_update_mode)

    @property
    @pulumi.getter(name="addonFeatures")
    def addon_features(self) -> Optional[Sequence[str]]:
        """
        List of add-on features to enable on the cluster.
        """
        return pulumi.get(self, "addon_features")

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[str]:
        """
        VM admin user password.
        """
        return pulumi.get(self, "admin_password")

    @property
    @pulumi.getter(name="adminUserName")
    def admin_user_name(self) -> str:
        """
        VM admin user name.
        """
        return pulumi.get(self, "admin_user_name")

    @property
    @pulumi.getter(name="allowRdpAccess")
    def allow_rdp_access(self) -> Optional[bool]:
        """
        Setting this to true enables RDP access to the VM. The default NSG rule opens RDP port to Internet which can be overridden with custom Network Security Rules. The default value for this setting is false.
        """
        return pulumi.get(self, "allow_rdp_access")

    @property
    @pulumi.getter(name="applicationTypeVersionsCleanupPolicy")
    def application_type_versions_cleanup_policy(self) -> Optional['outputs.ApplicationTypeVersionsCleanupPolicyResponse']:
        """
        The policy used to clean up unused versions.
        """
        return pulumi.get(self, "application_type_versions_cleanup_policy")

    @property
    @pulumi.getter(name="auxiliarySubnets")
    def auxiliary_subnets(self) -> Optional[Sequence['outputs.SubnetResponse']]:
        """
        Auxiliary subnets for the cluster.
        """
        return pulumi.get(self, "auxiliary_subnets")

    @property
    @pulumi.getter(name="azureActiveDirectory")
    def azure_active_directory(self) -> Optional['outputs.AzureActiveDirectoryResponse']:
        """
        The AAD authentication settings of the cluster.
        """
        return pulumi.get(self, "azure_active_directory")

    @property
    @pulumi.getter(name="clientConnectionPort")
    def client_connection_port(self) -> Optional[int]:
        """
        The port used for client connections to the cluster.
        """
        return pulumi.get(self, "client_connection_port")

    @property
    @pulumi.getter
    def clients(self) -> Optional[Sequence['outputs.ClientCertificateResponse']]:
        """
        Client certificates that are allowed to manage the cluster.
        """
        return pulumi.get(self, "clients")

    @property
    @pulumi.getter(name="clusterCertificateThumbprints")
    def cluster_certificate_thumbprints(self) -> Sequence[str]:
        """
        List of thumbprints of the cluster certificates.
        """
        return pulumi.get(self, "cluster_certificate_thumbprints")

    @property
    @pulumi.getter(name="clusterCodeVersion")
    def cluster_code_version(self) -> Optional[str]:
        """
        The Service Fabric runtime version of the cluster. This property is required when **clusterUpgradeMode** is set to 'Manual'. To get list of available Service Fabric versions for new clusters use [ClusterVersion API](./ClusterVersion.md). To get the list of available version for existing clusters use **availableClusterVersions**.
        """
        return pulumi.get(self, "cluster_code_version")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        A service generated unique identifier for the cluster resource.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterState")
    def cluster_state(self) -> str:
        """
        The current state of the cluster.
        """
        return pulumi.get(self, "cluster_state")

    @property
    @pulumi.getter(name="clusterUpgradeCadence")
    def cluster_upgrade_cadence(self) -> Optional[str]:
        """
        Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0. Only applies when **clusterUpgradeMode** is set to 'Automatic'.
        """
        return pulumi.get(self, "cluster_upgrade_cadence")

    @property
    @pulumi.getter(name="clusterUpgradeMode")
    def cluster_upgrade_mode(self) -> Optional[str]:
        """
        The upgrade mode of the cluster when new Service Fabric runtime version is available.
        """
        return pulumi.get(self, "cluster_upgrade_mode")

    @property
    @pulumi.getter(name="ddosProtectionPlanId")
    def ddos_protection_plan_id(self) -> Optional[str]:
        """
        Specify the resource id of a DDoS network protection plan that will be associated with the virtual network of the cluster.
        """
        return pulumi.get(self, "ddos_protection_plan_id")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> str:
        """
        The cluster dns name.
        """
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="enableAutoOSUpgrade")
    def enable_auto_os_upgrade(self) -> Optional[bool]:
        """
        Setting this to true enables automatic OS upgrade for the node types that are created using any platform OS image with version 'latest'. The default value for this setting is false.
        """
        return pulumi.get(self, "enable_auto_os_upgrade")

    @property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[bool]:
        """
        Setting this to true creates IPv6 address space for the default VNet used by the cluster. This setting cannot be changed once the cluster is created. The default value for this setting is false.
        """
        return pulumi.get(self, "enable_ipv6")

    @property
    @pulumi.getter(name="enableServicePublicIP")
    def enable_service_public_ip(self) -> Optional[bool]:
        """
        Setting this to true will link the IPv4 address as the ServicePublicIP of the IPv6 address. It can only be set to True if IPv6 is enabled on the cluster.
        """
        return pulumi.get(self, "enable_service_public_ip")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Azure resource etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="fabricSettings")
    def fabric_settings(self) -> Optional[Sequence['outputs.SettingsSectionDescriptionResponse']]:
        """
        The list of custom fabric settings to configure the cluster.
        """
        return pulumi.get(self, "fabric_settings")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The fully qualified domain name associated with the public load balancer of the cluster.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="httpGatewayConnectionPort")
    def http_gateway_connection_port(self) -> Optional[int]:
        """
        The port used for HTTP connections to the cluster.
        """
        return pulumi.get(self, "http_gateway_connection_port")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[Sequence['outputs.IPTagResponse']]:
        """
        The list of IP tags associated with the default public IP address of the cluster.
        """
        return pulumi.get(self, "ip_tags")

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> str:
        """
        The IPv4 address associated with the public load balancer of the cluster.
        """
        return pulumi.get(self, "ipv4_address")

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> str:
        """
        IPv6 address for the cluster if IPv6 is enabled.
        """
        return pulumi.get(self, "ipv6_address")

    @property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(self) -> Optional[Sequence['outputs.LoadBalancingRuleResponse']]:
        """
        Load balancing rules that are applied to the public load balancer of the cluster.
        """
        return pulumi.get(self, "load_balancing_rules")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Azure resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSecurityRules")
    def network_security_rules(self) -> Optional[Sequence['outputs.NetworkSecurityRuleResponse']]:
        """
        Custom Network Security Rules that are applied to the Virtual Network of the cluster.
        """
        return pulumi.get(self, "network_security_rules")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the managed cluster resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIPPrefixId")
    def public_ip_prefix_id(self) -> Optional[str]:
        """
        Specify the resource id of a public IP prefix that the load balancer will allocate a public IP address from. Only supports IPv4.
        """
        return pulumi.get(self, "public_ip_prefix_id")

    @property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> Optional[Sequence['outputs.ServiceEndpointResponse']]:
        """
        Service endpoints for subnets in the cluster.
        """
        return pulumi.get(self, "service_endpoints")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        The sku of the managed cluster
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        If specified, the node types for the cluster are created in this subnet instead of the default VNet. The **networkSecurityRules** specified for the cluster are also applied to this subnet. This setting cannot be changed once the cluster is created.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useCustomVnet")
    def use_custom_vnet(self) -> Optional[bool]:
        """
        For new clusters, this parameter indicates that it uses Bring your own VNet, but the subnet is specified at node type level; and for such clusters, the subnetId property is required for node types.
        """
        return pulumi.get(self, "use_custom_vnet")

    @property
    @pulumi.getter(name="zonalResiliency")
    def zonal_resiliency(self) -> Optional[bool]:
        """
        Indicates if the cluster has zone resiliency.
        """
        return pulumi.get(self, "zonal_resiliency")

    @property
    @pulumi.getter(name="zonalUpdateMode")
    def zonal_update_mode(self) -> Optional[str]:
        """
        Indicates the update mode for Cross Az clusters.
        """
        return pulumi.get(self, "zonal_update_mode")


class AwaitableGetManagedClusterResult(GetManagedClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedClusterResult(
            addon_features=self.addon_features,
            admin_password=self.admin_password,
            admin_user_name=self.admin_user_name,
            allow_rdp_access=self.allow_rdp_access,
            application_type_versions_cleanup_policy=self.application_type_versions_cleanup_policy,
            auxiliary_subnets=self.auxiliary_subnets,
            azure_active_directory=self.azure_active_directory,
            client_connection_port=self.client_connection_port,
            clients=self.clients,
            cluster_certificate_thumbprints=self.cluster_certificate_thumbprints,
            cluster_code_version=self.cluster_code_version,
            cluster_id=self.cluster_id,
            cluster_state=self.cluster_state,
            cluster_upgrade_cadence=self.cluster_upgrade_cadence,
            cluster_upgrade_mode=self.cluster_upgrade_mode,
            ddos_protection_plan_id=self.ddos_protection_plan_id,
            dns_name=self.dns_name,
            enable_auto_os_upgrade=self.enable_auto_os_upgrade,
            enable_ipv6=self.enable_ipv6,
            enable_service_public_ip=self.enable_service_public_ip,
            etag=self.etag,
            fabric_settings=self.fabric_settings,
            fqdn=self.fqdn,
            http_gateway_connection_port=self.http_gateway_connection_port,
            id=self.id,
            ip_tags=self.ip_tags,
            ipv4_address=self.ipv4_address,
            ipv6_address=self.ipv6_address,
            load_balancing_rules=self.load_balancing_rules,
            location=self.location,
            name=self.name,
            network_security_rules=self.network_security_rules,
            provisioning_state=self.provisioning_state,
            public_ip_prefix_id=self.public_ip_prefix_id,
            service_endpoints=self.service_endpoints,
            sku=self.sku,
            subnet_id=self.subnet_id,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            use_custom_vnet=self.use_custom_vnet,
            zonal_resiliency=self.zonal_resiliency,
            zonal_update_mode=self.zonal_update_mode)


def get_managed_cluster(cluster_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedClusterResult:
    """
    Get a Service Fabric managed cluster resource created or in the process of being created in the specified resource group.


    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20230701preview:getManagedCluster', __args__, opts=opts, typ=GetManagedClusterResult).value

    return AwaitableGetManagedClusterResult(
        addon_features=pulumi.get(__ret__, 'addon_features'),
        admin_password=pulumi.get(__ret__, 'admin_password'),
        admin_user_name=pulumi.get(__ret__, 'admin_user_name'),
        allow_rdp_access=pulumi.get(__ret__, 'allow_rdp_access'),
        application_type_versions_cleanup_policy=pulumi.get(__ret__, 'application_type_versions_cleanup_policy'),
        auxiliary_subnets=pulumi.get(__ret__, 'auxiliary_subnets'),
        azure_active_directory=pulumi.get(__ret__, 'azure_active_directory'),
        client_connection_port=pulumi.get(__ret__, 'client_connection_port'),
        clients=pulumi.get(__ret__, 'clients'),
        cluster_certificate_thumbprints=pulumi.get(__ret__, 'cluster_certificate_thumbprints'),
        cluster_code_version=pulumi.get(__ret__, 'cluster_code_version'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        cluster_state=pulumi.get(__ret__, 'cluster_state'),
        cluster_upgrade_cadence=pulumi.get(__ret__, 'cluster_upgrade_cadence'),
        cluster_upgrade_mode=pulumi.get(__ret__, 'cluster_upgrade_mode'),
        ddos_protection_plan_id=pulumi.get(__ret__, 'ddos_protection_plan_id'),
        dns_name=pulumi.get(__ret__, 'dns_name'),
        enable_auto_os_upgrade=pulumi.get(__ret__, 'enable_auto_os_upgrade'),
        enable_ipv6=pulumi.get(__ret__, 'enable_ipv6'),
        enable_service_public_ip=pulumi.get(__ret__, 'enable_service_public_ip'),
        etag=pulumi.get(__ret__, 'etag'),
        fabric_settings=pulumi.get(__ret__, 'fabric_settings'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        http_gateway_connection_port=pulumi.get(__ret__, 'http_gateway_connection_port'),
        id=pulumi.get(__ret__, 'id'),
        ip_tags=pulumi.get(__ret__, 'ip_tags'),
        ipv4_address=pulumi.get(__ret__, 'ipv4_address'),
        ipv6_address=pulumi.get(__ret__, 'ipv6_address'),
        load_balancing_rules=pulumi.get(__ret__, 'load_balancing_rules'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_security_rules=pulumi.get(__ret__, 'network_security_rules'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_ip_prefix_id=pulumi.get(__ret__, 'public_ip_prefix_id'),
        service_endpoints=pulumi.get(__ret__, 'service_endpoints'),
        sku=pulumi.get(__ret__, 'sku'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        use_custom_vnet=pulumi.get(__ret__, 'use_custom_vnet'),
        zonal_resiliency=pulumi.get(__ret__, 'zonal_resiliency'),
        zonal_update_mode=pulumi.get(__ret__, 'zonal_update_mode'))


@_utilities.lift_output_func(get_managed_cluster)
def get_managed_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedClusterResult]:
    """
    Get a Service Fabric managed cluster resource created or in the process of being created in the specified resource group.


    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    ...
