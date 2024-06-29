# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Source',
    'ThreatIntelligenceResourceInnerKind',
]


class Source(str, Enum):
    """
    The source of the watchlist
    """
    LOCAL_FILE = "Local file"
    REMOTE_STORAGE = "Remote storage"


class ThreatIntelligenceResourceInnerKind(str, Enum):
    """
    The kind of the entity.
    """
    INDICATOR = "indicator"
    """
    Entity represents threat intelligence indicator in the system.
    """
