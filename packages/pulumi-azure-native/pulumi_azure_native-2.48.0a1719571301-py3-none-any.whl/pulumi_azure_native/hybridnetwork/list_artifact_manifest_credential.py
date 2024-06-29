# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListArtifactManifestCredentialResult',
    'AwaitableListArtifactManifestCredentialResult',
    'list_artifact_manifest_credential',
    'list_artifact_manifest_credential_output',
]

@pulumi.output_type
class ListArtifactManifestCredentialResult:
    """
    The artifact manifest credential definition.
    """
    def __init__(__self__, credential_type=None):
        if credential_type and not isinstance(credential_type, str):
            raise TypeError("Expected argument 'credential_type' to be a str")
        pulumi.set(__self__, "credential_type", credential_type)

    @property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> str:
        """
        The credential type.
        """
        return pulumi.get(self, "credential_type")


class AwaitableListArtifactManifestCredentialResult(ListArtifactManifestCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListArtifactManifestCredentialResult(
            credential_type=self.credential_type)


def list_artifact_manifest_credential(artifact_manifest_name: Optional[str] = None,
                                      artifact_store_name: Optional[str] = None,
                                      publisher_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListArtifactManifestCredentialResult:
    """
    List credential for publishing artifacts defined in artifact manifest.
    Azure REST API version: 2023-09-01.


    :param str artifact_manifest_name: The name of the artifact manifest.
    :param str artifact_store_name: The name of the artifact store.
    :param str publisher_name: The name of the publisher.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['artifactManifestName'] = artifact_manifest_name
    __args__['artifactStoreName'] = artifact_store_name
    __args__['publisherName'] = publisher_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridnetwork:listArtifactManifestCredential', __args__, opts=opts, typ=ListArtifactManifestCredentialResult).value

    return AwaitableListArtifactManifestCredentialResult(
        credential_type=pulumi.get(__ret__, 'credential_type'))


@_utilities.lift_output_func(list_artifact_manifest_credential)
def list_artifact_manifest_credential_output(artifact_manifest_name: Optional[pulumi.Input[str]] = None,
                                             artifact_store_name: Optional[pulumi.Input[str]] = None,
                                             publisher_name: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListArtifactManifestCredentialResult]:
    """
    List credential for publishing artifacts defined in artifact manifest.
    Azure REST API version: 2023-09-01.


    :param str artifact_manifest_name: The name of the artifact manifest.
    :param str artifact_store_name: The name of the artifact store.
    :param str publisher_name: The name of the publisher.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
