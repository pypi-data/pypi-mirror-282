# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 admin_user_name: pulumi.Input[str],
                 auth_type: pulumi.Input[str],
                 shard_capacity: pulumi.Input[int],
                 shard_count: pulumi.Input[int],
                 admin_user_password: Optional[pulumi.Input[str]] = None,
                 backup_retention_period: Optional[pulumi.Input[int]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 shard_instance_count: Optional[pulumi.Input[int]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] admin_user_name: The name of the Amazon DocumentDB elastic clusters administrator.
               
               *Constraints* :
               
               - Must be from 1 to 63 letters or numbers.
               - The first character must be a letter.
               - Cannot be a reserved word.
        :param pulumi.Input[str] auth_type: The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are `PLAIN_TEXT` or `SECRET_ARN` .
        :param pulumi.Input[int] shard_capacity: The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        :param pulumi.Input[int] shard_count: The number of shards assigned to the elastic cluster. Maximum is 32.
        :param pulumi.Input[str] admin_user_password: The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.
               
               *Constraints* :
               
               - Must contain from 8 to 100 characters.
               - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).
               - A valid `AdminUserName` entry is also required.
        :param pulumi.Input[int] backup_retention_period: The number of days for which automatic snapshots are retained.
        :param pulumi.Input[str] cluster_name: The name of the new elastic cluster. This parameter is stored as a lowercase string.
               
               *Constraints* :
               
               - Must contain from 1 to 63 letters, numbers, or hyphens.
               - The first character must be a letter.
               - Cannot end with a hyphen or contain two consecutive hyphens.
               
               *Example* : `my-cluster`
        :param pulumi.Input[str] kms_key_id: The KMS key identifier to use to encrypt the new elastic cluster.
               
               The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.
               
               If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        :param pulumi.Input[str] preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod` .
        :param pulumi.Input[str] preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
               
               *Format* : `ddd:hh24:mi-ddd:hh24:mi`
               
               *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.
               
               *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun
               
               *Constraints* : Minimum 30-minute window.
        :param pulumi.Input[int] shard_instance_count: The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The Amazon EC2 subnet IDs for the new elastic cluster.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags to be assigned to the new elastic cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_security_group_ids: A list of EC2 VPC security groups to associate with the new elastic cluster.
        """
        pulumi.set(__self__, "admin_user_name", admin_user_name)
        pulumi.set(__self__, "auth_type", auth_type)
        pulumi.set(__self__, "shard_capacity", shard_capacity)
        pulumi.set(__self__, "shard_count", shard_count)
        if admin_user_password is not None:
            pulumi.set(__self__, "admin_user_password", admin_user_password)
        if backup_retention_period is not None:
            pulumi.set(__self__, "backup_retention_period", backup_retention_period)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if preferred_backup_window is not None:
            pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window is not None:
            pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if shard_instance_count is not None:
            pulumi.set(__self__, "shard_instance_count", shard_instance_count)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_security_group_ids is not None:
            pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="adminUserName")
    def admin_user_name(self) -> pulumi.Input[str]:
        """
        The name of the Amazon DocumentDB elastic clusters administrator.

        *Constraints* :

        - Must be from 1 to 63 letters or numbers.
        - The first character must be a letter.
        - Cannot be a reserved word.
        """
        return pulumi.get(self, "admin_user_name")

    @admin_user_name.setter
    def admin_user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "admin_user_name", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[str]:
        """
        The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are `PLAIN_TEXT` or `SECRET_ARN` .
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="shardCapacity")
    def shard_capacity(self) -> pulumi.Input[int]:
        """
        The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        """
        return pulumi.get(self, "shard_capacity")

    @shard_capacity.setter
    def shard_capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "shard_capacity", value)

    @property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Input[int]:
        """
        The number of shards assigned to the elastic cluster. Maximum is 32.
        """
        return pulumi.get(self, "shard_count")

    @shard_count.setter
    def shard_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "shard_count", value)

    @property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.

        *Constraints* :

        - Must contain from 8 to 100 characters.
        - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).
        - A valid `AdminUserName` entry is also required.
        """
        return pulumi.get(self, "admin_user_password")

    @admin_user_password.setter
    def admin_user_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_user_password", value)

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[int]]:
        """
        The number of days for which automatic snapshots are retained.
        """
        return pulumi.get(self, "backup_retention_period")

    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup_retention_period", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the new elastic cluster. This parameter is stored as a lowercase string.

        *Constraints* :

        - Must contain from 1 to 63 letters, numbers, or hyphens.
        - The first character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        *Example* : `my-cluster`
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The KMS key identifier to use to encrypt the new elastic cluster.

        The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.

        If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[str]]:
        """
        The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod` .
        """
        return pulumi.get(self, "preferred_backup_window")

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_backup_window", value)

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[str]]:
        """
        The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        *Format* : `ddd:hh24:mi-ddd:hh24:mi`

        *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.

        *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun

        *Constraints* : Minimum 30-minute window.
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_maintenance_window", value)

    @property
    @pulumi.getter(name="shardInstanceCount")
    def shard_instance_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
        """
        return pulumi.get(self, "shard_instance_count")

    @shard_instance_count.setter
    def shard_instance_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "shard_instance_count", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Amazon EC2 subnet IDs for the new elastic cluster.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags to be assigned to the new elastic cluster.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of EC2 VPC security groups to associate with the new elastic cluster.
        """
        return pulumi.get(self, "vpc_security_group_ids")

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "vpc_security_group_ids", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_user_name: Optional[pulumi.Input[str]] = None,
                 admin_user_password: Optional[pulumi.Input[str]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 backup_retention_period: Optional[pulumi.Input[int]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 shard_capacity: Optional[pulumi.Input[int]] = None,
                 shard_count: Optional[pulumi.Input[int]] = None,
                 shard_instance_count: Optional[pulumi.Input[int]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_user_name: The name of the Amazon DocumentDB elastic clusters administrator.
               
               *Constraints* :
               
               - Must be from 1 to 63 letters or numbers.
               - The first character must be a letter.
               - Cannot be a reserved word.
        :param pulumi.Input[str] admin_user_password: The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.
               
               *Constraints* :
               
               - Must contain from 8 to 100 characters.
               - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).
               - A valid `AdminUserName` entry is also required.
        :param pulumi.Input[str] auth_type: The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are `PLAIN_TEXT` or `SECRET_ARN` .
        :param pulumi.Input[int] backup_retention_period: The number of days for which automatic snapshots are retained.
        :param pulumi.Input[str] cluster_name: The name of the new elastic cluster. This parameter is stored as a lowercase string.
               
               *Constraints* :
               
               - Must contain from 1 to 63 letters, numbers, or hyphens.
               - The first character must be a letter.
               - Cannot end with a hyphen or contain two consecutive hyphens.
               
               *Example* : `my-cluster`
        :param pulumi.Input[str] kms_key_id: The KMS key identifier to use to encrypt the new elastic cluster.
               
               The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.
               
               If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        :param pulumi.Input[str] preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod` .
        :param pulumi.Input[str] preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
               
               *Format* : `ddd:hh24:mi-ddd:hh24:mi`
               
               *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.
               
               *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun
               
               *Constraints* : Minimum 30-minute window.
        :param pulumi.Input[int] shard_capacity: The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        :param pulumi.Input[int] shard_count: The number of shards assigned to the elastic cluster. Maximum is 32.
        :param pulumi.Input[int] shard_instance_count: The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The Amazon EC2 subnet IDs for the new elastic cluster.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The tags to be assigned to the new elastic cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_security_group_ids: A list of EC2 VPC security groups to associate with the new elastic cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_user_name: Optional[pulumi.Input[str]] = None,
                 admin_user_password: Optional[pulumi.Input[str]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 backup_retention_period: Optional[pulumi.Input[int]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 shard_capacity: Optional[pulumi.Input[int]] = None,
                 shard_count: Optional[pulumi.Input[int]] = None,
                 shard_instance_count: Optional[pulumi.Input[int]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if admin_user_name is None and not opts.urn:
                raise TypeError("Missing required property 'admin_user_name'")
            __props__.__dict__["admin_user_name"] = admin_user_name
            __props__.__dict__["admin_user_password"] = admin_user_password
            if auth_type is None and not opts.urn:
                raise TypeError("Missing required property 'auth_type'")
            __props__.__dict__["auth_type"] = auth_type
            __props__.__dict__["backup_retention_period"] = backup_retention_period
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["preferred_backup_window"] = preferred_backup_window
            __props__.__dict__["preferred_maintenance_window"] = preferred_maintenance_window
            if shard_capacity is None and not opts.urn:
                raise TypeError("Missing required property 'shard_capacity'")
            __props__.__dict__["shard_capacity"] = shard_capacity
            if shard_count is None and not opts.urn:
                raise TypeError("Missing required property 'shard_count'")
            __props__.__dict__["shard_count"] = shard_count
            __props__.__dict__["shard_instance_count"] = shard_instance_count
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_security_group_ids"] = vpc_security_group_ids
            __props__.__dict__["cluster_arn"] = None
            __props__.__dict__["cluster_endpoint"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["adminUserName", "authType", "clusterName", "kmsKeyId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Cluster, __self__).__init__(
            'aws-native:docdbelastic:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["admin_user_name"] = None
        __props__.__dict__["admin_user_password"] = None
        __props__.__dict__["auth_type"] = None
        __props__.__dict__["backup_retention_period"] = None
        __props__.__dict__["cluster_arn"] = None
        __props__.__dict__["cluster_endpoint"] = None
        __props__.__dict__["cluster_name"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["preferred_backup_window"] = None
        __props__.__dict__["preferred_maintenance_window"] = None
        __props__.__dict__["shard_capacity"] = None
        __props__.__dict__["shard_count"] = None
        __props__.__dict__["shard_instance_count"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_security_group_ids"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminUserName")
    def admin_user_name(self) -> pulumi.Output[str]:
        """
        The name of the Amazon DocumentDB elastic clusters administrator.

        *Constraints* :

        - Must be from 1 to 63 letters or numbers.
        - The first character must be a letter.
        - Cannot be a reserved word.
        """
        return pulumi.get(self, "admin_user_name")

    @property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> pulumi.Output[Optional[str]]:
        """
        The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.

        *Constraints* :

        - Must contain from 8 to 100 characters.
        - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).
        - A valid `AdminUserName` entry is also required.
        """
        return pulumi.get(self, "admin_user_password")

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[str]:
        """
        The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are `PLAIN_TEXT` or `SECRET_ARN` .
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> pulumi.Output[Optional[int]]:
        """
        The number of days for which automatic snapshots are retained.
        """
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_arn")

    @property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> pulumi.Output[str]:
        """
        The URL used to connect to the elastic cluster.
        """
        return pulumi.get(self, "cluster_endpoint")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        The name of the new elastic cluster. This parameter is stored as a lowercase string.

        *Constraints* :

        - Must contain from 1 to 63 letters, numbers, or hyphens.
        - The first character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        *Example* : `my-cluster`
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The KMS key identifier to use to encrypt the new elastic cluster.

        The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.

        If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> pulumi.Output[Optional[str]]:
        """
        The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod` .
        """
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[Optional[str]]:
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
    def shard_capacity(self) -> pulumi.Output[int]:
        """
        The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        """
        return pulumi.get(self, "shard_capacity")

    @property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Output[int]:
        """
        The number of shards assigned to the elastic cluster. Maximum is 32.
        """
        return pulumi.get(self, "shard_count")

    @property
    @pulumi.getter(name="shardInstanceCount")
    def shard_instance_count(self) -> pulumi.Output[Optional[int]]:
        """
        The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
        """
        return pulumi.get(self, "shard_instance_count")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Amazon EC2 subnet IDs for the new elastic cluster.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags to be assigned to the new elastic cluster.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of EC2 VPC security groups to associate with the new elastic cluster.
        """
        return pulumi.get(self, "vpc_security_group_ids")

