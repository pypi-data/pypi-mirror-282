# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ClusterType',
    'NetworkFunctionAdministrativeState',
    'NetworkFunctionType',
    'SkuDefinitions',
    'SkuDeploymentType',
]


class ClusterType(str, Enum):
    """
    Cluster Type
    """
    AKS = "Aks"
    """
    Azure Kubernetes Service
    """
    NEXUS_AKS = "NexusAks"
    """
    Azure Operator Nexus Kubernetes Service
    """


class NetworkFunctionAdministrativeState(str, Enum):
    """
    Administrative state of the network function
    """
    COMMISSIONED = "Commissioned"
    """
    Resource has been commissioned
    """
    DECOMMISSIONED = "Decommissioned"
    """
    Resource has been decommissioned
    """


class NetworkFunctionType(str, Enum):
    """
    Type of network function
    """
    AMF = "AMF"
    """
    Access and Mobility Function
    """
    SMF = "SMF"
    """
    Session Management Function
    """
    UPF = "UPF"
    """
    User Plane Function
    """
    NRF = "NRF"
    """
    Network Repository Function
    """
    NSSF = "NSSF"
    """
    Network Slice Selection Function
    """
    MME = "MME"
    """
    Mobility Management Entity
    """
    SAEGW_CONTROL_PLANE = "SaegwControlPlane"
    """
    System Architecture Evolution Gateway Control Plane, control and user plane separation (CUPS) architecture
    """
    SAEGW_USER_PLANE = "SaegwUserPlane"
    """
    System Architecture Evolution Gateway User Plane, control and user plane separation (CUPS) architecture
    """
    SAEGW = "Saegw"
    """
    System Architecture Evolution Gateway.  This combines the Serving Gateway (SGW) and the Packet Data Network Gateway (PGW) functionality
    """
    E_PDG = "ePDG"
    """
    Evolved Packet Data Gateway
    """
    N3_IWF = "N3IWF"
    """
    Non-3GPP Interworking Function
    """
    REMOTE_PAA_S = "RemotePaaS"
    """
    Remote Platform As A Service Components
    """
    EMS = "EMS"
    """
    Element Management System
    """
    OPERATIONS_POLICY_MANAGER = "OperationsPolicyManager"
    """
    Operations and Policy Manager
    """


class SkuDefinitions(str, Enum):
    """
    Provisioned SKU Value.
    """
    AZURE_LAB = "AzureLab"
    """
    Azure Lab SKU
    """
    AZURE_PRODUCTION = "AzureProduction"
    """
    Azure Production SKU
    """
    NEXUS_LAB = "NexusLab"
    """
    Nexus Lab SKU
    """
    NEXUS_PRODUCTION = "NexusProduction"
    """
    Nexus Production SKU
    """


class SkuDeploymentType(str, Enum):
    """
    Cluster type (Lab or Production)
    """
    PRODUCTION = "Production"
    """
    Production Deployment
    """
    LAB = "Lab"
    """
    Lab Deployment
    """
