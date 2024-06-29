# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetConnectorResult',
    'AwaitableGetConnectorResult',
    'get_connector',
    'get_connector_output',
]

@pulumi.output_type
class GetConnectorResult:
    def __init__(__self__, connector_arn=None):
        if connector_arn and not isinstance(connector_arn, str):
            raise TypeError("Expected argument 'connector_arn' to be a str")
        pulumi.set(__self__, "connector_arn", connector_arn)

    @property
    @pulumi.getter(name="connectorArn")
    def connector_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html) .
        """
        return pulumi.get(self, "connector_arn")


class AwaitableGetConnectorResult(GetConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectorResult(
            connector_arn=self.connector_arn)


def get_connector(connector_arn: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectorResult:
    """
    Definition of AWS::PCAConnectorAD::Connector Resource Type


    :param str connector_arn: The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html) .
    """
    __args__ = dict()
    __args__['connectorArn'] = connector_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pcaconnectorad:getConnector', __args__, opts=opts, typ=GetConnectorResult).value

    return AwaitableGetConnectorResult(
        connector_arn=pulumi.get(__ret__, 'connector_arn'))


@_utilities.lift_output_func(get_connector)
def get_connector_output(connector_arn: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectorResult]:
    """
    Definition of AWS::PCAConnectorAD::Connector Resource Type


    :param str connector_arn: The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html) .
    """
    ...
