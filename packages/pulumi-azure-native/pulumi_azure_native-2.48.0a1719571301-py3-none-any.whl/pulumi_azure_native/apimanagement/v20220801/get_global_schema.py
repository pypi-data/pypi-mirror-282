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
    'GetGlobalSchemaResult',
    'AwaitableGetGlobalSchemaResult',
    'get_global_schema',
    'get_global_schema_output',
]

@pulumi.output_type
class GetGlobalSchemaResult:
    """
    Global Schema Contract details.
    """
    def __init__(__self__, description=None, id=None, name=None, schema_type=None, type=None, value=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schema_type and not isinstance(schema_type, str):
            raise TypeError("Expected argument 'schema_type' to be a str")
        pulumi.set(__self__, "schema_type", schema_type)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, dict):
            raise TypeError("Expected argument 'value' to be a dict")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Free-form schema entity description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> str:
        """
        Schema Type. Immutable.
        """
        return pulumi.get(self, "schema_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        """
        Json-encoded string for non json-based schema.
        """
        return pulumi.get(self, "value")


class AwaitableGetGlobalSchemaResult(GetGlobalSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGlobalSchemaResult(
            description=self.description,
            id=self.id,
            name=self.name,
            schema_type=self.schema_type,
            type=self.type,
            value=self.value)


def get_global_schema(resource_group_name: Optional[str] = None,
                      schema_id: Optional[str] = None,
                      service_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGlobalSchemaResult:
    """
    Gets the details of the Schema specified by its identifier.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str schema_id: Schema id identifier. Must be unique in the current API Management service instance.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['schemaId'] = schema_id
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220801:getGlobalSchema', __args__, opts=opts, typ=GetGlobalSchemaResult).value

    return AwaitableGetGlobalSchemaResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        schema_type=pulumi.get(__ret__, 'schema_type'),
        type=pulumi.get(__ret__, 'type'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_global_schema)
def get_global_schema_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                             schema_id: Optional[pulumi.Input[str]] = None,
                             service_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGlobalSchemaResult]:
    """
    Gets the details of the Schema specified by its identifier.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str schema_id: Schema id identifier. Must be unique in the current API Management service instance.
    :param str service_name: The name of the API Management service.
    """
    ...
