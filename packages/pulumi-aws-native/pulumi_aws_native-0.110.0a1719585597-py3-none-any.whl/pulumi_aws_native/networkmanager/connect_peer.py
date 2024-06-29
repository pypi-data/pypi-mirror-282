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

__all__ = ['ConnectPeerArgs', 'ConnectPeer']

@pulumi.input_type
class ConnectPeerArgs:
    def __init__(__self__, *,
                 connect_attachment_id: pulumi.Input[str],
                 peer_address: pulumi.Input[str],
                 bgp_options: Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']] = None,
                 core_network_address: Optional[pulumi.Input[str]] = None,
                 inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ConnectPeer resource.
        :param pulumi.Input[str] connect_attachment_id: The ID of the attachment to connect.
        :param pulumi.Input[str] peer_address: The IP address of the Connect peer.
        :param pulumi.Input['ConnectPeerBgpOptionsArgs'] bgp_options: Bgp options for connect peer.
        :param pulumi.Input[str] core_network_address: The IP address of a core network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
        :param pulumi.Input[str] subnet_arn: The subnet ARN for the connect peer.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "connect_attachment_id", connect_attachment_id)
        pulumi.set(__self__, "peer_address", peer_address)
        if bgp_options is not None:
            pulumi.set(__self__, "bgp_options", bgp_options)
        if core_network_address is not None:
            pulumi.set(__self__, "core_network_address", core_network_address)
        if inside_cidr_blocks is not None:
            pulumi.set(__self__, "inside_cidr_blocks", inside_cidr_blocks)
        if subnet_arn is not None:
            pulumi.set(__self__, "subnet_arn", subnet_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> pulumi.Input[str]:
        """
        The ID of the attachment to connect.
        """
        return pulumi.get(self, "connect_attachment_id")

    @connect_attachment_id.setter
    def connect_attachment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "connect_attachment_id", value)

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Input[str]:
        """
        The IP address of the Connect peer.
        """
        return pulumi.get(self, "peer_address")

    @peer_address.setter
    def peer_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_address", value)

    @property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']]:
        """
        Bgp options for connect peer.
        """
        return pulumi.get(self, "bgp_options")

    @bgp_options.setter
    def bgp_options(self, value: Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']]):
        pulumi.set(self, "bgp_options", value)

    @property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of a core network.
        """
        return pulumi.get(self, "core_network_address")

    @core_network_address.setter
    def core_network_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "core_network_address", value)

    @property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The inside IP addresses used for a Connect peer configuration.
        """
        return pulumi.get(self, "inside_cidr_blocks")

    @inside_cidr_blocks.setter
    def inside_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "inside_cidr_blocks", value)

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The subnet ARN for the connect peer.
        """
        return pulumi.get(self, "subnet_arn")

    @subnet_arn.setter
    def subnet_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_arn", value)

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


class ConnectPeer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_options: Optional[pulumi.Input[pulumi.InputType['ConnectPeerBgpOptionsArgs']]] = None,
                 connect_attachment_id: Optional[pulumi.Input[str]] = None,
                 core_network_address: Optional[pulumi.Input[str]] = None,
                 inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 peer_address: Optional[pulumi.Input[str]] = None,
                 subnet_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        AWS::NetworkManager::ConnectPeer Resource Type Definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConnectPeerBgpOptionsArgs']] bgp_options: Bgp options for connect peer.
        :param pulumi.Input[str] connect_attachment_id: The ID of the attachment to connect.
        :param pulumi.Input[str] core_network_address: The IP address of a core network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
        :param pulumi.Input[str] peer_address: The IP address of the Connect peer.
        :param pulumi.Input[str] subnet_arn: The subnet ARN for the connect peer.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectPeerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::NetworkManager::ConnectPeer Resource Type Definition.

        :param str resource_name: The name of the resource.
        :param ConnectPeerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectPeerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_options: Optional[pulumi.Input[pulumi.InputType['ConnectPeerBgpOptionsArgs']]] = None,
                 connect_attachment_id: Optional[pulumi.Input[str]] = None,
                 core_network_address: Optional[pulumi.Input[str]] = None,
                 inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 peer_address: Optional[pulumi.Input[str]] = None,
                 subnet_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectPeerArgs.__new__(ConnectPeerArgs)

            __props__.__dict__["bgp_options"] = bgp_options
            if connect_attachment_id is None and not opts.urn:
                raise TypeError("Missing required property 'connect_attachment_id'")
            __props__.__dict__["connect_attachment_id"] = connect_attachment_id
            __props__.__dict__["core_network_address"] = core_network_address
            __props__.__dict__["inside_cidr_blocks"] = inside_cidr_blocks
            if peer_address is None and not opts.urn:
                raise TypeError("Missing required property 'peer_address'")
            __props__.__dict__["peer_address"] = peer_address
            __props__.__dict__["subnet_arn"] = subnet_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["configuration"] = None
            __props__.__dict__["connect_peer_id"] = None
            __props__.__dict__["core_network_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["edge_location"] = None
            __props__.__dict__["state"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bgpOptions", "connectAttachmentId", "coreNetworkAddress", "insideCidrBlocks[*]", "peerAddress", "subnetArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ConnectPeer, __self__).__init__(
            'aws-native:networkmanager:ConnectPeer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectPeer':
        """
        Get an existing ConnectPeer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectPeerArgs.__new__(ConnectPeerArgs)

        __props__.__dict__["bgp_options"] = None
        __props__.__dict__["configuration"] = None
        __props__.__dict__["connect_attachment_id"] = None
        __props__.__dict__["connect_peer_id"] = None
        __props__.__dict__["core_network_address"] = None
        __props__.__dict__["core_network_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["edge_location"] = None
        __props__.__dict__["inside_cidr_blocks"] = None
        __props__.__dict__["peer_address"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["subnet_arn"] = None
        __props__.__dict__["tags"] = None
        return ConnectPeer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> pulumi.Output[Optional['outputs.ConnectPeerBgpOptions']]:
        """
        Bgp options for connect peer.
        """
        return pulumi.get(self, "bgp_options")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output['outputs.ConnectPeerConfiguration']:
        """
        Configuration of the connect peer.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> pulumi.Output[str]:
        """
        The ID of the attachment to connect.
        """
        return pulumi.get(self, "connect_attachment_id")

    @property
    @pulumi.getter(name="connectPeerId")
    def connect_peer_id(self) -> pulumi.Output[str]:
        """
        The ID of the Connect peer.
        """
        return pulumi.get(self, "connect_peer_id")

    @property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> pulumi.Output[Optional[str]]:
        """
        The IP address of a core network.
        """
        return pulumi.get(self, "core_network_address")

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[str]:
        """
        The ID of the core network.
        """
        return pulumi.get(self, "core_network_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Connect peer creation time.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[str]:
        """
        The Connect peer Regions where edges are located.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The inside IP addresses used for a Connect peer configuration.
        """
        return pulumi.get(self, "inside_cidr_blocks")

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Output[str]:
        """
        The IP address of the Connect peer.
        """
        return pulumi.get(self, "peer_address")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the connect peer.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The subnet ARN for the connect peer.
        """
        return pulumi.get(self, "subnet_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

