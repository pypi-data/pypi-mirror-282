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
from ._enums import *
from ._inputs import *

__all__ = ['GatewayArgs', 'Gateway']

@pulumi.input_type
class GatewayArgs:
    def __init__(__self__, *,
                 egress_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[str]]],
                 networks: pulumi.Input[Sequence[pulumi.Input['GatewayNetworkArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] egress_cidr_blocks: The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param pulumi.Input[Sequence[pulumi.Input['GatewayNetworkArgs']]] networks: The list of networks in the gateway.
        :param pulumi.Input[str] name: The name of the gateway. This name can not be modified after the gateway is created.
        """
        pulumi.set(__self__, "egress_cidr_blocks", egress_cidr_blocks)
        pulumi.set(__self__, "networks", networks)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="egressCidrBlocks")
    def egress_cidr_blocks(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        """
        return pulumi.get(self, "egress_cidr_blocks")

    @egress_cidr_blocks.setter
    def egress_cidr_blocks(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "egress_cidr_blocks", value)

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Input[Sequence[pulumi.Input['GatewayNetworkArgs']]]:
        """
        The list of networks in the gateway.
        """
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: pulumi.Input[Sequence[pulumi.Input['GatewayNetworkArgs']]]):
        pulumi.set(self, "networks", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the gateway. This name can not be modified after the gateway is created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Gateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 egress_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GatewayNetworkArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::MediaConnect::Gateway

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] egress_cidr_blocks: The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param pulumi.Input[str] name: The name of the gateway. This name can not be modified after the gateway is created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GatewayNetworkArgs']]]] networks: The list of networks in the gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::MediaConnect::Gateway

        :param str resource_name: The name of the resource.
        :param GatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 egress_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GatewayNetworkArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GatewayArgs.__new__(GatewayArgs)

            if egress_cidr_blocks is None and not opts.urn:
                raise TypeError("Missing required property 'egress_cidr_blocks'")
            __props__.__dict__["egress_cidr_blocks"] = egress_cidr_blocks
            __props__.__dict__["name"] = name
            if networks is None and not opts.urn:
                raise TypeError("Missing required property 'networks'")
            __props__.__dict__["networks"] = networks
            __props__.__dict__["gateway_arn"] = None
            __props__.__dict__["gateway_state"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["egressCidrBlocks[*]", "name", "networks[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Gateway, __self__).__init__(
            'aws-native:mediaconnect:Gateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gateway':
        """
        Get an existing Gateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayArgs.__new__(GatewayArgs)

        __props__.__dict__["egress_cidr_blocks"] = None
        __props__.__dict__["gateway_arn"] = None
        __props__.__dict__["gateway_state"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["networks"] = None
        return Gateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="egressCidrBlocks")
    def egress_cidr_blocks(self) -> pulumi.Output[Sequence[str]]:
        """
        The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        """
        return pulumi.get(self, "egress_cidr_blocks")

    @property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the gateway.
        """
        return pulumi.get(self, "gateway_arn")

    @property
    @pulumi.getter(name="gatewayState")
    def gateway_state(self) -> pulumi.Output['GatewayState']:
        """
        The current status of the gateway.
        """
        return pulumi.get(self, "gateway_state")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the gateway. This name can not be modified after the gateway is created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Sequence['outputs.GatewayNetwork']]:
        """
        The list of networks in the gateway.
        """
        return pulumi.get(self, "networks")

