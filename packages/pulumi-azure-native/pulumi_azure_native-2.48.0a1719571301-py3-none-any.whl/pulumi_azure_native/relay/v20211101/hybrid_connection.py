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

__all__ = ['HybridConnectionArgs', 'HybridConnection']

@pulumi.input_type
class HybridConnectionArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 hybrid_connection_name: Optional[pulumi.Input[str]] = None,
                 requires_client_authorization: Optional[pulumi.Input[bool]] = None,
                 user_metadata: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HybridConnection resource.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] hybrid_connection_name: The hybrid connection name.
        :param pulumi.Input[bool] requires_client_authorization: Returns true if client authorization is needed for this hybrid connection; otherwise, false.
        :param pulumi.Input[str] user_metadata: The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if hybrid_connection_name is not None:
            pulumi.set(__self__, "hybrid_connection_name", hybrid_connection_name)
        if requires_client_authorization is not None:
            pulumi.set(__self__, "requires_client_authorization", requires_client_authorization)
        if user_metadata is not None:
            pulumi.set(__self__, "user_metadata", user_metadata)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="hybridConnectionName")
    def hybrid_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The hybrid connection name.
        """
        return pulumi.get(self, "hybrid_connection_name")

    @hybrid_connection_name.setter
    def hybrid_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hybrid_connection_name", value)

    @property
    @pulumi.getter(name="requiresClientAuthorization")
    def requires_client_authorization(self) -> Optional[pulumi.Input[bool]]:
        """
        Returns true if client authorization is needed for this hybrid connection; otherwise, false.
        """
        return pulumi.get(self, "requires_client_authorization")

    @requires_client_authorization.setter
    def requires_client_authorization(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "requires_client_authorization", value)

    @property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> Optional[pulumi.Input[str]]:
        """
        The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.
        """
        return pulumi.get(self, "user_metadata")

    @user_metadata.setter
    def user_metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_metadata", value)


class HybridConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hybrid_connection_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 requires_client_authorization: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 user_metadata: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Description of hybrid connection resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hybrid_connection_name: The hybrid connection name.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[bool] requires_client_authorization: Returns true if client authorization is needed for this hybrid connection; otherwise, false.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] user_metadata: The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HybridConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of hybrid connection resource.

        :param str resource_name: The name of the resource.
        :param HybridConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HybridConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hybrid_connection_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 requires_client_authorization: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 user_metadata: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HybridConnectionArgs.__new__(HybridConnectionArgs)

            __props__.__dict__["hybrid_connection_name"] = hybrid_connection_name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["requires_client_authorization"] = requires_client_authorization
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["user_metadata"] = user_metadata
            __props__.__dict__["created_at"] = None
            __props__.__dict__["listener_count"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:relay:HybridConnection"), pulumi.Alias(type_="azure-native:relay/v20160701:HybridConnection"), pulumi.Alias(type_="azure-native:relay/v20170401:HybridConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HybridConnection, __self__).__init__(
            'azure-native:relay/v20211101:HybridConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HybridConnection':
        """
        Get an existing HybridConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HybridConnectionArgs.__new__(HybridConnectionArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["listener_count"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["requires_client_authorization"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        __props__.__dict__["user_metadata"] = None
        return HybridConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time the hybrid connection was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="listenerCount")
    def listener_count(self) -> pulumi.Output[int]:
        """
        The number of listeners for this hybrid connection. Note that min : 1 and max:25 are supported.
        """
        return pulumi.get(self, "listener_count")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requiresClientAuthorization")
    def requires_client_authorization(self) -> pulumi.Output[Optional[bool]]:
        """
        Returns true if client authorization is needed for this hybrid connection; otherwise, false.
        """
        return pulumi.get(self, "requires_client_authorization")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> pulumi.Output[Optional[str]]:
        """
        The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.
        """
        return pulumi.get(self, "user_metadata")

