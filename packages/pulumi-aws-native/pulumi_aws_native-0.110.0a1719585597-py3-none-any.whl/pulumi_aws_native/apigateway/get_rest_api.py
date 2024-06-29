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

__all__ = [
    'GetRestApiResult',
    'AwaitableGetRestApiResult',
    'get_rest_api',
    'get_rest_api_output',
]

@pulumi.output_type
class GetRestApiResult:
    def __init__(__self__, api_key_source_type=None, binary_media_types=None, description=None, disable_execute_api_endpoint=None, endpoint_configuration=None, minimum_compression_size=None, name=None, policy=None, rest_api_id=None, root_resource_id=None, tags=None):
        if api_key_source_type and not isinstance(api_key_source_type, str):
            raise TypeError("Expected argument 'api_key_source_type' to be a str")
        pulumi.set(__self__, "api_key_source_type", api_key_source_type)
        if binary_media_types and not isinstance(binary_media_types, list):
            raise TypeError("Expected argument 'binary_media_types' to be a list")
        pulumi.set(__self__, "binary_media_types", binary_media_types)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disable_execute_api_endpoint and not isinstance(disable_execute_api_endpoint, bool):
            raise TypeError("Expected argument 'disable_execute_api_endpoint' to be a bool")
        pulumi.set(__self__, "disable_execute_api_endpoint", disable_execute_api_endpoint)
        if endpoint_configuration and not isinstance(endpoint_configuration, dict):
            raise TypeError("Expected argument 'endpoint_configuration' to be a dict")
        pulumi.set(__self__, "endpoint_configuration", endpoint_configuration)
        if minimum_compression_size and not isinstance(minimum_compression_size, int):
            raise TypeError("Expected argument 'minimum_compression_size' to be a int")
        pulumi.set(__self__, "minimum_compression_size", minimum_compression_size)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)
        if rest_api_id and not isinstance(rest_api_id, str):
            raise TypeError("Expected argument 'rest_api_id' to be a str")
        pulumi.set(__self__, "rest_api_id", rest_api_id)
        if root_resource_id and not isinstance(root_resource_id, str):
            raise TypeError("Expected argument 'root_resource_id' to be a str")
        pulumi.set(__self__, "root_resource_id", root_resource_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiKeySourceType")
    def api_key_source_type(self) -> Optional[str]:
        """
        The source of the API key for metering requests according to a usage plan. Valid values are: ``HEADER`` to read the API key from the ``X-API-Key`` header of a request. ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer.
        """
        return pulumi.get(self, "api_key_source_type")

    @property
    @pulumi.getter(name="binaryMediaTypes")
    def binary_media_types(self) -> Optional[Sequence[str]]:
        """
        The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.
        """
        return pulumi.get(self, "binary_media_types")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the RestApi.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> Optional[bool]:
        """
        Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint. By default, clients can invoke your API with the default ``https://{api_id}.execute-api.{region}.amazonaws.com`` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint
        """
        return pulumi.get(self, "disable_execute_api_endpoint")

    @property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(self) -> Optional['outputs.RestApiEndpointConfiguration']:
        """
        A list of the endpoint types of the API. Use this property when creating an API. When importing an existing API, specify the endpoint configuration types using the ``Parameters`` property.
        """
        return pulumi.get(self, "endpoint_configuration")

    @property
    @pulumi.getter(name="minimumCompressionSize")
    def minimum_compression_size(self) -> Optional[int]:
        """
        A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.
        """
        return pulumi.get(self, "minimum_compression_size")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the RestApi. A name is required if the REST API is not based on an OpenAPI specification.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        """
        A policy document that contains the permissions for the ``RestApi`` resource. To set the ARN for the policy, use the ``!Join`` intrinsic function with ``""`` as delimiter and values of ``"execute-api:/"`` and ``"*"``.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGateway::RestApi` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> Optional[str]:
        """
        The string identifier of the associated RestApi.
        """
        return pulumi.get(self, "rest_api_id")

    @property
    @pulumi.getter(name="rootResourceId")
    def root_resource_id(self) -> Optional[str]:
        """
        The root resource ID for a `RestApi` resource, such as `a0bc123d4e` .
        """
        return pulumi.get(self, "root_resource_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.
        """
        return pulumi.get(self, "tags")


class AwaitableGetRestApiResult(GetRestApiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRestApiResult(
            api_key_source_type=self.api_key_source_type,
            binary_media_types=self.binary_media_types,
            description=self.description,
            disable_execute_api_endpoint=self.disable_execute_api_endpoint,
            endpoint_configuration=self.endpoint_configuration,
            minimum_compression_size=self.minimum_compression_size,
            name=self.name,
            policy=self.policy,
            rest_api_id=self.rest_api_id,
            root_resource_id=self.root_resource_id,
            tags=self.tags)


def get_rest_api(rest_api_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRestApiResult:
    """
    The ``AWS::ApiGateway::RestApi`` resource creates a REST API. For more information, see [restapi:create](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateRestApi.html) in the *Amazon API Gateway REST API Reference*.
     On January 1, 2016, the Swagger Specification was donated to the [OpenAPI initiative](https://docs.aws.amazon.com/https://www.openapis.org/), becoming the foundation of the OpenAPI Specification.


    :param str rest_api_id: The string identifier of the associated RestApi.
    """
    __args__ = dict()
    __args__['restApiId'] = rest_api_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getRestApi', __args__, opts=opts, typ=GetRestApiResult).value

    return AwaitableGetRestApiResult(
        api_key_source_type=pulumi.get(__ret__, 'api_key_source_type'),
        binary_media_types=pulumi.get(__ret__, 'binary_media_types'),
        description=pulumi.get(__ret__, 'description'),
        disable_execute_api_endpoint=pulumi.get(__ret__, 'disable_execute_api_endpoint'),
        endpoint_configuration=pulumi.get(__ret__, 'endpoint_configuration'),
        minimum_compression_size=pulumi.get(__ret__, 'minimum_compression_size'),
        name=pulumi.get(__ret__, 'name'),
        policy=pulumi.get(__ret__, 'policy'),
        rest_api_id=pulumi.get(__ret__, 'rest_api_id'),
        root_resource_id=pulumi.get(__ret__, 'root_resource_id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_rest_api)
def get_rest_api_output(rest_api_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRestApiResult]:
    """
    The ``AWS::ApiGateway::RestApi`` resource creates a REST API. For more information, see [restapi:create](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateRestApi.html) in the *Amazon API Gateway REST API Reference*.
     On January 1, 2016, the Swagger Specification was donated to the [OpenAPI initiative](https://docs.aws.amazon.com/https://www.openapis.org/), becoming the foundation of the OpenAPI Specification.


    :param str rest_api_id: The string identifier of the associated RestApi.
    """
    ...
