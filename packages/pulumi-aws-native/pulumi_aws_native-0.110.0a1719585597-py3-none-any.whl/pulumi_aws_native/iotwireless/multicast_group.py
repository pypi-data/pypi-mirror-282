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

__all__ = ['MulticastGroupArgs', 'MulticastGroup']

@pulumi.input_type
class MulticastGroupArgs:
    def __init__(__self__, *,
                 lo_ra_wan: pulumi.Input['MulticastGroupLoRaWanArgs'],
                 associate_wireless_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disassociate_wireless_device: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a MulticastGroup resource.
        :param pulumi.Input['MulticastGroupLoRaWanArgs'] lo_ra_wan: Multicast group LoRaWAN
        :param pulumi.Input[str] associate_wireless_device: Wireless device to associate. Only for update request.
        :param pulumi.Input[str] description: Multicast group description
        :param pulumi.Input[str] disassociate_wireless_device: Wireless device to disassociate. Only for update request.
        :param pulumi.Input[str] name: Name of Multicast group
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of key-value pairs that contain metadata for the Multicast group.
        """
        pulumi.set(__self__, "lo_ra_wan", lo_ra_wan)
        if associate_wireless_device is not None:
            pulumi.set(__self__, "associate_wireless_device", associate_wireless_device)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disassociate_wireless_device is not None:
            pulumi.set(__self__, "disassociate_wireless_device", disassociate_wireless_device)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="loRaWan")
    def lo_ra_wan(self) -> pulumi.Input['MulticastGroupLoRaWanArgs']:
        """
        Multicast group LoRaWAN
        """
        return pulumi.get(self, "lo_ra_wan")

    @lo_ra_wan.setter
    def lo_ra_wan(self, value: pulumi.Input['MulticastGroupLoRaWanArgs']):
        pulumi.set(self, "lo_ra_wan", value)

    @property
    @pulumi.getter(name="associateWirelessDevice")
    def associate_wireless_device(self) -> Optional[pulumi.Input[str]]:
        """
        Wireless device to associate. Only for update request.
        """
        return pulumi.get(self, "associate_wireless_device")

    @associate_wireless_device.setter
    def associate_wireless_device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associate_wireless_device", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Multicast group description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> Optional[pulumi.Input[str]]:
        """
        Wireless device to disassociate. Only for update request.
        """
        return pulumi.get(self, "disassociate_wireless_device")

    @disassociate_wireless_device.setter
    def disassociate_wireless_device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disassociate_wireless_device", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Multicast group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the Multicast group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class MulticastGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associate_wireless_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disassociate_wireless_device: Optional[pulumi.Input[str]] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['MulticastGroupLoRaWanArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Create and manage Multicast groups.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] associate_wireless_device: Wireless device to associate. Only for update request.
        :param pulumi.Input[str] description: Multicast group description
        :param pulumi.Input[str] disassociate_wireless_device: Wireless device to disassociate. Only for update request.
        :param pulumi.Input[pulumi.InputType['MulticastGroupLoRaWanArgs']] lo_ra_wan: Multicast group LoRaWAN
        :param pulumi.Input[str] name: Name of Multicast group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: A list of key-value pairs that contain metadata for the Multicast group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MulticastGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create and manage Multicast groups.

        :param str resource_name: The name of the resource.
        :param MulticastGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MulticastGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associate_wireless_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disassociate_wireless_device: Optional[pulumi.Input[str]] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['MulticastGroupLoRaWanArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MulticastGroupArgs.__new__(MulticastGroupArgs)

            __props__.__dict__["associate_wireless_device"] = associate_wireless_device
            __props__.__dict__["description"] = description
            __props__.__dict__["disassociate_wireless_device"] = disassociate_wireless_device
            if lo_ra_wan is None and not opts.urn:
                raise TypeError("Missing required property 'lo_ra_wan'")
            __props__.__dict__["lo_ra_wan"] = lo_ra_wan
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["status"] = None
        super(MulticastGroup, __self__).__init__(
            'aws-native:iotwireless:MulticastGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MulticastGroup':
        """
        Get an existing MulticastGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MulticastGroupArgs.__new__(MulticastGroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["associate_wireless_device"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["disassociate_wireless_device"] = None
        __props__.__dict__["lo_ra_wan"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return MulticastGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Multicast group arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associateWirelessDevice")
    def associate_wireless_device(self) -> pulumi.Output[Optional[str]]:
        """
        Wireless device to associate. Only for update request.
        """
        return pulumi.get(self, "associate_wireless_device")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        Multicast group id. Returned after successful create.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Multicast group description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> pulumi.Output[Optional[str]]:
        """
        Wireless device to disassociate. Only for update request.
        """
        return pulumi.get(self, "disassociate_wireless_device")

    @property
    @pulumi.getter(name="loRaWan")
    def lo_ra_wan(self) -> pulumi.Output['outputs.MulticastGroupLoRaWan']:
        """
        Multicast group LoRaWAN
        """
        return pulumi.get(self, "lo_ra_wan")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of Multicast group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Multicast group status. Returned after successful read.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of key-value pairs that contain metadata for the Multicast group.
        """
        return pulumi.get(self, "tags")

