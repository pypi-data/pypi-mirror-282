# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['VpcArgs', 'Vpc']

@pulumi.input_type
class VpcArgs:
    def __init__(__self__, *,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns_hostnames: Optional[pulumi.Input[bool]] = None,
                 enable_dns_support: Optional[pulumi.Input[bool]] = None,
                 instance_tenancy: Optional[pulumi.Input[str]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Vpc resource.
        :param pulumi.Input[str] cidr_block: The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0/16``. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18/18``, we modify it to ``100.68.0.0/18``.
                You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        :param pulumi.Input[bool] enable_dns_hostnames: Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
                You can only enable DNS hostnames if you've enabled DNS support.
        :param pulumi.Input[bool] enable_dns_support: Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        :param pulumi.Input[str] instance_tenancy: The allowed tenancy of instances launched into the VPC.
                 +  ``default``: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
                 +  ``dedicated``: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of ``host`` during instance launch. You cannot specify a tenancy of ``default`` during instance launch.
                 
                Updating ``InstanceTenancy`` requires no replacement only if you are updating its value from ``dedicated`` to ``default``. Updating ``InstanceTenancy`` from ``default`` to ``dedicated`` requires replacement.
        :param pulumi.Input[str] ipv4_ipam_pool_id: The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
                You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        :param pulumi.Input[int] ipv4_netmask_length: The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags for the VPC.
        """
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)
        if enable_dns_hostnames is not None:
            pulumi.set(__self__, "enable_dns_hostnames", enable_dns_hostnames)
        if enable_dns_support is not None:
            pulumi.set(__self__, "enable_dns_support", enable_dns_support)
        if instance_tenancy is not None:
            pulumi.set(__self__, "instance_tenancy", instance_tenancy)
        if ipv4_ipam_pool_id is not None:
            pulumi.set(__self__, "ipv4_ipam_pool_id", ipv4_ipam_pool_id)
        if ipv4_netmask_length is not None:
            pulumi.set(__self__, "ipv4_netmask_length", ipv4_netmask_length)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0/16``. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18/18``, we modify it to ``100.68.0.0/18``.
         You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        """
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter(name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
         You can only enable DNS hostnames if you've enabled DNS support.
        """
        return pulumi.get(self, "enable_dns_hostnames")

    @enable_dns_hostnames.setter
    def enable_dns_hostnames(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dns_hostnames", value)

    @property
    @pulumi.getter(name="enableDnsSupport")
    def enable_dns_support(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        """
        return pulumi.get(self, "enable_dns_support")

    @enable_dns_support.setter
    def enable_dns_support(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dns_support", value)

    @property
    @pulumi.getter(name="instanceTenancy")
    def instance_tenancy(self) -> Optional[pulumi.Input[str]]:
        """
        The allowed tenancy of instances launched into the VPC.
          +  ``default``: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
          +  ``dedicated``: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of ``host`` during instance launch. You cannot specify a tenancy of ``default`` during instance launch.
          
         Updating ``InstanceTenancy`` requires no replacement only if you are updating its value from ``dedicated`` to ``default``. Updating ``InstanceTenancy`` from ``default`` to ``dedicated`` requires replacement.
        """
        return pulumi.get(self, "instance_tenancy")

    @instance_tenancy.setter
    def instance_tenancy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_tenancy", value)

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
         You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        """
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_ipam_pool_id", value)

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> Optional[pulumi.Input[int]]:
        """
        The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        """
        return pulumi.get(self, "ipv4_netmask_length")

    @ipv4_netmask_length.setter
    def ipv4_netmask_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv4_netmask_length", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags for the VPC.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Vpc(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns_hostnames: Optional[pulumi.Input[bool]] = None,
                 enable_dns_support: Optional[pulumi.Input[bool]] = None,
                 instance_tenancy: Optional[pulumi.Input[str]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Specifies a virtual private cloud (VPC).
         You can optionally request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (BYOIP).
         For more information, see [Virtual private clouds (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html) in the *Amazon VPC User Guide*.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_block: The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0/16``. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18/18``, we modify it to ``100.68.0.0/18``.
                You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        :param pulumi.Input[bool] enable_dns_hostnames: Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
                You can only enable DNS hostnames if you've enabled DNS support.
        :param pulumi.Input[bool] enable_dns_support: Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        :param pulumi.Input[str] instance_tenancy: The allowed tenancy of instances launched into the VPC.
                 +  ``default``: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
                 +  ``dedicated``: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of ``host`` during instance launch. You cannot specify a tenancy of ``default`` during instance launch.
                 
                Updating ``InstanceTenancy`` requires no replacement only if you are updating its value from ``dedicated`` to ``default``. Updating ``InstanceTenancy`` from ``default`` to ``dedicated`` requires replacement.
        :param pulumi.Input[str] ipv4_ipam_pool_id: The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
                You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        :param pulumi.Input[int] ipv4_netmask_length: The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The tags for the VPC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VpcArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies a virtual private cloud (VPC).
         You can optionally request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (BYOIP).
         For more information, see [Virtual private clouds (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html) in the *Amazon VPC User Guide*.

        :param str resource_name: The name of the resource.
        :param VpcArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 enable_dns_hostnames: Optional[pulumi.Input[bool]] = None,
                 enable_dns_support: Optional[pulumi.Input[bool]] = None,
                 instance_tenancy: Optional[pulumi.Input[str]] = None,
                 ipv4_ipam_pool_id: Optional[pulumi.Input[str]] = None,
                 ipv4_netmask_length: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcArgs.__new__(VpcArgs)

            __props__.__dict__["cidr_block"] = cidr_block
            __props__.__dict__["enable_dns_hostnames"] = enable_dns_hostnames
            __props__.__dict__["enable_dns_support"] = enable_dns_support
            __props__.__dict__["instance_tenancy"] = instance_tenancy
            __props__.__dict__["ipv4_ipam_pool_id"] = ipv4_ipam_pool_id
            __props__.__dict__["ipv4_netmask_length"] = ipv4_netmask_length
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cidr_block_associations"] = None
            __props__.__dict__["default_network_acl"] = None
            __props__.__dict__["default_security_group"] = None
            __props__.__dict__["ipv6_cidr_blocks"] = None
            __props__.__dict__["vpc_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["cidrBlock", "ipv4IpamPoolId", "ipv4NetmaskLength"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Vpc, __self__).__init__(
            'aws-native:ec2:Vpc',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Vpc':
        """
        Get an existing Vpc resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpcArgs.__new__(VpcArgs)

        __props__.__dict__["cidr_block"] = None
        __props__.__dict__["cidr_block_associations"] = None
        __props__.__dict__["default_network_acl"] = None
        __props__.__dict__["default_security_group"] = None
        __props__.__dict__["enable_dns_hostnames"] = None
        __props__.__dict__["enable_dns_support"] = None
        __props__.__dict__["instance_tenancy"] = None
        __props__.__dict__["ipv4_ipam_pool_id"] = None
        __props__.__dict__["ipv4_netmask_length"] = None
        __props__.__dict__["ipv6_cidr_blocks"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_id"] = None
        return Vpc(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0/16``. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18/18``, we modify it to ``100.68.0.0/18``.
         You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="cidrBlockAssociations")
    def cidr_block_associations(self) -> pulumi.Output[Sequence[str]]:
        """
        The association IDs of the IPv4 CIDR blocks for the VPC. For example, [ vpc-cidr-assoc-0280ab6b ].
        """
        return pulumi.get(self, "cidr_block_associations")

    @property
    @pulumi.getter(name="defaultNetworkAcl")
    def default_network_acl(self) -> pulumi.Output[str]:
        """
        The ID of the default network ACL for the VPC. For example, acl-814dafe3.
        """
        return pulumi.get(self, "default_network_acl")

    @property
    @pulumi.getter(name="defaultSecurityGroup")
    def default_security_group(self) -> pulumi.Output[str]:
        """
        The ID of the default security group for the VPC. For example, sg-b178e0d3.
        """
        return pulumi.get(self, "default_security_group")

    @property
    @pulumi.getter(name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
         You can only enable DNS hostnames if you've enabled DNS support.
        """
        return pulumi.get(self, "enable_dns_hostnames")

    @property
    @pulumi.getter(name="enableDnsSupport")
    def enable_dns_support(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        """
        return pulumi.get(self, "enable_dns_support")

    @property
    @pulumi.getter(name="instanceTenancy")
    def instance_tenancy(self) -> pulumi.Output[Optional[str]]:
        """
        The allowed tenancy of instances launched into the VPC.
          +  ``default``: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
          +  ``dedicated``: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of ``host`` during instance launch. You cannot specify a tenancy of ``default`` during instance launch.
          
         Updating ``InstanceTenancy`` requires no replacement only if you are updating its value from ``dedicated`` to ``default``. Updating ``InstanceTenancy`` from ``default`` to ``dedicated`` requires replacement.
        """
        return pulumi.get(self, "instance_tenancy")

    @property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
         You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        """
        return pulumi.get(self, "ipv4_ipam_pool_id")

    @property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> pulumi.Output[Optional[int]]:
        """
        The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        """
        return pulumi.get(self, "ipv4_netmask_length")

    @property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> pulumi.Output[Sequence[str]]:
        """
        The IPv6 CIDR blocks for the VPC. For example, [ 2001:db8:1234:1a00::/56 ].
        """
        return pulumi.get(self, "ipv6_cidr_blocks")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags for the VPC.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC.
        """
        return pulumi.get(self, "vpc_id")

