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
    'BusinessProcessIdentifierArgs',
    'BusinessProcessMappingItemArgs',
    'BusinessProcessStageArgs',
    'TrackingDataStoreArgs',
]

@pulumi.input_type
class BusinessProcessIdentifierArgs:
    def __init__(__self__, *,
                 property_name: Optional[pulumi.Input[str]] = None,
                 property_type: Optional[pulumi.Input[str]] = None):
        """
        The properties of business process identifier.
        :param pulumi.Input[str] property_name: The property name of the business process identifier.
        :param pulumi.Input[str] property_type: The property type of the business process identifier.
        """
        if property_name is not None:
            pulumi.set(__self__, "property_name", property_name)
        if property_type is not None:
            pulumi.set(__self__, "property_type", property_type)

    @property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[str]]:
        """
        The property name of the business process identifier.
        """
        return pulumi.get(self, "property_name")

    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_name", value)

    @property
    @pulumi.getter(name="propertyType")
    def property_type(self) -> Optional[pulumi.Input[str]]:
        """
        The property type of the business process identifier.
        """
        return pulumi.get(self, "property_type")

    @property_type.setter
    def property_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_type", value)


@pulumi.input_type
class BusinessProcessMappingItemArgs:
    def __init__(__self__, *,
                 logic_app_resource_id: Optional[pulumi.Input[str]] = None,
                 operation_name: Optional[pulumi.Input[str]] = None,
                 operation_type: Optional[pulumi.Input[str]] = None,
                 workflow_name: Optional[pulumi.Input[str]] = None):
        """
        The properties of business process mapping.
        :param pulumi.Input[str] logic_app_resource_id: The logic app resource id.
        :param pulumi.Input[str] operation_name: The operation name.
        :param pulumi.Input[str] operation_type: The mapping item operation type of the business process.
        :param pulumi.Input[str] workflow_name: The workflow name within the logic app.
        """
        if logic_app_resource_id is not None:
            pulumi.set(__self__, "logic_app_resource_id", logic_app_resource_id)
        if operation_name is not None:
            pulumi.set(__self__, "operation_name", operation_name)
        if operation_type is not None:
            pulumi.set(__self__, "operation_type", operation_type)
        if workflow_name is not None:
            pulumi.set(__self__, "workflow_name", workflow_name)

    @property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The logic app resource id.
        """
        return pulumi.get(self, "logic_app_resource_id")

    @logic_app_resource_id.setter
    def logic_app_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logic_app_resource_id", value)

    @property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The operation name.
        """
        return pulumi.get(self, "operation_name")

    @operation_name.setter
    def operation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_name", value)

    @property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[pulumi.Input[str]]:
        """
        The mapping item operation type of the business process.
        """
        return pulumi.get(self, "operation_type")

    @operation_type.setter
    def operation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_type", value)

    @property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[pulumi.Input[str]]:
        """
        The workflow name within the logic app.
        """
        return pulumi.get(self, "workflow_name")

    @workflow_name.setter
    def workflow_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workflow_name", value)


@pulumi.input_type
class BusinessProcessStageArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 stages_before: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The properties of business process stage.
        :param pulumi.Input[str] description: The description of the business stage.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The properties within the properties of the business process stage.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] stages_before: The property to keep track of stages before current in the business process stage.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if stages_before is not None:
            pulumi.set(__self__, "stages_before", stages_before)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the business stage.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The properties within the properties of the business process stage.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="stagesBefore")
    def stages_before(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The property to keep track of stages before current in the business process stage.
        """
        return pulumi.get(self, "stages_before")

    @stages_before.setter
    def stages_before(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "stages_before", value)


@pulumi.input_type
class TrackingDataStoreArgs:
    def __init__(__self__, *,
                 data_store_ingestion_uri: Optional[pulumi.Input[str]] = None,
                 data_store_resource_id: Optional[pulumi.Input[str]] = None,
                 data_store_uri: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None):
        """
        The properties of tracking data store.
        :param pulumi.Input[str] data_store_ingestion_uri: The data store ingestion URI.
        :param pulumi.Input[str] data_store_resource_id: The data store resource id.
        :param pulumi.Input[str] data_store_uri: The data store URI.
        :param pulumi.Input[str] database_name: The database name.
        """
        if data_store_ingestion_uri is not None:
            pulumi.set(__self__, "data_store_ingestion_uri", data_store_ingestion_uri)
        if data_store_resource_id is not None:
            pulumi.set(__self__, "data_store_resource_id", data_store_resource_id)
        if data_store_uri is not None:
            pulumi.set(__self__, "data_store_uri", data_store_uri)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)

    @property
    @pulumi.getter(name="dataStoreIngestionUri")
    def data_store_ingestion_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The data store ingestion URI.
        """
        return pulumi.get(self, "data_store_ingestion_uri")

    @data_store_ingestion_uri.setter
    def data_store_ingestion_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_store_ingestion_uri", value)

    @property
    @pulumi.getter(name="dataStoreResourceId")
    def data_store_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The data store resource id.
        """
        return pulumi.get(self, "data_store_resource_id")

    @data_store_resource_id.setter
    def data_store_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_store_resource_id", value)

    @property
    @pulumi.getter(name="dataStoreUri")
    def data_store_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The data store URI.
        """
        return pulumi.get(self, "data_store_uri")

    @data_store_uri.setter
    def data_store_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_store_uri", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The database name.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)


