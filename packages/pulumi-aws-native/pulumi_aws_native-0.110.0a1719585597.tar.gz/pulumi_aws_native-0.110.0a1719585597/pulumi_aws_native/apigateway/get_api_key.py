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
    'GetApiKeyResult',
    'AwaitableGetApiKeyResult',
    'get_api_key',
    'get_api_key_output',
]

@pulumi.output_type
class GetApiKeyResult:
    def __init__(__self__, api_key_id=None, customer_id=None, description=None, enabled=None, stage_keys=None, tags=None):
        if api_key_id and not isinstance(api_key_id, str):
            raise TypeError("Expected argument 'api_key_id' to be a str")
        pulumi.set(__self__, "api_key_id", api_key_id)
        if customer_id and not isinstance(customer_id, str):
            raise TypeError("Expected argument 'customer_id' to be a str")
        pulumi.set(__self__, "customer_id", customer_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if stage_keys and not isinstance(stage_keys, list):
            raise TypeError("Expected argument 'stage_keys' to be a list")
        pulumi.set(__self__, "stage_keys", stage_keys)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> Optional[str]:
        """
        The ID for the API key. For example: `abc123` .
        """
        return pulumi.get(self, "api_key_id")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[str]:
        """
        An MKT customer identifier, when integrating with the AWS SaaS Marketplace.
        """
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the ApiKey.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Specifies whether the ApiKey can be used by callers.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="stageKeys")
    def stage_keys(self) -> Optional[Sequence['outputs.ApiKeyStageKey']]:
        """
        DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
        """
        return pulumi.get(self, "stage_keys")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.
        """
        return pulumi.get(self, "tags")


class AwaitableGetApiKeyResult(GetApiKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiKeyResult(
            api_key_id=self.api_key_id,
            customer_id=self.customer_id,
            description=self.description,
            enabled=self.enabled,
            stage_keys=self.stage_keys,
            tags=self.tags)


def get_api_key(api_key_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiKeyResult:
    """
    The ``AWS::ApiGateway::ApiKey`` resource creates a unique key that you can distribute to clients who are executing API Gateway ``Method`` resources that require an API key. To specify which API key clients must use, map the API key with the ``RestApi`` and ``Stage`` resources that include the methods that require a key.


    :param str api_key_id: The ID for the API key. For example: `abc123` .
    """
    __args__ = dict()
    __args__['apiKeyId'] = api_key_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getApiKey', __args__, opts=opts, typ=GetApiKeyResult).value

    return AwaitableGetApiKeyResult(
        api_key_id=pulumi.get(__ret__, 'api_key_id'),
        customer_id=pulumi.get(__ret__, 'customer_id'),
        description=pulumi.get(__ret__, 'description'),
        enabled=pulumi.get(__ret__, 'enabled'),
        stage_keys=pulumi.get(__ret__, 'stage_keys'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_api_key)
def get_api_key_output(api_key_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiKeyResult]:
    """
    The ``AWS::ApiGateway::ApiKey`` resource creates a unique key that you can distribute to clients who are executing API Gateway ``Method`` resources that require an API key. To specify which API key clients must use, map the API key with the ``RestApi`` and ``Stage`` resources that include the methods that require a key.


    :param str api_key_id: The ID for the API key. For example: `abc123` .
    """
    ...
