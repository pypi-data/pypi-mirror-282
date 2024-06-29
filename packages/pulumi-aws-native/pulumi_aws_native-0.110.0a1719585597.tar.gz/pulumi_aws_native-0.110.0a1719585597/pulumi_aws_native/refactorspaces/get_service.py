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
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
    'get_service_output',
]

@pulumi.output_type
class GetServiceResult:
    def __init__(__self__, arn=None, service_identifier=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if service_identifier and not isinstance(service_identifier, str):
            raise TypeError("Expected argument 'service_identifier' to be a str")
        pulumi.set(__self__, "service_identifier", service_identifier)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the service.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> Optional[str]:
        """
        The unique identifier of the service.
        """
        return pulumi.get(self, "service_identifier")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        """
        return pulumi.get(self, "tags")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            arn=self.arn,
            service_identifier=self.service_identifier,
            tags=self.tags)


def get_service(application_identifier: Optional[str] = None,
                environment_identifier: Optional[str] = None,
                service_identifier: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Definition of AWS::RefactorSpaces::Service Resource Type


    :param str application_identifier: The unique identifier of the application.
    :param str environment_identifier: The unique identifier of the environment.
    :param str service_identifier: The unique identifier of the service.
    """
    __args__ = dict()
    __args__['applicationIdentifier'] = application_identifier
    __args__['environmentIdentifier'] = environment_identifier
    __args__['serviceIdentifier'] = service_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:refactorspaces:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        arn=pulumi.get(__ret__, 'arn'),
        service_identifier=pulumi.get(__ret__, 'service_identifier'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_service)
def get_service_output(application_identifier: Optional[pulumi.Input[str]] = None,
                       environment_identifier: Optional[pulumi.Input[str]] = None,
                       service_identifier: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    Definition of AWS::RefactorSpaces::Service Resource Type


    :param str application_identifier: The unique identifier of the application.
    :param str environment_identifier: The unique identifier of the environment.
    :param str service_identifier: The unique identifier of the service.
    """
    ...
