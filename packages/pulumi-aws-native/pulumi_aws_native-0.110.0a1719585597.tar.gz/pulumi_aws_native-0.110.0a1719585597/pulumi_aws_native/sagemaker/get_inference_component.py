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
    'GetInferenceComponentResult',
    'AwaitableGetInferenceComponentResult',
    'get_inference_component',
    'get_inference_component_output',
]

@pulumi.output_type
class GetInferenceComponentResult:
    def __init__(__self__, creation_time=None, endpoint_arn=None, endpoint_name=None, failure_reason=None, inference_component_arn=None, inference_component_name=None, inference_component_status=None, last_modified_time=None, runtime_config=None, specification=None, tags=None, variant_name=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if endpoint_arn and not isinstance(endpoint_arn, str):
            raise TypeError("Expected argument 'endpoint_arn' to be a str")
        pulumi.set(__self__, "endpoint_arn", endpoint_arn)
        if endpoint_name and not isinstance(endpoint_name, str):
            raise TypeError("Expected argument 'endpoint_name' to be a str")
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        if failure_reason and not isinstance(failure_reason, str):
            raise TypeError("Expected argument 'failure_reason' to be a str")
        pulumi.set(__self__, "failure_reason", failure_reason)
        if inference_component_arn and not isinstance(inference_component_arn, str):
            raise TypeError("Expected argument 'inference_component_arn' to be a str")
        pulumi.set(__self__, "inference_component_arn", inference_component_arn)
        if inference_component_name and not isinstance(inference_component_name, str):
            raise TypeError("Expected argument 'inference_component_name' to be a str")
        pulumi.set(__self__, "inference_component_name", inference_component_name)
        if inference_component_status and not isinstance(inference_component_status, str):
            raise TypeError("Expected argument 'inference_component_status' to be a str")
        pulumi.set(__self__, "inference_component_status", inference_component_status)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if runtime_config and not isinstance(runtime_config, dict):
            raise TypeError("Expected argument 'runtime_config' to be a dict")
        pulumi.set(__self__, "runtime_config", runtime_config)
        if specification and not isinstance(specification, dict):
            raise TypeError("Expected argument 'specification' to be a dict")
        pulumi.set(__self__, "specification", specification)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if variant_name and not isinstance(variant_name, str):
            raise TypeError("Expected argument 'variant_name' to be a str")
        pulumi.set(__self__, "variant_name", variant_name)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The time when the inference component was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="endpointArn")
    def endpoint_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.
        """
        return pulumi.get(self, "endpoint_arn")

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[str]:
        """
        The name of the endpoint that hosts the inference component.
        """
        return pulumi.get(self, "endpoint_name")

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[str]:
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter(name="inferenceComponentArn")
    def inference_component_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the inference component.
        """
        return pulumi.get(self, "inference_component_arn")

    @property
    @pulumi.getter(name="inferenceComponentName")
    def inference_component_name(self) -> Optional[str]:
        """
        The name of the inference component.
        """
        return pulumi.get(self, "inference_component_name")

    @property
    @pulumi.getter(name="inferenceComponentStatus")
    def inference_component_status(self) -> Optional['InferenceComponentStatus']:
        """
        The status of the inference component.
        """
        return pulumi.get(self, "inference_component_status")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        """
        The time when the inference component was last updated.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(self) -> Optional['outputs.InferenceComponentRuntimeConfig']:
        return pulumi.get(self, "runtime_config")

    @property
    @pulumi.getter
    def specification(self) -> Optional['outputs.InferenceComponentSpecification']:
        return pulumi.get(self, "specification")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="variantName")
    def variant_name(self) -> Optional[str]:
        """
        The name of the production variant that hosts the inference component.
        """
        return pulumi.get(self, "variant_name")


class AwaitableGetInferenceComponentResult(GetInferenceComponentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInferenceComponentResult(
            creation_time=self.creation_time,
            endpoint_arn=self.endpoint_arn,
            endpoint_name=self.endpoint_name,
            failure_reason=self.failure_reason,
            inference_component_arn=self.inference_component_arn,
            inference_component_name=self.inference_component_name,
            inference_component_status=self.inference_component_status,
            last_modified_time=self.last_modified_time,
            runtime_config=self.runtime_config,
            specification=self.specification,
            tags=self.tags,
            variant_name=self.variant_name)


def get_inference_component(inference_component_arn: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInferenceComponentResult:
    """
    Resource Type definition for AWS::SageMaker::InferenceComponent


    :param str inference_component_arn: The Amazon Resource Name (ARN) of the inference component.
    """
    __args__ = dict()
    __args__['inferenceComponentArn'] = inference_component_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getInferenceComponent', __args__, opts=opts, typ=GetInferenceComponentResult).value

    return AwaitableGetInferenceComponentResult(
        creation_time=pulumi.get(__ret__, 'creation_time'),
        endpoint_arn=pulumi.get(__ret__, 'endpoint_arn'),
        endpoint_name=pulumi.get(__ret__, 'endpoint_name'),
        failure_reason=pulumi.get(__ret__, 'failure_reason'),
        inference_component_arn=pulumi.get(__ret__, 'inference_component_arn'),
        inference_component_name=pulumi.get(__ret__, 'inference_component_name'),
        inference_component_status=pulumi.get(__ret__, 'inference_component_status'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        runtime_config=pulumi.get(__ret__, 'runtime_config'),
        specification=pulumi.get(__ret__, 'specification'),
        tags=pulumi.get(__ret__, 'tags'),
        variant_name=pulumi.get(__ret__, 'variant_name'))


@_utilities.lift_output_func(get_inference_component)
def get_inference_component_output(inference_component_arn: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInferenceComponentResult]:
    """
    Resource Type definition for AWS::SageMaker::InferenceComponent


    :param str inference_component_arn: The Amazon Resource Name (ARN) of the inference component.
    """
    ...
