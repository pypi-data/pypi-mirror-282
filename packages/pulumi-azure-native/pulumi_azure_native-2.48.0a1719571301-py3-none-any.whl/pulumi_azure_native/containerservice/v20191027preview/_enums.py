# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'OSType',
    'OpenShiftAgentPoolProfileRole',
    'OpenShiftContainerServiceVMSize',
]


class OSType(str, Enum):
    """
    OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux.
    """
    LINUX = "Linux"
    WINDOWS = "Windows"


class OpenShiftAgentPoolProfileRole(str, Enum):
    """
    Define the role of the AgentPoolProfile.
    """
    COMPUTE = "compute"
    INFRA = "infra"


class OpenShiftContainerServiceVMSize(str, Enum):
    """
    Size of agent VMs.
    """
    STANDARD_D2S_V3 = "Standard_D2s_v3"
    STANDARD_D4S_V3 = "Standard_D4s_v3"
    STANDARD_D8S_V3 = "Standard_D8s_v3"
    STANDARD_D16S_V3 = "Standard_D16s_v3"
    STANDARD_D32S_V3 = "Standard_D32s_v3"
    STANDARD_D64S_V3 = "Standard_D64s_v3"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_F8S_V2 = "Standard_F8s_v2"
    STANDARD_F16S_V2 = "Standard_F16s_v2"
    STANDARD_F32S_V2 = "Standard_F32s_v2"
    STANDARD_F64S_V2 = "Standard_F64s_v2"
    STANDARD_F72S_V2 = "Standard_F72s_v2"
    STANDARD_F8S = "Standard_F8s"
    STANDARD_F16S = "Standard_F16s"
    STANDARD_E4S_V3 = "Standard_E4s_v3"
    STANDARD_E8S_V3 = "Standard_E8s_v3"
    STANDARD_E16S_V3 = "Standard_E16s_v3"
    STANDARD_E20S_V3 = "Standard_E20s_v3"
    STANDARD_E32S_V3 = "Standard_E32s_v3"
    STANDARD_E64S_V3 = "Standard_E64s_v3"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS5 = "Standard_GS5"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_DS14_V2 = "Standard_DS14_v2"
    STANDARD_DS15_V2 = "Standard_DS15_v2"
    STANDARD_L4S = "Standard_L4s"
    STANDARD_L8S = "Standard_L8s"
    STANDARD_L16S = "Standard_L16s"
    STANDARD_L32S = "Standard_L32s"
