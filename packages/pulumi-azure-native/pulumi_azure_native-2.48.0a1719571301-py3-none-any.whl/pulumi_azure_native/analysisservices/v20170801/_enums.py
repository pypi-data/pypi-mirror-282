# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ConnectionMode',
    'SkuTier',
]


class ConnectionMode(str, Enum):
    """
    How the read-write server's participation in the query pool is controlled.<br/>It can have the following values: <ul><li>readOnly - indicates that the read-write server is intended not to participate in query operations</li><li>all - indicates that the read-write server can participate in query operations</li></ul>Specifying readOnly when capacity is 1 results in error.
    """
    ALL = "All"
    READ_ONLY = "ReadOnly"


class SkuTier(str, Enum):
    """
    The name of the Azure pricing tier to which the SKU applies.
    """
    DEVELOPMENT = "Development"
    BASIC = "Basic"
    STANDARD = "Standard"
