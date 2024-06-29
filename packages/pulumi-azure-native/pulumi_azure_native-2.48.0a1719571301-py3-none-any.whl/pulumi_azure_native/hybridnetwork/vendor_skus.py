# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['VendorSkusArgs', 'VendorSkus']

@pulumi.input_type
class VendorSkusArgs:
    def __init__(__self__, *,
                 vendor_name: pulumi.Input[str],
                 deployment_mode: Optional[pulumi.Input[Union[str, 'SkuDeploymentMode']]] = None,
                 managed_application_parameters: Optional[Any] = None,
                 managed_application_template: Optional[Any] = None,
                 network_function_template: Optional[pulumi.Input['NetworkFunctionTemplateArgs']] = None,
                 network_function_type: Optional[pulumi.Input[Union[str, 'NetworkFunctionType']]] = None,
                 preview: Optional[pulumi.Input[bool]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 sku_type: Optional[pulumi.Input[Union[str, 'SkuType']]] = None):
        """
        The set of arguments for constructing a VendorSkus resource.
        :param pulumi.Input[str] vendor_name: The name of the vendor.
        :param pulumi.Input[Union[str, 'SkuDeploymentMode']] deployment_mode: The sku deployment mode.
        :param Any managed_application_parameters: The parameters for the managed application to be supplied by the vendor.
        :param Any managed_application_template: The template for the managed application deployment.
        :param pulumi.Input['NetworkFunctionTemplateArgs'] network_function_template: The template definition of the network function.
        :param pulumi.Input[Union[str, 'NetworkFunctionType']] network_function_type: The network function type.
        :param pulumi.Input[bool] preview: Indicates if the vendor sku is in preview mode.
        :param pulumi.Input[str] sku_name: The name of the sku.
        :param pulumi.Input[Union[str, 'SkuType']] sku_type: The sku type.
        """
        pulumi.set(__self__, "vendor_name", vendor_name)
        if deployment_mode is not None:
            pulumi.set(__self__, "deployment_mode", deployment_mode)
        if managed_application_parameters is not None:
            pulumi.set(__self__, "managed_application_parameters", managed_application_parameters)
        if managed_application_template is not None:
            pulumi.set(__self__, "managed_application_template", managed_application_template)
        if network_function_template is not None:
            pulumi.set(__self__, "network_function_template", network_function_template)
        if network_function_type is not None:
            pulumi.set(__self__, "network_function_type", network_function_type)
        if preview is not None:
            pulumi.set(__self__, "preview", preview)
        if sku_name is not None:
            pulumi.set(__self__, "sku_name", sku_name)
        if sku_type is not None:
            pulumi.set(__self__, "sku_type", sku_type)

    @property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> pulumi.Input[str]:
        """
        The name of the vendor.
        """
        return pulumi.get(self, "vendor_name")

    @vendor_name.setter
    def vendor_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vendor_name", value)

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> Optional[pulumi.Input[Union[str, 'SkuDeploymentMode']]]:
        """
        The sku deployment mode.
        """
        return pulumi.get(self, "deployment_mode")

    @deployment_mode.setter
    def deployment_mode(self, value: Optional[pulumi.Input[Union[str, 'SkuDeploymentMode']]]):
        pulumi.set(self, "deployment_mode", value)

    @property
    @pulumi.getter(name="managedApplicationParameters")
    def managed_application_parameters(self) -> Optional[Any]:
        """
        The parameters for the managed application to be supplied by the vendor.
        """
        return pulumi.get(self, "managed_application_parameters")

    @managed_application_parameters.setter
    def managed_application_parameters(self, value: Optional[Any]):
        pulumi.set(self, "managed_application_parameters", value)

    @property
    @pulumi.getter(name="managedApplicationTemplate")
    def managed_application_template(self) -> Optional[Any]:
        """
        The template for the managed application deployment.
        """
        return pulumi.get(self, "managed_application_template")

    @managed_application_template.setter
    def managed_application_template(self, value: Optional[Any]):
        pulumi.set(self, "managed_application_template", value)

    @property
    @pulumi.getter(name="networkFunctionTemplate")
    def network_function_template(self) -> Optional[pulumi.Input['NetworkFunctionTemplateArgs']]:
        """
        The template definition of the network function.
        """
        return pulumi.get(self, "network_function_template")

    @network_function_template.setter
    def network_function_template(self, value: Optional[pulumi.Input['NetworkFunctionTemplateArgs']]):
        pulumi.set(self, "network_function_template", value)

    @property
    @pulumi.getter(name="networkFunctionType")
    def network_function_type(self) -> Optional[pulumi.Input[Union[str, 'NetworkFunctionType']]]:
        """
        The network function type.
        """
        return pulumi.get(self, "network_function_type")

    @network_function_type.setter
    def network_function_type(self, value: Optional[pulumi.Input[Union[str, 'NetworkFunctionType']]]):
        pulumi.set(self, "network_function_type", value)

    @property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the vendor sku is in preview mode.
        """
        return pulumi.get(self, "preview")

    @preview.setter
    def preview(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "preview", value)

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the sku.
        """
        return pulumi.get(self, "sku_name")

    @sku_name.setter
    def sku_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_name", value)

    @property
    @pulumi.getter(name="skuType")
    def sku_type(self) -> Optional[pulumi.Input[Union[str, 'SkuType']]]:
        """
        The sku type.
        """
        return pulumi.get(self, "sku_type")

    @sku_type.setter
    def sku_type(self, value: Optional[pulumi.Input[Union[str, 'SkuType']]]):
        pulumi.set(self, "sku_type", value)


class VendorSkus(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_mode: Optional[pulumi.Input[Union[str, 'SkuDeploymentMode']]] = None,
                 managed_application_parameters: Optional[Any] = None,
                 managed_application_template: Optional[Any] = None,
                 network_function_template: Optional[pulumi.Input[pulumi.InputType['NetworkFunctionTemplateArgs']]] = None,
                 network_function_type: Optional[pulumi.Input[Union[str, 'NetworkFunctionType']]] = None,
                 preview: Optional[pulumi.Input[bool]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 sku_type: Optional[pulumi.Input[Union[str, 'SkuType']]] = None,
                 vendor_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Sku sub resource.
        Azure REST API version: 2022-01-01-preview. Prior API version in Azure Native 1.x: 2020-01-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'SkuDeploymentMode']] deployment_mode: The sku deployment mode.
        :param Any managed_application_parameters: The parameters for the managed application to be supplied by the vendor.
        :param Any managed_application_template: The template for the managed application deployment.
        :param pulumi.Input[pulumi.InputType['NetworkFunctionTemplateArgs']] network_function_template: The template definition of the network function.
        :param pulumi.Input[Union[str, 'NetworkFunctionType']] network_function_type: The network function type.
        :param pulumi.Input[bool] preview: Indicates if the vendor sku is in preview mode.
        :param pulumi.Input[str] sku_name: The name of the sku.
        :param pulumi.Input[Union[str, 'SkuType']] sku_type: The sku type.
        :param pulumi.Input[str] vendor_name: The name of the vendor.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VendorSkusArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Sku sub resource.
        Azure REST API version: 2022-01-01-preview. Prior API version in Azure Native 1.x: 2020-01-01-preview.

        :param str resource_name: The name of the resource.
        :param VendorSkusArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VendorSkusArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_mode: Optional[pulumi.Input[Union[str, 'SkuDeploymentMode']]] = None,
                 managed_application_parameters: Optional[Any] = None,
                 managed_application_template: Optional[Any] = None,
                 network_function_template: Optional[pulumi.Input[pulumi.InputType['NetworkFunctionTemplateArgs']]] = None,
                 network_function_type: Optional[pulumi.Input[Union[str, 'NetworkFunctionType']]] = None,
                 preview: Optional[pulumi.Input[bool]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 sku_type: Optional[pulumi.Input[Union[str, 'SkuType']]] = None,
                 vendor_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VendorSkusArgs.__new__(VendorSkusArgs)

            __props__.__dict__["deployment_mode"] = deployment_mode
            __props__.__dict__["managed_application_parameters"] = managed_application_parameters
            __props__.__dict__["managed_application_template"] = managed_application_template
            __props__.__dict__["network_function_template"] = network_function_template
            __props__.__dict__["network_function_type"] = network_function_type
            __props__.__dict__["preview"] = preview
            __props__.__dict__["sku_name"] = sku_name
            __props__.__dict__["sku_type"] = sku_type
            if vendor_name is None and not opts.urn:
                raise TypeError("Missing required property 'vendor_name'")
            __props__.__dict__["vendor_name"] = vendor_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridnetwork/v20200101preview:VendorSkus"), pulumi.Alias(type_="azure-native:hybridnetwork/v20210501:VendorSkus"), pulumi.Alias(type_="azure-native:hybridnetwork/v20220101preview:VendorSkus")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VendorSkus, __self__).__init__(
            'azure-native:hybridnetwork:VendorSkus',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VendorSkus':
        """
        Get an existing VendorSkus resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VendorSkusArgs.__new__(VendorSkusArgs)

        __props__.__dict__["deployment_mode"] = None
        __props__.__dict__["managed_application_parameters"] = None
        __props__.__dict__["managed_application_template"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_function_template"] = None
        __props__.__dict__["network_function_type"] = None
        __props__.__dict__["preview"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return VendorSkus(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The sku deployment mode.
        """
        return pulumi.get(self, "deployment_mode")

    @property
    @pulumi.getter(name="managedApplicationParameters")
    def managed_application_parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        The parameters for the managed application to be supplied by the vendor.
        """
        return pulumi.get(self, "managed_application_parameters")

    @property
    @pulumi.getter(name="managedApplicationTemplate")
    def managed_application_template(self) -> pulumi.Output[Optional[Any]]:
        """
        The template for the managed application deployment.
        """
        return pulumi.get(self, "managed_application_template")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFunctionTemplate")
    def network_function_template(self) -> pulumi.Output[Optional['outputs.NetworkFunctionTemplateResponse']]:
        """
        The template definition of the network function.
        """
        return pulumi.get(self, "network_function_template")

    @property
    @pulumi.getter(name="networkFunctionType")
    def network_function_type(self) -> pulumi.Output[Optional[str]]:
        """
        The network function type.
        """
        return pulumi.get(self, "network_function_type")

    @property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates if the vendor sku is in preview mode.
        """
        return pulumi.get(self, "preview")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the vendor sku sub resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="skuType")
    def sku_type(self) -> pulumi.Output[Optional[str]]:
        """
        The sku type.
        """
        return pulumi.get(self, "sku_type")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

