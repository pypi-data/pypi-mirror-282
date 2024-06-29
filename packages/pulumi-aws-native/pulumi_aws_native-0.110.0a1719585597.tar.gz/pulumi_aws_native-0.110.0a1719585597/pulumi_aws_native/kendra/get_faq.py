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
    'GetFaqResult',
    'AwaitableGetFaqResult',
    'get_faq',
    'get_faq_output',
]

@pulumi.output_type
class GetFaqResult:
    def __init__(__self__, arn=None, id=None, language_code=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if language_code and not isinstance(language_code, str):
            raise TypeError("Expected argument 'language_code' to be a str")
        pulumi.set(__self__, "language_code", language_code)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        `arn:aws:kendra:us-west-2:111122223333:index/335c3741-41df-46a6-b5d3-61f85b787884/faq/f61995a6-cd5c-4e99-9cfc-58816d8bfaa7`
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The identifier for the FAQ. For example:

        `f61995a6-cd5c-4e99-9cfc-58816d8bfaa7`
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[str]:
        """
        The code for a language. This shows a supported language for the FAQ document as part of the summary information for FAQs. English is supported by default. For more information on supported languages, including their codes, see [Adding documents in languages other than English](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html) .
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Tags for labeling the FAQ
        """
        return pulumi.get(self, "tags")


class AwaitableGetFaqResult(GetFaqResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFaqResult(
            arn=self.arn,
            id=self.id,
            language_code=self.language_code,
            tags=self.tags)


def get_faq(id: Optional[str] = None,
            index_id: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFaqResult:
    """
    A Kendra FAQ resource


    :param str id: The identifier for the FAQ. For example:
           
           `f61995a6-cd5c-4e99-9cfc-58816d8bfaa7`
    :param str index_id: Index ID
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kendra:getFaq', __args__, opts=opts, typ=GetFaqResult).value

    return AwaitableGetFaqResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        language_code=pulumi.get(__ret__, 'language_code'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_faq)
def get_faq_output(id: Optional[pulumi.Input[str]] = None,
                   index_id: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFaqResult]:
    """
    A Kendra FAQ resource


    :param str id: The identifier for the FAQ. For example:
           
           `f61995a6-cd5c-4e99-9cfc-58816d8bfaa7`
    :param str index_id: Index ID
    """
    ...
