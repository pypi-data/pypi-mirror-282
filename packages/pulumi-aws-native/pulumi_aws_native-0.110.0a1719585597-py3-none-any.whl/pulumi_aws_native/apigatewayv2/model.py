# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ModelArgs', 'Model']

@pulumi.input_type
class ModelArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 schema: Any,
                 content_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Model resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param Any schema: The schema for the model. For application/json models, this should be JSON schema draft 4 model.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Model` for more information about the expected schema for this property.
        :param pulumi.Input[str] content_type: The content-type for the model, for example, "application/json".
        :param pulumi.Input[str] description: The description of the model.
        :param pulumi.Input[str] name: The name of the model.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "schema", schema)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def schema(self) -> Any:
        """
        The schema for the model. For application/json models, this should be JSON schema draft 4 model.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Model` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Any):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        The content-type for the model, for example, "application/json".
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the model.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the model.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Model(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema: Optional[Any] = None,
                 __props__=None):
        """
        The ``AWS::ApiGatewayV2::Model`` resource updates data model for a WebSocket API. For more information, see [Model Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) in the *API Gateway Developer Guide*.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] content_type: The content-type for the model, for example, "application/json".
        :param pulumi.Input[str] description: The description of the model.
        :param pulumi.Input[str] name: The name of the model.
        :param Any schema: The schema for the model. For application/json models, this should be JSON schema draft 4 model.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Model` for more information about the expected schema for this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``AWS::ApiGatewayV2::Model`` resource updates data model for a WebSocket API. For more information, see [Model Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) in the *API Gateway Developer Guide*.

        :param str resource_name: The name of the resource.
        :param ModelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModelArgs.__new__(ModelArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if schema is None and not opts.urn:
                raise TypeError("Missing required property 'schema'")
            __props__.__dict__["schema"] = schema
            __props__.__dict__["model_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["apiId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Model, __self__).__init__(
            'aws-native:apigatewayv2:Model',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Model':
        """
        Get an existing Model resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ModelArgs.__new__(ModelArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["content_type"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["model_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schema"] = None
        return Model(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        """
        The content-type for the model, for example, "application/json".
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the model.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Output[str]:
        """
        The model ID.
        """
        return pulumi.get(self, "model_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the model.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Any]:
        """
        The schema for the model. For application/json models, this should be JSON schema draft 4 model.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Model` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "schema")

