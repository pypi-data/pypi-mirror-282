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

__all__ = ['ReplicaKeyArgs', 'ReplicaKey']

@pulumi.input_type
class ReplicaKeyArgs:
    def __init__(__self__, *,
                 key_policy: Any,
                 primary_key_arn: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 pending_window_in_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ReplicaKey resource.
        :param Any key_policy: The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
        :param pulumi.Input[str] primary_key_arn: Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
        :param pulumi.Input[str] description: A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        :param pulumi.Input[bool] enabled: Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
        :param pulumi.Input[int] pending_window_in_days: Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "key_policy", key_policy)
        pulumi.set(__self__, "primary_key_arn", primary_key_arn)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if pending_window_in_days is not None:
            pulumi.set(__self__, "pending_window_in_days", pending_window_in_days)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyPolicy")
    def key_policy(self) -> Any:
        """
        The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "key_policy")

    @key_policy.setter
    def key_policy(self, value: Any):
        pulumi.set(self, "key_policy", value)

    @property
    @pulumi.getter(name="primaryKeyArn")
    def primary_key_arn(self) -> pulumi.Input[str]:
        """
        Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
        """
        return pulumi.get(self, "primary_key_arn")

    @primary_key_arn.setter
    def primary_key_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary_key_arn", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="pendingWindowInDays")
    def pending_window_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        """
        return pulumi.get(self, "pending_window_in_days")

    @pending_window_in_days.setter
    def pending_window_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pending_window_in_days", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class ReplicaKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_policy: Optional[Any] = None,
                 pending_window_in_days: Optional[pulumi.Input[int]] = None,
                 primary_key_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::KMS::ReplicaKey resource specifies a multi-region replica AWS KMS key in AWS Key Management Service (AWS KMS).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        :param pulumi.Input[bool] enabled: Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
        :param Any key_policy: The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
        :param pulumi.Input[int] pending_window_in_days: Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        :param pulumi.Input[str] primary_key_arn: Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicaKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::KMS::ReplicaKey resource specifies a multi-region replica AWS KMS key in AWS Key Management Service (AWS KMS).

        :param str resource_name: The name of the resource.
        :param ReplicaKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicaKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_policy: Optional[Any] = None,
                 pending_window_in_days: Optional[pulumi.Input[int]] = None,
                 primary_key_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReplicaKeyArgs.__new__(ReplicaKeyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            if key_policy is None and not opts.urn:
                raise TypeError("Missing required property 'key_policy'")
            __props__.__dict__["key_policy"] = key_policy
            __props__.__dict__["pending_window_in_days"] = pending_window_in_days
            if primary_key_arn is None and not opts.urn:
                raise TypeError("Missing required property 'primary_key_arn'")
            __props__.__dict__["primary_key_arn"] = primary_key_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["key_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["primaryKeyArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ReplicaKey, __self__).__init__(
            'aws-native:kms:ReplicaKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReplicaKey':
        """
        Get an existing ReplicaKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReplicaKeyArgs.__new__(ReplicaKeyArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["key_id"] = None
        __props__.__dict__["key_policy"] = None
        __props__.__dict__["pending_window_in_days"] = None
        __props__.__dict__["primary_key_arn"] = None
        __props__.__dict__["tags"] = None
        return ReplicaKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the replica key, such as `arn:aws:kms:us-west-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab` .

        The key ARNs of related multi-Region keys differ only in the Region value. For information about the key ARNs of multi-Region keys, see [How multi-Region keys work](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-how-it-works) in the *AWS Key Management Service Developer Guide* .
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[str]:
        """
        The key ID of the replica key, such as `mrk-1234abcd12ab34cd56ef1234567890ab` .

        Related multi-Region keys have the same key ID. For information about the key IDs of multi-Region keys, see [How multi-Region keys work](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-how-it-works) in the *AWS Key Management Service Developer Guide* .
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="keyPolicy")
    def key_policy(self) -> pulumi.Output[Any]:
        """
        The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "key_policy")

    @property
    @pulumi.getter(name="pendingWindowInDays")
    def pending_window_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        """
        return pulumi.get(self, "pending_window_in_days")

    @property
    @pulumi.getter(name="primaryKeyArn")
    def primary_key_arn(self) -> pulumi.Output[str]:
        """
        Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
        """
        return pulumi.get(self, "primary_key_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

