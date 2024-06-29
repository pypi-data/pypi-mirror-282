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
from ._inputs import *

__all__ = ['SchedulingPolicyArgs', 'SchedulingPolicy']

@pulumi.input_type
class SchedulingPolicyArgs:
    def __init__(__self__, *,
                 fairshare_policy: Optional[pulumi.Input['SchedulingPolicyFairsharePolicyArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SchedulingPolicy resource.
        :param pulumi.Input['SchedulingPolicyFairsharePolicyArgs'] fairshare_policy: The fair share policy of the scheduling policy.
        :param pulumi.Input[str] name: Name of Scheduling Policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A key-value pair to associate with a resource.
        """
        if fairshare_policy is not None:
            pulumi.set(__self__, "fairshare_policy", fairshare_policy)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="fairsharePolicy")
    def fairshare_policy(self) -> Optional[pulumi.Input['SchedulingPolicyFairsharePolicyArgs']]:
        """
        The fair share policy of the scheduling policy.
        """
        return pulumi.get(self, "fairshare_policy")

    @fairshare_policy.setter
    def fairshare_policy(self, value: Optional[pulumi.Input['SchedulingPolicyFairsharePolicyArgs']]):
        pulumi.set(self, "fairshare_policy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Scheduling Policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class SchedulingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fairshare_policy: Optional[pulumi.Input[pulumi.InputType['SchedulingPolicyFairsharePolicyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource Type schema for AWS::Batch::SchedulingPolicy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SchedulingPolicyFairsharePolicyArgs']] fairshare_policy: The fair share policy of the scheduling policy.
        :param pulumi.Input[str] name: Name of Scheduling Policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A key-value pair to associate with a resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SchedulingPolicyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type schema for AWS::Batch::SchedulingPolicy

        :param str resource_name: The name of the resource.
        :param SchedulingPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SchedulingPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fairshare_policy: Optional[pulumi.Input[pulumi.InputType['SchedulingPolicyFairsharePolicyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SchedulingPolicyArgs.__new__(SchedulingPolicyArgs)

            __props__.__dict__["fairshare_policy"] = fairshare_policy
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "tags.*"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SchedulingPolicy, __self__).__init__(
            'aws-native:batch:SchedulingPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SchedulingPolicy':
        """
        Get an existing SchedulingPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SchedulingPolicyArgs.__new__(SchedulingPolicyArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["fairshare_policy"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return SchedulingPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Returns the scheduling policy ARN, such as `batch: *us-east-1* : *111122223333* :scheduling-policy/ *HighPriority*` .
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="fairsharePolicy")
    def fairshare_policy(self) -> pulumi.Output[Optional['outputs.SchedulingPolicyFairsharePolicy']]:
        """
        The fair share policy of the scheduling policy.
        """
        return pulumi.get(self, "fairshare_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of Scheduling Policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

