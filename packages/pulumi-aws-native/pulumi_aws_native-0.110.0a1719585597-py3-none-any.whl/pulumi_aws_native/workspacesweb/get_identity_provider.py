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

__all__ = [
    'GetIdentityProviderResult',
    'AwaitableGetIdentityProviderResult',
    'get_identity_provider',
    'get_identity_provider_output',
]

@pulumi.output_type
class GetIdentityProviderResult:
    def __init__(__self__, identity_provider_arn=None, identity_provider_details=None, identity_provider_name=None, identity_provider_type=None):
        if identity_provider_arn and not isinstance(identity_provider_arn, str):
            raise TypeError("Expected argument 'identity_provider_arn' to be a str")
        pulumi.set(__self__, "identity_provider_arn", identity_provider_arn)
        if identity_provider_details and not isinstance(identity_provider_details, dict):
            raise TypeError("Expected argument 'identity_provider_details' to be a dict")
        pulumi.set(__self__, "identity_provider_details", identity_provider_details)
        if identity_provider_name and not isinstance(identity_provider_name, str):
            raise TypeError("Expected argument 'identity_provider_name' to be a str")
        pulumi.set(__self__, "identity_provider_name", identity_provider_name)
        if identity_provider_type and not isinstance(identity_provider_type, str):
            raise TypeError("Expected argument 'identity_provider_type' to be a str")
        pulumi.set(__self__, "identity_provider_type", identity_provider_type)

    @property
    @pulumi.getter(name="identityProviderArn")
    def identity_provider_arn(self) -> Optional[str]:
        """
        The ARN of the identity provider.
        """
        return pulumi.get(self, "identity_provider_arn")

    @property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> Optional[Mapping[str, str]]:
        """
        The identity provider details. The following list describes the provider detail keys for each identity provider type.

        - For Google and Login with Amazon:

        - `client_id`
        - `client_secret`
        - `authorize_scopes`
        - For Facebook:

        - `client_id`
        - `client_secret`
        - `authorize_scopes`
        - `api_version`
        - For Sign in with Apple:

        - `client_id`
        - `team_id`
        - `key_id`
        - `private_key`
        - `authorize_scopes`
        - For OIDC providers:

        - `client_id`
        - `client_secret`
        - `attributes_request_method`
        - `oidc_issuer`
        - `authorize_scopes`
        - `authorize_url` *if not available from discovery URL specified by oidc_issuer key*
        - `token_url` *if not available from discovery URL specified by oidc_issuer key*
        - `attributes_url` *if not available from discovery URL specified by oidc_issuer key*
        - `jwks_uri` *if not available from discovery URL specified by oidc_issuer key*
        - For SAML providers:

        - `MetadataFile` OR `MetadataURL`
        - `IDPSignout` (boolean) *optional*
        - `IDPInit` (boolean) *optional*
        - `RequestSigningAlgorithm` (string) *optional* - Only accepts `rsa-sha256`
        - `EncryptedResponses` (boolean) *optional*
        """
        return pulumi.get(self, "identity_provider_details")

    @property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> Optional[str]:
        """
        The identity provider name.
        """
        return pulumi.get(self, "identity_provider_name")

    @property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> Optional['IdentityProviderType']:
        """
        The identity provider type.
        """
        return pulumi.get(self, "identity_provider_type")


class AwaitableGetIdentityProviderResult(GetIdentityProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIdentityProviderResult(
            identity_provider_arn=self.identity_provider_arn,
            identity_provider_details=self.identity_provider_details,
            identity_provider_name=self.identity_provider_name,
            identity_provider_type=self.identity_provider_type)


def get_identity_provider(identity_provider_arn: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIdentityProviderResult:
    """
    Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type


    :param str identity_provider_arn: The ARN of the identity provider.
    """
    __args__ = dict()
    __args__['identityProviderArn'] = identity_provider_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:workspacesweb:getIdentityProvider', __args__, opts=opts, typ=GetIdentityProviderResult).value

    return AwaitableGetIdentityProviderResult(
        identity_provider_arn=pulumi.get(__ret__, 'identity_provider_arn'),
        identity_provider_details=pulumi.get(__ret__, 'identity_provider_details'),
        identity_provider_name=pulumi.get(__ret__, 'identity_provider_name'),
        identity_provider_type=pulumi.get(__ret__, 'identity_provider_type'))


@_utilities.lift_output_func(get_identity_provider)
def get_identity_provider_output(identity_provider_arn: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIdentityProviderResult]:
    """
    Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type


    :param str identity_provider_arn: The ARN of the identity provider.
    """
    ...
