# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetUrlSuffixResult',
    'AwaitableGetUrlSuffixResult',
    'get_url_suffix',
    'get_url_suffix_output',
]

@pulumi.output_type
class GetUrlSuffixResult:
    def __init__(__self__, url_suffix=None):
        if url_suffix and not isinstance(url_suffix, str):
            raise TypeError("Expected argument 'url_suffix' to be a str")
        pulumi.set(__self__, "url_suffix", url_suffix)

    @property
    @pulumi.getter(name="urlSuffix")
    def url_suffix(self) -> str:
        return pulumi.get(self, "url_suffix")


class AwaitableGetUrlSuffixResult(GetUrlSuffixResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUrlSuffixResult(
            url_suffix=self.url_suffix)


def get_url_suffix(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUrlSuffixResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:index:getUrlSuffix', __args__, opts=opts, typ=GetUrlSuffixResult).value

    return AwaitableGetUrlSuffixResult(
        url_suffix=pulumi.get(__ret__, 'url_suffix'))


@_utilities.lift_output_func(get_url_suffix)
def get_url_suffix_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUrlSuffixResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
