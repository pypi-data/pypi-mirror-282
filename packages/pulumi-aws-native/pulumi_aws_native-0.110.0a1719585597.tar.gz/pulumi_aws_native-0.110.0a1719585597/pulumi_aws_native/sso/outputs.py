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
from ._enums import *

__all__ = [
    'ApplicationPortalOptionsConfiguration',
    'ApplicationSignInOptions',
    'InstanceAccessControlAttributeConfigurationAccessControlAttribute',
    'InstanceAccessControlAttributeConfigurationAccessControlAttributeValue',
    'InstanceAccessControlAttributeConfigurationProperties',
    'PermissionSetCustomerManagedPolicyReference',
    'PermissionSetPermissionsBoundary',
]

@pulumi.output_type
class ApplicationPortalOptionsConfiguration(dict):
    """
    A structure that describes the options for the access portal associated with an application
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "signInOptions":
            suggest = "sign_in_options"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationPortalOptionsConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationPortalOptionsConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationPortalOptionsConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 sign_in_options: Optional['outputs.ApplicationSignInOptions'] = None,
                 visibility: Optional['ApplicationPortalOptionsConfigurationVisibility'] = None):
        """
        A structure that describes the options for the access portal associated with an application
        :param 'ApplicationSignInOptions' sign_in_options: A structure that describes the sign-in options for the access portal
        :param 'ApplicationPortalOptionsConfigurationVisibility' visibility: Indicates whether this application is visible in the access portal
        """
        if sign_in_options is not None:
            pulumi.set(__self__, "sign_in_options", sign_in_options)
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter(name="signInOptions")
    def sign_in_options(self) -> Optional['outputs.ApplicationSignInOptions']:
        """
        A structure that describes the sign-in options for the access portal
        """
        return pulumi.get(self, "sign_in_options")

    @property
    @pulumi.getter
    def visibility(self) -> Optional['ApplicationPortalOptionsConfigurationVisibility']:
        """
        Indicates whether this application is visible in the access portal
        """
        return pulumi.get(self, "visibility")


@pulumi.output_type
class ApplicationSignInOptions(dict):
    """
    A structure that describes the sign-in options for an application portal
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "applicationUrl":
            suggest = "application_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationSignInOptions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationSignInOptions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationSignInOptions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 origin: 'ApplicationSignInOptionsOrigin',
                 application_url: Optional[str] = None):
        """
        A structure that describes the sign-in options for an application portal
        :param 'ApplicationSignInOptionsOrigin' origin: This determines how IAM Identity Center navigates the user to the target application
        :param str application_url: The URL that accepts authentication requests for an application, this is a required parameter if the Origin parameter is APPLICATION
        """
        pulumi.set(__self__, "origin", origin)
        if application_url is not None:
            pulumi.set(__self__, "application_url", application_url)

    @property
    @pulumi.getter
    def origin(self) -> 'ApplicationSignInOptionsOrigin':
        """
        This determines how IAM Identity Center navigates the user to the target application
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> Optional[str]:
        """
        The URL that accepts authentication requests for an application, this is a required parameter if the Origin parameter is APPLICATION
        """
        return pulumi.get(self, "application_url")


@pulumi.output_type
class InstanceAccessControlAttributeConfigurationAccessControlAttribute(dict):
    def __init__(__self__, *,
                 key: str,
                 value: 'outputs.InstanceAccessControlAttributeConfigurationAccessControlAttributeValue'):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> 'outputs.InstanceAccessControlAttributeConfigurationAccessControlAttributeValue':
        return pulumi.get(self, "value")


@pulumi.output_type
class InstanceAccessControlAttributeConfigurationAccessControlAttributeValue(dict):
    def __init__(__self__, *,
                 source: Sequence[str]):
        pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def source(self) -> Sequence[str]:
        return pulumi.get(self, "source")


@pulumi.output_type
class InstanceAccessControlAttributeConfigurationProperties(dict):
    """
    The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use  AccessControlAttributes property instead.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessControlAttributes":
            suggest = "access_control_attributes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceAccessControlAttributeConfigurationProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceAccessControlAttributeConfigurationProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceAccessControlAttributeConfigurationProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_control_attributes: Sequence['outputs.InstanceAccessControlAttributeConfigurationAccessControlAttribute']):
        """
        The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use  AccessControlAttributes property instead.
        """
        pulumi.set(__self__, "access_control_attributes", access_control_attributes)

    @property
    @pulumi.getter(name="accessControlAttributes")
    def access_control_attributes(self) -> Sequence['outputs.InstanceAccessControlAttributeConfigurationAccessControlAttribute']:
        return pulumi.get(self, "access_control_attributes")


@pulumi.output_type
class PermissionSetCustomerManagedPolicyReference(dict):
    def __init__(__self__, *,
                 name: str,
                 path: Optional[str] = None):
        """
        :param str name: The name of the IAM policy that you have configured in each account where you want to deploy your permission set.
        :param str path: The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is `/` . For more information, see [Friendly names and paths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide* .
        """
        pulumi.set(__self__, "name", name)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the IAM policy that you have configured in each account where you want to deploy your permission set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is `/` . For more information, see [Friendly names and paths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide* .
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class PermissionSetPermissionsBoundary(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customerManagedPolicyReference":
            suggest = "customer_managed_policy_reference"
        elif key == "managedPolicyArn":
            suggest = "managed_policy_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PermissionSetPermissionsBoundary. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PermissionSetPermissionsBoundary.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PermissionSetPermissionsBoundary.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 customer_managed_policy_reference: Optional['outputs.PermissionSetCustomerManagedPolicyReference'] = None,
                 managed_policy_arn: Optional[str] = None):
        """
        :param 'PermissionSetCustomerManagedPolicyReference' customer_managed_policy_reference: Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.
        :param str managed_policy_arn: The AWS managed policy ARN that you want to attach to a permission set as a permissions boundary.
        """
        if customer_managed_policy_reference is not None:
            pulumi.set(__self__, "customer_managed_policy_reference", customer_managed_policy_reference)
        if managed_policy_arn is not None:
            pulumi.set(__self__, "managed_policy_arn", managed_policy_arn)

    @property
    @pulumi.getter(name="customerManagedPolicyReference")
    def customer_managed_policy_reference(self) -> Optional['outputs.PermissionSetCustomerManagedPolicyReference']:
        """
        Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.
        """
        return pulumi.get(self, "customer_managed_policy_reference")

    @property
    @pulumi.getter(name="managedPolicyArn")
    def managed_policy_arn(self) -> Optional[str]:
        """
        The AWS managed policy ARN that you want to attach to a permission set as a permissions boundary.
        """
        return pulumi.get(self, "managed_policy_arn")


