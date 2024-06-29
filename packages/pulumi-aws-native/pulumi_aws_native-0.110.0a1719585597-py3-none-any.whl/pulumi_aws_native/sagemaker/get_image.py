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
    'GetImageResult',
    'AwaitableGetImageResult',
    'get_image',
    'get_image_output',
]

@pulumi.output_type
class GetImageResult:
    def __init__(__self__, image_arn=None, image_description=None, image_display_name=None, image_role_arn=None, tags=None):
        if image_arn and not isinstance(image_arn, str):
            raise TypeError("Expected argument 'image_arn' to be a str")
        pulumi.set(__self__, "image_arn", image_arn)
        if image_description and not isinstance(image_description, str):
            raise TypeError("Expected argument 'image_description' to be a str")
        pulumi.set(__self__, "image_description", image_description)
        if image_display_name and not isinstance(image_display_name, str):
            raise TypeError("Expected argument 'image_display_name' to be a str")
        pulumi.set(__self__, "image_display_name", image_display_name)
        if image_role_arn and not isinstance(image_role_arn, str):
            raise TypeError("Expected argument 'image_role_arn' to be a str")
        pulumi.set(__self__, "image_role_arn", image_role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the image.

        *Type* : String

        *Length Constraints* : Maximum length of 256.

        *Pattern* : `^arn:aws(-[\\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-z0-9]([-.]?[a-z0-9])*$`
        """
        return pulumi.get(self, "image_arn")

    @property
    @pulumi.getter(name="imageDescription")
    def image_description(self) -> Optional[str]:
        """
        The description of the image.
        """
        return pulumi.get(self, "image_description")

    @property
    @pulumi.getter(name="imageDisplayName")
    def image_display_name(self) -> Optional[str]:
        """
        The display name of the image.

        *Length Constraints* : Minimum length of 1. Maximum length of 128.

        *Pattern* : `^\\S(.*\\S)?$`
        """
        return pulumi.get(self, "image_display_name")

    @property
    @pulumi.getter(name="imageRoleArn")
    def image_role_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.

        *Length Constraints* : Minimum length of 20. Maximum length of 2048.

        *Pattern* : `^arn:aws[a-z\\-]*:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+$`
        """
        return pulumi.get(self, "image_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            image_arn=self.image_arn,
            image_description=self.image_description,
            image_display_name=self.image_display_name,
            image_role_arn=self.image_role_arn,
            tags=self.tags)


def get_image(image_arn: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageResult:
    """
    Resource Type definition for AWS::SageMaker::Image


    :param str image_arn: The Amazon Resource Name (ARN) of the image.
           
           *Type* : String
           
           *Length Constraints* : Maximum length of 256.
           
           *Pattern* : `^arn:aws(-[\\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-z0-9]([-.]?[a-z0-9])*$`
    """
    __args__ = dict()
    __args__['imageArn'] = image_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getImage', __args__, opts=opts, typ=GetImageResult).value

    return AwaitableGetImageResult(
        image_arn=pulumi.get(__ret__, 'image_arn'),
        image_description=pulumi.get(__ret__, 'image_description'),
        image_display_name=pulumi.get(__ret__, 'image_display_name'),
        image_role_arn=pulumi.get(__ret__, 'image_role_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_image)
def get_image_output(image_arn: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImageResult]:
    """
    Resource Type definition for AWS::SageMaker::Image


    :param str image_arn: The Amazon Resource Name (ARN) of the image.
           
           *Type* : String
           
           *Length Constraints* : Maximum length of 256.
           
           *Pattern* : `^arn:aws(-[\\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-z0-9]([-.]?[a-z0-9])*$`
    """
    ...
