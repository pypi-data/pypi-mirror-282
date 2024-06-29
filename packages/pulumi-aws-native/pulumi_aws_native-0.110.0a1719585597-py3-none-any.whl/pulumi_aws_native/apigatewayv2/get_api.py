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
    'GetApiResult',
    'AwaitableGetApiResult',
    'get_api',
    'get_api_output',
]

@pulumi.output_type
class GetApiResult:
    def __init__(__self__, api_endpoint=None, api_id=None, api_key_selection_expression=None, cors_configuration=None, description=None, disable_execute_api_endpoint=None, name=None, route_selection_expression=None, tags=None, version=None):
        if api_endpoint and not isinstance(api_endpoint, str):
            raise TypeError("Expected argument 'api_endpoint' to be a str")
        pulumi.set(__self__, "api_endpoint", api_endpoint)
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if api_key_selection_expression and not isinstance(api_key_selection_expression, str):
            raise TypeError("Expected argument 'api_key_selection_expression' to be a str")
        pulumi.set(__self__, "api_key_selection_expression", api_key_selection_expression)
        if cors_configuration and not isinstance(cors_configuration, dict):
            raise TypeError("Expected argument 'cors_configuration' to be a dict")
        pulumi.set(__self__, "cors_configuration", cors_configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disable_execute_api_endpoint and not isinstance(disable_execute_api_endpoint, bool):
            raise TypeError("Expected argument 'disable_execute_api_endpoint' to be a bool")
        pulumi.set(__self__, "disable_execute_api_endpoint", disable_execute_api_endpoint)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if route_selection_expression and not isinstance(route_selection_expression, str):
            raise TypeError("Expected argument 'route_selection_expression' to be a str")
        pulumi.set(__self__, "route_selection_expression", route_selection_expression)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> Optional[str]:
        """
        The default endpoint for an API. For example: `https://abcdef.execute-api.us-west-2.amazonaws.com` .
        """
        return pulumi.get(self, "api_endpoint")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> Optional[str]:
        """
        An API key selection expression. Supported only for WebSocket APIs. See [API Key Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions).
        """
        return pulumi.get(self, "api_key_selection_expression")

    @property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional['outputs.ApiCors']:
        """
        A CORS configuration. Supported only for HTTP APIs. See [Configuring CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html) for more information.
        """
        return pulumi.get(self, "cors_configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the API.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> Optional[bool]:
        """
        Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.
        """
        return pulumi.get(self, "disable_execute_api_endpoint")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the API. Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation``.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routeSelectionExpression")
    def route_selection_expression(self) -> Optional[str]:
        """
        The route selection expression for the API. For HTTP APIs, the ``routeSelectionExpression`` must be ``${request.method} ${request.path}``. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.
        """
        return pulumi.get(self, "route_selection_expression")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        A version identifier for the API.
        """
        return pulumi.get(self, "version")


class AwaitableGetApiResult(GetApiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiResult(
            api_endpoint=self.api_endpoint,
            api_id=self.api_id,
            api_key_selection_expression=self.api_key_selection_expression,
            cors_configuration=self.cors_configuration,
            description=self.description,
            disable_execute_api_endpoint=self.disable_execute_api_endpoint,
            name=self.name,
            route_selection_expression=self.route_selection_expression,
            tags=self.tags,
            version=self.version)


def get_api(api_id: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiResult:
    """
    The ``AWS::ApiGatewayV2::Api`` resource creates an API. WebSocket APIs and HTTP APIs are supported. For more information about WebSocket APIs, see [About WebSocket APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html) in the *API Gateway Developer Guide*. For more information about HTTP APIs, see [HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) in the *API Gateway Developer Guide.*


    :param str api_id: The API identifier.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigatewayv2:getApi', __args__, opts=opts, typ=GetApiResult).value

    return AwaitableGetApiResult(
        api_endpoint=pulumi.get(__ret__, 'api_endpoint'),
        api_id=pulumi.get(__ret__, 'api_id'),
        api_key_selection_expression=pulumi.get(__ret__, 'api_key_selection_expression'),
        cors_configuration=pulumi.get(__ret__, 'cors_configuration'),
        description=pulumi.get(__ret__, 'description'),
        disable_execute_api_endpoint=pulumi.get(__ret__, 'disable_execute_api_endpoint'),
        name=pulumi.get(__ret__, 'name'),
        route_selection_expression=pulumi.get(__ret__, 'route_selection_expression'),
        tags=pulumi.get(__ret__, 'tags'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_api)
def get_api_output(api_id: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiResult]:
    """
    The ``AWS::ApiGatewayV2::Api`` resource creates an API. WebSocket APIs and HTTP APIs are supported. For more information about WebSocket APIs, see [About WebSocket APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html) in the *API Gateway Developer Guide*. For more information about HTTP APIs, see [HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) in the *API Gateway Developer Guide.*


    :param str api_id: The API identifier.
    """
    ...
