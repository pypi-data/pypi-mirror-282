# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['StaticIpArgs', 'StaticIp']

@pulumi.input_type
class StaticIpArgs:
    def __init__(__self__, *,
                 attached_to: Optional[pulumi.Input[str]] = None,
                 static_ip_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StaticIp resource.
        :param pulumi.Input[str] attached_to: The instance where the static IP is attached.
        :param pulumi.Input[str] static_ip_name: The name of the static IP address.
        """
        if attached_to is not None:
            pulumi.set(__self__, "attached_to", attached_to)
        if static_ip_name is not None:
            pulumi.set(__self__, "static_ip_name", static_ip_name)

    @property
    @pulumi.getter(name="attachedTo")
    def attached_to(self) -> Optional[pulumi.Input[str]]:
        """
        The instance where the static IP is attached.
        """
        return pulumi.get(self, "attached_to")

    @attached_to.setter
    def attached_to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attached_to", value)

    @property
    @pulumi.getter(name="staticIpName")
    def static_ip_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the static IP address.
        """
        return pulumi.get(self, "static_ip_name")

    @static_ip_name.setter
    def static_ip_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "static_ip_name", value)


class StaticIp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_to: Optional[pulumi.Input[str]] = None,
                 static_ip_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Lightsail::StaticIp

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attached_to: The instance where the static IP is attached.
        :param pulumi.Input[str] static_ip_name: The name of the static IP address.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StaticIpArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Lightsail::StaticIp

        :param str resource_name: The name of the resource.
        :param StaticIpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticIpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_to: Optional[pulumi.Input[str]] = None,
                 static_ip_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StaticIpArgs.__new__(StaticIpArgs)

            __props__.__dict__["attached_to"] = attached_to
            __props__.__dict__["static_ip_name"] = static_ip_name
            __props__.__dict__["ip_address"] = None
            __props__.__dict__["is_attached"] = None
            __props__.__dict__["static_ip_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["staticIpName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(StaticIp, __self__).__init__(
            'aws-native:lightsail:StaticIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StaticIp':
        """
        Get an existing StaticIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StaticIpArgs.__new__(StaticIpArgs)

        __props__.__dict__["attached_to"] = None
        __props__.__dict__["ip_address"] = None
        __props__.__dict__["is_attached"] = None
        __props__.__dict__["static_ip_arn"] = None
        __props__.__dict__["static_ip_name"] = None
        return StaticIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachedTo")
    def attached_to(self) -> pulumi.Output[Optional[str]]:
        """
        The instance where the static IP is attached.
        """
        return pulumi.get(self, "attached_to")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The static IP address.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isAttached")
    def is_attached(self) -> pulumi.Output[bool]:
        """
        A Boolean value indicating whether the static IP is attached.
        """
        return pulumi.get(self, "is_attached")

    @property
    @pulumi.getter(name="staticIpArn")
    def static_ip_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the static IP (for example, `arn:aws:lightsail:us-east-2:123456789101:StaticIp/244ad76f-8aad-4741-809f-12345EXAMPLE` ).
        """
        return pulumi.get(self, "static_ip_arn")

    @property
    @pulumi.getter(name="staticIpName")
    def static_ip_name(self) -> pulumi.Output[str]:
        """
        The name of the static IP address.
        """
        return pulumi.get(self, "static_ip_name")

