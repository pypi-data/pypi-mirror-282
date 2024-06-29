# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ManagedServiceIdentityType',
    'OnFailure',
    'OnSuccess',
    'StorageTaskOperationName',
]


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class OnFailure(str, Enum):
    """
    Action to be taken when the operation fails for a object.
    """
    BREAK_ = "break"


class OnSuccess(str, Enum):
    """
    Action to be taken when the operation is successful for a object.
    """
    CONTINUE_ = "continue"


class StorageTaskOperationName(str, Enum):
    """
    The operation to be performed on the object.
    """
    SET_BLOB_TIER = "SetBlobTier"
    SET_BLOB_TAGS = "SetBlobTags"
    SET_BLOB_IMMUTABILITY_POLICY = "SetBlobImmutabilityPolicy"
    SET_BLOB_LEGAL_HOLD = "SetBlobLegalHold"
    SET_BLOB_EXPIRY = "SetBlobExpiry"
    DELETE_BLOB = "DeleteBlob"
    UNDELETE_BLOB = "UndeleteBlob"
