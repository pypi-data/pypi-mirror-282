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
    'GetConfigurationResult',
    'AwaitableGetConfigurationResult',
    'get_configuration',
    'get_configuration_output',
]

@pulumi.output_type
class GetConfigurationResult:
    def __init__(__self__, arn=None, description=None, latest_revision=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if latest_revision and not isinstance(latest_revision, dict):
            raise TypeError("Expected argument 'latest_revision' to be a dict")
        pulumi.set(__self__, "latest_revision", latest_revision)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> Optional['outputs.ConfigurationLatestRevision']:
        """
        Latest revision of the configuration.
        """
        return pulumi.get(self, "latest_revision")


class AwaitableGetConfigurationResult(GetConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationResult(
            arn=self.arn,
            description=self.description,
            latest_revision=self.latest_revision)


def get_configuration(arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationResult:
    """
    Resource Type definition for AWS::MSK::Configuration
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:msk:getConfiguration', __args__, opts=opts, typ=GetConfigurationResult).value

    return AwaitableGetConfigurationResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        latest_revision=pulumi.get(__ret__, 'latest_revision'))


@_utilities.lift_output_func(get_configuration)
def get_configuration_output(arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationResult]:
    """
    Resource Type definition for AWS::MSK::Configuration
    """
    ...
