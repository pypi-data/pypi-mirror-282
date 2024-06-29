# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetSubnetGroupResult',
    'AwaitableGetSubnetGroupResult',
    'get_subnet_group',
    'get_subnet_group_output',
]

@pulumi.output_type
class GetSubnetGroupResult:
    def __init__(__self__, description=None, subnet_ids=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description for the cache subnet group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        """
        The EC2 subnet IDs for the cache subnet group.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A tag that can be added to an ElastiCache subnet group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your subnet groups. A tag with a null Value is permitted.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSubnetGroupResult(GetSubnetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubnetGroupResult(
            description=self.description,
            subnet_ids=self.subnet_ids,
            tags=self.tags)


def get_subnet_group(cache_subnet_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubnetGroupResult:
    """
    Resource Type definition for AWS::ElastiCache::SubnetGroup


    :param str cache_subnet_group_name: The name for the cache subnet group. This value is stored as a lowercase string.
    """
    __args__ = dict()
    __args__['cacheSubnetGroupName'] = cache_subnet_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:elasticache:getSubnetGroup', __args__, opts=opts, typ=GetSubnetGroupResult).value

    return AwaitableGetSubnetGroupResult(
        description=pulumi.get(__ret__, 'description'),
        subnet_ids=pulumi.get(__ret__, 'subnet_ids'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_subnet_group)
def get_subnet_group_output(cache_subnet_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubnetGroupResult]:
    """
    Resource Type definition for AWS::ElastiCache::SubnetGroup


    :param str cache_subnet_group_name: The name for the cache subnet group. This value is stored as a lowercase string.
    """
    ...
