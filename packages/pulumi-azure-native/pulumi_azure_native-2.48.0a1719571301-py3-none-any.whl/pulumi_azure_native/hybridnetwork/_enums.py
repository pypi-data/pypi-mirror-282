# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationEnablement',
    'ArtifactReplicationStrategy',
    'ArtifactStoreType',
    'ArtifactType',
    'AzureArcKubernetesArtifactType',
    'AzureCoreArtifactType',
    'AzureOperatorNexusArtifactType',
    'ConfigurationGroupValueConfigurationType',
    'ContainerizedNetworkFunctionNFVIType',
    'DeviceType',
    'DiskCreateOptionTypes',
    'IPAllocationMethod',
    'IPVersion',
    'IdType',
    'ManagedServiceIdentityType',
    'NFVIType',
    'NetworkFunctionRoleConfigurationType',
    'NetworkFunctionType',
    'OperatingSystemTypes',
    'PublisherScope',
    'SkuDeploymentMode',
    'SkuName',
    'SkuType',
    'TemplateType',
    'Type',
    'VMSwitchType',
    'VirtualMachineSizeTypes',
    'VirtualNetworkFunctionNFVIType',
]


class ApplicationEnablement(str, Enum):
    """
    The application enablement.
    """
    UNKNOWN = "Unknown"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ArtifactReplicationStrategy(str, Enum):
    """
    The replication strategy.
    """
    UNKNOWN = "Unknown"
    SINGLE_REPLICATION = "SingleReplication"


class ArtifactStoreType(str, Enum):
    """
    The artifact store type.
    """
    UNKNOWN = "Unknown"
    AZURE_CONTAINER_REGISTRY = "AzureContainerRegistry"
    AZURE_STORAGE_ACCOUNT = "AzureStorageAccount"


class ArtifactType(str, Enum):
    """
    The artifact type.
    """
    UNKNOWN = "Unknown"
    OCI_ARTIFACT = "OCIArtifact"
    VHD_IMAGE_FILE = "VhdImageFile"
    ARM_TEMPLATE = "ArmTemplate"
    IMAGE_FILE = "ImageFile"


class AzureArcKubernetesArtifactType(str, Enum):
    """
    The artifact type.
    """
    UNKNOWN = "Unknown"
    HELM_PACKAGE = "HelmPackage"


class AzureCoreArtifactType(str, Enum):
    """
    The artifact type.
    """
    UNKNOWN = "Unknown"
    VHD_IMAGE_FILE = "VhdImageFile"
    ARM_TEMPLATE = "ArmTemplate"


class AzureOperatorNexusArtifactType(str, Enum):
    """
    The artifact type.
    """
    UNKNOWN = "Unknown"
    IMAGE_FILE = "ImageFile"
    ARM_TEMPLATE = "ArmTemplate"


class ConfigurationGroupValueConfigurationType(str, Enum):
    """
    The value which indicates if configuration values are secrets
    """
    UNKNOWN = "Unknown"
    SECRET = "Secret"
    OPEN = "Open"


class ContainerizedNetworkFunctionNFVIType(str, Enum):
    """
    The network function type.
    """
    UNKNOWN = "Unknown"
    AZURE_ARC_KUBERNETES = "AzureArcKubernetes"


class DeviceType(str, Enum):
    """
    The type of the device.
    """
    UNKNOWN = "Unknown"
    AZURE_STACK_EDGE = "AzureStackEdge"


class DiskCreateOptionTypes(str, Enum):
    """
    Specifies how the virtual machine should be created.
    """
    UNKNOWN = "Unknown"
    EMPTY = "Empty"


class IPAllocationMethod(str, Enum):
    """
    IP address allocation method.
    """
    UNKNOWN = "Unknown"
    STATIC = "Static"
    DYNAMIC = "Dynamic"


class IPVersion(str, Enum):
    """
    IP address version.
    """
    UNKNOWN = "Unknown"
    I_PV4 = "IPv4"


class IdType(str, Enum):
    """
    The resource reference arm id type.
    """
    UNKNOWN = "Unknown"
    OPEN = "Open"
    SECRET = "Secret"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class NFVIType(str, Enum):
    """
    The NFVI type.
    """
    UNKNOWN = "Unknown"
    AZURE_ARC_KUBERNETES = "AzureArcKubernetes"
    AZURE_CORE = "AzureCore"
    AZURE_OPERATOR_NEXUS = "AzureOperatorNexus"


class NetworkFunctionRoleConfigurationType(str, Enum):
    """
    Role type.
    """
    UNKNOWN = "Unknown"
    VIRTUAL_MACHINE = "VirtualMachine"


class NetworkFunctionType(str, Enum):
    """
    The network function type.
    """
    UNKNOWN = "Unknown"
    VIRTUAL_NETWORK_FUNCTION = "VirtualNetworkFunction"
    CONTAINERIZED_NETWORK_FUNCTION = "ContainerizedNetworkFunction"


class OperatingSystemTypes(str, Enum):
    """
    The OS type.
    """
    UNKNOWN = "Unknown"
    WINDOWS = "Windows"
    LINUX = "Linux"


class PublisherScope(str, Enum):
    """
    The publisher scope.
    """
    UNKNOWN = "Unknown"
    PRIVATE = "Private"


class SkuDeploymentMode(str, Enum):
    """
    The sku deployment mode.
    """
    UNKNOWN = "Unknown"
    AZURE = "Azure"
    PRIVATE_EDGE_ZONE = "PrivateEdgeZone"


class SkuName(str, Enum):
    """
    Name of this Sku
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class SkuType(str, Enum):
    """
    The sku type.
    """
    UNKNOWN = "Unknown"
    EVOLVED_PACKET_CORE = "EvolvedPacketCore"
    SDWAN = "SDWAN"
    FIREWALL = "Firewall"


class TemplateType(str, Enum):
    """
    The template type.
    """
    UNKNOWN = "Unknown"
    ARM_TEMPLATE = "ArmTemplate"


class Type(str, Enum):
    """
    The resource element template type.
    """
    UNKNOWN = "Unknown"
    ARM_RESOURCE_DEFINITION = "ArmResourceDefinition"
    NETWORK_FUNCTION_DEFINITION = "NetworkFunctionDefinition"


class VMSwitchType(str, Enum):
    """
    The type of the VM switch.
    """
    UNKNOWN = "Unknown"
    MANAGEMENT = "Management"
    WAN = "Wan"
    LAN = "Lan"


class VirtualMachineSizeTypes(str, Enum):
    """
    The size of the virtual machine.
    """
    UNKNOWN = "Unknown"
    STANDARD_D1_V2 = "Standard_D1_v2"
    STANDARD_D2_V2 = "Standard_D2_v2"
    STANDARD_D3_V2 = "Standard_D3_v2"
    STANDARD_D4_V2 = "Standard_D4_v2"
    STANDARD_D5_V2 = "Standard_D5_v2"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_DS1_V2 = "Standard_DS1_v2"
    STANDARD_DS2_V2 = "Standard_DS2_v2"
    STANDARD_DS3_V2 = "Standard_DS3_v2"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_DS11_V2 = "Standard_DS11_v2"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_F1 = "Standard_F1"
    STANDARD_F2 = "Standard_F2"
    STANDARD_F4 = "Standard_F4"
    STANDARD_F8 = "Standard_F8"
    STANDARD_F16 = "Standard_F16"
    STANDARD_F1S = "Standard_F1s"
    STANDARD_F2S = "Standard_F2s"
    STANDARD_F4S = "Standard_F4s"
    STANDARD_F8S = "Standard_F8s"
    STANDARD_F16S = "Standard_F16s"


class VirtualNetworkFunctionNFVIType(str, Enum):
    """
    The network function type.
    """
    UNKNOWN = "Unknown"
    AZURE_CORE = "AzureCore"
    AZURE_OPERATOR_NEXUS = "AzureOperatorNexus"
