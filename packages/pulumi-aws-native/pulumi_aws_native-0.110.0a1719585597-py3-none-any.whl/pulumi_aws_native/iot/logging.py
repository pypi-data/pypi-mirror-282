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

__all__ = ['LoggingArgs', 'Logging']

@pulumi.input_type
class LoggingArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 default_log_level: pulumi.Input['LoggingDefaultLogLevel'],
                 role_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a Logging resource.
        :param pulumi.Input[str] account_id: Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
        :param pulumi.Input['LoggingDefaultLogLevel'] default_log_level: The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        :param pulumi.Input[str] role_arn: The ARN of the role that allows IoT to write to Cloudwatch logs.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "default_log_level", default_log_level)
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="defaultLogLevel")
    def default_log_level(self) -> pulumi.Input['LoggingDefaultLogLevel']:
        """
        The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        """
        return pulumi.get(self, "default_log_level")

    @default_log_level.setter
    def default_log_level(self, value: pulumi.Input['LoggingDefaultLogLevel']):
        pulumi.set(self, "default_log_level", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the role that allows IoT to write to Cloudwatch logs.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)


class Logging(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 default_log_level: Optional[pulumi.Input['LoggingDefaultLogLevel']] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
        :param pulumi.Input['LoggingDefaultLogLevel'] default_log_level: The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        :param pulumi.Input[str] role_arn: The ARN of the role that allows IoT to write to Cloudwatch logs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoggingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.

        :param str resource_name: The name of the resource.
        :param LoggingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoggingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 default_log_level: Optional[pulumi.Input['LoggingDefaultLogLevel']] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LoggingArgs.__new__(LoggingArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if default_log_level is None and not opts.urn:
                raise TypeError("Missing required property 'default_log_level'")
            __props__.__dict__["default_log_level"] = default_log_level
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["accountId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Logging, __self__).__init__(
            'aws-native:iot:Logging',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Logging':
        """
        Get an existing Logging resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LoggingArgs.__new__(LoggingArgs)

        __props__.__dict__["account_id"] = None
        __props__.__dict__["default_log_level"] = None
        __props__.__dict__["role_arn"] = None
        return Logging(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="defaultLogLevel")
    def default_log_level(self) -> pulumi.Output['LoggingDefaultLogLevel']:
        """
        The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
        """
        return pulumi.get(self, "default_log_level")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the role that allows IoT to write to Cloudwatch logs.
        """
        return pulumi.get(self, "role_arn")

