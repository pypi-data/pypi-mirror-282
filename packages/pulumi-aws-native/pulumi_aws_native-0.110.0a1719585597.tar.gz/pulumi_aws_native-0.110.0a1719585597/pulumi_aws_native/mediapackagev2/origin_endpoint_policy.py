# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['OriginEndpointPolicyArgs', 'OriginEndpointPolicy']

@pulumi.input_type
class OriginEndpointPolicyArgs:
    def __init__(__self__, *,
                 channel_group_name: pulumi.Input[str],
                 channel_name: pulumi.Input[str],
                 origin_endpoint_name: pulumi.Input[str],
                 policy: Any):
        """
        The set of arguments for constructing a OriginEndpointPolicy resource.
        :param pulumi.Input[str] channel_group_name: The name of the channel group associated with the origin endpoint policy.
        :param pulumi.Input[str] channel_name: The channel name associated with the origin endpoint policy.
        :param pulumi.Input[str] origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint policy.
        :param Any policy: The policy associated with the origin endpoint.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::OriginEndpointPolicy` for more information about the expected schema for this property.
        """
        pulumi.set(__self__, "channel_group_name", channel_group_name)
        pulumi.set(__self__, "channel_name", channel_name)
        pulumi.set(__self__, "origin_endpoint_name", origin_endpoint_name)
        pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter(name="channelGroupName")
    def channel_group_name(self) -> pulumi.Input[str]:
        """
        The name of the channel group associated with the origin endpoint policy.
        """
        return pulumi.get(self, "channel_group_name")

    @channel_group_name.setter
    def channel_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "channel_group_name", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[str]:
        """
        The channel name associated with the origin endpoint policy.
        """
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter(name="originEndpointName")
    def origin_endpoint_name(self) -> pulumi.Input[str]:
        """
        The name of the origin endpoint associated with the origin endpoint policy.
        """
        return pulumi.get(self, "origin_endpoint_name")

    @origin_endpoint_name.setter
    def origin_endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "origin_endpoint_name", value)

    @property
    @pulumi.getter
    def policy(self) -> Any:
        """
        The policy associated with the origin endpoint.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::OriginEndpointPolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Any):
        pulumi.set(self, "policy", value)


class OriginEndpointPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_group_name: Optional[pulumi.Input[str]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 origin_endpoint_name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None,
                 __props__=None):
        """
        <p>Represents a resource policy that allows or denies access to an origin endpoint.</p>

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] channel_group_name: The name of the channel group associated with the origin endpoint policy.
        :param pulumi.Input[str] channel_name: The channel name associated with the origin endpoint policy.
        :param pulumi.Input[str] origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint policy.
        :param Any policy: The policy associated with the origin endpoint.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::OriginEndpointPolicy` for more information about the expected schema for this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OriginEndpointPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <p>Represents a resource policy that allows or denies access to an origin endpoint.</p>

        :param str resource_name: The name of the resource.
        :param OriginEndpointPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OriginEndpointPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_group_name: Optional[pulumi.Input[str]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 origin_endpoint_name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OriginEndpointPolicyArgs.__new__(OriginEndpointPolicyArgs)

            if channel_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'channel_group_name'")
            __props__.__dict__["channel_group_name"] = channel_group_name
            if channel_name is None and not opts.urn:
                raise TypeError("Missing required property 'channel_name'")
            __props__.__dict__["channel_name"] = channel_name
            if origin_endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'origin_endpoint_name'")
            __props__.__dict__["origin_endpoint_name"] = origin_endpoint_name
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["channelGroupName", "channelName", "originEndpointName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(OriginEndpointPolicy, __self__).__init__(
            'aws-native:mediapackagev2:OriginEndpointPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OriginEndpointPolicy':
        """
        Get an existing OriginEndpointPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OriginEndpointPolicyArgs.__new__(OriginEndpointPolicyArgs)

        __props__.__dict__["channel_group_name"] = None
        __props__.__dict__["channel_name"] = None
        __props__.__dict__["origin_endpoint_name"] = None
        __props__.__dict__["policy"] = None
        return OriginEndpointPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="channelGroupName")
    def channel_group_name(self) -> pulumi.Output[str]:
        """
        The name of the channel group associated with the origin endpoint policy.
        """
        return pulumi.get(self, "channel_group_name")

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Output[str]:
        """
        The channel name associated with the origin endpoint policy.
        """
        return pulumi.get(self, "channel_name")

    @property
    @pulumi.getter(name="originEndpointName")
    def origin_endpoint_name(self) -> pulumi.Output[str]:
        """
        The name of the origin endpoint associated with the origin endpoint policy.
        """
        return pulumi.get(self, "origin_endpoint_name")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Any]:
        """
        The policy associated with the origin endpoint.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::OriginEndpointPolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy")

