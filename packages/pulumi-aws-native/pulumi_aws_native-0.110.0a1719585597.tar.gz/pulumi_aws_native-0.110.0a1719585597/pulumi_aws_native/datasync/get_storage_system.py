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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetStorageSystemResult',
    'AwaitableGetStorageSystemResult',
    'get_storage_system',
    'get_storage_system_output',
]

@pulumi.output_type
class GetStorageSystemResult:
    def __init__(__self__, agent_arns=None, cloud_watch_log_group_arn=None, connectivity_status=None, name=None, secrets_manager_arn=None, server_configuration=None, storage_system_arn=None, system_type=None, tags=None):
        if agent_arns and not isinstance(agent_arns, list):
            raise TypeError("Expected argument 'agent_arns' to be a list")
        pulumi.set(__self__, "agent_arns", agent_arns)
        if cloud_watch_log_group_arn and not isinstance(cloud_watch_log_group_arn, str):
            raise TypeError("Expected argument 'cloud_watch_log_group_arn' to be a str")
        pulumi.set(__self__, "cloud_watch_log_group_arn", cloud_watch_log_group_arn)
        if connectivity_status and not isinstance(connectivity_status, str):
            raise TypeError("Expected argument 'connectivity_status' to be a str")
        pulumi.set(__self__, "connectivity_status", connectivity_status)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if secrets_manager_arn and not isinstance(secrets_manager_arn, str):
            raise TypeError("Expected argument 'secrets_manager_arn' to be a str")
        pulumi.set(__self__, "secrets_manager_arn", secrets_manager_arn)
        if server_configuration and not isinstance(server_configuration, dict):
            raise TypeError("Expected argument 'server_configuration' to be a dict")
        pulumi.set(__self__, "server_configuration", server_configuration)
        if storage_system_arn and not isinstance(storage_system_arn, str):
            raise TypeError("Expected argument 'storage_system_arn' to be a str")
        pulumi.set(__self__, "storage_system_arn", storage_system_arn)
        if system_type and not isinstance(system_type, str):
            raise TypeError("Expected argument 'system_type' to be a str")
        pulumi.set(__self__, "system_type", system_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> Optional[Sequence[str]]:
        """
        The ARN of the DataSync agent that connects to and reads from the on-premises storage system's management interface.
        """
        return pulumi.get(self, "agent_arns")

    @property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[str]:
        """
        The ARN of the Amazon CloudWatch log group used to monitor and log discovery job events.
        """
        return pulumi.get(self, "cloud_watch_log_group_arn")

    @property
    @pulumi.getter(name="connectivityStatus")
    def connectivity_status(self) -> Optional['StorageSystemConnectivityStatus']:
        """
        Indicates whether the DataSync agent can access the on-premises storage system.
        """
        return pulumi.get(self, "connectivity_status")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A familiar name for the on-premises storage system.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> Optional[str]:
        """
        The ARN of a secret stored by AWS Secrets Manager.
        """
        return pulumi.get(self, "secrets_manager_arn")

    @property
    @pulumi.getter(name="serverConfiguration")
    def server_configuration(self) -> Optional['outputs.StorageSystemServerConfiguration']:
        """
        Specifies the server name and network port required to connect with the management interface of your on-premises storage system.
        """
        return pulumi.get(self, "server_configuration")

    @property
    @pulumi.getter(name="storageSystemArn")
    def storage_system_arn(self) -> Optional[str]:
        """
        The ARN of the on-premises storage system added to DataSync Discovery.
        """
        return pulumi.get(self, "storage_system_arn")

    @property
    @pulumi.getter(name="systemType")
    def system_type(self) -> Optional['StorageSystemSystemType']:
        """
        The type of on-premises storage system that DataSync Discovery will analyze.
        """
        return pulumi.get(self, "system_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetStorageSystemResult(GetStorageSystemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageSystemResult(
            agent_arns=self.agent_arns,
            cloud_watch_log_group_arn=self.cloud_watch_log_group_arn,
            connectivity_status=self.connectivity_status,
            name=self.name,
            secrets_manager_arn=self.secrets_manager_arn,
            server_configuration=self.server_configuration,
            storage_system_arn=self.storage_system_arn,
            system_type=self.system_type,
            tags=self.tags)


def get_storage_system(storage_system_arn: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageSystemResult:
    """
    Resource schema for AWS::DataSync::StorageSystem.


    :param str storage_system_arn: The ARN of the on-premises storage system added to DataSync Discovery.
    """
    __args__ = dict()
    __args__['storageSystemArn'] = storage_system_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datasync:getStorageSystem', __args__, opts=opts, typ=GetStorageSystemResult).value

    return AwaitableGetStorageSystemResult(
        agent_arns=pulumi.get(__ret__, 'agent_arns'),
        cloud_watch_log_group_arn=pulumi.get(__ret__, 'cloud_watch_log_group_arn'),
        connectivity_status=pulumi.get(__ret__, 'connectivity_status'),
        name=pulumi.get(__ret__, 'name'),
        secrets_manager_arn=pulumi.get(__ret__, 'secrets_manager_arn'),
        server_configuration=pulumi.get(__ret__, 'server_configuration'),
        storage_system_arn=pulumi.get(__ret__, 'storage_system_arn'),
        system_type=pulumi.get(__ret__, 'system_type'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_storage_system)
def get_storage_system_output(storage_system_arn: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageSystemResult]:
    """
    Resource schema for AWS::DataSync::StorageSystem.


    :param str storage_system_arn: The ARN of the on-premises storage system added to DataSync Discovery.
    """
    ...
