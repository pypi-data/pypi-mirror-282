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
    'GetUserPoolUiCustomizationAttachmentResult',
    'AwaitableGetUserPoolUiCustomizationAttachmentResult',
    'get_user_pool_ui_customization_attachment',
    'get_user_pool_ui_customization_attachment_output',
]

@pulumi.output_type
class GetUserPoolUiCustomizationAttachmentResult:
    def __init__(__self__, css=None, id=None):
        if css and not isinstance(css, str):
            raise TypeError("Expected argument 'css' to be a str")
        pulumi.set(__self__, "css", css)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def css(self) -> Optional[str]:
        """
        The CSS values in the UI customization.
        """
        return pulumi.get(self, "css")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")


class AwaitableGetUserPoolUiCustomizationAttachmentResult(GetUserPoolUiCustomizationAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolUiCustomizationAttachmentResult(
            css=self.css,
            id=self.id)


def get_user_pool_ui_customization_attachment(id: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPoolUiCustomizationAttachmentResult:
    """
    Resource Type definition for AWS::Cognito::UserPoolUICustomizationAttachment


    :param str id: The resource ID.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cognito:getUserPoolUiCustomizationAttachment', __args__, opts=opts, typ=GetUserPoolUiCustomizationAttachmentResult).value

    return AwaitableGetUserPoolUiCustomizationAttachmentResult(
        css=pulumi.get(__ret__, 'css'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_user_pool_ui_customization_attachment)
def get_user_pool_ui_customization_attachment_output(id: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPoolUiCustomizationAttachmentResult]:
    """
    Resource Type definition for AWS::Cognito::UserPoolUICustomizationAttachment


    :param str id: The resource ID.
    """
    ...
