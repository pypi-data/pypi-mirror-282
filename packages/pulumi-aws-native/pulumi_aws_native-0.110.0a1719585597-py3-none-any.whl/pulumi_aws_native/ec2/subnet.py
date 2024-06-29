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

__all__ = ['SubnetArgs', 'Subnet']

@pulumi.input_type
class SubnetArgs:
    def __init__(__self__, *,
                 vpc_id: pulumi.Input[str],
                 assign_ipv6_address_on_creation: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns64: Optional[pulumi.Input[bool]] = None,
                 enable_lni_at_device_index: Optional[pulumi.Input[int]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_native: Optional[pulumi.Input[bool]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 private_dns_name_options_on_launch: Optional[pulumi.Input['PrivateDnsNameOptionsOnLaunchPropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Subnet resource.
        :param pulumi.Input[str] vpc_id: The ID of the VPC the subnet is in.
                If you update this property, you must also update the ``CidrBlock`` property.
        :param pulumi.Input[bool] assign_ipv6_address_on_creation: Indicates whether a network interface created in this subnet receives an IPv6 address. The default value is ``false``.
                If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        :param pulumi.Input[str] availability_zone: The Availability Zone of the subnet.
                If you update this property, you must also update the ``CidrBlock`` property.
        :param pulumi.Input[str] availability_zone_id: The AZ ID of the subnet.
        :param pulumi.Input[str] cidr_block: The IPv4 CIDR block assigned to the subnet.
                If you update this property, we create a new subnet, and then delete the existing one.
        :param pulumi.Input[bool] enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. For more information, see [DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-nat64-dns64) in the *User Guide*.
        :param pulumi.Input[int] enable_lni_at_device_index: Indicates the device position for local network interfaces in this subnet. For example, ``1`` indicates local network interfaces in this subnet are the secondary network interface (eth1).
        :param pulumi.Input[str] ipv4_ipam_pool_id: An IPv4 IPAM pool ID for the subnet.
        :param pulumi.Input[int] ipv4_netmask_length: An IPv4 netmask length for the subnet.
        :param pulumi.Input[str] ipv6_cidr_block: The IPv6 CIDR block.
                If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ipv6_cidr_blocks: The IPv6 network ranges for the subnet, in CIDR notation.
        :param pulumi.Input[str] ipv6_ipam_pool_id: An IPv6 IPAM pool ID for the subnet.
        :param pulumi.Input[bool] ipv6_native: Indicates whether this is an IPv6 only subnet. For more information, see [Subnet basics](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#subnet-basics) in the *User Guide*.
        :param pulumi.Input[int] ipv6_netmask_length: An IPv6 netmask length for the subnet.
        :param pulumi.Input[bool] map_public_ip_on_launch: Indicates whether instances launched in this subnet receive a public IPv4 address. The default value is ``false``.
                 AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [VPC pricing page](https://docs.aws.amazon.com/vpc/pricing/).
        :param pulumi.Input[str] outpost_arn: The Amazon Resource Name (ARN) of the Outpost.
        :param pulumi.Input['PrivateDnsNameOptionsOnLaunchPropertiesArgs'] private_dns_name_options_on_launch: The hostname type for EC2 instances launched into this subnet and how DNS A and AAAA record queries to the instances should be handled. For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *User Guide*.
                Available options:
                 +  EnableResourceNameDnsAAAARecord (true | false)
                 +  EnableResourceNameDnsARecord (true | false)
                 +  HostnameType (ip-name | resource-name)
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Any tags assigned to the subnet.
        """
        pulumi.set(__self__, "vpc_id", vpc_id)
        if assign_ipv6_address_on_creation is not None:
            pulumi.set(__self__, "assign_ipv6_address_on_creation", assign_ipv6_address_on_creation)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if availability_zone_id is not None:
            pulumi.set(__self__, "availability_zone_id", availability_zone_id)
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)
        if enable_dns64 is not None:
            pulumi.set(__self__, "enable_dns64", enable_dns64)
        if enable_lni_at_device_index is not None:
            pulumi.set(__self__, "enable_lni_at_device_index", enable_lni_at_device_index)
        if ipv4_ipam_pool_id is not None:
            pulumi.set(__self__, "ipv4_ipam_pool_id", ipv4_ipam_pool_id)
        if ipv4_netmask_length is not None:
            pulumi.set(__self__, "ipv4_netmask_length", ipv4_netmask_length)
        if ipv6_cidr_block is not None:
            pulumi.set(__self__, "ipv6_cidr_block", ipv6_cidr_block)
        if ipv6_cidr_blocks is not None:
            pulumi.set(__self__, "ipv6_cidr_blocks", ipv6_cidr_blocks)
        if ipv6_ipam_pool_id is not None:
            pulumi.set(__self__, "ipv6_ipam_pool_id", ipv6_ipam_pool_id)
        if ipv6_native is not None:
            pulumi.set(__self__, "ipv6_native", ipv6_native)
        if ipv6_netmask_length is not None:
            pulumi.set(__self__, "ipv6_netmask_length", ipv6_netmask_length)
        if map_public_ip_on_launch is not None:
            pulumi.set(__self__, "map_public_ip_on_launch", map_public_ip_on_launch)
        if outpost_arn is not None:
            pulumi.set(__self__, "outpost_arn", outpost_arn)
        if private_dns_name_options_on_launch is not None:
            pulumi.set(__self__, "private_dns_name_options_on_launch", private_dns_name_options_on_launch)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPC the subnet is in.
         If you update this property, you must also update the ``CidrBlock`` property.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether a network interface created in this subnet receives an IPv6 address. The default value is ``false``.
         If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        """
        return pulumi.get(self, "assign_ipv6_address_on_creation")

    @assign_ipv6_address_on_creation.setter
    def assign_ipv6_address_on_creation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "assign_ipv6_address_on_creation", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The Availability Zone of the subnet.
         If you update this property, you must also update the ``CidrBlock`` property.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AZ ID of the subnet.
        """
        return pulumi.get(self, "availability_zone_id")

    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone_id", value)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 CIDR block assigned to the subnet.
         If you update this property, we create a new subnet, and then delete the existing one.
        """
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. For more information, see [DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-nat64-dns64) in the *User Guide*.
        """
        return pulumi.get(self, "enable_dns64")

    @enable_dns64.setter
    def enable_dns64(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dns64", value)

    @property
    @pulumi.getter(name="enableLniAtDeviceIndex")
    def enable_lni_at_device_index(self) -> Optional[pulumi.Input[int]]:
        """
        Indicates the device position for local network interfaces in this subnet. For example, ``1`` indicates local network interfaces in this subnet are the secondary network interface (eth1).
        """
        return pulumi.get(self, "enable_lni_at_device_index")

    @enable_lni_at_device_index.setter
    def enable_lni_at_device_index(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "enable_lni_at_device_index", value)

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        An IPv4 IPAM pool ID for the subnet.
        """
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_ipam_pool_id", value)

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        An IPv4 netmask length for the subnet.
        """
        return pulumi.get(self, "ipv4_netmask_length")

    @ipv4_netmask_length.setter
    def ipv4_netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv4_netmask_length", value)

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 CIDR block.
         If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        """
        return pulumi.get(self, "ipv6_cidr_block")

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_cidr_block", value)

    @property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The IPv6 network ranges for the subnet, in CIDR notation.
        """
        return pulumi.get(self, "ipv6_cidr_blocks")

    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ipv6_cidr_blocks", value)

    @property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        An IPv6 IPAM pool ID for the subnet.
        """
        return pulumi.get(self, "ipv6_ipam_pool_id")

    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_ipam_pool_id", value)

    @property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this is an IPv6 only subnet. For more information, see [Subnet basics](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#subnet-basics) in the *User Guide*.
        """
        return pulumi.get(self, "ipv6_native")

    @ipv6_native.setter
    def ipv6_native(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ipv6_native", value)

    @property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        An IPv6 netmask length for the subnet.
        """
        return pulumi.get(self, "ipv6_netmask_length")

    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv6_netmask_length", value)

    @property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether instances launched in this subnet receive a public IPv4 address. The default value is ``false``.
          AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [VPC pricing page](https://docs.aws.amazon.com/vpc/pricing/).
        """
        return pulumi.get(self, "map_public_ip_on_launch")

    @map_public_ip_on_launch.setter
    def map_public_ip_on_launch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "map_public_ip_on_launch", value)

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the Outpost.
        """
        return pulumi.get(self, "outpost_arn")

    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outpost_arn", value)

    @property
    @pulumi.getter(name="privateDnsNameOptionsOnLaunch")
    def private_dns_name_options_on_launch(self) -> Optional[pulumi.Input['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]:
        """
        The hostname type for EC2 instances launched into this subnet and how DNS A and AAAA record queries to the instances should be handled. For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *User Guide*.
         Available options:
          +  EnableResourceNameDnsAAAARecord (true | false)
          +  EnableResourceNameDnsARecord (true | false)
          +  HostnameType (ip-name | resource-name)
        """
        return pulumi.get(self, "private_dns_name_options_on_launch")

    @private_dns_name_options_on_launch.setter
    def private_dns_name_options_on_launch(self, value: Optional[pulumi.Input['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]):
        pulumi.set(self, "private_dns_name_options_on_launch", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Any tags assigned to the subnet.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Subnet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assign_ipv6_address_on_creation: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns64: Optional[pulumi.Input[bool]] = None,
                 enable_lni_at_device_index: Optional[pulumi.Input[int]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_native: Optional[pulumi.Input[bool]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 private_dns_name_options_on_launch: Optional[pulumi.Input[pulumi.InputType['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Specifies a subnet for the specified VPC.
         For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block.
         For more information, see [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] assign_ipv6_address_on_creation: Indicates whether a network interface created in this subnet receives an IPv6 address. The default value is ``false``.
                If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        :param pulumi.Input[str] availability_zone: The Availability Zone of the subnet.
                If you update this property, you must also update the ``CidrBlock`` property.
        :param pulumi.Input[str] availability_zone_id: The AZ ID of the subnet.
        :param pulumi.Input[str] cidr_block: The IPv4 CIDR block assigned to the subnet.
                If you update this property, we create a new subnet, and then delete the existing one.
        :param pulumi.Input[bool] enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. For more information, see [DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-nat64-dns64) in the *User Guide*.
        :param pulumi.Input[int] enable_lni_at_device_index: Indicates the device position for local network interfaces in this subnet. For example, ``1`` indicates local network interfaces in this subnet are the secondary network interface (eth1).
        :param pulumi.Input[str] ipv4_ipam_pool_id: An IPv4 IPAM pool ID for the subnet.
        :param pulumi.Input[int] ipv4_netmask_length: An IPv4 netmask length for the subnet.
        :param pulumi.Input[str] ipv6_cidr_block: The IPv6 CIDR block.
                If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ipv6_cidr_blocks: The IPv6 network ranges for the subnet, in CIDR notation.
        :param pulumi.Input[str] ipv6_ipam_pool_id: An IPv6 IPAM pool ID for the subnet.
        :param pulumi.Input[bool] ipv6_native: Indicates whether this is an IPv6 only subnet. For more information, see [Subnet basics](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#subnet-basics) in the *User Guide*.
        :param pulumi.Input[int] ipv6_netmask_length: An IPv6 netmask length for the subnet.
        :param pulumi.Input[bool] map_public_ip_on_launch: Indicates whether instances launched in this subnet receive a public IPv4 address. The default value is ``false``.
                 AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [VPC pricing page](https://docs.aws.amazon.com/vpc/pricing/).
        :param pulumi.Input[str] outpost_arn: The Amazon Resource Name (ARN) of the Outpost.
        :param pulumi.Input[pulumi.InputType['PrivateDnsNameOptionsOnLaunchPropertiesArgs']] private_dns_name_options_on_launch: The hostname type for EC2 instances launched into this subnet and how DNS A and AAAA record queries to the instances should be handled. For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *User Guide*.
                Available options:
                 +  EnableResourceNameDnsAAAARecord (true | false)
                 +  EnableResourceNameDnsARecord (true | false)
                 +  HostnameType (ip-name | resource-name)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: Any tags assigned to the subnet.
        :param pulumi.Input[str] vpc_id: The ID of the VPC the subnet is in.
                If you update this property, you must also update the ``CidrBlock`` property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubnetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies a subnet for the specified VPC.
         For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block.
         For more information, see [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.

        :param str resource_name: The name of the resource.
        :param SubnetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubnetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assign_ipv6_address_on_creation: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns64: Optional[pulumi.Input[bool]] = None,
                 enable_lni_at_device_index: Optional[pulumi.Input[int]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ipv6_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv6_native: Optional[pulumi.Input[bool]] = None,
                 ipv6_netmask_length: Optional[pulumi.Input[int]] = None,
                 map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 private_dns_name_options_on_launch: Optional[pulumi.Input[pulumi.InputType['PrivateDnsNameOptionsOnLaunchPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubnetArgs.__new__(SubnetArgs)

            __props__.__dict__["assign_ipv6_address_on_creation"] = assign_ipv6_address_on_creation
            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["availability_zone_id"] = availability_zone_id
            __props__.__dict__["cidr_block"] = cidr_block
            __props__.__dict__["enable_dns64"] = enable_dns64
            __props__.__dict__["enable_lni_at_device_index"] = enable_lni_at_device_index
            __props__.__dict__["ipv4_ipam_pool_id"] = ipv4_ipam_pool_id
            __props__.__dict__["ipv4_netmask_length"] = ipv4_netmask_length
            __props__.__dict__["ipv6_cidr_block"] = ipv6_cidr_block
            __props__.__dict__["ipv6_cidr_blocks"] = ipv6_cidr_blocks
            __props__.__dict__["ipv6_ipam_pool_id"] = ipv6_ipam_pool_id
            __props__.__dict__["ipv6_native"] = ipv6_native
            __props__.__dict__["ipv6_netmask_length"] = ipv6_netmask_length
            __props__.__dict__["map_public_ip_on_launch"] = map_public_ip_on_launch
            __props__.__dict__["outpost_arn"] = outpost_arn
            __props__.__dict__["private_dns_name_options_on_launch"] = private_dns_name_options_on_launch
            __props__.__dict__["tags"] = tags
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["network_acl_association_id"] = None
            __props__.__dict__["subnet_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["availabilityZone", "availabilityZoneId", "cidrBlock", "ipv4IpamPoolId", "ipv4NetmaskLength", "ipv6IpamPoolId", "ipv6Native", "ipv6NetmaskLength", "outpostArn", "vpcId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Subnet, __self__).__init__(
            'aws-native:ec2:Subnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subnet':
        """
        Get an existing Subnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubnetArgs.__new__(SubnetArgs)

        __props__.__dict__["assign_ipv6_address_on_creation"] = None
        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["availability_zone_id"] = None
        __props__.__dict__["cidr_block"] = None
        __props__.__dict__["enable_dns64"] = None
        __props__.__dict__["enable_lni_at_device_index"] = None
        __props__.__dict__["ipv4_ipam_pool_id"] = None
        __props__.__dict__["ipv4_netmask_length"] = None
        __props__.__dict__["ipv6_cidr_block"] = None
        __props__.__dict__["ipv6_cidr_blocks"] = None
        __props__.__dict__["ipv6_ipam_pool_id"] = None
        __props__.__dict__["ipv6_native"] = None
        __props__.__dict__["ipv6_netmask_length"] = None
        __props__.__dict__["map_public_ip_on_launch"] = None
        __props__.__dict__["network_acl_association_id"] = None
        __props__.__dict__["outpost_arn"] = None
        __props__.__dict__["private_dns_name_options_on_launch"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_id"] = None
        return Subnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether a network interface created in this subnet receives an IPv6 address. The default value is ``false``.
         If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        """
        return pulumi.get(self, "assign_ipv6_address_on_creation")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        The Availability Zone of the subnet.
         If you update this property, you must also update the ``CidrBlock`` property.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The AZ ID of the subnet.
        """
        return pulumi.get(self, "availability_zone_id")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv4 CIDR block assigned to the subnet.
         If you update this property, we create a new subnet, and then delete the existing one.
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. For more information, see [DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-nat64-dns64) in the *User Guide*.
        """
        return pulumi.get(self, "enable_dns64")

    @property
    @pulumi.getter(name="enableLniAtDeviceIndex")
    def enable_lni_at_device_index(self) -> pulumi.Output[Optional[int]]:
        """
        Indicates the device position for local network interfaces in this subnet. For example, ``1`` indicates local network interfaces in this subnet are the secondary network interface (eth1).
        """
        return pulumi.get(self, "enable_lni_at_device_index")

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        An IPv4 IPAM pool ID for the subnet.
        """
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        An IPv4 netmask length for the subnet.
        """
        return pulumi.get(self, "ipv4_netmask_length")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv6 CIDR block.
         If you specify ``AssignIpv6AddressOnCreation``, you must also specify an IPv6 CIDR block.
        """
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The IPv6 network ranges for the subnet, in CIDR notation.
        """
        return pulumi.get(self, "ipv6_cidr_blocks")

    @property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        An IPv6 IPAM pool ID for the subnet.
        """
        return pulumi.get(self, "ipv6_ipam_pool_id")

    @property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether this is an IPv6 only subnet. For more information, see [Subnet basics](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#subnet-basics) in the *User Guide*.
        """
        return pulumi.get(self, "ipv6_native")

    @property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        An IPv6 netmask length for the subnet.
        """
        return pulumi.get(self, "ipv6_netmask_length")

    @property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether instances launched in this subnet receive a public IPv4 address. The default value is ``false``.
          AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [VPC pricing page](https://docs.aws.amazon.com/vpc/pricing/).
        """
        return pulumi.get(self, "map_public_ip_on_launch")

    @property
    @pulumi.getter(name="networkAclAssociationId")
    def network_acl_association_id(self) -> pulumi.Output[str]:
        """
        The ID of the network ACL that is associated with the subnet's VPC, such as `acl-5fb85d36` .
        """
        return pulumi.get(self, "network_acl_association_id")

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the Outpost.
        """
        return pulumi.get(self, "outpost_arn")

    @property
    @pulumi.getter(name="privateDnsNameOptionsOnLaunch")
    def private_dns_name_options_on_launch(self) -> pulumi.Output[Optional['outputs.PrivateDnsNameOptionsOnLaunchProperties']]:
        """
        The hostname type for EC2 instances launched into this subnet and how DNS A and AAAA record queries to the instances should be handled. For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *User Guide*.
         Available options:
          +  EnableResourceNameDnsAAAARecord (true | false)
          +  EnableResourceNameDnsARecord (true | false)
          +  HostnameType (ip-name | resource-name)
        """
        return pulumi.get(self, "private_dns_name_options_on_launch")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Any tags assigned to the subnet.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC the subnet is in.
         If you update this property, you must also update the ``CidrBlock`` property.
        """
        return pulumi.get(self, "vpc_id")

