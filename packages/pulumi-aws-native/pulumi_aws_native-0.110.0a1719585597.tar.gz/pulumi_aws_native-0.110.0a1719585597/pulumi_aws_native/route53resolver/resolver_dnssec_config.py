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

__all__ = ['ResolverDnssecConfigArgs', 'ResolverDnssecConfig']

@pulumi.input_type
class ResolverDnssecConfigArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ResolverDnssecConfig resource.
        :param pulumi.Input[str] resource_id: ResourceId
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ResourceId
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


class ResolverDnssecConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Route53Resolver::ResolverDNSSECConfig.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_id: ResourceId
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ResolverDnssecConfigArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Route53Resolver::ResolverDNSSECConfig.

        :param str resource_name: The name of the resource.
        :param ResolverDnssecConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResolverDnssecConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResolverDnssecConfigArgs.__new__(ResolverDnssecConfigArgs)

            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["owner_id"] = None
            __props__.__dict__["validation_status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["resourceId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ResolverDnssecConfig, __self__).__init__(
            'aws-native:route53resolver:ResolverDnssecConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResolverDnssecConfig':
        """
        Get an existing ResolverDnssecConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResolverDnssecConfigArgs.__new__(ResolverDnssecConfigArgs)

        __props__.__dict__["aws_id"] = None
        __props__.__dict__["owner_id"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["validation_status"] = None
        return ResolverDnssecConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        Id
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        AccountId
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        ResourceId
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> pulumi.Output['ResolverDnssecConfigValidationStatus']:
        """
        ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
        """
        return pulumi.get(self, "validation_status")

