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
    'GetFindingsFilterResult',
    'AwaitableGetFindingsFilterResult',
    'get_findings_filter',
    'get_findings_filter_output',
]

@pulumi.output_type
class GetFindingsFilterResult:
    def __init__(__self__, action=None, arn=None, description=None, finding_criteria=None, id=None, name=None, position=None, tags=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if finding_criteria and not isinstance(finding_criteria, dict):
            raise TypeError("Expected argument 'finding_criteria' to be a dict")
        pulumi.set(__self__, "finding_criteria", finding_criteria)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if position and not isinstance(position, int):
            raise TypeError("Expected argument 'position' to be a int")
        pulumi.set(__self__, "position", position)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def action(self) -> Optional['FindingsFilterFindingFilterAction']:
        """
        Findings filter action.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Findings filter ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Findings filter description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="findingCriteria")
    def finding_criteria(self) -> Optional['outputs.FindingsFilterFindingCriteria']:
        """
        Findings filter criteria.
        """
        return pulumi.get(self, "finding_criteria")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Findings filter ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Findings filter name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def position(self) -> Optional[int]:
        """
        Findings filter position.
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")


class AwaitableGetFindingsFilterResult(GetFindingsFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFindingsFilterResult(
            action=self.action,
            arn=self.arn,
            description=self.description,
            finding_criteria=self.finding_criteria,
            id=self.id,
            name=self.name,
            position=self.position,
            tags=self.tags)


def get_findings_filter(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFindingsFilterResult:
    """
    Macie FindingsFilter resource schema.


    :param str id: Findings filter ID.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:macie:getFindingsFilter', __args__, opts=opts, typ=GetFindingsFilterResult).value

    return AwaitableGetFindingsFilterResult(
        action=pulumi.get(__ret__, 'action'),
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        finding_criteria=pulumi.get(__ret__, 'finding_criteria'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        position=pulumi.get(__ret__, 'position'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_findings_filter)
def get_findings_filter_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFindingsFilterResult]:
    """
    Macie FindingsFilter resource schema.


    :param str id: Findings filter ID.
    """
    ...
