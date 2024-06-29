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
    'GetStandardResult',
    'AwaitableGetStandardResult',
    'get_standard',
    'get_standard_output',
]

@pulumi.output_type
class GetStandardResult:
    def __init__(__self__, disabled_standards_controls=None, standards_subscription_arn=None):
        if disabled_standards_controls and not isinstance(disabled_standards_controls, list):
            raise TypeError("Expected argument 'disabled_standards_controls' to be a list")
        pulumi.set(__self__, "disabled_standards_controls", disabled_standards_controls)
        if standards_subscription_arn and not isinstance(standards_subscription_arn, str):
            raise TypeError("Expected argument 'standards_subscription_arn' to be a str")
        pulumi.set(__self__, "standards_subscription_arn", standards_subscription_arn)

    @property
    @pulumi.getter(name="disabledStandardsControls")
    def disabled_standards_controls(self) -> Optional[Sequence['outputs.StandardsControl']]:
        """
        Specifies which controls are to be disabled in a standard. 
         *Maximum*: ``100``
        """
        return pulumi.get(self, "disabled_standards_controls")

    @property
    @pulumi.getter(name="standardsSubscriptionArn")
    def standards_subscription_arn(self) -> Optional[str]:
        """
        The ARN of a resource that represents your subscription to a supported standard.
        """
        return pulumi.get(self, "standards_subscription_arn")


class AwaitableGetStandardResult(GetStandardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStandardResult(
            disabled_standards_controls=self.disabled_standards_controls,
            standards_subscription_arn=self.standards_subscription_arn)


def get_standard(standards_subscription_arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStandardResult:
    """
    The ``AWS::SecurityHub::Standard`` resource specifies the enablement of a security standard. The standard is identified by the ``StandardsArn`` property. To view a list of ASH standards and their Amazon Resource Names (ARNs), use the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API operation.
     You must create a separate ``AWS::SecurityHub::Standard`` resource for each standard that you want to enable.
     For more information about ASH standards, see [standards reference](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html) in the *User Guide*.


    :param str standards_subscription_arn: The ARN of a resource that represents your subscription to a supported standard.
    """
    __args__ = dict()
    __args__['standardsSubscriptionArn'] = standards_subscription_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:securityhub:getStandard', __args__, opts=opts, typ=GetStandardResult).value

    return AwaitableGetStandardResult(
        disabled_standards_controls=pulumi.get(__ret__, 'disabled_standards_controls'),
        standards_subscription_arn=pulumi.get(__ret__, 'standards_subscription_arn'))


@_utilities.lift_output_func(get_standard)
def get_standard_output(standards_subscription_arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStandardResult]:
    """
    The ``AWS::SecurityHub::Standard`` resource specifies the enablement of a security standard. The standard is identified by the ``StandardsArn`` property. To view a list of ASH standards and their Amazon Resource Names (ARNs), use the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API operation.
     You must create a separate ``AWS::SecurityHub::Standard`` resource for each standard that you want to enable.
     For more information about ASH standards, see [standards reference](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html) in the *User Guide*.


    :param str standards_subscription_arn: The ARN of a resource that represents your subscription to a supported standard.
    """
    ...
