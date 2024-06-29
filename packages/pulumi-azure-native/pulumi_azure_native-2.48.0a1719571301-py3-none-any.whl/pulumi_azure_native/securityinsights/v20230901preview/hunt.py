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

__all__ = ['HuntArgs', 'Hunt']

@pulumi.input_type
class HuntArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 attack_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]] = None,
                 attack_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hunt_id: Optional[pulumi.Input[str]] = None,
                 hypothesis_status: Optional[pulumi.Input[Union[str, 'HypothesisStatus']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 owner: Optional[pulumi.Input['HuntOwnerArgs']] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None):
        """
        The set of arguments for constructing a Hunt resource.
        :param pulumi.Input[str] description: The description of the hunt
        :param pulumi.Input[str] display_name: The display name of the hunt
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]] attack_tactics: A list of mitre attack tactics the hunt is associated with
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attack_techniques: A list of a mitre attack techniques the hunt is associated with
        :param pulumi.Input[str] hunt_id: The hunt id (GUID)
        :param pulumi.Input[Union[str, 'HypothesisStatus']] hypothesis_status: The hypothesis status of the hunt.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this hunt 
        :param pulumi.Input['HuntOwnerArgs'] owner: Describes a user that the hunt is assigned to
        :param pulumi.Input[Union[str, 'Status']] status: The status of the hunt.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if attack_tactics is not None:
            pulumi.set(__self__, "attack_tactics", attack_tactics)
        if attack_techniques is not None:
            pulumi.set(__self__, "attack_techniques", attack_techniques)
        if hunt_id is not None:
            pulumi.set(__self__, "hunt_id", hunt_id)
        if hypothesis_status is None:
            hypothesis_status = 'Unknown'
        if hypothesis_status is not None:
            pulumi.set(__self__, "hypothesis_status", hypothesis_status)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if status is None:
            status = 'New'
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the hunt
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the hunt
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

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
    @pulumi.getter(name="attackTactics")
    def attack_tactics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]]:
        """
        A list of mitre attack tactics the hunt is associated with
        """
        return pulumi.get(self, "attack_tactics")

    @attack_tactics.setter
    def attack_tactics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]]):
        pulumi.set(self, "attack_tactics", value)

    @property
    @pulumi.getter(name="attackTechniques")
    def attack_techniques(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of a mitre attack techniques the hunt is associated with
        """
        return pulumi.get(self, "attack_techniques")

    @attack_techniques.setter
    def attack_techniques(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attack_techniques", value)

    @property
    @pulumi.getter(name="huntId")
    def hunt_id(self) -> Optional[pulumi.Input[str]]:
        """
        The hunt id (GUID)
        """
        return pulumi.get(self, "hunt_id")

    @hunt_id.setter
    def hunt_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hunt_id", value)

    @property
    @pulumi.getter(name="hypothesisStatus")
    def hypothesis_status(self) -> Optional[pulumi.Input[Union[str, 'HypothesisStatus']]]:
        """
        The hypothesis status of the hunt.
        """
        return pulumi.get(self, "hypothesis_status")

    @hypothesis_status.setter
    def hypothesis_status(self, value: Optional[pulumi.Input[Union[str, 'HypothesisStatus']]]):
        pulumi.set(self, "hypothesis_status", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of labels relevant to this hunt 
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input['HuntOwnerArgs']]:
        """
        Describes a user that the hunt is assigned to
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input['HuntOwnerArgs']]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'Status']]]:
        """
        The status of the hunt.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'Status']]]):
        pulumi.set(self, "status", value)


class Hunt(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attack_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]] = None,
                 attack_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 hunt_id: Optional[pulumi.Input[str]] = None,
                 hypothesis_status: Optional[pulumi.Input[Union[str, 'HypothesisStatus']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 owner: Optional[pulumi.Input[pulumi.InputType['HuntOwnerArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a Hunt in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]] attack_tactics: A list of mitre attack tactics the hunt is associated with
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attack_techniques: A list of a mitre attack techniques the hunt is associated with
        :param pulumi.Input[str] description: The description of the hunt
        :param pulumi.Input[str] display_name: The display name of the hunt
        :param pulumi.Input[str] hunt_id: The hunt id (GUID)
        :param pulumi.Input[Union[str, 'HypothesisStatus']] hypothesis_status: The hypothesis status of the hunt.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this hunt 
        :param pulumi.Input[pulumi.InputType['HuntOwnerArgs']] owner: Describes a user that the hunt is assigned to
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'Status']] status: The status of the hunt.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HuntArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Hunt in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param HuntArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HuntArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attack_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]] = None,
                 attack_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 hunt_id: Optional[pulumi.Input[str]] = None,
                 hypothesis_status: Optional[pulumi.Input[Union[str, 'HypothesisStatus']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 owner: Optional[pulumi.Input[pulumi.InputType['HuntOwnerArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HuntArgs.__new__(HuntArgs)

            __props__.__dict__["attack_tactics"] = attack_tactics
            __props__.__dict__["attack_techniques"] = attack_techniques
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["hunt_id"] = hunt_id
            if hypothesis_status is None:
                hypothesis_status = 'Unknown'
            __props__.__dict__["hypothesis_status"] = hypothesis_status
            __props__.__dict__["labels"] = labels
            __props__.__dict__["owner"] = owner
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if status is None:
                status = 'New'
            __props__.__dict__["status"] = status
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:Hunt"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:Hunt")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Hunt, __self__).__init__(
            'azure-native:securityinsights/v20230901preview:Hunt',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Hunt':
        """
        Get an existing Hunt resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HuntArgs.__new__(HuntArgs)

        __props__.__dict__["attack_tactics"] = None
        __props__.__dict__["attack_techniques"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["hypothesis_status"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Hunt(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attackTactics")
    def attack_tactics(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of mitre attack tactics the hunt is associated with
        """
        return pulumi.get(self, "attack_tactics")

    @property
    @pulumi.getter(name="attackTechniques")
    def attack_techniques(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of a mitre attack techniques the hunt is associated with
        """
        return pulumi.get(self, "attack_techniques")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the hunt
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the hunt
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hypothesisStatus")
    def hypothesis_status(self) -> pulumi.Output[Optional[str]]:
        """
        The hypothesis status of the hunt.
        """
        return pulumi.get(self, "hypothesis_status")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of labels relevant to this hunt 
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional['outputs.HuntOwnerResponse']]:
        """
        Describes a user that the hunt is assigned to
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the hunt.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

