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
    'APIServerProfileArgs',
    'ClusterProfileArgs',
    'ConsoleProfileArgs',
    'IngressProfileArgs',
    'MasterProfileArgs',
    'NetworkProfileArgs',
    'ServicePrincipalProfileArgs',
    'WorkerProfileArgs',
]

@pulumi.input_type
class APIServerProfileArgs:
    def __init__(__self__, *,
                 ip: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 visibility: Optional[pulumi.Input[Union[str, 'Visibility']]] = None):
        """
        APIServerProfile represents an API server profile.
        :param pulumi.Input[str] ip: The IP of the cluster API server.
        :param pulumi.Input[str] url: The URL to access the cluster API server.
        :param pulumi.Input[Union[str, 'Visibility']] visibility: API server visibility.
        """
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP of the cluster API server.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to access the cluster API server.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[Union[str, 'Visibility']]]:
        """
        API server visibility.
        """
        return pulumi.get(self, "visibility")

    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[Union[str, 'Visibility']]]):
        pulumi.set(self, "visibility", value)


@pulumi.input_type
class ClusterProfileArgs:
    def __init__(__self__, *,
                 domain: Optional[pulumi.Input[str]] = None,
                 fips_validated_modules: Optional[pulumi.Input[Union[str, 'FipsValidatedModules']]] = None,
                 pull_secret: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        ClusterProfile represents a cluster profile.
        :param pulumi.Input[str] domain: The domain for the cluster.
        :param pulumi.Input[Union[str, 'FipsValidatedModules']] fips_validated_modules: If FIPS validated crypto modules are used
        :param pulumi.Input[str] pull_secret: The pull secret for the cluster.
        :param pulumi.Input[str] resource_group_id: The ID of the cluster resource group.
        :param pulumi.Input[str] version: The version of the cluster.
        """
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if fips_validated_modules is not None:
            pulumi.set(__self__, "fips_validated_modules", fips_validated_modules)
        if pull_secret is not None:
            pulumi.set(__self__, "pull_secret", pull_secret)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain for the cluster.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="fipsValidatedModules")
    def fips_validated_modules(self) -> Optional[pulumi.Input[Union[str, 'FipsValidatedModules']]]:
        """
        If FIPS validated crypto modules are used
        """
        return pulumi.get(self, "fips_validated_modules")

    @fips_validated_modules.setter
    def fips_validated_modules(self, value: Optional[pulumi.Input[Union[str, 'FipsValidatedModules']]]):
        pulumi.set(self, "fips_validated_modules", value)

    @property
    @pulumi.getter(name="pullSecret")
    def pull_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The pull secret for the cluster.
        """
        return pulumi.get(self, "pull_secret")

    @pull_secret.setter
    def pull_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pull_secret", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the cluster resource group.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the cluster.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class ConsoleProfileArgs:
    def __init__(__self__, *,
                 url: Optional[pulumi.Input[str]] = None):
        """
        ConsoleProfile represents a console profile.
        :param pulumi.Input[str] url: The URL to access the cluster console.
        """
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to access the cluster console.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class IngressProfileArgs:
    def __init__(__self__, *,
                 ip: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 visibility: Optional[pulumi.Input[Union[str, 'Visibility']]] = None):
        """
        IngressProfile represents an ingress profile.
        :param pulumi.Input[str] ip: The IP of the ingress.
        :param pulumi.Input[str] name: The ingress profile name.
        :param pulumi.Input[Union[str, 'Visibility']] visibility: Ingress visibility.
        """
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP of the ingress.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The ingress profile name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[Union[str, 'Visibility']]]:
        """
        Ingress visibility.
        """
        return pulumi.get(self, "visibility")

    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[Union[str, 'Visibility']]]):
        pulumi.set(self, "visibility", value)


@pulumi.input_type
class MasterProfileArgs:
    def __init__(__self__, *,
                 disk_encryption_set_id: Optional[pulumi.Input[str]] = None,
                 encryption_at_host: Optional[pulumi.Input[Union[str, 'EncryptionAtHost']]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vm_size: Optional[pulumi.Input[str]] = None):
        """
        MasterProfile represents a master profile.
        :param pulumi.Input[str] disk_encryption_set_id: The resource ID of an associated DiskEncryptionSet, if applicable.
        :param pulumi.Input[Union[str, 'EncryptionAtHost']] encryption_at_host: Whether master virtual machines are encrypted at host.
        :param pulumi.Input[str] subnet_id: The Azure resource ID of the master subnet.
        :param pulumi.Input[str] vm_size: The size of the master VMs.
        """
        if disk_encryption_set_id is not None:
            pulumi.set(__self__, "disk_encryption_set_id", disk_encryption_set_id)
        if encryption_at_host is not None:
            pulumi.set(__self__, "encryption_at_host", encryption_at_host)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if vm_size is not None:
            pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of an associated DiskEncryptionSet, if applicable.
        """
        return pulumi.get(self, "disk_encryption_set_id")

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_encryption_set_id", value)

    @property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[Union[str, 'EncryptionAtHost']]]:
        """
        Whether master virtual machines are encrypted at host.
        """
        return pulumi.get(self, "encryption_at_host")

    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[Union[str, 'EncryptionAtHost']]]):
        pulumi.set(self, "encryption_at_host", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure resource ID of the master subnet.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of the master VMs.
        """
        return pulumi.get(self, "vm_size")

    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_size", value)


@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *,
                 pod_cidr: Optional[pulumi.Input[str]] = None,
                 service_cidr: Optional[pulumi.Input[str]] = None):
        """
        NetworkProfile represents a network profile.
        :param pulumi.Input[str] pod_cidr: The CIDR used for OpenShift/Kubernetes Pods.
        :param pulumi.Input[str] service_cidr: The CIDR used for OpenShift/Kubernetes Services.
        """
        if pod_cidr is not None:
            pulumi.set(__self__, "pod_cidr", pod_cidr)
        if service_cidr is not None:
            pulumi.set(__self__, "service_cidr", service_cidr)

    @property
    @pulumi.getter(name="podCidr")
    def pod_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The CIDR used for OpenShift/Kubernetes Pods.
        """
        return pulumi.get(self, "pod_cidr")

    @pod_cidr.setter
    def pod_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pod_cidr", value)

    @property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The CIDR used for OpenShift/Kubernetes Services.
        """
        return pulumi.get(self, "service_cidr")

    @service_cidr.setter
    def service_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_cidr", value)


@pulumi.input_type
class ServicePrincipalProfileArgs:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None):
        """
        ServicePrincipalProfile represents a service principal profile.
        :param pulumi.Input[str] client_id: The client ID used for the cluster.
        :param pulumi.Input[str] client_secret: The client secret used for the cluster.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client ID used for the cluster.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The client secret used for the cluster.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)


@pulumi.input_type
class WorkerProfileArgs:
    def __init__(__self__, *,
                 count: Optional[pulumi.Input[int]] = None,
                 disk_encryption_set_id: Optional[pulumi.Input[str]] = None,
                 disk_size_gb: Optional[pulumi.Input[int]] = None,
                 encryption_at_host: Optional[pulumi.Input[Union[str, 'EncryptionAtHost']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vm_size: Optional[pulumi.Input[str]] = None):
        """
        WorkerProfile represents a worker profile.
        :param pulumi.Input[int] count: The number of worker VMs.
        :param pulumi.Input[str] disk_encryption_set_id: The resource ID of an associated DiskEncryptionSet, if applicable.
        :param pulumi.Input[int] disk_size_gb: The disk size of the worker VMs.
        :param pulumi.Input[Union[str, 'EncryptionAtHost']] encryption_at_host: Whether master virtual machines are encrypted at host.
        :param pulumi.Input[str] name: The worker profile name.
        :param pulumi.Input[str] subnet_id: The Azure resource ID of the worker subnet.
        :param pulumi.Input[str] vm_size: The size of the worker VMs.
        """
        if count is not None:
            pulumi.set(__self__, "count", count)
        if disk_encryption_set_id is not None:
            pulumi.set(__self__, "disk_encryption_set_id", disk_encryption_set_id)
        if disk_size_gb is not None:
            pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if encryption_at_host is not None:
            pulumi.set(__self__, "encryption_at_host", encryption_at_host)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if vm_size is not None:
            pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of worker VMs.
        """
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of an associated DiskEncryptionSet, if applicable.
        """
        return pulumi.get(self, "disk_encryption_set_id")

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_encryption_set_id", value)

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[int]]:
        """
        The disk size of the worker VMs.
        """
        return pulumi.get(self, "disk_size_gb")

    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_size_gb", value)

    @property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[Union[str, 'EncryptionAtHost']]]:
        """
        Whether master virtual machines are encrypted at host.
        """
        return pulumi.get(self, "encryption_at_host")

    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[Union[str, 'EncryptionAtHost']]]):
        pulumi.set(self, "encryption_at_host", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The worker profile name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure resource ID of the worker subnet.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of the worker VMs.
        """
        return pulumi.get(self, "vm_size")

    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_size", value)


