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

__all__ = ['BridgeSourceInitArgs', 'BridgeSource']

@pulumi.input_type
class BridgeSourceInitArgs:
    def __init__(__self__, *,
                 bridge_arn: pulumi.Input[str],
                 flow_source: Optional[pulumi.Input['BridgeSourceBridgeFlowSourceArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_source: Optional[pulumi.Input['BridgeSourceBridgeNetworkSourceArgs']] = None):
        """
        The set of arguments for constructing a BridgeSource resource.
        :param pulumi.Input[str] bridge_arn: The Amazon Resource Number (ARN) of the bridge.
        :param pulumi.Input['BridgeSourceBridgeFlowSourceArgs'] flow_source: Add a flow source to an existing bridge.
        :param pulumi.Input[str] name: The name of the source.
        :param pulumi.Input['BridgeSourceBridgeNetworkSourceArgs'] network_source: Add a network source to an existing bridge.
        """
        pulumi.set(__self__, "bridge_arn", bridge_arn)
        if flow_source is not None:
            pulumi.set(__self__, "flow_source", flow_source)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_source is not None:
            pulumi.set(__self__, "network_source", network_source)

    @property
    @pulumi.getter(name="bridgeArn")
    def bridge_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Number (ARN) of the bridge.
        """
        return pulumi.get(self, "bridge_arn")

    @bridge_arn.setter
    def bridge_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "bridge_arn", value)

    @property
    @pulumi.getter(name="flowSource")
    def flow_source(self) -> Optional[pulumi.Input['BridgeSourceBridgeFlowSourceArgs']]:
        """
        Add a flow source to an existing bridge.
        """
        return pulumi.get(self, "flow_source")

    @flow_source.setter
    def flow_source(self, value: Optional[pulumi.Input['BridgeSourceBridgeFlowSourceArgs']]):
        pulumi.set(self, "flow_source", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the source.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkSource")
    def network_source(self) -> Optional[pulumi.Input['BridgeSourceBridgeNetworkSourceArgs']]:
        """
        Add a network source to an existing bridge.
        """
        return pulumi.get(self, "network_source")

    @network_source.setter
    def network_source(self, value: Optional[pulumi.Input['BridgeSourceBridgeNetworkSourceArgs']]):
        pulumi.set(self, "network_source", value)


class BridgeSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_arn: Optional[pulumi.Input[str]] = None,
                 flow_source: Optional[pulumi.Input[pulumi.InputType['BridgeSourceBridgeFlowSourceArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_source: Optional[pulumi.Input[pulumi.InputType['BridgeSourceBridgeNetworkSourceArgs']]] = None,
                 __props__=None):
        """
        Resource schema for AWS::MediaConnect::BridgeSource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bridge_arn: The Amazon Resource Number (ARN) of the bridge.
        :param pulumi.Input[pulumi.InputType['BridgeSourceBridgeFlowSourceArgs']] flow_source: Add a flow source to an existing bridge.
        :param pulumi.Input[str] name: The name of the source.
        :param pulumi.Input[pulumi.InputType['BridgeSourceBridgeNetworkSourceArgs']] network_source: Add a network source to an existing bridge.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BridgeSourceInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::MediaConnect::BridgeSource

        :param str resource_name: The name of the resource.
        :param BridgeSourceInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BridgeSourceInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_arn: Optional[pulumi.Input[str]] = None,
                 flow_source: Optional[pulumi.Input[pulumi.InputType['BridgeSourceBridgeFlowSourceArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_source: Optional[pulumi.Input[pulumi.InputType['BridgeSourceBridgeNetworkSourceArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BridgeSourceInitArgs.__new__(BridgeSourceInitArgs)

            if bridge_arn is None and not opts.urn:
                raise TypeError("Missing required property 'bridge_arn'")
            __props__.__dict__["bridge_arn"] = bridge_arn
            __props__.__dict__["flow_source"] = flow_source
            __props__.__dict__["name"] = name
            __props__.__dict__["network_source"] = network_source
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bridgeArn", "name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(BridgeSource, __self__).__init__(
            'aws-native:mediaconnect:BridgeSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BridgeSource':
        """
        Get an existing BridgeSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BridgeSourceInitArgs.__new__(BridgeSourceInitArgs)

        __props__.__dict__["bridge_arn"] = None
        __props__.__dict__["flow_source"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_source"] = None
        return BridgeSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bridgeArn")
    def bridge_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Number (ARN) of the bridge.
        """
        return pulumi.get(self, "bridge_arn")

    @property
    @pulumi.getter(name="flowSource")
    def flow_source(self) -> pulumi.Output[Optional['outputs.BridgeSourceBridgeFlowSource']]:
        """
        Add a flow source to an existing bridge.
        """
        return pulumi.get(self, "flow_source")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the source.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSource")
    def network_source(self) -> pulumi.Output[Optional['outputs.BridgeSourceBridgeNetworkSource']]:
        """
        Add a network source to an existing bridge.
        """
        return pulumi.get(self, "network_source")

