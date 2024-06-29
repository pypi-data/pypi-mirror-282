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
    'AzureDevOpsResourceInfoArgs',
    'ContentPathMapArgs',
    'DeploymentInfoArgs',
    'DeploymentArgs',
    'GitHubResourceInfoArgs',
    'RepositoryResourceInfoArgs',
    'RepositoryArgs',
    'WebhookArgs',
]

@pulumi.input_type
class AzureDevOpsResourceInfoArgs:
    def __init__(__self__, *,
                 pipeline_id: Optional[pulumi.Input[str]] = None,
                 service_connection_id: Optional[pulumi.Input[str]] = None):
        """
        Resources created in Azure DevOps repository.
        :param pulumi.Input[str] pipeline_id: Id of the pipeline created for the source-control.
        :param pulumi.Input[str] service_connection_id: Id of the service-connection created for the source-control.
        """
        if pipeline_id is not None:
            pulumi.set(__self__, "pipeline_id", pipeline_id)
        if service_connection_id is not None:
            pulumi.set(__self__, "service_connection_id", service_connection_id)

    @property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the pipeline created for the source-control.
        """
        return pulumi.get(self, "pipeline_id")

    @pipeline_id.setter
    def pipeline_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_id", value)

    @property
    @pulumi.getter(name="serviceConnectionId")
    def service_connection_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the service-connection created for the source-control.
        """
        return pulumi.get(self, "service_connection_id")

    @service_connection_id.setter
    def service_connection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_connection_id", value)


@pulumi.input_type
class ContentPathMapArgs:
    def __init__(__self__, *,
                 content_type: Optional[pulumi.Input[Union[str, 'ContentType']]] = None,
                 path: Optional[pulumi.Input[str]] = None):
        """
        The mapping of content type to a repo path.
        :param pulumi.Input[Union[str, 'ContentType']] content_type: Content type.
        :param pulumi.Input[str] path: The path to the content.
        """
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[Union[str, 'ContentType']]]:
        """
        Content type.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[Union[str, 'ContentType']]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the content.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)


@pulumi.input_type
class DeploymentInfoArgs:
    def __init__(__self__, *,
                 deployment: Optional[pulumi.Input['DeploymentArgs']] = None,
                 deployment_fetch_status: Optional[pulumi.Input[Union[str, 'DeploymentFetchStatus']]] = None,
                 message: Optional[pulumi.Input[str]] = None):
        """
        Information regarding a deployment.
        :param pulumi.Input['DeploymentArgs'] deployment: Deployment information.
        :param pulumi.Input[Union[str, 'DeploymentFetchStatus']] deployment_fetch_status: Status while fetching the last deployment.
        :param pulumi.Input[str] message: Additional details about the deployment that can be shown to the user.
        """
        if deployment is not None:
            pulumi.set(__self__, "deployment", deployment)
        if deployment_fetch_status is not None:
            pulumi.set(__self__, "deployment_fetch_status", deployment_fetch_status)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input['DeploymentArgs']]:
        """
        Deployment information.
        """
        return pulumi.get(self, "deployment")

    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input['DeploymentArgs']]):
        pulumi.set(self, "deployment", value)

    @property
    @pulumi.getter(name="deploymentFetchStatus")
    def deployment_fetch_status(self) -> Optional[pulumi.Input[Union[str, 'DeploymentFetchStatus']]]:
        """
        Status while fetching the last deployment.
        """
        return pulumi.get(self, "deployment_fetch_status")

    @deployment_fetch_status.setter
    def deployment_fetch_status(self, value: Optional[pulumi.Input[Union[str, 'DeploymentFetchStatus']]]):
        pulumi.set(self, "deployment_fetch_status", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        Additional details about the deployment that can be shown to the user.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)


@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 deployment_logs_url: Optional[pulumi.Input[str]] = None,
                 deployment_result: Optional[pulumi.Input[Union[str, 'DeploymentResult']]] = None,
                 deployment_state: Optional[pulumi.Input[Union[str, 'DeploymentState']]] = None,
                 deployment_time: Optional[pulumi.Input[str]] = None):
        """
        Description about a deployment.
        :param pulumi.Input[str] deployment_id: Deployment identifier.
        :param pulumi.Input[str] deployment_logs_url: Url to access repository action logs.
        :param pulumi.Input[Union[str, 'DeploymentResult']] deployment_result: The outcome of the deployment.
        :param pulumi.Input[Union[str, 'DeploymentState']] deployment_state: Current status of the deployment.
        :param pulumi.Input[str] deployment_time: The time when the deployment finished.
        """
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if deployment_logs_url is not None:
            pulumi.set(__self__, "deployment_logs_url", deployment_logs_url)
        if deployment_result is not None:
            pulumi.set(__self__, "deployment_result", deployment_result)
        if deployment_state is not None:
            pulumi.set(__self__, "deployment_state", deployment_state)
        if deployment_time is not None:
            pulumi.set(__self__, "deployment_time", deployment_time)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        Deployment identifier.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="deploymentLogsUrl")
    def deployment_logs_url(self) -> Optional[pulumi.Input[str]]:
        """
        Url to access repository action logs.
        """
        return pulumi.get(self, "deployment_logs_url")

    @deployment_logs_url.setter
    def deployment_logs_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_logs_url", value)

    @property
    @pulumi.getter(name="deploymentResult")
    def deployment_result(self) -> Optional[pulumi.Input[Union[str, 'DeploymentResult']]]:
        """
        The outcome of the deployment.
        """
        return pulumi.get(self, "deployment_result")

    @deployment_result.setter
    def deployment_result(self, value: Optional[pulumi.Input[Union[str, 'DeploymentResult']]]):
        pulumi.set(self, "deployment_result", value)

    @property
    @pulumi.getter(name="deploymentState")
    def deployment_state(self) -> Optional[pulumi.Input[Union[str, 'DeploymentState']]]:
        """
        Current status of the deployment.
        """
        return pulumi.get(self, "deployment_state")

    @deployment_state.setter
    def deployment_state(self, value: Optional[pulumi.Input[Union[str, 'DeploymentState']]]):
        pulumi.set(self, "deployment_state", value)

    @property
    @pulumi.getter(name="deploymentTime")
    def deployment_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the deployment finished.
        """
        return pulumi.get(self, "deployment_time")

    @deployment_time.setter
    def deployment_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_time", value)


@pulumi.input_type
class GitHubResourceInfoArgs:
    def __init__(__self__, *,
                 app_installation_id: Optional[pulumi.Input[str]] = None):
        """
        Resources created in GitHub repository.
        :param pulumi.Input[str] app_installation_id: GitHub application installation id.
        """
        if app_installation_id is not None:
            pulumi.set(__self__, "app_installation_id", app_installation_id)

    @property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[pulumi.Input[str]]:
        """
        GitHub application installation id.
        """
        return pulumi.get(self, "app_installation_id")

    @app_installation_id.setter
    def app_installation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_installation_id", value)


@pulumi.input_type
class RepositoryResourceInfoArgs:
    def __init__(__self__, *,
                 azure_dev_ops_resource_info: Optional[pulumi.Input['AzureDevOpsResourceInfoArgs']] = None,
                 git_hub_resource_info: Optional[pulumi.Input['GitHubResourceInfoArgs']] = None,
                 webhook: Optional[pulumi.Input['WebhookArgs']] = None):
        """
        Resources created in user's repository for the source-control.
        :param pulumi.Input['AzureDevOpsResourceInfoArgs'] azure_dev_ops_resource_info: Resources created in Azure DevOps for this source-control.
        :param pulumi.Input['GitHubResourceInfoArgs'] git_hub_resource_info: Resources created in GitHub for this source-control.
        :param pulumi.Input['WebhookArgs'] webhook: The webhook object created for the source-control.
        """
        if azure_dev_ops_resource_info is not None:
            pulumi.set(__self__, "azure_dev_ops_resource_info", azure_dev_ops_resource_info)
        if git_hub_resource_info is not None:
            pulumi.set(__self__, "git_hub_resource_info", git_hub_resource_info)
        if webhook is not None:
            pulumi.set(__self__, "webhook", webhook)

    @property
    @pulumi.getter(name="azureDevOpsResourceInfo")
    def azure_dev_ops_resource_info(self) -> Optional[pulumi.Input['AzureDevOpsResourceInfoArgs']]:
        """
        Resources created in Azure DevOps for this source-control.
        """
        return pulumi.get(self, "azure_dev_ops_resource_info")

    @azure_dev_ops_resource_info.setter
    def azure_dev_ops_resource_info(self, value: Optional[pulumi.Input['AzureDevOpsResourceInfoArgs']]):
        pulumi.set(self, "azure_dev_ops_resource_info", value)

    @property
    @pulumi.getter(name="gitHubResourceInfo")
    def git_hub_resource_info(self) -> Optional[pulumi.Input['GitHubResourceInfoArgs']]:
        """
        Resources created in GitHub for this source-control.
        """
        return pulumi.get(self, "git_hub_resource_info")

    @git_hub_resource_info.setter
    def git_hub_resource_info(self, value: Optional[pulumi.Input['GitHubResourceInfoArgs']]):
        pulumi.set(self, "git_hub_resource_info", value)

    @property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input['WebhookArgs']]:
        """
        The webhook object created for the source-control.
        """
        return pulumi.get(self, "webhook")

    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input['WebhookArgs']]):
        pulumi.set(self, "webhook", value)


@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *,
                 branch: Optional[pulumi.Input[str]] = None,
                 deployment_logs_url: Optional[pulumi.Input[str]] = None,
                 display_url: Optional[pulumi.Input[str]] = None,
                 path_mapping: Optional[pulumi.Input[Sequence[pulumi.Input['ContentPathMapArgs']]]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        metadata of a repository.
        :param pulumi.Input[str] branch: Branch name of repository.
        :param pulumi.Input[str] deployment_logs_url: Url to access repository action logs.
        :param pulumi.Input[str] display_url: Display url of repository.
        :param pulumi.Input[Sequence[pulumi.Input['ContentPathMapArgs']]] path_mapping: Dictionary of source control content type and path mapping.
        :param pulumi.Input[str] url: Url of repository.
        """
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if deployment_logs_url is not None:
            pulumi.set(__self__, "deployment_logs_url", deployment_logs_url)
        if display_url is not None:
            pulumi.set(__self__, "display_url", display_url)
        if path_mapping is not None:
            pulumi.set(__self__, "path_mapping", path_mapping)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        Branch name of repository.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="deploymentLogsUrl")
    def deployment_logs_url(self) -> Optional[pulumi.Input[str]]:
        """
        Url to access repository action logs.
        """
        return pulumi.get(self, "deployment_logs_url")

    @deployment_logs_url.setter
    def deployment_logs_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_logs_url", value)

    @property
    @pulumi.getter(name="displayUrl")
    def display_url(self) -> Optional[pulumi.Input[str]]:
        """
        Display url of repository.
        """
        return pulumi.get(self, "display_url")

    @display_url.setter
    def display_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_url", value)

    @property
    @pulumi.getter(name="pathMapping")
    def path_mapping(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContentPathMapArgs']]]]:
        """
        Dictionary of source control content type and path mapping.
        """
        return pulumi.get(self, "path_mapping")

    @path_mapping.setter
    def path_mapping(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContentPathMapArgs']]]]):
        pulumi.set(self, "path_mapping", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        Url of repository.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class WebhookArgs:
    def __init__(__self__, *,
                 rotate_webhook_secret: Optional[pulumi.Input[bool]] = None,
                 webhook_id: Optional[pulumi.Input[str]] = None,
                 webhook_secret_update_time: Optional[pulumi.Input[str]] = None,
                 webhook_url: Optional[pulumi.Input[str]] = None):
        """
        Detail about the webhook object.
        :param pulumi.Input[bool] rotate_webhook_secret: A flag to instruct the backend service to rotate webhook secret.
        :param pulumi.Input[str] webhook_id: Unique identifier for the webhook.
        :param pulumi.Input[str] webhook_secret_update_time: Time when the webhook secret was updated.
        :param pulumi.Input[str] webhook_url: URL that gets invoked by the webhook.
        """
        if rotate_webhook_secret is not None:
            pulumi.set(__self__, "rotate_webhook_secret", rotate_webhook_secret)
        if webhook_id is not None:
            pulumi.set(__self__, "webhook_id", webhook_id)
        if webhook_secret_update_time is not None:
            pulumi.set(__self__, "webhook_secret_update_time", webhook_secret_update_time)
        if webhook_url is not None:
            pulumi.set(__self__, "webhook_url", webhook_url)

    @property
    @pulumi.getter(name="rotateWebhookSecret")
    def rotate_webhook_secret(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag to instruct the backend service to rotate webhook secret.
        """
        return pulumi.get(self, "rotate_webhook_secret")

    @rotate_webhook_secret.setter
    def rotate_webhook_secret(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "rotate_webhook_secret", value)

    @property
    @pulumi.getter(name="webhookId")
    def webhook_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier for the webhook.
        """
        return pulumi.get(self, "webhook_id")

    @webhook_id.setter
    def webhook_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_id", value)

    @property
    @pulumi.getter(name="webhookSecretUpdateTime")
    def webhook_secret_update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time when the webhook secret was updated.
        """
        return pulumi.get(self, "webhook_secret_update_time")

    @webhook_secret_update_time.setter
    def webhook_secret_update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_secret_update_time", value)

    @property
    @pulumi.getter(name="webhookUrl")
    def webhook_url(self) -> Optional[pulumi.Input[str]]:
        """
        URL that gets invoked by the webhook.
        """
        return pulumi.get(self, "webhook_url")

    @webhook_url.setter
    def webhook_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_url", value)


