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
    'GetNetworkInsightsAnalysisResult',
    'AwaitableGetNetworkInsightsAnalysisResult',
    'get_network_insights_analysis',
    'get_network_insights_analysis_output',
]

@pulumi.output_type
class GetNetworkInsightsAnalysisResult:
    def __init__(__self__, additional_accounts=None, alternate_path_hints=None, explanations=None, forward_path_components=None, network_insights_analysis_arn=None, network_insights_analysis_id=None, network_path_found=None, return_path_components=None, start_date=None, status=None, status_message=None, suggested_accounts=None, tags=None):
        if additional_accounts and not isinstance(additional_accounts, list):
            raise TypeError("Expected argument 'additional_accounts' to be a list")
        pulumi.set(__self__, "additional_accounts", additional_accounts)
        if alternate_path_hints and not isinstance(alternate_path_hints, list):
            raise TypeError("Expected argument 'alternate_path_hints' to be a list")
        pulumi.set(__self__, "alternate_path_hints", alternate_path_hints)
        if explanations and not isinstance(explanations, list):
            raise TypeError("Expected argument 'explanations' to be a list")
        pulumi.set(__self__, "explanations", explanations)
        if forward_path_components and not isinstance(forward_path_components, list):
            raise TypeError("Expected argument 'forward_path_components' to be a list")
        pulumi.set(__self__, "forward_path_components", forward_path_components)
        if network_insights_analysis_arn and not isinstance(network_insights_analysis_arn, str):
            raise TypeError("Expected argument 'network_insights_analysis_arn' to be a str")
        pulumi.set(__self__, "network_insights_analysis_arn", network_insights_analysis_arn)
        if network_insights_analysis_id and not isinstance(network_insights_analysis_id, str):
            raise TypeError("Expected argument 'network_insights_analysis_id' to be a str")
        pulumi.set(__self__, "network_insights_analysis_id", network_insights_analysis_id)
        if network_path_found and not isinstance(network_path_found, bool):
            raise TypeError("Expected argument 'network_path_found' to be a bool")
        pulumi.set(__self__, "network_path_found", network_path_found)
        if return_path_components and not isinstance(return_path_components, list):
            raise TypeError("Expected argument 'return_path_components' to be a list")
        pulumi.set(__self__, "return_path_components", return_path_components)
        if start_date and not isinstance(start_date, str):
            raise TypeError("Expected argument 'start_date' to be a str")
        pulumi.set(__self__, "start_date", start_date)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)
        if suggested_accounts and not isinstance(suggested_accounts, list):
            raise TypeError("Expected argument 'suggested_accounts' to be a list")
        pulumi.set(__self__, "suggested_accounts", suggested_accounts)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="additionalAccounts")
    def additional_accounts(self) -> Optional[Sequence[str]]:
        """
        The member accounts that contain resources that the path can traverse.
        """
        return pulumi.get(self, "additional_accounts")

    @property
    @pulumi.getter(name="alternatePathHints")
    def alternate_path_hints(self) -> Optional[Sequence['outputs.NetworkInsightsAnalysisAlternatePathHint']]:
        """
        Potential intermediate components.
        """
        return pulumi.get(self, "alternate_path_hints")

    @property
    @pulumi.getter
    def explanations(self) -> Optional[Sequence['outputs.NetworkInsightsAnalysisExplanation']]:
        """
        The explanations. For more information, see [Reachability Analyzer explanation codes](https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html) .
        """
        return pulumi.get(self, "explanations")

    @property
    @pulumi.getter(name="forwardPathComponents")
    def forward_path_components(self) -> Optional[Sequence['outputs.NetworkInsightsAnalysisPathComponent']]:
        """
        The components in the path from source to destination.
        """
        return pulumi.get(self, "forward_path_components")

    @property
    @pulumi.getter(name="networkInsightsAnalysisArn")
    def network_insights_analysis_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the network insights analysis.
        """
        return pulumi.get(self, "network_insights_analysis_arn")

    @property
    @pulumi.getter(name="networkInsightsAnalysisId")
    def network_insights_analysis_id(self) -> Optional[str]:
        """
        The ID of the network insights analysis.
        """
        return pulumi.get(self, "network_insights_analysis_id")

    @property
    @pulumi.getter(name="networkPathFound")
    def network_path_found(self) -> Optional[bool]:
        """
        Indicates whether the destination is reachable from the source.
        """
        return pulumi.get(self, "network_path_found")

    @property
    @pulumi.getter(name="returnPathComponents")
    def return_path_components(self) -> Optional[Sequence['outputs.NetworkInsightsAnalysisPathComponent']]:
        """
        The components in the path from destination to source.
        """
        return pulumi.get(self, "return_path_components")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[str]:
        """
        The time the analysis started.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def status(self) -> Optional['NetworkInsightsAnalysisStatus']:
        """
        The status of the network insights analysis.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[str]:
        """
        The status message, if the status is `failed` .
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="suggestedAccounts")
    def suggested_accounts(self) -> Optional[Sequence[str]]:
        """
        The IDs of potential intermediate accounts.
        """
        return pulumi.get(self, "suggested_accounts")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags to apply.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNetworkInsightsAnalysisResult(GetNetworkInsightsAnalysisResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInsightsAnalysisResult(
            additional_accounts=self.additional_accounts,
            alternate_path_hints=self.alternate_path_hints,
            explanations=self.explanations,
            forward_path_components=self.forward_path_components,
            network_insights_analysis_arn=self.network_insights_analysis_arn,
            network_insights_analysis_id=self.network_insights_analysis_id,
            network_path_found=self.network_path_found,
            return_path_components=self.return_path_components,
            start_date=self.start_date,
            status=self.status,
            status_message=self.status_message,
            suggested_accounts=self.suggested_accounts,
            tags=self.tags)


def get_network_insights_analysis(network_insights_analysis_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInsightsAnalysisResult:
    """
    Resource schema for AWS::EC2::NetworkInsightsAnalysis


    :param str network_insights_analysis_id: The ID of the network insights analysis.
    """
    __args__ = dict()
    __args__['networkInsightsAnalysisId'] = network_insights_analysis_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNetworkInsightsAnalysis', __args__, opts=opts, typ=GetNetworkInsightsAnalysisResult).value

    return AwaitableGetNetworkInsightsAnalysisResult(
        additional_accounts=pulumi.get(__ret__, 'additional_accounts'),
        alternate_path_hints=pulumi.get(__ret__, 'alternate_path_hints'),
        explanations=pulumi.get(__ret__, 'explanations'),
        forward_path_components=pulumi.get(__ret__, 'forward_path_components'),
        network_insights_analysis_arn=pulumi.get(__ret__, 'network_insights_analysis_arn'),
        network_insights_analysis_id=pulumi.get(__ret__, 'network_insights_analysis_id'),
        network_path_found=pulumi.get(__ret__, 'network_path_found'),
        return_path_components=pulumi.get(__ret__, 'return_path_components'),
        start_date=pulumi.get(__ret__, 'start_date'),
        status=pulumi.get(__ret__, 'status'),
        status_message=pulumi.get(__ret__, 'status_message'),
        suggested_accounts=pulumi.get(__ret__, 'suggested_accounts'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network_insights_analysis)
def get_network_insights_analysis_output(network_insights_analysis_id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkInsightsAnalysisResult]:
    """
    Resource schema for AWS::EC2::NetworkInsightsAnalysis


    :param str network_insights_analysis_id: The ID of the network insights analysis.
    """
    ...
