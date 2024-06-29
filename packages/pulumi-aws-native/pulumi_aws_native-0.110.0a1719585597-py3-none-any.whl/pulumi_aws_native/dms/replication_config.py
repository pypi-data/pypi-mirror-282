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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['ReplicationConfigArgs', 'ReplicationConfig']

@pulumi.input_type
class ReplicationConfigArgs:
    def __init__(__self__, *,
                 compute_config: Optional[pulumi.Input['ReplicationConfigComputeConfigArgs']] = None,
                 replication_config_identifier: Optional[pulumi.Input[str]] = None,
                 replication_settings: Optional[Any] = None,
                 replication_type: Optional[pulumi.Input['ReplicationConfigReplicationType']] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 source_endpoint_arn: Optional[pulumi.Input[str]] = None,
                 supplemental_settings: Optional[Any] = None,
                 table_mappings: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 target_endpoint_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ReplicationConfig resource.
        :param pulumi.Input['ReplicationConfigComputeConfigArgs'] compute_config: Configuration parameters for provisioning an AWS DMS Serverless replication.
        :param pulumi.Input[str] replication_config_identifier: A unique identifier of replication configuration
        :param Any replication_settings: JSON settings for Servereless replications that are provisioned using this replication configuration
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        :param pulumi.Input['ReplicationConfigReplicationType'] replication_type: The type of AWS DMS Serverless replication to provision using this replication configuration
        :param pulumi.Input[str] resource_identifier: A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
        :param pulumi.Input[str] source_endpoint_arn: The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
        :param Any supplemental_settings: JSON settings for specifying supplemental data
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        :param Any table_mappings: JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        :param pulumi.Input[str] target_endpoint_arn: The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
        """
        if compute_config is not None:
            pulumi.set(__self__, "compute_config", compute_config)
        if replication_config_identifier is not None:
            pulumi.set(__self__, "replication_config_identifier", replication_config_identifier)
        if replication_settings is not None:
            pulumi.set(__self__, "replication_settings", replication_settings)
        if replication_type is not None:
            pulumi.set(__self__, "replication_type", replication_type)
        if resource_identifier is not None:
            pulumi.set(__self__, "resource_identifier", resource_identifier)
        if source_endpoint_arn is not None:
            pulumi.set(__self__, "source_endpoint_arn", source_endpoint_arn)
        if supplemental_settings is not None:
            pulumi.set(__self__, "supplemental_settings", supplemental_settings)
        if table_mappings is not None:
            pulumi.set(__self__, "table_mappings", table_mappings)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_endpoint_arn is not None:
            pulumi.set(__self__, "target_endpoint_arn", target_endpoint_arn)

    @property
    @pulumi.getter(name="computeConfig")
    def compute_config(self) -> Optional[pulumi.Input['ReplicationConfigComputeConfigArgs']]:
        """
        Configuration parameters for provisioning an AWS DMS Serverless replication.
        """
        return pulumi.get(self, "compute_config")

    @compute_config.setter
    def compute_config(self, value: Optional[pulumi.Input['ReplicationConfigComputeConfigArgs']]):
        pulumi.set(self, "compute_config", value)

    @property
    @pulumi.getter(name="replicationConfigIdentifier")
    def replication_config_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier of replication configuration
        """
        return pulumi.get(self, "replication_config_identifier")

    @replication_config_identifier.setter
    def replication_config_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_config_identifier", value)

    @property
    @pulumi.getter(name="replicationSettings")
    def replication_settings(self) -> Optional[Any]:
        """
        JSON settings for Servereless replications that are provisioned using this replication configuration

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "replication_settings")

    @replication_settings.setter
    def replication_settings(self, value: Optional[Any]):
        pulumi.set(self, "replication_settings", value)

    @property
    @pulumi.getter(name="replicationType")
    def replication_type(self) -> Optional[pulumi.Input['ReplicationConfigReplicationType']]:
        """
        The type of AWS DMS Serverless replication to provision using this replication configuration
        """
        return pulumi.get(self, "replication_type")

    @replication_type.setter
    def replication_type(self, value: Optional[pulumi.Input['ReplicationConfigReplicationType']]):
        pulumi.set(self, "replication_type", value)

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
        """
        return pulumi.get(self, "resource_identifier")

    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_identifier", value)

    @property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
        """
        return pulumi.get(self, "source_endpoint_arn")

    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_endpoint_arn", value)

    @property
    @pulumi.getter(name="supplementalSettings")
    def supplemental_settings(self) -> Optional[Any]:
        """
        JSON settings for specifying supplemental data

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "supplemental_settings")

    @supplemental_settings.setter
    def supplemental_settings(self, value: Optional[Any]):
        pulumi.set(self, "supplemental_settings", value)

    @property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> Optional[Any]:
        """
        JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "table_mappings")

    @table_mappings.setter
    def table_mappings(self, value: Optional[Any]):
        pulumi.set(self, "table_mappings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
        """
        return pulumi.get(self, "target_endpoint_arn")

    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_endpoint_arn", value)


class ReplicationConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_config: Optional[pulumi.Input[pulumi.InputType['ReplicationConfigComputeConfigArgs']]] = None,
                 replication_config_identifier: Optional[pulumi.Input[str]] = None,
                 replication_settings: Optional[Any] = None,
                 replication_type: Optional[pulumi.Input['ReplicationConfigReplicationType']] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 source_endpoint_arn: Optional[pulumi.Input[str]] = None,
                 supplemental_settings: Optional[Any] = None,
                 table_mappings: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_endpoint_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A replication configuration that you later provide to configure and start a AWS DMS Serverless replication

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ReplicationConfigComputeConfigArgs']] compute_config: Configuration parameters for provisioning an AWS DMS Serverless replication.
        :param pulumi.Input[str] replication_config_identifier: A unique identifier of replication configuration
        :param Any replication_settings: JSON settings for Servereless replications that are provisioned using this replication configuration
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        :param pulumi.Input['ReplicationConfigReplicationType'] replication_type: The type of AWS DMS Serverless replication to provision using this replication configuration
        :param pulumi.Input[str] resource_identifier: A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
        :param pulumi.Input[str] source_endpoint_arn: The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
        :param Any supplemental_settings: JSON settings for specifying supplemental data
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        :param Any table_mappings: JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        :param pulumi.Input[str] target_endpoint_arn: The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ReplicationConfigArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A replication configuration that you later provide to configure and start a AWS DMS Serverless replication

        :param str resource_name: The name of the resource.
        :param ReplicationConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_config: Optional[pulumi.Input[pulumi.InputType['ReplicationConfigComputeConfigArgs']]] = None,
                 replication_config_identifier: Optional[pulumi.Input[str]] = None,
                 replication_settings: Optional[Any] = None,
                 replication_type: Optional[pulumi.Input['ReplicationConfigReplicationType']] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 source_endpoint_arn: Optional[pulumi.Input[str]] = None,
                 supplemental_settings: Optional[Any] = None,
                 table_mappings: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_endpoint_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReplicationConfigArgs.__new__(ReplicationConfigArgs)

            __props__.__dict__["compute_config"] = compute_config
            __props__.__dict__["replication_config_identifier"] = replication_config_identifier
            __props__.__dict__["replication_settings"] = replication_settings
            __props__.__dict__["replication_type"] = replication_type
            __props__.__dict__["resource_identifier"] = resource_identifier
            __props__.__dict__["source_endpoint_arn"] = source_endpoint_arn
            __props__.__dict__["supplemental_settings"] = supplemental_settings
            __props__.__dict__["table_mappings"] = table_mappings
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_endpoint_arn"] = target_endpoint_arn
            __props__.__dict__["replication_config_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["resourceIdentifier"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ReplicationConfig, __self__).__init__(
            'aws-native:dms:ReplicationConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReplicationConfig':
        """
        Get an existing ReplicationConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReplicationConfigArgs.__new__(ReplicationConfigArgs)

        __props__.__dict__["compute_config"] = None
        __props__.__dict__["replication_config_arn"] = None
        __props__.__dict__["replication_config_identifier"] = None
        __props__.__dict__["replication_settings"] = None
        __props__.__dict__["replication_type"] = None
        __props__.__dict__["resource_identifier"] = None
        __props__.__dict__["source_endpoint_arn"] = None
        __props__.__dict__["supplemental_settings"] = None
        __props__.__dict__["table_mappings"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_endpoint_arn"] = None
        return ReplicationConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computeConfig")
    def compute_config(self) -> pulumi.Output[Optional['outputs.ReplicationConfigComputeConfig']]:
        """
        Configuration parameters for provisioning an AWS DMS Serverless replication.
        """
        return pulumi.get(self, "compute_config")

    @property
    @pulumi.getter(name="replicationConfigArn")
    def replication_config_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Replication Config
        """
        return pulumi.get(self, "replication_config_arn")

    @property
    @pulumi.getter(name="replicationConfigIdentifier")
    def replication_config_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        A unique identifier of replication configuration
        """
        return pulumi.get(self, "replication_config_identifier")

    @property
    @pulumi.getter(name="replicationSettings")
    def replication_settings(self) -> pulumi.Output[Optional[Any]]:
        """
        JSON settings for Servereless replications that are provisioned using this replication configuration

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "replication_settings")

    @property
    @pulumi.getter(name="replicationType")
    def replication_type(self) -> pulumi.Output[Optional['ReplicationConfigReplicationType']]:
        """
        The type of AWS DMS Serverless replication to provision using this replication configuration
        """
        return pulumi.get(self, "replication_type")

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
        """
        return pulumi.get(self, "resource_identifier")

    @property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
        """
        return pulumi.get(self, "source_endpoint_arn")

    @property
    @pulumi.getter(name="supplementalSettings")
    def supplemental_settings(self) -> pulumi.Output[Optional[Any]]:
        """
        JSON settings for specifying supplemental data

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "supplemental_settings")

    @property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> pulumi.Output[Optional[Any]]:
        """
        JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "table_mappings")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
        """
        return pulumi.get(self, "target_endpoint_arn")

