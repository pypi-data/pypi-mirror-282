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
    'GetAnalysisResult',
    'AwaitableGetAnalysisResult',
    'get_analysis',
    'get_analysis_output',
]

@pulumi.output_type
class GetAnalysisResult:
    def __init__(__self__, arn=None, created_time=None, data_set_arns=None, errors=None, last_updated_time=None, name=None, permissions=None, sheets=None, tags=None, theme_arn=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if data_set_arns and not isinstance(data_set_arns, list):
            raise TypeError("Expected argument 'data_set_arns' to be a list")
        pulumi.set(__self__, "data_set_arns", data_set_arns)
        if errors and not isinstance(errors, list):
            raise TypeError("Expected argument 'errors' to be a list")
        pulumi.set(__self__, "errors", errors)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if sheets and not isinstance(sheets, list):
            raise TypeError("Expected argument 'sheets' to be a list")
        pulumi.set(__self__, "sheets", sheets)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if theme_arn and not isinstance(theme_arn, str):
            raise TypeError("Expected argument 'theme_arn' to be a str")
        pulumi.set(__self__, "theme_arn", theme_arn)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        <p>The Amazon Resource Name (ARN) of the analysis.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        <p>The time that the analysis was created.</p>
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="dataSetArns")
    def data_set_arns(self) -> Optional[Sequence[str]]:
        """
        <p>The ARNs of the datasets of the analysis.</p>
        """
        return pulumi.get(self, "data_set_arns")

    @property
    @pulumi.getter
    def errors(self) -> Optional[Sequence['outputs.AnalysisError']]:
        """
        <p>Errors associated with the analysis.</p>
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        <p>The time that the analysis was last updated.</p>
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        <p>The descriptive name of the analysis.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence['outputs.AnalysisResourcePermission']]:
        """
        A structure that describes the principals and the resource-level permissions on an analysis. You can use the `Permissions` structure to grant permissions by providing a list of AWS Identity and Access Management (IAM) action information for each principal listed by Amazon Resource Name (ARN).

        To specify no permissions, omit `Permissions` .
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def sheets(self) -> Optional[Sequence['outputs.AnalysisSheet']]:
        """
        <p>A list of the associated sheets with the unique identifier and name of each sheet.</p>
        """
        return pulumi.get(self, "sheets")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Contains a map of the key-value pairs for the resource tag or tags assigned to the analysis.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> Optional[str]:
        """
        <p>The ARN of the theme of the analysis.</p>
        """
        return pulumi.get(self, "theme_arn")


class AwaitableGetAnalysisResult(GetAnalysisResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAnalysisResult(
            arn=self.arn,
            created_time=self.created_time,
            data_set_arns=self.data_set_arns,
            errors=self.errors,
            last_updated_time=self.last_updated_time,
            name=self.name,
            permissions=self.permissions,
            sheets=self.sheets,
            tags=self.tags,
            theme_arn=self.theme_arn)


def get_analysis(analysis_id: Optional[str] = None,
                 aws_account_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAnalysisResult:
    """
    Definition of the AWS::QuickSight::Analysis Resource Type.


    :param str analysis_id: The ID for the analysis that you're creating. This ID displays in the URL of the analysis.
    :param str aws_account_id: The ID of the AWS account where you are creating an analysis.
    """
    __args__ = dict()
    __args__['analysisId'] = analysis_id
    __args__['awsAccountId'] = aws_account_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:quicksight:getAnalysis', __args__, opts=opts, typ=GetAnalysisResult).value

    return AwaitableGetAnalysisResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        data_set_arns=pulumi.get(__ret__, 'data_set_arns'),
        errors=pulumi.get(__ret__, 'errors'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        name=pulumi.get(__ret__, 'name'),
        permissions=pulumi.get(__ret__, 'permissions'),
        sheets=pulumi.get(__ret__, 'sheets'),
        tags=pulumi.get(__ret__, 'tags'),
        theme_arn=pulumi.get(__ret__, 'theme_arn'))


@_utilities.lift_output_func(get_analysis)
def get_analysis_output(analysis_id: Optional[pulumi.Input[str]] = None,
                        aws_account_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAnalysisResult]:
    """
    Definition of the AWS::QuickSight::Analysis Resource Type.


    :param str analysis_id: The ID for the analysis that you're creating. This ID displays in the URL of the analysis.
    :param str aws_account_id: The ID of the AWS account where you are creating an analysis.
    """
    ...
