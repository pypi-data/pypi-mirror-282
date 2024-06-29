# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PrincipalType',
]


class PrincipalType(str, Enum):
    """
    The principal type of the assigned principal ID.
    """
    USER = "User"
    GROUP = "Group"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    FOREIGN_GROUP = "ForeignGroup"
