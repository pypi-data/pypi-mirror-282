# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['GlobalClusterArgs', 'GlobalCluster']

@pulumi.input_type
class GlobalClusterArgs:
    def __init__(__self__, *,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input['GlobalClusterEngine']] = None,
                 engine_lifecycle_support: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GlobalCluster resource.
        :param pulumi.Input[bool] deletion_protection: The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
        :param pulumi.Input['GlobalClusterEngine'] engine: The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
               If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        :param pulumi.Input[str] engine_lifecycle_support: The life cycle type of the global cluster. You can use this setting to enroll your global cluster into Amazon RDS Extended Support.
        :param pulumi.Input[str] engine_version: The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        :param pulumi.Input[str] global_cluster_identifier: The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
        :param pulumi.Input[str] source_db_cluster_identifier: The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.
        :param pulumi.Input[bool] storage_encrypted:  The storage encryption setting for the new global database cluster.
               If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)
        if engine is not None:
            pulumi.set(__self__, "engine", engine)
        if engine_lifecycle_support is not None:
            pulumi.set(__self__, "engine_lifecycle_support", engine_lifecycle_support)
        if engine_version is not None:
            pulumi.set(__self__, "engine_version", engine_version)
        if global_cluster_identifier is not None:
            pulumi.set(__self__, "global_cluster_identifier", global_cluster_identifier)
        if source_db_cluster_identifier is not None:
            pulumi.set(__self__, "source_db_cluster_identifier", source_db_cluster_identifier)
        if storage_encrypted is not None:
            pulumi.set(__self__, "storage_encrypted", storage_encrypted)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
        """
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)

    @property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input['GlobalClusterEngine']]:
        """
        The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
        If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: Optional[pulumi.Input['GlobalClusterEngine']]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> Optional[pulumi.Input[str]]:
        """
        The life cycle type of the global cluster. You can use this setting to enroll your global cluster into Amazon RDS Extended Support.
        """
        return pulumi.get(self, "engine_lifecycle_support")

    @engine_lifecycle_support.setter
    def engine_lifecycle_support(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_lifecycle_support", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
        """
        return pulumi.get(self, "global_cluster_identifier")

    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_cluster_identifier", value)

    @property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.
        """
        return pulumi.get(self, "source_db_cluster_identifier")

    @source_db_cluster_identifier.setter
    def source_db_cluster_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_db_cluster_identifier", value)

    @property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
         The storage encryption setting for the new global database cluster.
        If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        return pulumi.get(self, "storage_encrypted")

    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "storage_encrypted", value)


class GlobalCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input['GlobalClusterEngine']] = None,
                 engine_lifecycle_support: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::RDS::GlobalCluster

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] deletion_protection: The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
        :param pulumi.Input['GlobalClusterEngine'] engine: The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
               If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        :param pulumi.Input[str] engine_lifecycle_support: The life cycle type of the global cluster. You can use this setting to enroll your global cluster into Amazon RDS Extended Support.
        :param pulumi.Input[str] engine_version: The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        :param pulumi.Input[str] global_cluster_identifier: The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
        :param pulumi.Input[str] source_db_cluster_identifier: The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.
        :param pulumi.Input[bool] storage_encrypted:  The storage encryption setting for the new global database cluster.
               If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GlobalClusterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::RDS::GlobalCluster

        :param str resource_name: The name of the resource.
        :param GlobalClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input['GlobalClusterEngine']] = None,
                 engine_lifecycle_support: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 global_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 source_db_cluster_identifier: Optional[pulumi.Input[str]] = None,
                 storage_encrypted: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GlobalClusterArgs.__new__(GlobalClusterArgs)

            __props__.__dict__["deletion_protection"] = deletion_protection
            __props__.__dict__["engine"] = engine
            __props__.__dict__["engine_lifecycle_support"] = engine_lifecycle_support
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["global_cluster_identifier"] = global_cluster_identifier
            __props__.__dict__["source_db_cluster_identifier"] = source_db_cluster_identifier
            __props__.__dict__["storage_encrypted"] = storage_encrypted
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["engine", "globalClusterIdentifier", "sourceDbClusterIdentifier", "storageEncrypted"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(GlobalCluster, __self__).__init__(
            'aws-native:rds:GlobalCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GlobalCluster':
        """
        Get an existing GlobalCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GlobalClusterArgs.__new__(GlobalClusterArgs)

        __props__.__dict__["deletion_protection"] = None
        __props__.__dict__["engine"] = None
        __props__.__dict__["engine_lifecycle_support"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["global_cluster_identifier"] = None
        __props__.__dict__["source_db_cluster_identifier"] = None
        __props__.__dict__["storage_encrypted"] = None
        return GlobalCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[Optional['GlobalClusterEngine']]:
        """
        The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
        If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> pulumi.Output[Optional[str]]:
        """
        The life cycle type of the global cluster. You can use this setting to enroll your global cluster into Amazon RDS Extended Support.
        """
        return pulumi.get(self, "engine_lifecycle_support")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
        """
        return pulumi.get(self, "global_cluster_identifier")

    @property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.
        """
        return pulumi.get(self, "source_db_cluster_identifier")

    @property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[Optional[bool]]:
        """
         The storage encryption setting for the new global database cluster.
        If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        """
        return pulumi.get(self, "storage_encrypted")

