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

__all__ = ['GalleryimageRetrieveArgs', 'GalleryimageRetrieve']

@pulumi.input_type
class GalleryimageRetrieveArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 cloud_init_data_source: Optional[pulumi.Input[Union[str, 'CloudInitDataSource']]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 galleryimages_name: Optional[pulumi.Input[str]] = None,
                 hyper_v_generation: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]] = None,
                 identifier: Optional[pulumi.Input['GalleryImageIdentifierArgs']] = None,
                 image_path: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input['OperatingSystemTypes']] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input['GalleryImageVersionArgs']] = None):
        """
        The set of arguments for constructing a GalleryimageRetrieve resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'CloudInitDataSource']] cloud_init_data_source: Datasource for the gallery image when provisioning with cloud-init (Azure or NoCloud)
        :param pulumi.Input[str] container_name: Container Name for storage container
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[str] galleryimages_name: Name of the gallery image
        :param pulumi.Input[Union[str, 'HyperVGeneration']] hyper_v_generation: The hypervisor generation of the Virtual Machine [V1, V2]
        :param pulumi.Input['GalleryImageIdentifierArgs'] identifier: This is the gallery image definition identifier.
        :param pulumi.Input[str] image_path: location of the image the gallery image should be created from
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['OperatingSystemTypes'] os_type: operating system type that the gallery image uses. Expected to be linux or windows
        :param pulumi.Input[str] resource_name: name of the object to be used in moc
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['GalleryImageVersionArgs'] version: Specifies information about the gallery image version that you want to create or update.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cloud_init_data_source is not None:
            pulumi.set(__self__, "cloud_init_data_source", cloud_init_data_source)
        if container_name is not None:
            pulumi.set(__self__, "container_name", container_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if galleryimages_name is not None:
            pulumi.set(__self__, "galleryimages_name", galleryimages_name)
        if hyper_v_generation is not None:
            pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if image_path is not None:
            pulumi.set(__self__, "image_path", image_path)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

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
    @pulumi.getter(name="cloudInitDataSource")
    def cloud_init_data_source(self) -> Optional[pulumi.Input[Union[str, 'CloudInitDataSource']]]:
        """
        Datasource for the gallery image when provisioning with cloud-init (Azure or NoCloud)
        """
        return pulumi.get(self, "cloud_init_data_source")

    @cloud_init_data_source.setter
    def cloud_init_data_source(self, value: Optional[pulumi.Input[Union[str, 'CloudInitDataSource']]]):
        pulumi.set(self, "cloud_init_data_source", value)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[str]]:
        """
        Container Name for storage container
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="galleryimagesName")
    def galleryimages_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the gallery image
        """
        return pulumi.get(self, "galleryimages_name")

    @galleryimages_name.setter
    def galleryimages_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "galleryimages_name", value)

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[pulumi.Input[Union[str, 'HyperVGeneration']]]:
        """
        The hypervisor generation of the Virtual Machine [V1, V2]
        """
        return pulumi.get(self, "hyper_v_generation")

    @hyper_v_generation.setter
    def hyper_v_generation(self, value: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]]):
        pulumi.set(self, "hyper_v_generation", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input['GalleryImageIdentifierArgs']]:
        """
        This is the gallery image definition identifier.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input['GalleryImageIdentifierArgs']]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="imagePath")
    def image_path(self) -> Optional[pulumi.Input[str]]:
        """
        location of the image the gallery image should be created from
        """
        return pulumi.get(self, "image_path")

    @image_path.setter
    def image_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_path", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input['OperatingSystemTypes']]:
        """
        operating system type that the gallery image uses. Expected to be linux or windows
        """
        return pulumi.get(self, "os_type")

    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input['OperatingSystemTypes']]):
        pulumi.set(self, "os_type", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input['GalleryImageVersionArgs']]:
        """
        Specifies information about the gallery image version that you want to create or update.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input['GalleryImageVersionArgs']]):
        pulumi.set(self, "version", value)


class GalleryimageRetrieve(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_init_data_source: Optional[pulumi.Input[Union[str, 'CloudInitDataSource']]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 galleryimages_name: Optional[pulumi.Input[str]] = None,
                 hyper_v_generation: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]] = None,
                 identifier: Optional[pulumi.Input[pulumi.InputType['GalleryImageIdentifierArgs']]] = None,
                 image_path: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input['OperatingSystemTypes']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[pulumi.InputType['GalleryImageVersionArgs']]] = None,
                 __props__=None):
        """
        The gallery image resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'CloudInitDataSource']] cloud_init_data_source: Datasource for the gallery image when provisioning with cloud-init (Azure or NoCloud)
        :param pulumi.Input[str] container_name: Container Name for storage container
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[str] galleryimages_name: Name of the gallery image
        :param pulumi.Input[Union[str, 'HyperVGeneration']] hyper_v_generation: The hypervisor generation of the Virtual Machine [V1, V2]
        :param pulumi.Input[pulumi.InputType['GalleryImageIdentifierArgs']] identifier: This is the gallery image definition identifier.
        :param pulumi.Input[str] image_path: location of the image the gallery image should be created from
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['OperatingSystemTypes'] os_type: operating system type that the gallery image uses. Expected to be linux or windows
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: name of the object to be used in moc
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['GalleryImageVersionArgs']] version: Specifies information about the gallery image version that you want to create or update.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GalleryimageRetrieveArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The gallery image resource definition.

        :param str resource_name: The name of the resource.
        :param GalleryimageRetrieveArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GalleryimageRetrieveArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_init_data_source: Optional[pulumi.Input[Union[str, 'CloudInitDataSource']]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 galleryimages_name: Optional[pulumi.Input[str]] = None,
                 hyper_v_generation: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]] = None,
                 identifier: Optional[pulumi.Input[pulumi.InputType['GalleryImageIdentifierArgs']]] = None,
                 image_path: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input['OperatingSystemTypes']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[pulumi.InputType['GalleryImageVersionArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GalleryimageRetrieveArgs.__new__(GalleryimageRetrieveArgs)

            __props__.__dict__["cloud_init_data_source"] = cloud_init_data_source
            __props__.__dict__["container_name"] = container_name
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["galleryimages_name"] = galleryimages_name
            __props__.__dict__["hyper_v_generation"] = hyper_v_generation
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["image_path"] = image_path
            __props__.__dict__["location"] = location
            __props__.__dict__["os_type"] = os_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci/v20210901preview:galleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:GalleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:galleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20210701preview:GalleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20210701preview:galleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:GalleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:galleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:GalleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:galleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230901preview:GalleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230901preview:galleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:GalleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:galleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240201preview:GalleryimageRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240201preview:galleryimageRetrieve")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GalleryimageRetrieve, __self__).__init__(
            'azure-native:azurestackhci/v20210901preview:GalleryimageRetrieve',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GalleryimageRetrieve':
        """
        Get an existing GalleryimageRetrieve resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GalleryimageRetrieveArgs.__new__(GalleryimageRetrieveArgs)

        __props__.__dict__["cloud_init_data_source"] = None
        __props__.__dict__["container_name"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["hyper_v_generation"] = None
        __props__.__dict__["identifier"] = None
        __props__.__dict__["image_path"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["os_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return GalleryimageRetrieve(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudInitDataSource")
    def cloud_init_data_source(self) -> pulumi.Output[Optional[str]]:
        """
        Datasource for the gallery image when provisioning with cloud-init (Azure or NoCloud)
        """
        return pulumi.get(self, "cloud_init_data_source")

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[Optional[str]]:
        """
        Container Name for storage container
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Output[Optional[str]]:
        """
        The hypervisor generation of the Virtual Machine [V1, V2]
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[Optional['outputs.GalleryImageIdentifierResponse']]:
        """
        This is the gallery image definition identifier.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter(name="imagePath")
    def image_path(self) -> pulumi.Output[Optional[str]]:
        """
        location of the image the gallery image should be created from
        """
        return pulumi.get(self, "image_path")

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
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[str]]:
        """
        operating system type that the gallery image uses. Expected to be linux or windows
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the gallery image.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.GalleryImageStatusResponse']:
        """
        GalleryImageStatus defines the observed state of galleryimages
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional['outputs.GalleryImageVersionResponse']]:
        """
        Specifies information about the gallery image version that you want to create or update.
        """
        return pulumi.get(self, "version")

