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
from ._enums import *

__all__ = [
    'GetLoggingConfigurationResult',
    'AwaitableGetLoggingConfigurationResult',
    'get_logging_configuration',
    'get_logging_configuration_output',
]

@pulumi.output_type
class GetLoggingConfigurationResult:
    def __init__(__self__, logging_configuration=None):
        if logging_configuration and not isinstance(logging_configuration, dict):
            raise TypeError("Expected argument 'logging_configuration' to be a dict")
        pulumi.set(__self__, "logging_configuration", logging_configuration)

    @property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> Optional['outputs.LoggingConfiguration']:
        """
        Defines how AWS Network Firewall performs logging for a `Firewall` .
        """
        return pulumi.get(self, "logging_configuration")


class AwaitableGetLoggingConfigurationResult(GetLoggingConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoggingConfigurationResult(
            logging_configuration=self.logging_configuration)


def get_logging_configuration(firewall_arn: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoggingConfigurationResult:
    """
    Resource type definition for AWS::NetworkFirewall::LoggingConfiguration


    :param str firewall_arn: The Amazon Resource Name (ARN) of the `Firewall` that the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.
    """
    __args__ = dict()
    __args__['firewallArn'] = firewall_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:networkfirewall:getLoggingConfiguration', __args__, opts=opts, typ=GetLoggingConfigurationResult).value

    return AwaitableGetLoggingConfigurationResult(
        logging_configuration=pulumi.get(__ret__, 'logging_configuration'))


@_utilities.lift_output_func(get_logging_configuration)
def get_logging_configuration_output(firewall_arn: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoggingConfigurationResult]:
    """
    Resource type definition for AWS::NetworkFirewall::LoggingConfiguration


    :param str firewall_arn: The Amazon Resource Name (ARN) of the `Firewall` that the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.
    """
    ...
