# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'DatasetPropertyKeyResponse',
    'ExtendedLocationResponse',
    'PipelineInputResponse',
    'PipelineStageResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class DatasetPropertyKeyResponse(dict):
    """
    Key that can be used for joining on enrich.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "primaryKey":
            suggest = "primary_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DatasetPropertyKeyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DatasetPropertyKeyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DatasetPropertyKeyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 path: str,
                 primary_key: Optional[bool] = None):
        """
        Key that can be used for joining on enrich.
        :param str path: Path to the input value from the message.
        :param bool primary_key: If true the property will be used as a primary key. At most one primary key can exists.
        """
        pulumi.set(__self__, "path", path)
        if primary_key is not None:
            pulumi.set(__self__, "primary_key", primary_key)

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path to the input value from the message.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[bool]:
        """
        If true the property will be used as a primary key. At most one primary key can exists.
        """
        return pulumi.get(self, "primary_key")


@pulumi.output_type
class ExtendedLocationResponse(dict):
    """
    Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances.
    """
    def __init__(__self__, *,
                 name: str,
                 type: str):
        """
        Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances.
        :param str name: The name of the extended location.
        :param str type: The type of the extended location.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the extended location.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the extended location.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class PipelineInputResponse(dict):
    """
    Stage configuration for Pipeline input stage.
    """
    def __init__(__self__, *,
                 next: Sequence[str],
                 type: str,
                 description: Optional[str] = None):
        """
        Stage configuration for Pipeline input stage.
        :param Sequence[str] next: Next stage in the pipeline.
        :param str type: ARM resource type.
        :param str description: Description for stage.
        """
        pulumi.set(__self__, "next", next)
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def next(self) -> Sequence[str]:
        """
        Next stage in the pipeline.
        """
        return pulumi.get(self, "next")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        ARM resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description for stage.
        """
        return pulumi.get(self, "description")


@pulumi.output_type
class PipelineStageResponse(dict):
    """
    Stage configurations for all Pipeline processing and output stages.
    """
    def __init__(__self__, *,
                 type: str,
                 description: Optional[str] = None,
                 next: Optional[Sequence[str]] = None):
        """
        Stage configurations for all Pipeline processing and output stages.
        :param str type: ARM resource type.
        :param str description: Description for stage.
        :param Sequence[str] next: Next stage in the pipeline. Not required if output stage.
        """
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if next is not None:
            pulumi.set(__self__, "next", next)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        ARM resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description for stage.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def next(self) -> Optional[Sequence[str]]:
        """
        Next stage in the pipeline. Not required if output stage.
        """
        return pulumi.get(self, "next")


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


