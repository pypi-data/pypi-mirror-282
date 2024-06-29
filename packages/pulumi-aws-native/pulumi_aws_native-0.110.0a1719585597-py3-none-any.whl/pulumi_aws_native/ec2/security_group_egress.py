# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecurityGroupEgressInitArgs', 'SecurityGroupEgress']

@pulumi.input_type
class SecurityGroupEgressInitArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 ip_protocol: pulumi.Input[str],
                 cidr_ip: Optional[pulumi.Input[str]] = None,
                 cidr_ipv6: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_prefix_list_id: Optional[pulumi.Input[str]] = None,
                 destination_security_group_id: Optional[pulumi.Input[str]] = None,
                 from_port: Optional[pulumi.Input[int]] = None,
                 to_port: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SecurityGroupEgress resource.
        :param pulumi.Input[str] group_id: The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
        :param pulumi.Input[str] ip_protocol: The IP protocol name (``tcp``, ``udp``, ``icmp``, ``icmpv6``) or number (see [Protocol Numbers](https://docs.aws.amazon.com/http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
                Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp``, ``udp``, ``icmp``, or ``icmpv6`` allows traffic on all ports, regardless of any port range you specify. For ``tcp``, ``udp``, and ``icmp``, you must specify a port range. For ``icmpv6``, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
        :param pulumi.Input[str] cidr_ip: The IPv4 address range, in CIDR format.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
                For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        :param pulumi.Input[str] cidr_ipv6: The IPv6 address range, in CIDR format.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
                For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        :param pulumi.Input[str] description: The description of an egress (outbound) security group rule.
                Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        :param pulumi.Input[str] destination_prefix_list_id: The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        :param pulumi.Input[str] destination_security_group_id: The ID of the security group.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        :param pulumi.Input[int] from_port: If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
        :param pulumi.Input[int] to_port: If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "ip_protocol", ip_protocol)
        if cidr_ip is not None:
            pulumi.set(__self__, "cidr_ip", cidr_ip)
        if cidr_ipv6 is not None:
            pulumi.set(__self__, "cidr_ipv6", cidr_ipv6)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination_prefix_list_id is not None:
            pulumi.set(__self__, "destination_prefix_list_id", destination_prefix_list_id)
        if destination_security_group_id is not None:
            pulumi.set(__self__, "destination_security_group_id", destination_security_group_id)
        if from_port is not None:
            pulumi.set(__self__, "from_port", from_port)
        if to_port is not None:
            pulumi.set(__self__, "to_port", to_port)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[str]:
        """
        The IP protocol name (``tcp``, ``udp``, ``icmp``, ``icmpv6``) or number (see [Protocol Numbers](https://docs.aws.amazon.com/http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
         Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp``, ``udp``, ``icmp``, or ``icmpv6`` allows traffic on all ports, regardless of any port range you specify. For ``tcp``, ``udp``, and ``icmp``, you must specify a port range. For ``icmpv6``, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
        """
        return pulumi.get(self, "ip_protocol")

    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_protocol", value)

    @property
    @pulumi.getter(name="cidrIp")
    def cidr_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address range, in CIDR format.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
         For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        """
        return pulumi.get(self, "cidr_ip")

    @cidr_ip.setter
    def cidr_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_ip", value)

    @property
    @pulumi.getter(name="cidrIpv6")
    def cidr_ipv6(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 address range, in CIDR format.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
         For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        """
        return pulumi.get(self, "cidr_ipv6")

    @cidr_ipv6.setter
    def cidr_ipv6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_ipv6", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of an egress (outbound) security group rule.
         Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        """
        return pulumi.get(self, "destination_prefix_list_id")

    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_prefix_list_id", value)

    @property
    @pulumi.getter(name="destinationSecurityGroupId")
    def destination_security_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the security group.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        """
        return pulumi.get(self, "destination_security_group_id")

    @destination_security_group_id.setter
    def destination_security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_security_group_id", value)

    @property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[int]]:
        """
        If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
        """
        return pulumi.get(self, "from_port")

    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "from_port", value)

    @property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[int]]:
        """
        If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
        """
        return pulumi.get(self, "to_port")

    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "to_port", value)


class SecurityGroupEgress(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_ip: Optional[pulumi.Input[str]] = None,
                 cidr_ipv6: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_prefix_list_id: Optional[pulumi.Input[str]] = None,
                 destination_security_group_id: Optional[pulumi.Input[str]] = None,
                 from_port: Optional[pulumi.Input[int]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 to_port: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Adds the specified outbound (egress) rule to a security group.
         An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).
         You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.
         You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code. To specify all types or all codes, use -1.
         Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_ip: The IPv4 address range, in CIDR format.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
                For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        :param pulumi.Input[str] cidr_ipv6: The IPv6 address range, in CIDR format.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
                For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        :param pulumi.Input[str] description: The description of an egress (outbound) security group rule.
                Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        :param pulumi.Input[str] destination_prefix_list_id: The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        :param pulumi.Input[str] destination_security_group_id: The ID of the security group.
                You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        :param pulumi.Input[int] from_port: If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
        :param pulumi.Input[str] group_id: The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
        :param pulumi.Input[str] ip_protocol: The IP protocol name (``tcp``, ``udp``, ``icmp``, ``icmpv6``) or number (see [Protocol Numbers](https://docs.aws.amazon.com/http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
                Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp``, ``udp``, ``icmp``, or ``icmpv6`` allows traffic on all ports, regardless of any port range you specify. For ``tcp``, ``udp``, and ``icmp``, you must specify a port range. For ``icmpv6``, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
        :param pulumi.Input[int] to_port: If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityGroupEgressInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Adds the specified outbound (egress) rule to a security group.
         An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address range, the IP addresses that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).
         You must specify exactly one of the following destinations: an IPv4 address range, an IPv6 address range, a prefix list, or a security group.
         You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code. To specify all types or all codes, use -1.
         Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.

        :param str resource_name: The name of the resource.
        :param SecurityGroupEgressInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityGroupEgressInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_ip: Optional[pulumi.Input[str]] = None,
                 cidr_ipv6: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_prefix_list_id: Optional[pulumi.Input[str]] = None,
                 destination_security_group_id: Optional[pulumi.Input[str]] = None,
                 from_port: Optional[pulumi.Input[int]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 to_port: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityGroupEgressInitArgs.__new__(SecurityGroupEgressInitArgs)

            __props__.__dict__["cidr_ip"] = cidr_ip
            __props__.__dict__["cidr_ipv6"] = cidr_ipv6
            __props__.__dict__["description"] = description
            __props__.__dict__["destination_prefix_list_id"] = destination_prefix_list_id
            __props__.__dict__["destination_security_group_id"] = destination_security_group_id
            __props__.__dict__["from_port"] = from_port
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if ip_protocol is None and not opts.urn:
                raise TypeError("Missing required property 'ip_protocol'")
            __props__.__dict__["ip_protocol"] = ip_protocol
            __props__.__dict__["to_port"] = to_port
            __props__.__dict__["aws_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["cidrIp", "cidrIpv6", "destinationPrefixListId", "destinationSecurityGroupId", "fromPort", "groupId", "ipProtocol", "toPort"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SecurityGroupEgress, __self__).__init__(
            'aws-native:ec2:SecurityGroupEgress',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityGroupEgress':
        """
        Get an existing SecurityGroupEgress resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityGroupEgressInitArgs.__new__(SecurityGroupEgressInitArgs)

        __props__.__dict__["aws_id"] = None
        __props__.__dict__["cidr_ip"] = None
        __props__.__dict__["cidr_ipv6"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["destination_prefix_list_id"] = None
        __props__.__dict__["destination_security_group_id"] = None
        __props__.__dict__["from_port"] = None
        __props__.__dict__["group_id"] = None
        __props__.__dict__["ip_protocol"] = None
        __props__.__dict__["to_port"] = None
        return SecurityGroupEgress(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="cidrIp")
    def cidr_ip(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv4 address range, in CIDR format.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
         For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        """
        return pulumi.get(self, "cidr_ip")

    @property
    @pulumi.getter(name="cidrIpv6")
    def cidr_ipv6(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv6 address range, in CIDR format.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
         For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *User Guide*.
        """
        return pulumi.get(self, "cidr_ipv6")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of an egress (outbound) security group rule.
         Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> pulumi.Output[Optional[str]]:
        """
        The prefix list IDs for an AWS service. This is the AWS service to access through a VPC endpoint from instances associated with the security group.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        """
        return pulumi.get(self, "destination_prefix_list_id")

    @property
    @pulumi.getter(name="destinationSecurityGroupId")
    def destination_security_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the security group.
         You must specify exactly one of the following: ``CidrIp``, ``CidrIpv6``, ``DestinationPrefixListId``, or ``DestinationSecurityGroupId``.
        """
        return pulumi.get(self, "destination_security_group_id")

    @property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Output[Optional[int]]:
        """
        If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
        """
        return pulumi.get(self, "from_port")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[str]:
        """
        The IP protocol name (``tcp``, ``udp``, ``icmp``, ``icmpv6``) or number (see [Protocol Numbers](https://docs.aws.amazon.com/http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
         Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp``, ``udp``, ``icmp``, or ``icmpv6`` allows traffic on all ports, regardless of any port range you specify. For ``tcp``, ``udp``, and ``icmp``, you must specify a port range. For ``icmpv6``, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
        """
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Output[Optional[int]]:
        """
        If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
        """
        return pulumi.get(self, "to_port")

