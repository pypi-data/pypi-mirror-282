# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['FileImportArgs', 'FileImport']

@pulumi.input_type
class FileImportArgs:
    def __init__(__self__, *,
                 content_type: pulumi.Input[Union[str, 'FileImportContentType']],
                 import_file: pulumi.Input['FileMetadataArgs'],
                 ingestion_mode: pulumi.Input[Union[str, 'IngestionMode']],
                 resource_group_name: pulumi.Input[str],
                 source: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 file_import_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FileImport resource.
        :param pulumi.Input[Union[str, 'FileImportContentType']] content_type: The content type of this file.
        :param pulumi.Input['FileMetadataArgs'] import_file: Represents the imported file.
        :param pulumi.Input[Union[str, 'IngestionMode']] ingestion_mode: Describes how to ingest the records in the file.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] source: The source for the data in the file.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] file_import_id: File import ID
        """
        pulumi.set(__self__, "content_type", content_type)
        pulumi.set(__self__, "import_file", import_file)
        pulumi.set(__self__, "ingestion_mode", ingestion_mode)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if file_import_id is not None:
            pulumi.set(__self__, "file_import_id", file_import_id)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[Union[str, 'FileImportContentType']]:
        """
        The content type of this file.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: pulumi.Input[Union[str, 'FileImportContentType']]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="importFile")
    def import_file(self) -> pulumi.Input['FileMetadataArgs']:
        """
        Represents the imported file.
        """
        return pulumi.get(self, "import_file")

    @import_file.setter
    def import_file(self, value: pulumi.Input['FileMetadataArgs']):
        pulumi.set(self, "import_file", value)

    @property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> pulumi.Input[Union[str, 'IngestionMode']]:
        """
        Describes how to ingest the records in the file.
        """
        return pulumi.get(self, "ingestion_mode")

    @ingestion_mode.setter
    def ingestion_mode(self, value: pulumi.Input[Union[str, 'IngestionMode']]):
        pulumi.set(self, "ingestion_mode", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        The source for the data in the file.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="fileImportId")
    def file_import_id(self) -> Optional[pulumi.Input[str]]:
        """
        File import ID
        """
        return pulumi.get(self, "file_import_id")

    @file_import_id.setter
    def file_import_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_import_id", value)


class FileImport(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[Union[str, 'FileImportContentType']]] = None,
                 file_import_id: Optional[pulumi.Input[str]] = None,
                 import_file: Optional[pulumi.Input[pulumi.InputType['FileMetadataArgs']]] = None,
                 ingestion_mode: Optional[pulumi.Input[Union[str, 'IngestionMode']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a file import in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'FileImportContentType']] content_type: The content type of this file.
        :param pulumi.Input[str] file_import_id: File import ID
        :param pulumi.Input[pulumi.InputType['FileMetadataArgs']] import_file: Represents the imported file.
        :param pulumi.Input[Union[str, 'IngestionMode']] ingestion_mode: Describes how to ingest the records in the file.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] source: The source for the data in the file.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FileImportArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a file import in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param FileImportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileImportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[Union[str, 'FileImportContentType']]] = None,
                 file_import_id: Optional[pulumi.Input[str]] = None,
                 import_file: Optional[pulumi.Input[pulumi.InputType['FileMetadataArgs']]] = None,
                 ingestion_mode: Optional[pulumi.Input[Union[str, 'IngestionMode']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FileImportArgs.__new__(FileImportArgs)

            if content_type is None and not opts.urn:
                raise TypeError("Missing required property 'content_type'")
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["file_import_id"] = file_import_id
            if import_file is None and not opts.urn:
                raise TypeError("Missing required property 'import_file'")
            __props__.__dict__["import_file"] = import_file
            if ingestion_mode is None and not opts.urn:
                raise TypeError("Missing required property 'ingestion_mode'")
            __props__.__dict__["ingestion_mode"] = ingestion_mode
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["created_time_utc"] = None
            __props__.__dict__["error_file"] = None
            __props__.__dict__["errors_preview"] = None
            __props__.__dict__["files_valid_until_time_utc"] = None
            __props__.__dict__["import_valid_until_time_utc"] = None
            __props__.__dict__["ingested_record_count"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["total_record_count"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["valid_record_count"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:FileImport"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:FileImport")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FileImport, __self__).__init__(
            'azure-native:securityinsights/v20230801preview:FileImport',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FileImport':
        """
        Get an existing FileImport resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FileImportArgs.__new__(FileImportArgs)

        __props__.__dict__["content_type"] = None
        __props__.__dict__["created_time_utc"] = None
        __props__.__dict__["error_file"] = None
        __props__.__dict__["errors_preview"] = None
        __props__.__dict__["files_valid_until_time_utc"] = None
        __props__.__dict__["import_file"] = None
        __props__.__dict__["import_valid_until_time_utc"] = None
        __props__.__dict__["ingested_record_count"] = None
        __props__.__dict__["ingestion_mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["total_record_count"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["valid_record_count"] = None
        return FileImport(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[str]:
        """
        The content type of this file.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="createdTimeUTC")
    def created_time_utc(self) -> pulumi.Output[str]:
        """
        The time the file was imported.
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter(name="errorFile")
    def error_file(self) -> pulumi.Output['outputs.FileMetadataResponse']:
        """
        Represents the error file (if the import was ingested with errors or failed the validation).
        """
        return pulumi.get(self, "error_file")

    @property
    @pulumi.getter(name="errorsPreview")
    def errors_preview(self) -> pulumi.Output[Sequence['outputs.ValidationErrorResponse']]:
        """
        An ordered list of some of the errors that were encountered during validation.
        """
        return pulumi.get(self, "errors_preview")

    @property
    @pulumi.getter(name="filesValidUntilTimeUTC")
    def files_valid_until_time_utc(self) -> pulumi.Output[str]:
        """
        The time the files associated with this import are deleted from the storage account.
        """
        return pulumi.get(self, "files_valid_until_time_utc")

    @property
    @pulumi.getter(name="importFile")
    def import_file(self) -> pulumi.Output['outputs.FileMetadataResponse']:
        """
        Represents the imported file.
        """
        return pulumi.get(self, "import_file")

    @property
    @pulumi.getter(name="importValidUntilTimeUTC")
    def import_valid_until_time_utc(self) -> pulumi.Output[str]:
        """
        The time the file import record is soft deleted from the database and history.
        """
        return pulumi.get(self, "import_valid_until_time_utc")

    @property
    @pulumi.getter(name="ingestedRecordCount")
    def ingested_record_count(self) -> pulumi.Output[int]:
        """
        The number of records that have been successfully ingested.
        """
        return pulumi.get(self, "ingested_record_count")

    @property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> pulumi.Output[str]:
        """
        Describes how to ingest the records in the file.
        """
        return pulumi.get(self, "ingestion_mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        The source for the data in the file.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the file import.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="totalRecordCount")
    def total_record_count(self) -> pulumi.Output[int]:
        """
        The number of records in the file.
        """
        return pulumi.get(self, "total_record_count")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validRecordCount")
    def valid_record_count(self) -> pulumi.Output[int]:
        """
        The number of records that have passed validation.
        """
        return pulumi.get(self, "valid_record_count")

