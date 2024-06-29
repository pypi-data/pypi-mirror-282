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

__all__ = [
    'GetRouteResponseResult',
    'AwaitableGetRouteResponseResult',
    'get_route_response',
    'get_route_response_output',
]

@pulumi.output_type
class GetRouteResponseResult:
    def __init__(__self__, model_selection_expression=None, response_models=None, response_parameters=None, route_response_id=None, route_response_key=None):
        if model_selection_expression and not isinstance(model_selection_expression, str):
            raise TypeError("Expected argument 'model_selection_expression' to be a str")
        pulumi.set(__self__, "model_selection_expression", model_selection_expression)
        if response_models and not isinstance(response_models, dict):
            raise TypeError("Expected argument 'response_models' to be a dict")
        pulumi.set(__self__, "response_models", response_models)
        if response_parameters and not isinstance(response_parameters, dict):
            raise TypeError("Expected argument 'response_parameters' to be a dict")
        pulumi.set(__self__, "response_parameters", response_parameters)
        if route_response_id and not isinstance(route_response_id, str):
            raise TypeError("Expected argument 'route_response_id' to be a str")
        pulumi.set(__self__, "route_response_id", route_response_id)
        if route_response_key and not isinstance(route_response_key, str):
            raise TypeError("Expected argument 'route_response_key' to be a str")
        pulumi.set(__self__, "route_response_key", route_response_key)

    @property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[str]:
        """
        The model selection expression for the route response. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "model_selection_expression")

    @property
    @pulumi.getter(name="responseModels")
    def response_models(self) -> Optional[Any]:
        """
        The response models for the route response.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::RouteResponse` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "response_models")

    @property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[Mapping[str, 'outputs.RouteResponseParameterConstraints']]:
        """
        The route response parameters.
        """
        return pulumi.get(self, "response_parameters")

    @property
    @pulumi.getter(name="routeResponseId")
    def route_response_id(self) -> Optional[str]:
        """
        The route response ID.
        """
        return pulumi.get(self, "route_response_id")

    @property
    @pulumi.getter(name="routeResponseKey")
    def route_response_key(self) -> Optional[str]:
        """
        The route response key.
        """
        return pulumi.get(self, "route_response_key")


class AwaitableGetRouteResponseResult(GetRouteResponseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteResponseResult(
            model_selection_expression=self.model_selection_expression,
            response_models=self.response_models,
            response_parameters=self.response_parameters,
            route_response_id=self.route_response_id,
            route_response_key=self.route_response_key)


def get_route_response(api_id: Optional[str] = None,
                       route_id: Optional[str] = None,
                       route_response_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteResponseResult:
    """
    The ``AWS::ApiGatewayV2::RouteResponse`` resource creates a route response for a WebSocket API. For more information, see [Set up Route Responses for a WebSocket API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-response.html) in the *API Gateway Developer Guide*.


    :param str api_id: The API identifier.
    :param str route_id: The route ID.
    :param str route_response_id: The route response ID.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['routeId'] = route_id
    __args__['routeResponseId'] = route_response_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigatewayv2:getRouteResponse', __args__, opts=opts, typ=GetRouteResponseResult).value

    return AwaitableGetRouteResponseResult(
        model_selection_expression=pulumi.get(__ret__, 'model_selection_expression'),
        response_models=pulumi.get(__ret__, 'response_models'),
        response_parameters=pulumi.get(__ret__, 'response_parameters'),
        route_response_id=pulumi.get(__ret__, 'route_response_id'),
        route_response_key=pulumi.get(__ret__, 'route_response_key'))


@_utilities.lift_output_func(get_route_response)
def get_route_response_output(api_id: Optional[pulumi.Input[str]] = None,
                              route_id: Optional[pulumi.Input[str]] = None,
                              route_response_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteResponseResult]:
    """
    The ``AWS::ApiGatewayV2::RouteResponse`` resource creates a route response for a WebSocket API. For more information, see [Set up Route Responses for a WebSocket API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-response.html) in the *API Gateway Developer Guide*.


    :param str api_id: The API identifier.
    :param str route_id: The route ID.
    :param str route_response_id: The route response ID.
    """
    ...
