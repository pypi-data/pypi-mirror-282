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

__all__ = [
    'GetHostPoolResult',
    'AwaitableGetHostPoolResult',
    'get_host_pool',
    'get_host_pool_output',
]

@pulumi.output_type
class GetHostPoolResult:
    """
    Represents a HostPool definition.
    """
    def __init__(__self__, agent_update=None, app_attach_package_references=None, application_group_references=None, cloud_pc_resource=None, custom_rdp_property=None, description=None, etag=None, friendly_name=None, host_pool_type=None, id=None, identity=None, kind=None, load_balancer_type=None, location=None, managed_by=None, max_session_limit=None, name=None, object_id=None, personal_desktop_assignment_type=None, plan=None, preferred_app_group_type=None, private_endpoint_connections=None, public_network_access=None, registration_info=None, ring=None, sku=None, sso_client_id=None, sso_client_secret_key_vault_path=None, sso_secret_type=None, ssoadfs_authority=None, start_vm_on_connect=None, system_data=None, tags=None, type=None, validation_environment=None, vm_template=None):
        if agent_update and not isinstance(agent_update, dict):
            raise TypeError("Expected argument 'agent_update' to be a dict")
        pulumi.set(__self__, "agent_update", agent_update)
        if app_attach_package_references and not isinstance(app_attach_package_references, list):
            raise TypeError("Expected argument 'app_attach_package_references' to be a list")
        pulumi.set(__self__, "app_attach_package_references", app_attach_package_references)
        if application_group_references and not isinstance(application_group_references, list):
            raise TypeError("Expected argument 'application_group_references' to be a list")
        pulumi.set(__self__, "application_group_references", application_group_references)
        if cloud_pc_resource and not isinstance(cloud_pc_resource, bool):
            raise TypeError("Expected argument 'cloud_pc_resource' to be a bool")
        pulumi.set(__self__, "cloud_pc_resource", cloud_pc_resource)
        if custom_rdp_property and not isinstance(custom_rdp_property, str):
            raise TypeError("Expected argument 'custom_rdp_property' to be a str")
        pulumi.set(__self__, "custom_rdp_property", custom_rdp_property)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if host_pool_type and not isinstance(host_pool_type, str):
            raise TypeError("Expected argument 'host_pool_type' to be a str")
        pulumi.set(__self__, "host_pool_type", host_pool_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if load_balancer_type and not isinstance(load_balancer_type, str):
            raise TypeError("Expected argument 'load_balancer_type' to be a str")
        pulumi.set(__self__, "load_balancer_type", load_balancer_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if max_session_limit and not isinstance(max_session_limit, int):
            raise TypeError("Expected argument 'max_session_limit' to be a int")
        pulumi.set(__self__, "max_session_limit", max_session_limit)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if personal_desktop_assignment_type and not isinstance(personal_desktop_assignment_type, str):
            raise TypeError("Expected argument 'personal_desktop_assignment_type' to be a str")
        pulumi.set(__self__, "personal_desktop_assignment_type", personal_desktop_assignment_type)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if preferred_app_group_type and not isinstance(preferred_app_group_type, str):
            raise TypeError("Expected argument 'preferred_app_group_type' to be a str")
        pulumi.set(__self__, "preferred_app_group_type", preferred_app_group_type)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if registration_info and not isinstance(registration_info, dict):
            raise TypeError("Expected argument 'registration_info' to be a dict")
        pulumi.set(__self__, "registration_info", registration_info)
        if ring and not isinstance(ring, int):
            raise TypeError("Expected argument 'ring' to be a int")
        pulumi.set(__self__, "ring", ring)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if sso_client_id and not isinstance(sso_client_id, str):
            raise TypeError("Expected argument 'sso_client_id' to be a str")
        pulumi.set(__self__, "sso_client_id", sso_client_id)
        if sso_client_secret_key_vault_path and not isinstance(sso_client_secret_key_vault_path, str):
            raise TypeError("Expected argument 'sso_client_secret_key_vault_path' to be a str")
        pulumi.set(__self__, "sso_client_secret_key_vault_path", sso_client_secret_key_vault_path)
        if sso_secret_type and not isinstance(sso_secret_type, str):
            raise TypeError("Expected argument 'sso_secret_type' to be a str")
        pulumi.set(__self__, "sso_secret_type", sso_secret_type)
        if ssoadfs_authority and not isinstance(ssoadfs_authority, str):
            raise TypeError("Expected argument 'ssoadfs_authority' to be a str")
        pulumi.set(__self__, "ssoadfs_authority", ssoadfs_authority)
        if start_vm_on_connect and not isinstance(start_vm_on_connect, bool):
            raise TypeError("Expected argument 'start_vm_on_connect' to be a bool")
        pulumi.set(__self__, "start_vm_on_connect", start_vm_on_connect)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if validation_environment and not isinstance(validation_environment, bool):
            raise TypeError("Expected argument 'validation_environment' to be a bool")
        pulumi.set(__self__, "validation_environment", validation_environment)
        if vm_template and not isinstance(vm_template, str):
            raise TypeError("Expected argument 'vm_template' to be a str")
        pulumi.set(__self__, "vm_template", vm_template)

    @property
    @pulumi.getter(name="agentUpdate")
    def agent_update(self) -> Optional['outputs.AgentUpdatePropertiesResponse']:
        """
        The session host configuration for updating agent, monitoring agent, and stack component.
        """
        return pulumi.get(self, "agent_update")

    @property
    @pulumi.getter(name="appAttachPackageReferences")
    def app_attach_package_references(self) -> Sequence[str]:
        """
        List of App Attach Package links.
        """
        return pulumi.get(self, "app_attach_package_references")

    @property
    @pulumi.getter(name="applicationGroupReferences")
    def application_group_references(self) -> Sequence[str]:
        """
        List of applicationGroup links.
        """
        return pulumi.get(self, "application_group_references")

    @property
    @pulumi.getter(name="cloudPcResource")
    def cloud_pc_resource(self) -> bool:
        """
        Is cloud pc resource.
        """
        return pulumi.get(self, "cloud_pc_resource")

    @property
    @pulumi.getter(name="customRdpProperty")
    def custom_rdp_property(self) -> Optional[str]:
        """
        Custom rdp property of HostPool.
        """
        return pulumi.get(self, "custom_rdp_property")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of HostPool.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. 
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Friendly name of HostPool.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPoolType")
    def host_pool_type(self) -> str:
        """
        HostPool type for desktop.
        """
        return pulumi.get(self, "host_pool_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponseIdentity']:
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> str:
        """
        The type of the load balancer.
        """
        return pulumi.get(self, "load_balancer_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[str]:
        """
        The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter(name="maxSessionLimit")
    def max_session_limit(self) -> Optional[int]:
        """
        The max session limit of HostPool.
        """
        return pulumi.get(self, "max_session_limit")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        """
        ObjectId of HostPool. (internal use)
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="personalDesktopAssignmentType")
    def personal_desktop_assignment_type(self) -> Optional[str]:
        """
        PersonalDesktopAssignment type for HostPool.
        """
        return pulumi.get(self, "personal_desktop_assignment_type")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponsePlan']:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="preferredAppGroupType")
    def preferred_app_group_type(self) -> str:
        """
        The type of preferred application group type, default to Desktop Application Group
        """
        return pulumi.get(self, "preferred_app_group_type")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        List of private endpoint connection associated with the specified resource
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Enabled allows this resource to be accessed from both public and private networks, Disabled allows this resource to only be accessed via private endpoints
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="registrationInfo")
    def registration_info(self) -> Optional['outputs.RegistrationInfoResponse']:
        """
        The registration info of HostPool.
        """
        return pulumi.get(self, "registration_info")

    @property
    @pulumi.getter
    def ring(self) -> Optional[int]:
        """
        The ring number of HostPool.
        """
        return pulumi.get(self, "ring")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponseSku']:
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="ssoClientId")
    def sso_client_id(self) -> Optional[str]:
        """
        ClientId for the registered Relying Party used to issue WVD SSO certificates.
        """
        return pulumi.get(self, "sso_client_id")

    @property
    @pulumi.getter(name="ssoClientSecretKeyVaultPath")
    def sso_client_secret_key_vault_path(self) -> Optional[str]:
        """
        Path to Azure KeyVault storing the secret used for communication to ADFS.
        """
        return pulumi.get(self, "sso_client_secret_key_vault_path")

    @property
    @pulumi.getter(name="ssoSecretType")
    def sso_secret_type(self) -> Optional[str]:
        """
        The type of single sign on Secret Type.
        """
        return pulumi.get(self, "sso_secret_type")

    @property
    @pulumi.getter(name="ssoadfsAuthority")
    def ssoadfs_authority(self) -> Optional[str]:
        """
        URL to customer ADFS server for signing WVD SSO certificates.
        """
        return pulumi.get(self, "ssoadfs_authority")

    @property
    @pulumi.getter(name="startVMOnConnect")
    def start_vm_on_connect(self) -> Optional[bool]:
        """
        The flag to turn on/off StartVMOnConnect feature.
        """
        return pulumi.get(self, "start_vm_on_connect")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationEnvironment")
    def validation_environment(self) -> Optional[bool]:
        """
        Is validation environment.
        """
        return pulumi.get(self, "validation_environment")

    @property
    @pulumi.getter(name="vmTemplate")
    def vm_template(self) -> Optional[str]:
        """
        VM template for sessionhosts configuration within hostpool.
        """
        return pulumi.get(self, "vm_template")


class AwaitableGetHostPoolResult(GetHostPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHostPoolResult(
            agent_update=self.agent_update,
            app_attach_package_references=self.app_attach_package_references,
            application_group_references=self.application_group_references,
            cloud_pc_resource=self.cloud_pc_resource,
            custom_rdp_property=self.custom_rdp_property,
            description=self.description,
            etag=self.etag,
            friendly_name=self.friendly_name,
            host_pool_type=self.host_pool_type,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            load_balancer_type=self.load_balancer_type,
            location=self.location,
            managed_by=self.managed_by,
            max_session_limit=self.max_session_limit,
            name=self.name,
            object_id=self.object_id,
            personal_desktop_assignment_type=self.personal_desktop_assignment_type,
            plan=self.plan,
            preferred_app_group_type=self.preferred_app_group_type,
            private_endpoint_connections=self.private_endpoint_connections,
            public_network_access=self.public_network_access,
            registration_info=self.registration_info,
            ring=self.ring,
            sku=self.sku,
            sso_client_id=self.sso_client_id,
            sso_client_secret_key_vault_path=self.sso_client_secret_key_vault_path,
            sso_secret_type=self.sso_secret_type,
            ssoadfs_authority=self.ssoadfs_authority,
            start_vm_on_connect=self.start_vm_on_connect,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            validation_environment=self.validation_environment,
            vm_template=self.vm_template)


def get_host_pool(host_pool_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHostPoolResult:
    """
    Get a host pool.


    :param str host_pool_name: The name of the host pool within the specified resource group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['hostPoolName'] = host_pool_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20240403:getHostPool', __args__, opts=opts, typ=GetHostPoolResult).value

    return AwaitableGetHostPoolResult(
        agent_update=pulumi.get(__ret__, 'agent_update'),
        app_attach_package_references=pulumi.get(__ret__, 'app_attach_package_references'),
        application_group_references=pulumi.get(__ret__, 'application_group_references'),
        cloud_pc_resource=pulumi.get(__ret__, 'cloud_pc_resource'),
        custom_rdp_property=pulumi.get(__ret__, 'custom_rdp_property'),
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        friendly_name=pulumi.get(__ret__, 'friendly_name'),
        host_pool_type=pulumi.get(__ret__, 'host_pool_type'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        kind=pulumi.get(__ret__, 'kind'),
        load_balancer_type=pulumi.get(__ret__, 'load_balancer_type'),
        location=pulumi.get(__ret__, 'location'),
        managed_by=pulumi.get(__ret__, 'managed_by'),
        max_session_limit=pulumi.get(__ret__, 'max_session_limit'),
        name=pulumi.get(__ret__, 'name'),
        object_id=pulumi.get(__ret__, 'object_id'),
        personal_desktop_assignment_type=pulumi.get(__ret__, 'personal_desktop_assignment_type'),
        plan=pulumi.get(__ret__, 'plan'),
        preferred_app_group_type=pulumi.get(__ret__, 'preferred_app_group_type'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        registration_info=pulumi.get(__ret__, 'registration_info'),
        ring=pulumi.get(__ret__, 'ring'),
        sku=pulumi.get(__ret__, 'sku'),
        sso_client_id=pulumi.get(__ret__, 'sso_client_id'),
        sso_client_secret_key_vault_path=pulumi.get(__ret__, 'sso_client_secret_key_vault_path'),
        sso_secret_type=pulumi.get(__ret__, 'sso_secret_type'),
        ssoadfs_authority=pulumi.get(__ret__, 'ssoadfs_authority'),
        start_vm_on_connect=pulumi.get(__ret__, 'start_vm_on_connect'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        validation_environment=pulumi.get(__ret__, 'validation_environment'),
        vm_template=pulumi.get(__ret__, 'vm_template'))


@_utilities.lift_output_func(get_host_pool)
def get_host_pool_output(host_pool_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHostPoolResult]:
    """
    Get a host pool.


    :param str host_pool_name: The name of the host pool within the specified resource group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
