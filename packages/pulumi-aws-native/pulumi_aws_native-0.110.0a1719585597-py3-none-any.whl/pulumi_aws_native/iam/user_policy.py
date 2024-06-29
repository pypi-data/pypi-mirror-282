# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserPolicyInitArgs', 'UserPolicy']

@pulumi.input_type
class UserPolicyInitArgs:
    def __init__(__self__, *,
                 user_name: pulumi.Input[str],
                 policy_document: Optional[Any] = None,
                 policy_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserPolicy resource.
        :param pulumi.Input[str] user_name: The name of the user to associate the policy with.
                This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param Any policy_document: The policy document.
                You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.
                The [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
                 +  Any printable ASCII character ranging from the space character (``\\u0020``) through the end of the ASCII character range
                 +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF``)
                 +  The special characters tab (``\\u0009``), line feed (``\\u000A``), and carriage return (``\\u000D``)
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::UserPolicy` for more information about the expected schema for this property.
        :param pulumi.Input[str] policy_name: The name of the policy document.
                This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        pulumi.set(__self__, "user_name", user_name)
        if policy_document is not None:
            pulumi.set(__self__, "policy_document", policy_document)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[str]:
        """
        The name of the user to associate the policy with.
         This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_name", value)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[Any]:
        """
        The policy document.
         You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.
         The [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
          +  Any printable ASCII character ranging from the space character (``\\u0020``) through the end of the ASCII character range
          +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF``)
          +  The special characters tab (``\\u0009``), line feed (``\\u000A``), and carriage return (``\\u000D``)

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::UserPolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Optional[Any]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy document.
         This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)


class UserPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_document: Optional[Any] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Adds or updates an inline policy document that is embedded in the specified IAM user.
         An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html). To create a new managed policy, use [AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html). For information about policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.
         For information about the maximum number of inline policies that you can embed in a user, see [IAM and quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any policy_document: The policy document.
                You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.
                The [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
                 +  Any printable ASCII character ranging from the space character (``\\u0020``) through the end of the ASCII character range
                 +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF``)
                 +  The special characters tab (``\\u0009``), line feed (``\\u000A``), and carriage return (``\\u000D``)
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::UserPolicy` for more information about the expected schema for this property.
        :param pulumi.Input[str] policy_name: The name of the policy document.
                This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param pulumi.Input[str] user_name: The name of the user to associate the policy with.
                This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserPolicyInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Adds or updates an inline policy document that is embedded in the specified IAM user.
         An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html). To create a new managed policy, use [AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html). For information about policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.
         For information about the maximum number of inline policies that you can embed in a user, see [IAM and quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.

        :param str resource_name: The name of the resource.
        :param UserPolicyInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserPolicyInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_document: Optional[Any] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserPolicyInitArgs.__new__(UserPolicyInitArgs)

            __props__.__dict__["policy_document"] = policy_document
            __props__.__dict__["policy_name"] = policy_name
            if user_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_name'")
            __props__.__dict__["user_name"] = user_name
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["policyName", "userName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(UserPolicy, __self__).__init__(
            'aws-native:iam:UserPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserPolicy':
        """
        Get an existing UserPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserPolicyInitArgs.__new__(UserPolicyInitArgs)

        __props__.__dict__["policy_document"] = None
        __props__.__dict__["policy_name"] = None
        __props__.__dict__["user_name"] = None
        return UserPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy document.
         You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.
         The [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
          +  Any printable ASCII character ranging from the space character (``\\u0020``) through the end of the ASCII character range
          +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF``)
          +  The special characters tab (``\\u0009``), line feed (``\\u000A``), and carriage return (``\\u000D``)

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::UserPolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        The name of the policy document.
         This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        The name of the user to associate the policy with.
         This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        """
        return pulumi.get(self, "user_name")

