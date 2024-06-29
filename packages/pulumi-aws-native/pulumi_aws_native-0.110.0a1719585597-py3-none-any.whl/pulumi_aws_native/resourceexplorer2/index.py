# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['IndexArgs', 'Index']

@pulumi.input_type
class IndexArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['IndexType'],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Index resource.
        :param pulumi.Input['IndexType'] type: Specifies the type of the index in this Region. For information about the aggregator index and how it differs from a local index, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the *AWS Resource Explorer User Guide.* .
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The specified tags are attached to only the index created in this AWS Region . The tags don't attach to any of the resources listed in the index.
        """
        pulumi.set(__self__, "type", type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['IndexType']:
        """
        Specifies the type of the index in this Region. For information about the aggregator index and how it differs from a local index, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the *AWS Resource Explorer User Guide.* .
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['IndexType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The specified tags are attached to only the index created in this AWS Region . The tags don't attach to any of the resources listed in the index.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Index(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input['IndexType']] = None,
                 __props__=None):
        """
        Definition of AWS::ResourceExplorer2::Index Resource Type

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        sample_index = aws_native.resourceexplorer2.Index("sampleIndex",
            type=aws_native.resourceexplorer2.IndexType.AGGREGATOR,
            tags={
                "purpose": "ResourceExplorer Sample Stack",
            })

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        sample_index = aws_native.resourceexplorer2.Index("sampleIndex",
            type=aws_native.resourceexplorer2.IndexType.AGGREGATOR,
            tags={
                "purpose": "ResourceExplorer Sample Stack",
            })

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The specified tags are attached to only the index created in this AWS Region . The tags don't attach to any of the resources listed in the index.
        :param pulumi.Input['IndexType'] type: Specifies the type of the index in this Region. For information about the aggregator index and how it differs from a local index, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the *AWS Resource Explorer User Guide.* .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IndexArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::ResourceExplorer2::Index Resource Type

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        sample_index = aws_native.resourceexplorer2.Index("sampleIndex",
            type=aws_native.resourceexplorer2.IndexType.AGGREGATOR,
            tags={
                "purpose": "ResourceExplorer Sample Stack",
            })

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        sample_index = aws_native.resourceexplorer2.Index("sampleIndex",
            type=aws_native.resourceexplorer2.IndexType.AGGREGATOR,
            tags={
                "purpose": "ResourceExplorer Sample Stack",
            })

        ```

        :param str resource_name: The name of the resource.
        :param IndexArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IndexArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input['IndexType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IndexArgs.__new__(IndexArgs)

            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["arn"] = None
            __props__.__dict__["index_state"] = None
        super(Index, __self__).__init__(
            'aws-native:resourceexplorer2:Index',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Index':
        """
        Get an existing Index resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IndexArgs.__new__(IndexArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["index_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Index(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the new index for the AWS Region . For example:

        `arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222`
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="indexState")
    def index_state(self) -> pulumi.Output['IndexState']:
        """
        Indicates the current state of the index. For example:

        `CREATING`
        """
        return pulumi.get(self, "index_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The specified tags are attached to only the index created in this AWS Region . The tags don't attach to any of the resources listed in the index.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['IndexType']:
        """
        Specifies the type of the index in this Region. For information about the aggregator index and how it differs from a local index, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) in the *AWS Resource Explorer User Guide.* .
        """
        return pulumi.get(self, "type")

