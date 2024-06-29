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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetDashboardResult',
    'AwaitableGetDashboardResult',
    'get_dashboard',
    'get_dashboard_output',
]

@pulumi.output_type
class GetDashboardResult:
    def __init__(__self__, arn=None, created_time=None, last_published_time=None, last_updated_time=None, link_entities=None, name=None, permissions=None, tags=None, version=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if last_published_time and not isinstance(last_published_time, str):
            raise TypeError("Expected argument 'last_published_time' to be a str")
        pulumi.set(__self__, "last_published_time", last_published_time)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if link_entities and not isinstance(link_entities, list):
            raise TypeError("Expected argument 'link_entities' to be a list")
        pulumi.set(__self__, "link_entities", link_entities)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if version and not isinstance(version, dict):
            raise TypeError("Expected argument 'version' to be a dict")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        <p>The Amazon Resource Name (ARN) of the resource.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        <p>The time that this dashboard was created.</p>
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="lastPublishedTime")
    def last_published_time(self) -> Optional[str]:
        """
        <p>The last time that this dashboard was published.</p>
        """
        return pulumi.get(self, "last_published_time")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        <p>The last time that this dashboard was updated.</p>
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="linkEntities")
    def link_entities(self) -> Optional[Sequence[str]]:
        """
        A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.
        """
        return pulumi.get(self, "link_entities")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The display name of the dashboard.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence['outputs.DashboardResourcePermission']]:
        """
        A structure that contains the permissions of the dashboard. You can use this structure for granting permissions by providing a list of IAM action information for each principal ARN.

        To specify no permissions, omit the permissions list.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Contains a map of the key-value pairs for the resource tag or tags assigned to the dashboard.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> Optional['outputs.DashboardVersion']:
        return pulumi.get(self, "version")


class AwaitableGetDashboardResult(GetDashboardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDashboardResult(
            arn=self.arn,
            created_time=self.created_time,
            last_published_time=self.last_published_time,
            last_updated_time=self.last_updated_time,
            link_entities=self.link_entities,
            name=self.name,
            permissions=self.permissions,
            tags=self.tags,
            version=self.version)


def get_dashboard(aws_account_id: Optional[str] = None,
                  dashboard_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDashboardResult:
    """
    Definition of the AWS::QuickSight::Dashboard Resource Type.


    :param str aws_account_id: The ID of the AWS account where you want to create the dashboard.
    :param str dashboard_id: The ID for the dashboard, also added to the IAM policy.
    """
    __args__ = dict()
    __args__['awsAccountId'] = aws_account_id
    __args__['dashboardId'] = dashboard_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:quicksight:getDashboard', __args__, opts=opts, typ=GetDashboardResult).value

    return AwaitableGetDashboardResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        last_published_time=pulumi.get(__ret__, 'last_published_time'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        link_entities=pulumi.get(__ret__, 'link_entities'),
        name=pulumi.get(__ret__, 'name'),
        permissions=pulumi.get(__ret__, 'permissions'),
        tags=pulumi.get(__ret__, 'tags'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_dashboard)
def get_dashboard_output(aws_account_id: Optional[pulumi.Input[str]] = None,
                         dashboard_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDashboardResult]:
    """
    Definition of the AWS::QuickSight::Dashboard Resource Type.


    :param str aws_account_id: The ID of the AWS account where you want to create the dashboard.
    :param str dashboard_id: The ID for the dashboard, also added to the IAM policy.
    """
    ...
