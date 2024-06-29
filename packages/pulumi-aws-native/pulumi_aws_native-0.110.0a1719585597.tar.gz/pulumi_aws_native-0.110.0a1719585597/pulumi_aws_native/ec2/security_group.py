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
from ._inputs import *

__all__ = ['SecurityGroupArgs', 'SecurityGroup']

@pulumi.input_type
class SecurityGroupArgs:
    def __init__(__self__, *,
                 group_description: pulumi.Input[str],
                 group_name: Optional[pulumi.Input[str]] = None,
                 security_group_egress: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityGroupEgressArgs']]]] = None,
                 security_group_ingress: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityGroupIngressArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityGroup resource.
        :param pulumi.Input[str] group_description: A description for the security group.
        :param pulumi.Input[str] group_name: The name of the security group.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityGroupEgressArgs']]] security_group_egress: [VPC only] The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityGroupIngressArgs']]] security_group_ingress: The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Any tags assigned to the security group.
        :param pulumi.Input[str] vpc_id: The ID of the VPC for the security group.
        """
        pulumi.set(__self__, "group_description", group_description)
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if security_group_egress is not None:
            pulumi.set(__self__, "security_group_egress", security_group_egress)
        if security_group_ingress is not None:
            pulumi.set(__self__, "security_group_ingress", security_group_ingress)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="groupDescription")
    def group_description(self) -> pulumi.Input[str]:
        """
        A description for the security group.
        """
        return pulumi.get(self, "group_description")

    @group_description.setter
    def group_description(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_description", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security group.
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="securityGroupEgress")
    def security_group_egress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityGroupEgressArgs']]]]:
        """
        [VPC only] The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        """
        return pulumi.get(self, "security_group_egress")

    @security_group_egress.setter
    def security_group_egress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityGroupEgressArgs']]]]):
        pulumi.set(self, "security_group_egress", value)

    @property
    @pulumi.getter(name="securityGroupIngress")
    def security_group_ingress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityGroupIngressArgs']]]]:
        """
        The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        """
        return pulumi.get(self, "security_group_ingress")

    @security_group_ingress.setter
    def security_group_ingress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityGroupIngressArgs']]]]):
        pulumi.set(self, "security_group_ingress", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Any tags assigned to the security group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPC for the security group.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class SecurityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_description: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 security_group_egress: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityGroupEgressArgs']]]]] = None,
                 security_group_ingress: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityGroupIngressArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::SecurityGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_description: A description for the security group.
        :param pulumi.Input[str] group_name: The name of the security group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityGroupEgressArgs']]]] security_group_egress: [VPC only] The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityGroupIngressArgs']]]] security_group_ingress: The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: Any tags assigned to the security group.
        :param pulumi.Input[str] vpc_id: The ID of the VPC for the security group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::SecurityGroup

        :param str resource_name: The name of the resource.
        :param SecurityGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_description: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 security_group_egress: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityGroupEgressArgs']]]]] = None,
                 security_group_ingress: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityGroupIngressArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityGroupArgs.__new__(SecurityGroupArgs)

            if group_description is None and not opts.urn:
                raise TypeError("Missing required property 'group_description'")
            __props__.__dict__["group_description"] = group_description
            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["security_group_egress"] = security_group_egress
            __props__.__dict__["security_group_ingress"] = security_group_ingress
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["group_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["groupDescription", "groupName", "vpcId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SecurityGroup, __self__).__init__(
            'aws-native:ec2:SecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityGroup':
        """
        Get an existing SecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityGroupArgs.__new__(SecurityGroupArgs)

        __props__.__dict__["aws_id"] = None
        __props__.__dict__["group_description"] = None
        __props__.__dict__["group_id"] = None
        __props__.__dict__["group_name"] = None
        __props__.__dict__["security_group_egress"] = None
        __props__.__dict__["security_group_ingress"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_id"] = None
        return SecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        The group name or group ID depending on whether the SG is created in default or specific VPC
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="groupDescription")
    def group_description(self) -> pulumi.Output[str]:
        """
        A description for the security group.
        """
        return pulumi.get(self, "group_description")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The group ID of the specified security group.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the security group.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="securityGroupEgress")
    def security_group_egress(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityGroupEgress']]]:
        """
        [VPC only] The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        """
        return pulumi.get(self, "security_group_egress")

    @property
    @pulumi.getter(name="securityGroupIngress")
    def security_group_ingress(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityGroupIngress']]]:
        """
        The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.
        """
        return pulumi.get(self, "security_group_ingress")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Any tags assigned to the security group.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the VPC for the security group.
        """
        return pulumi.get(self, "vpc_id")

