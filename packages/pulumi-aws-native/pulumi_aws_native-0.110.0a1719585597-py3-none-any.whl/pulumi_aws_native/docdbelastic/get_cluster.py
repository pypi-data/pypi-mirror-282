# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    def __init__(__self__, backup_retention_period=None, cluster_arn=None, cluster_endpoint=None, preferred_backup_window=None, preferred_maintenance_window=None, shard_capacity=None, shard_count=None, shard_instance_count=None, subnet_ids=None, tags=None, vpc_security_group_ids=None):
        if backup_retention_period and not isinstance(backup_retention_period, int):
            raise TypeError("Expected argument 'backup_retention_period' to be a int")
        pulumi.set(__self__, "backup_retention_period", backup_retention_period)
        if cluster_arn and not isinstance(cluster_arn, str):
            raise TypeError("Expected argument 'cluster_arn' to be a str")
        pulumi.set(__self__, "cluster_arn", cluster_arn)
        if cluster_endpoint and not isinstance(cluster_endpoint, str):
            raise TypeError("Expected argument 'cluster_endpoint' to be a str")
        pulumi.set(__self__, "cluster_endpoint", cluster_endpoint)
        if preferred_backup_window and not isinstance(preferred_backup_window, str):
            raise TypeError("Expected argument 'preferred_backup_window' to be a str")
        pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, str):
            raise TypeError("Expected argument 'preferred_maintenance_window' to be a str")
        pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if shard_capacity and not isinstance(shard_capacity, int):
            raise TypeError("Expected argument 'shard_capacity' to be a int")
        pulumi.set(__self__, "shard_capacity", shard_capacity)
        if shard_count and not isinstance(shard_count, int):
            raise TypeError("Expected argument 'shard_count' to be a int")
        pulumi.set(__self__, "shard_count", shard_count)
        if shard_instance_count and not isinstance(shard_instance_count, int):
            raise TypeError("Expected argument 'shard_instance_count' to be a int")
        pulumi.set(__self__, "shard_instance_count", shard_instance_count)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError("Expected argument 'vpc_security_group_ids' to be a list")
        pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[int]:
        """
        The number of days for which automatic snapshots are retained.
        """
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> Optional[str]:
        return pulumi.get(self, "cluster_arn")

    @property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> Optional[str]:
        """
        The URL used to connect to the elastic cluster.
        """
        return pulumi.get(self, "cluster_endpoint")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[str]:
        """
        The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod` .
        """
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        """
        The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        *Format* : `ddd:hh24:mi-ddd:hh24:mi`

        *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.

        *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun

        *Constraints* : Minimum 30-minute window.
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="shardCapacity")
    def shard_capacity(self) -> Optional[int]:
        """
        The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        """
        return pulumi.get(self, "shard_capacity")

    @property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[int]:
        """
        The number of shards assigned to the elastic cluster. Maximum is 32.
        """
        return pulumi.get(self, "shard_count")

    @property
    @pulumi.getter(name="shardInstanceCount")
    def shard_instance_count(self) -> Optional[int]:
        """
        The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
        """
        return pulumi.get(self, "shard_instance_count")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        """
        The Amazon EC2 subnet IDs for the new elastic cluster.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags to be assigned to the new elastic cluster.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[Sequence[str]]:
        """
        A list of EC2 VPC security groups to associate with the new elastic cluster.
        """
        return pulumi.get(self, "vpc_security_group_ids")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            backup_retention_period=self.backup_retention_period,
            cluster_arn=self.cluster_arn,
            cluster_endpoint=self.cluster_endpoint,
            preferred_backup_window=self.preferred_backup_window,
            preferred_maintenance_window=self.preferred_maintenance_window,
            shard_capacity=self.shard_capacity,
            shard_count=self.shard_count,
            shard_instance_count=self.shard_instance_count,
            subnet_ids=self.subnet_ids,
            tags=self.tags,
            vpc_security_group_ids=self.vpc_security_group_ids)


def get_cluster(cluster_arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster
    """
    __args__ = dict()
    __args__['clusterArn'] = cluster_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:docdbelastic:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        backup_retention_period=pulumi.get(__ret__, 'backup_retention_period'),
        cluster_arn=pulumi.get(__ret__, 'cluster_arn'),
        cluster_endpoint=pulumi.get(__ret__, 'cluster_endpoint'),
        preferred_backup_window=pulumi.get(__ret__, 'preferred_backup_window'),
        preferred_maintenance_window=pulumi.get(__ret__, 'preferred_maintenance_window'),
        shard_capacity=pulumi.get(__ret__, 'shard_capacity'),
        shard_count=pulumi.get(__ret__, 'shard_count'),
        shard_instance_count=pulumi.get(__ret__, 'shard_instance_count'),
        subnet_ids=pulumi.get(__ret__, 'subnet_ids'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_security_group_ids=pulumi.get(__ret__, 'vpc_security_group_ids'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster
    """
    ...
