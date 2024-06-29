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
from ._inputs import *

__all__ = ['RouteArgs', 'Route']

@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 route_key: pulumi.Input[str],
                 api_key_required: Optional[pulumi.Input[bool]] = None,
                 authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authorization_type: Optional[pulumi.Input[str]] = None,
                 authorizer_id: Optional[pulumi.Input[str]] = None,
                 model_selection_expression: Optional[pulumi.Input[str]] = None,
                 operation_name: Optional[pulumi.Input[str]] = None,
                 request_models: Optional[Any] = None,
                 request_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['RouteParameterConstraintsArgs']]]] = None,
                 route_response_selection_expression: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Route resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] route_key: The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
        :param pulumi.Input[bool] api_key_required: Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] authorization_scopes: The authorization scopes supported by this route.
        :param pulumi.Input[str] authorization_type: The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        :param pulumi.Input[str] authorizer_id: The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        :param pulumi.Input[str] model_selection_expression: The model selection expression for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[str] operation_name: The operation name for the route.
        :param Any request_models: The request models for the route. Supported only for WebSocket APIs.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Route` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input['RouteParameterConstraintsArgs']]] request_parameters: The request parameters for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[str] route_response_selection_expression: The route response selection expression for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[str] target: The target for the route.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "route_key", route_key)
        if api_key_required is not None:
            pulumi.set(__self__, "api_key_required", api_key_required)
        if authorization_scopes is not None:
            pulumi.set(__self__, "authorization_scopes", authorization_scopes)
        if authorization_type is not None:
            pulumi.set(__self__, "authorization_type", authorization_type)
        if authorizer_id is not None:
            pulumi.set(__self__, "authorizer_id", authorizer_id)
        if model_selection_expression is not None:
            pulumi.set(__self__, "model_selection_expression", model_selection_expression)
        if operation_name is not None:
            pulumi.set(__self__, "operation_name", operation_name)
        if request_models is not None:
            pulumi.set(__self__, "request_models", request_models)
        if request_parameters is not None:
            pulumi.set(__self__, "request_parameters", request_parameters)
        if route_response_selection_expression is not None:
            pulumi.set(__self__, "route_response_selection_expression", route_response_selection_expression)
        if target is not None:
            pulumi.set(__self__, "target", target)

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
    @pulumi.getter(name="routeKey")
    def route_key(self) -> pulumi.Input[str]:
        """
        The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
        """
        return pulumi.get(self, "route_key")

    @route_key.setter
    def route_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "route_key", value)

    @property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "api_key_required")

    @api_key_required.setter
    def api_key_required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "api_key_required", value)

    @property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The authorization scopes supported by this route.
        """
        return pulumi.get(self, "authorization_scopes")

    @authorization_scopes.setter
    def authorization_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "authorization_scopes", value)

    @property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[str]]:
        """
        The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        """
        return pulumi.get(self, "authorization_type")

    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_type", value)

    @property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        """
        return pulumi.get(self, "authorizer_id")

    @authorizer_id.setter
    def authorizer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorizer_id", value)

    @property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[pulumi.Input[str]]:
        """
        The model selection expression for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "model_selection_expression")

    @model_selection_expression.setter
    def model_selection_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_selection_expression", value)

    @property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The operation name for the route.
        """
        return pulumi.get(self, "operation_name")

    @operation_name.setter
    def operation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_name", value)

    @property
    @pulumi.getter(name="requestModels")
    def request_models(self) -> Optional[Any]:
        """
        The request models for the route. Supported only for WebSocket APIs.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Route` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "request_models")

    @request_models.setter
    def request_models(self, value: Optional[Any]):
        pulumi.set(self, "request_models", value)

    @property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RouteParameterConstraintsArgs']]]]:
        """
        The request parameters for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "request_parameters")

    @request_parameters.setter
    def request_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RouteParameterConstraintsArgs']]]]):
        pulumi.set(self, "request_parameters", value)

    @property
    @pulumi.getter(name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> Optional[pulumi.Input[str]]:
        """
        The route response selection expression for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "route_response_selection_expression")

    @route_response_selection_expression.setter
    def route_response_selection_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_response_selection_expression", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The target for the route.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)


class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 api_key_required: Optional[pulumi.Input[bool]] = None,
                 authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authorization_type: Optional[pulumi.Input[str]] = None,
                 authorizer_id: Optional[pulumi.Input[str]] = None,
                 model_selection_expression: Optional[pulumi.Input[str]] = None,
                 operation_name: Optional[pulumi.Input[str]] = None,
                 request_models: Optional[Any] = None,
                 request_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteParameterConstraintsArgs']]]]] = None,
                 route_key: Optional[pulumi.Input[str]] = None,
                 route_response_selection_expression: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The ``AWS::ApiGatewayV2::Route`` resource creates a route for an API.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[bool] api_key_required: Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] authorization_scopes: The authorization scopes supported by this route.
        :param pulumi.Input[str] authorization_type: The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        :param pulumi.Input[str] authorizer_id: The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        :param pulumi.Input[str] model_selection_expression: The model selection expression for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[str] operation_name: The operation name for the route.
        :param Any request_models: The request models for the route. Supported only for WebSocket APIs.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Route` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteParameterConstraintsArgs']]]] request_parameters: The request parameters for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[str] route_key: The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
        :param pulumi.Input[str] route_response_selection_expression: The route response selection expression for the route. Supported only for WebSocket APIs.
        :param pulumi.Input[str] target: The target for the route.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``AWS::ApiGatewayV2::Route`` resource creates a route for an API.

        :param str resource_name: The name of the resource.
        :param RouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 api_key_required: Optional[pulumi.Input[bool]] = None,
                 authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authorization_type: Optional[pulumi.Input[str]] = None,
                 authorizer_id: Optional[pulumi.Input[str]] = None,
                 model_selection_expression: Optional[pulumi.Input[str]] = None,
                 operation_name: Optional[pulumi.Input[str]] = None,
                 request_models: Optional[Any] = None,
                 request_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteParameterConstraintsArgs']]]]] = None,
                 route_key: Optional[pulumi.Input[str]] = None,
                 route_response_selection_expression: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteArgs.__new__(RouteArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["api_key_required"] = api_key_required
            __props__.__dict__["authorization_scopes"] = authorization_scopes
            __props__.__dict__["authorization_type"] = authorization_type
            __props__.__dict__["authorizer_id"] = authorizer_id
            __props__.__dict__["model_selection_expression"] = model_selection_expression
            __props__.__dict__["operation_name"] = operation_name
            __props__.__dict__["request_models"] = request_models
            __props__.__dict__["request_parameters"] = request_parameters
            if route_key is None and not opts.urn:
                raise TypeError("Missing required property 'route_key'")
            __props__.__dict__["route_key"] = route_key
            __props__.__dict__["route_response_selection_expression"] = route_response_selection_expression
            __props__.__dict__["target"] = target
            __props__.__dict__["route_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["apiId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Route, __self__).__init__(
            'aws-native:apigatewayv2:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RouteArgs.__new__(RouteArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["api_key_required"] = None
        __props__.__dict__["authorization_scopes"] = None
        __props__.__dict__["authorization_type"] = None
        __props__.__dict__["authorizer_id"] = None
        __props__.__dict__["model_selection_expression"] = None
        __props__.__dict__["operation_name"] = None
        __props__.__dict__["request_models"] = None
        __props__.__dict__["request_parameters"] = None
        __props__.__dict__["route_id"] = None
        __props__.__dict__["route_key"] = None
        __props__.__dict__["route_response_selection_expression"] = None
        __props__.__dict__["target"] = None
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "api_key_required")

    @property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The authorization scopes supported by this route.
        """
        return pulumi.get(self, "authorization_scopes")

    @property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Output[Optional[str]]:
        """
        The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        """
        return pulumi.get(self, "authorization_type")

    @property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        """
        return pulumi.get(self, "authorizer_id")

    @property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> pulumi.Output[Optional[str]]:
        """
        The model selection expression for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "model_selection_expression")

    @property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> pulumi.Output[Optional[str]]:
        """
        The operation name for the route.
        """
        return pulumi.get(self, "operation_name")

    @property
    @pulumi.getter(name="requestModels")
    def request_models(self) -> pulumi.Output[Optional[Any]]:
        """
        The request models for the route. Supported only for WebSocket APIs.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Route` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "request_models")

    @property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.RouteParameterConstraints']]]:
        """
        The request parameters for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "request_parameters")

    @property
    @pulumi.getter(name="routeId")
    def route_id(self) -> pulumi.Output[str]:
        """
        The route ID.
        """
        return pulumi.get(self, "route_id")

    @property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> pulumi.Output[str]:
        """
        The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
        """
        return pulumi.get(self, "route_key")

    @property
    @pulumi.getter(name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> pulumi.Output[Optional[str]]:
        """
        The route response selection expression for the route. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "route_response_selection_expression")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[str]]:
        """
        The target for the route.
        """
        return pulumi.get(self, "target")

