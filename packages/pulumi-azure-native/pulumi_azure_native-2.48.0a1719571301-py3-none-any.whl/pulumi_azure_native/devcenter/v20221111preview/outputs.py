# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ImageReferenceResponse',
    'ImageValidationErrorDetailsResponse',
    'SkuResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class ImageReferenceResponse(dict):
    """
    Image reference information
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "exactVersion":
            suggest = "exact_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ImageReferenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ImageReferenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ImageReferenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 exact_version: str,
                 id: Optional[str] = None,
                 offer: Optional[str] = None,
                 publisher: Optional[str] = None,
                 sku: Optional[str] = None):
        """
        Image reference information
        :param str exact_version: The actual version of the image after use. When id references a gallery image latest version, this will indicate the actual version in use.
        :param str id: Image ID, or Image version ID. When Image ID is provided, its latest version will be used.
        :param str offer: The image offer.
        :param str publisher: The image publisher.
        :param str sku: The image sku.
        """
        pulumi.set(__self__, "exact_version", exact_version)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if offer is not None:
            pulumi.set(__self__, "offer", offer)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)

    @property
    @pulumi.getter(name="exactVersion")
    def exact_version(self) -> str:
        """
        The actual version of the image after use. When id references a gallery image latest version, this will indicate the actual version in use.
        """
        return pulumi.get(self, "exact_version")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Image ID, or Image version ID. When Image ID is provided, its latest version will be used.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def offer(self) -> Optional[str]:
        """
        The image offer.
        """
        return pulumi.get(self, "offer")

    @property
    @pulumi.getter
    def publisher(self) -> Optional[str]:
        """
        The image publisher.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def sku(self) -> Optional[str]:
        """
        The image sku.
        """
        return pulumi.get(self, "sku")


@pulumi.output_type
class ImageValidationErrorDetailsResponse(dict):
    """
    Image validation error details
    """
    def __init__(__self__, *,
                 code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        Image validation error details
        :param str code: An identifier for the error.
        :param str message: A message describing the error.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        An identifier for the error.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        A message describing the error.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class SkuResponse(dict):
    """
    The resource model definition representing SKU
    """
    def __init__(__self__, *,
                 name: str,
                 capacity: Optional[int] = None,
                 family: Optional[str] = None,
                 size: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        The resource model definition representing SKU
        :param str name: The name of the SKU. Ex - P3. It is typically a letter+number code
        :param int capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        :param str family: If the service has different generations of hardware, for the same SKU, then that can be captured here.
        :param str size: The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        :param str tier: This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU. Ex - P3. It is typically a letter+number code
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


