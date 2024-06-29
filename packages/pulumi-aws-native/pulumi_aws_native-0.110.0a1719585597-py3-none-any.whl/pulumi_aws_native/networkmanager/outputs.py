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

__all__ = [
    'ConnectAttachmentOptions',
    'ConnectAttachmentProposedSegmentChange',
    'ConnectAttachmentTag',
    'ConnectPeerBgpConfiguration',
    'ConnectPeerBgpOptions',
    'ConnectPeerConfiguration',
    'CoreNetworkEdge',
    'CoreNetworkSegment',
    'DeviceAwsLocation',
    'DeviceLocation',
    'LinkBandwidth',
    'SiteLocation',
    'SiteToSiteVpnAttachmentProposedSegmentChange',
    'SiteToSiteVpnAttachmentTag',
    'TransitGatewayRouteTableAttachmentProposedSegmentChange',
    'TransitGatewayRouteTableAttachmentTag',
    'VpcAttachmentProposedSegmentChange',
    'VpcAttachmentTag',
    'VpcAttachmentVpcOptions',
]

@pulumi.output_type
class ConnectAttachmentOptions(dict):
    """
    Connect attachment options for protocol
    """
    def __init__(__self__, *,
                 protocol: Optional[str] = None):
        """
        Connect attachment options for protocol
        :param str protocol: Tunnel protocol for connect attachment
        """
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        Tunnel protocol for connect attachment
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class ConnectAttachmentProposedSegmentChange(dict):
    """
    The attachment to move from one segment to another.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attachmentPolicyRuleNumber":
            suggest = "attachment_policy_rule_number"
        elif key == "segmentName":
            suggest = "segment_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConnectAttachmentProposedSegmentChange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConnectAttachmentProposedSegmentChange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConnectAttachmentProposedSegmentChange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attachment_policy_rule_number: Optional[int] = None,
                 segment_name: Optional[str] = None,
                 tags: Optional[Sequence['outputs.ConnectAttachmentTag']] = None):
        """
        The attachment to move from one segment to another.
        :param int attachment_policy_rule_number: The rule number in the policy document that applies to this change.
        :param str segment_name: The name of the segment to change.
        :param Sequence['ConnectAttachmentTag'] tags: The list of key-value tags that changed for the segment.
        """
        if attachment_policy_rule_number is not None:
            pulumi.set(__self__, "attachment_policy_rule_number", attachment_policy_rule_number)
        if segment_name is not None:
            pulumi.set(__self__, "segment_name", segment_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> Optional[int]:
        """
        The rule number in the policy document that applies to this change.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[str]:
        """
        The name of the segment to change.
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ConnectAttachmentTag']]:
        """
        The list of key-value tags that changed for the segment.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class ConnectAttachmentTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ConnectPeerBgpConfiguration(dict):
    """
    Bgp configuration for connect peer
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "coreNetworkAddress":
            suggest = "core_network_address"
        elif key == "coreNetworkAsn":
            suggest = "core_network_asn"
        elif key == "peerAddress":
            suggest = "peer_address"
        elif key == "peerAsn":
            suggest = "peer_asn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConnectPeerBgpConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConnectPeerBgpConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConnectPeerBgpConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 core_network_address: Optional[str] = None,
                 core_network_asn: Optional[float] = None,
                 peer_address: Optional[str] = None,
                 peer_asn: Optional[float] = None):
        """
        Bgp configuration for connect peer
        :param str core_network_address: The address of a core network.
        :param float core_network_asn: The ASN of the Coret Network.
        :param str peer_address: The address of a core network Connect peer.
        :param float peer_asn: The ASN of the Connect peer.
        """
        if core_network_address is not None:
            pulumi.set(__self__, "core_network_address", core_network_address)
        if core_network_asn is not None:
            pulumi.set(__self__, "core_network_asn", core_network_asn)
        if peer_address is not None:
            pulumi.set(__self__, "peer_address", peer_address)
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)

    @property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[str]:
        """
        The address of a core network.
        """
        return pulumi.get(self, "core_network_address")

    @property
    @pulumi.getter(name="coreNetworkAsn")
    def core_network_asn(self) -> Optional[float]:
        """
        The ASN of the Coret Network.
        """
        return pulumi.get(self, "core_network_asn")

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[str]:
        """
        The address of a core network Connect peer.
        """
        return pulumi.get(self, "peer_address")

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[float]:
        """
        The ASN of the Connect peer.
        """
        return pulumi.get(self, "peer_asn")


@pulumi.output_type
class ConnectPeerBgpOptions(dict):
    """
    Bgp options
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "peerAsn":
            suggest = "peer_asn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConnectPeerBgpOptions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConnectPeerBgpOptions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConnectPeerBgpOptions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 peer_asn: Optional[float] = None):
        """
        Bgp options
        :param float peer_asn: The Peer ASN of the BGP.
        """
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[float]:
        """
        The Peer ASN of the BGP.
        """
        return pulumi.get(self, "peer_asn")


@pulumi.output_type
class ConnectPeerConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bgpConfigurations":
            suggest = "bgp_configurations"
        elif key == "coreNetworkAddress":
            suggest = "core_network_address"
        elif key == "insideCidrBlocks":
            suggest = "inside_cidr_blocks"
        elif key == "peerAddress":
            suggest = "peer_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConnectPeerConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConnectPeerConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConnectPeerConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bgp_configurations: Optional[Sequence['outputs.ConnectPeerBgpConfiguration']] = None,
                 core_network_address: Optional[str] = None,
                 inside_cidr_blocks: Optional[Sequence[str]] = None,
                 peer_address: Optional[str] = None,
                 protocol: Optional[str] = None):
        """
        :param Sequence['ConnectPeerBgpConfiguration'] bgp_configurations: The Connect peer BGP configurations.
        :param str core_network_address: The IP address of a core network.
        :param Sequence[str] inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
        :param str peer_address: The IP address of the Connect peer.
        :param str protocol: The protocol used for a Connect peer configuration.
        """
        if bgp_configurations is not None:
            pulumi.set(__self__, "bgp_configurations", bgp_configurations)
        if core_network_address is not None:
            pulumi.set(__self__, "core_network_address", core_network_address)
        if inside_cidr_blocks is not None:
            pulumi.set(__self__, "inside_cidr_blocks", inside_cidr_blocks)
        if peer_address is not None:
            pulumi.set(__self__, "peer_address", peer_address)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="bgpConfigurations")
    def bgp_configurations(self) -> Optional[Sequence['outputs.ConnectPeerBgpConfiguration']]:
        """
        The Connect peer BGP configurations.
        """
        return pulumi.get(self, "bgp_configurations")

    @property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[str]:
        """
        The IP address of a core network.
        """
        return pulumi.get(self, "core_network_address")

    @property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[str]]:
        """
        The inside IP addresses used for a Connect peer configuration.
        """
        return pulumi.get(self, "inside_cidr_blocks")

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[str]:
        """
        The IP address of the Connect peer.
        """
        return pulumi.get(self, "peer_address")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        The protocol used for a Connect peer configuration.
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class CoreNetworkEdge(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "edgeLocation":
            suggest = "edge_location"
        elif key == "insideCidrBlocks":
            suggest = "inside_cidr_blocks"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CoreNetworkEdge. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CoreNetworkEdge.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CoreNetworkEdge.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 asn: Optional[float] = None,
                 edge_location: Optional[str] = None,
                 inside_cidr_blocks: Optional[Sequence[str]] = None):
        """
        :param float asn: The ASN of a core network edge.
        :param str edge_location: The Region where a core network edge is located.
        :param Sequence[str] inside_cidr_blocks: The inside IP addresses used for core network edges.
        """
        if asn is not None:
            pulumi.set(__self__, "asn", asn)
        if edge_location is not None:
            pulumi.set(__self__, "edge_location", edge_location)
        if inside_cidr_blocks is not None:
            pulumi.set(__self__, "inside_cidr_blocks", inside_cidr_blocks)

    @property
    @pulumi.getter
    def asn(self) -> Optional[float]:
        """
        The ASN of a core network edge.
        """
        return pulumi.get(self, "asn")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[str]:
        """
        The Region where a core network edge is located.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[str]]:
        """
        The inside IP addresses used for core network edges.
        """
        return pulumi.get(self, "inside_cidr_blocks")


@pulumi.output_type
class CoreNetworkSegment(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "edgeLocations":
            suggest = "edge_locations"
        elif key == "sharedSegments":
            suggest = "shared_segments"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CoreNetworkSegment. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CoreNetworkSegment.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CoreNetworkSegment.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 edge_locations: Optional[Sequence[str]] = None,
                 name: Optional[str] = None,
                 shared_segments: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] edge_locations: The Regions where the edges are located.
        :param str name: Name of segment
        :param Sequence[str] shared_segments: The shared segments of a core network.
        """
        if edge_locations is not None:
            pulumi.set(__self__, "edge_locations", edge_locations)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if shared_segments is not None:
            pulumi.set(__self__, "shared_segments", shared_segments)

    @property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> Optional[Sequence[str]]:
        """
        The Regions where the edges are located.
        """
        return pulumi.get(self, "edge_locations")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of segment
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sharedSegments")
    def shared_segments(self) -> Optional[Sequence[str]]:
        """
        The shared segments of a core network.
        """
        return pulumi.get(self, "shared_segments")


@pulumi.output_type
class DeviceAwsLocation(dict):
    """
    The Amazon Web Services location of the device, if applicable.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetArn":
            suggest = "subnet_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeviceAwsLocation. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeviceAwsLocation.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeviceAwsLocation.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_arn: Optional[str] = None,
                 zone: Optional[str] = None):
        """
        The Amazon Web Services location of the device, if applicable.
        :param str subnet_arn: The Amazon Resource Name (ARN) of the subnet that the device is located in.
        :param str zone: The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.
        """
        if subnet_arn is not None:
            pulumi.set(__self__, "subnet_arn", subnet_arn)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the subnet that the device is located in.
        """
        return pulumi.get(self, "subnet_arn")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        """
        The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.
        """
        return pulumi.get(self, "zone")


@pulumi.output_type
class DeviceLocation(dict):
    """
    The site location.
    """
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 latitude: Optional[str] = None,
                 longitude: Optional[str] = None):
        """
        The site location.
        :param str address: The physical address.
        :param str latitude: The latitude.
        :param str longitude: The longitude.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if latitude is not None:
            pulumi.set(__self__, "latitude", latitude)
        if longitude is not None:
            pulumi.set(__self__, "longitude", longitude)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The physical address.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def latitude(self) -> Optional[str]:
        """
        The latitude.
        """
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter
    def longitude(self) -> Optional[str]:
        """
        The longitude.
        """
        return pulumi.get(self, "longitude")


@pulumi.output_type
class LinkBandwidth(dict):
    """
    The bandwidth for the link.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "downloadSpeed":
            suggest = "download_speed"
        elif key == "uploadSpeed":
            suggest = "upload_speed"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LinkBandwidth. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LinkBandwidth.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LinkBandwidth.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 download_speed: Optional[int] = None,
                 upload_speed: Optional[int] = None):
        """
        The bandwidth for the link.
        :param int download_speed: Download speed in Mbps.
        :param int upload_speed: Upload speed in Mbps.
        """
        if download_speed is not None:
            pulumi.set(__self__, "download_speed", download_speed)
        if upload_speed is not None:
            pulumi.set(__self__, "upload_speed", upload_speed)

    @property
    @pulumi.getter(name="downloadSpeed")
    def download_speed(self) -> Optional[int]:
        """
        Download speed in Mbps.
        """
        return pulumi.get(self, "download_speed")

    @property
    @pulumi.getter(name="uploadSpeed")
    def upload_speed(self) -> Optional[int]:
        """
        Upload speed in Mbps.
        """
        return pulumi.get(self, "upload_speed")


@pulumi.output_type
class SiteLocation(dict):
    """
    The location of the site
    """
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 latitude: Optional[str] = None,
                 longitude: Optional[str] = None):
        """
        The location of the site
        :param str address: The physical address.
        :param str latitude: The latitude.
        :param str longitude: The longitude.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if latitude is not None:
            pulumi.set(__self__, "latitude", latitude)
        if longitude is not None:
            pulumi.set(__self__, "longitude", longitude)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The physical address.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def latitude(self) -> Optional[str]:
        """
        The latitude.
        """
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter
    def longitude(self) -> Optional[str]:
        """
        The longitude.
        """
        return pulumi.get(self, "longitude")


@pulumi.output_type
class SiteToSiteVpnAttachmentProposedSegmentChange(dict):
    """
    The attachment to move from one segment to another.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attachmentPolicyRuleNumber":
            suggest = "attachment_policy_rule_number"
        elif key == "segmentName":
            suggest = "segment_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SiteToSiteVpnAttachmentProposedSegmentChange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SiteToSiteVpnAttachmentProposedSegmentChange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SiteToSiteVpnAttachmentProposedSegmentChange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attachment_policy_rule_number: Optional[int] = None,
                 segment_name: Optional[str] = None,
                 tags: Optional[Sequence['outputs.SiteToSiteVpnAttachmentTag']] = None):
        """
        The attachment to move from one segment to another.
        :param int attachment_policy_rule_number: The rule number in the policy document that applies to this change.
        :param str segment_name: The name of the segment to change.
        :param Sequence['SiteToSiteVpnAttachmentTag'] tags: The key-value tags that changed for the segment.
        """
        if attachment_policy_rule_number is not None:
            pulumi.set(__self__, "attachment_policy_rule_number", attachment_policy_rule_number)
        if segment_name is not None:
            pulumi.set(__self__, "segment_name", segment_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> Optional[int]:
        """
        The rule number in the policy document that applies to this change.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[str]:
        """
        The name of the segment to change.
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SiteToSiteVpnAttachmentTag']]:
        """
        The key-value tags that changed for the segment.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class SiteToSiteVpnAttachmentTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class TransitGatewayRouteTableAttachmentProposedSegmentChange(dict):
    """
    The attachment to move from one segment to another.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attachmentPolicyRuleNumber":
            suggest = "attachment_policy_rule_number"
        elif key == "segmentName":
            suggest = "segment_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TransitGatewayRouteTableAttachmentProposedSegmentChange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TransitGatewayRouteTableAttachmentProposedSegmentChange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TransitGatewayRouteTableAttachmentProposedSegmentChange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attachment_policy_rule_number: Optional[int] = None,
                 segment_name: Optional[str] = None,
                 tags: Optional[Sequence['outputs.TransitGatewayRouteTableAttachmentTag']] = None):
        """
        The attachment to move from one segment to another.
        :param int attachment_policy_rule_number: The rule number in the policy document that applies to this change.
        :param str segment_name: The name of the segment to change.
        :param Sequence['TransitGatewayRouteTableAttachmentTag'] tags: The key-value tags that changed for the segment.
        """
        if attachment_policy_rule_number is not None:
            pulumi.set(__self__, "attachment_policy_rule_number", attachment_policy_rule_number)
        if segment_name is not None:
            pulumi.set(__self__, "segment_name", segment_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> Optional[int]:
        """
        The rule number in the policy document that applies to this change.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[str]:
        """
        The name of the segment to change.
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TransitGatewayRouteTableAttachmentTag']]:
        """
        The key-value tags that changed for the segment.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class TransitGatewayRouteTableAttachmentTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class VpcAttachmentProposedSegmentChange(dict):
    """
    The attachment to move from one segment to another.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attachmentPolicyRuleNumber":
            suggest = "attachment_policy_rule_number"
        elif key == "segmentName":
            suggest = "segment_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VpcAttachmentProposedSegmentChange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VpcAttachmentProposedSegmentChange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VpcAttachmentProposedSegmentChange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attachment_policy_rule_number: Optional[int] = None,
                 segment_name: Optional[str] = None,
                 tags: Optional[Sequence['outputs.VpcAttachmentTag']] = None):
        """
        The attachment to move from one segment to another.
        :param int attachment_policy_rule_number: The rule number in the policy document that applies to this change.
        :param str segment_name: The name of the segment to change.
        :param Sequence['VpcAttachmentTag'] tags: The key-value tags that changed for the segment.
        """
        if attachment_policy_rule_number is not None:
            pulumi.set(__self__, "attachment_policy_rule_number", attachment_policy_rule_number)
        if segment_name is not None:
            pulumi.set(__self__, "segment_name", segment_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> Optional[int]:
        """
        The rule number in the policy document that applies to this change.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[str]:
        """
        The name of the segment to change.
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.VpcAttachmentTag']]:
        """
        The key-value tags that changed for the segment.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class VpcAttachmentTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class VpcAttachmentVpcOptions(dict):
    """
    Vpc options of the attachment.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "applianceModeSupport":
            suggest = "appliance_mode_support"
        elif key == "ipv6Support":
            suggest = "ipv6_support"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VpcAttachmentVpcOptions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VpcAttachmentVpcOptions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VpcAttachmentVpcOptions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 appliance_mode_support: Optional[bool] = None,
                 ipv6_support: Optional[bool] = None):
        """
        Vpc options of the attachment.
        :param bool appliance_mode_support: Indicates whether to enable ApplianceModeSupport Support for Vpc Attachment. Valid Values: true | false
        :param bool ipv6_support: Indicates whether to enable Ipv6 Support for Vpc Attachment. Valid Values: enable | disable
        """
        if appliance_mode_support is not None:
            pulumi.set(__self__, "appliance_mode_support", appliance_mode_support)
        if ipv6_support is not None:
            pulumi.set(__self__, "ipv6_support", ipv6_support)

    @property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> Optional[bool]:
        """
        Indicates whether to enable ApplianceModeSupport Support for Vpc Attachment. Valid Values: true | false
        """
        return pulumi.get(self, "appliance_mode_support")

    @property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> Optional[bool]:
        """
        Indicates whether to enable Ipv6 Support for Vpc Attachment. Valid Values: enable | disable
        """
        return pulumi.get(self, "ipv6_support")


