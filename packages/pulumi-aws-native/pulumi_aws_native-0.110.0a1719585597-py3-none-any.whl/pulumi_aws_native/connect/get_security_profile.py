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

__all__ = [
    'GetSecurityProfileResult',
    'AwaitableGetSecurityProfileResult',
    'get_security_profile',
    'get_security_profile_output',
]

@pulumi.output_type
class GetSecurityProfileResult:
    def __init__(__self__, allowed_access_control_hierarchy_group_id=None, allowed_access_control_tags=None, applications=None, description=None, hierarchy_restricted_resources=None, last_modified_region=None, last_modified_time=None, permissions=None, security_profile_arn=None, tag_restricted_resources=None, tags=None):
        if allowed_access_control_hierarchy_group_id and not isinstance(allowed_access_control_hierarchy_group_id, str):
            raise TypeError("Expected argument 'allowed_access_control_hierarchy_group_id' to be a str")
        pulumi.set(__self__, "allowed_access_control_hierarchy_group_id", allowed_access_control_hierarchy_group_id)
        if allowed_access_control_tags and not isinstance(allowed_access_control_tags, list):
            raise TypeError("Expected argument 'allowed_access_control_tags' to be a list")
        pulumi.set(__self__, "allowed_access_control_tags", allowed_access_control_tags)
        if applications and not isinstance(applications, list):
            raise TypeError("Expected argument 'applications' to be a list")
        pulumi.set(__self__, "applications", applications)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if hierarchy_restricted_resources and not isinstance(hierarchy_restricted_resources, list):
            raise TypeError("Expected argument 'hierarchy_restricted_resources' to be a list")
        pulumi.set(__self__, "hierarchy_restricted_resources", hierarchy_restricted_resources)
        if last_modified_region and not isinstance(last_modified_region, str):
            raise TypeError("Expected argument 'last_modified_region' to be a str")
        pulumi.set(__self__, "last_modified_region", last_modified_region)
        if last_modified_time and not isinstance(last_modified_time, float):
            raise TypeError("Expected argument 'last_modified_time' to be a float")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if security_profile_arn and not isinstance(security_profile_arn, str):
            raise TypeError("Expected argument 'security_profile_arn' to be a str")
        pulumi.set(__self__, "security_profile_arn", security_profile_arn)
        if tag_restricted_resources and not isinstance(tag_restricted_resources, list):
            raise TypeError("Expected argument 'tag_restricted_resources' to be a list")
        pulumi.set(__self__, "tag_restricted_resources", tag_restricted_resources)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allowedAccessControlHierarchyGroupId")
    def allowed_access_control_hierarchy_group_id(self) -> Optional[str]:
        """
        The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.
        """
        return pulumi.get(self, "allowed_access_control_hierarchy_group_id")

    @property
    @pulumi.getter(name="allowedAccessControlTags")
    def allowed_access_control_tags(self) -> Optional[Sequence['outputs.SecurityProfileTag']]:
        """
        The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        """
        return pulumi.get(self, "allowed_access_control_tags")

    @property
    @pulumi.getter
    def applications(self) -> Optional[Sequence['outputs.SecurityProfileApplication']]:
        """
        A list of third-party applications that the security profile will give access to.
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the security profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hierarchyRestrictedResources")
    def hierarchy_restricted_resources(self) -> Optional[Sequence[str]]:
        """
        The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect.
        """
        return pulumi.get(self, "hierarchy_restricted_resources")

    @property
    @pulumi.getter(name="lastModifiedRegion")
    def last_modified_region(self) -> Optional[str]:
        """
        The AWS Region where this resource was last modified.
        """
        return pulumi.get(self, "last_modified_region")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[float]:
        """
        The timestamp when this resource was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[str]]:
        """
        Permissions assigned to the security profile.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="securityProfileArn")
    def security_profile_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the security profile.
        """
        return pulumi.get(self, "security_profile_arn")

    @property
    @pulumi.getter(name="tagRestrictedResources")
    def tag_restricted_resources(self) -> Optional[Sequence[str]]:
        """
        The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        """
        return pulumi.get(self, "tag_restricted_resources")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags used to organize, track, or control access for this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSecurityProfileResult(GetSecurityProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityProfileResult(
            allowed_access_control_hierarchy_group_id=self.allowed_access_control_hierarchy_group_id,
            allowed_access_control_tags=self.allowed_access_control_tags,
            applications=self.applications,
            description=self.description,
            hierarchy_restricted_resources=self.hierarchy_restricted_resources,
            last_modified_region=self.last_modified_region,
            last_modified_time=self.last_modified_time,
            permissions=self.permissions,
            security_profile_arn=self.security_profile_arn,
            tag_restricted_resources=self.tag_restricted_resources,
            tags=self.tags)


def get_security_profile(security_profile_arn: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityProfileResult:
    """
    Resource Type definition for AWS::Connect::SecurityProfile


    :param str security_profile_arn: The Amazon Resource Name (ARN) for the security profile.
    """
    __args__ = dict()
    __args__['securityProfileArn'] = security_profile_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getSecurityProfile', __args__, opts=opts, typ=GetSecurityProfileResult).value

    return AwaitableGetSecurityProfileResult(
        allowed_access_control_hierarchy_group_id=pulumi.get(__ret__, 'allowed_access_control_hierarchy_group_id'),
        allowed_access_control_tags=pulumi.get(__ret__, 'allowed_access_control_tags'),
        applications=pulumi.get(__ret__, 'applications'),
        description=pulumi.get(__ret__, 'description'),
        hierarchy_restricted_resources=pulumi.get(__ret__, 'hierarchy_restricted_resources'),
        last_modified_region=pulumi.get(__ret__, 'last_modified_region'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        permissions=pulumi.get(__ret__, 'permissions'),
        security_profile_arn=pulumi.get(__ret__, 'security_profile_arn'),
        tag_restricted_resources=pulumi.get(__ret__, 'tag_restricted_resources'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_security_profile)
def get_security_profile_output(security_profile_arn: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityProfileResult]:
    """
    Resource Type definition for AWS::Connect::SecurityProfile


    :param str security_profile_arn: The Amazon Resource Name (ARN) for the security profile.
    """
    ...
