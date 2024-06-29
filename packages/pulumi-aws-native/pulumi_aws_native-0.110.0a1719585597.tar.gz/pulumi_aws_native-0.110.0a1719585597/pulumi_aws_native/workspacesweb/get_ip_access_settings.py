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
    'GetIpAccessSettingsResult',
    'AwaitableGetIpAccessSettingsResult',
    'get_ip_access_settings',
    'get_ip_access_settings_output',
]

@pulumi.output_type
class GetIpAccessSettingsResult:
    def __init__(__self__, associated_portal_arns=None, creation_date=None, description=None, display_name=None, ip_access_settings_arn=None, ip_rules=None, tags=None):
        if associated_portal_arns and not isinstance(associated_portal_arns, list):
            raise TypeError("Expected argument 'associated_portal_arns' to be a list")
        pulumi.set(__self__, "associated_portal_arns", associated_portal_arns)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if ip_access_settings_arn and not isinstance(ip_access_settings_arn, str):
            raise TypeError("Expected argument 'ip_access_settings_arn' to be a str")
        pulumi.set(__self__, "ip_access_settings_arn", ip_access_settings_arn)
        if ip_rules and not isinstance(ip_rules, list):
            raise TypeError("Expected argument 'ip_rules' to be a list")
        pulumi.set(__self__, "ip_rules", ip_rules)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(self) -> Optional[Sequence[str]]:
        """
        A list of web portal ARNs that this IP access settings resource is associated with.
        """
        return pulumi.get(self, "associated_portal_arns")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        """
        The creation date timestamp of the IP access settings.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the IP access settings.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the IP access settings.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> Optional[str]:
        """
        The ARN of the IP access settings resource.
        """
        return pulumi.get(self, "ip_access_settings_arn")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence['outputs.IpAccessSettingsIpRule']]:
        """
        The IP rules of the IP access settings.
        """
        return pulumi.get(self, "ip_rules")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags to add to the IP access settings resource. A tag is a key-value pair.
        """
        return pulumi.get(self, "tags")


class AwaitableGetIpAccessSettingsResult(GetIpAccessSettingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpAccessSettingsResult(
            associated_portal_arns=self.associated_portal_arns,
            creation_date=self.creation_date,
            description=self.description,
            display_name=self.display_name,
            ip_access_settings_arn=self.ip_access_settings_arn,
            ip_rules=self.ip_rules,
            tags=self.tags)


def get_ip_access_settings(ip_access_settings_arn: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpAccessSettingsResult:
    """
    Definition of AWS::WorkSpacesWeb::IpAccessSettings Resource Type


    :param str ip_access_settings_arn: The ARN of the IP access settings resource.
    """
    __args__ = dict()
    __args__['ipAccessSettingsArn'] = ip_access_settings_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:workspacesweb:getIpAccessSettings', __args__, opts=opts, typ=GetIpAccessSettingsResult).value

    return AwaitableGetIpAccessSettingsResult(
        associated_portal_arns=pulumi.get(__ret__, 'associated_portal_arns'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        ip_access_settings_arn=pulumi.get(__ret__, 'ip_access_settings_arn'),
        ip_rules=pulumi.get(__ret__, 'ip_rules'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_ip_access_settings)
def get_ip_access_settings_output(ip_access_settings_arn: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpAccessSettingsResult]:
    """
    Definition of AWS::WorkSpacesWeb::IpAccessSettings Resource Type


    :param str ip_access_settings_arn: The ARN of the IP access settings resource.
    """
    ...
