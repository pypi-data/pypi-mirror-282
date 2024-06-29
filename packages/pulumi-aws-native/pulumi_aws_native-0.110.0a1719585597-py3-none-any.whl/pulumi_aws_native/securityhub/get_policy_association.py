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
    'GetPolicyAssociationResult',
    'AwaitableGetPolicyAssociationResult',
    'get_policy_association',
    'get_policy_association_output',
]

@pulumi.output_type
class GetPolicyAssociationResult:
    def __init__(__self__, association_identifier=None, association_status=None, association_status_message=None, association_type=None, configuration_policy_id=None, updated_at=None):
        if association_identifier and not isinstance(association_identifier, str):
            raise TypeError("Expected argument 'association_identifier' to be a str")
        pulumi.set(__self__, "association_identifier", association_identifier)
        if association_status and not isinstance(association_status, str):
            raise TypeError("Expected argument 'association_status' to be a str")
        pulumi.set(__self__, "association_status", association_status)
        if association_status_message and not isinstance(association_status_message, str):
            raise TypeError("Expected argument 'association_status_message' to be a str")
        pulumi.set(__self__, "association_status_message", association_status_message)
        if association_type and not isinstance(association_type, str):
            raise TypeError("Expected argument 'association_type' to be a str")
        pulumi.set(__self__, "association_type", association_type)
        if configuration_policy_id and not isinstance(configuration_policy_id, str):
            raise TypeError("Expected argument 'configuration_policy_id' to be a str")
        pulumi.set(__self__, "configuration_policy_id", configuration_policy_id)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="associationIdentifier")
    def association_identifier(self) -> Optional[str]:
        """
        A unique identifier to indicates if the target has an association
        """
        return pulumi.get(self, "association_identifier")

    @property
    @pulumi.getter(name="associationStatus")
    def association_status(self) -> Optional['PolicyAssociationAssociationStatus']:
        """
        The current status of the association between the specified target and the configuration
        """
        return pulumi.get(self, "association_status")

    @property
    @pulumi.getter(name="associationStatusMessage")
    def association_status_message(self) -> Optional[str]:
        """
        An explanation for a FAILED value for AssociationStatus
        """
        return pulumi.get(self, "association_status_message")

    @property
    @pulumi.getter(name="associationType")
    def association_type(self) -> Optional['PolicyAssociationAssociationType']:
        """
        Indicates whether the association between the specified target and the configuration was directly applied by the Security Hub delegated administrator or inherited from a parent
        """
        return pulumi.get(self, "association_type")

    @property
    @pulumi.getter(name="configurationPolicyId")
    def configuration_policy_id(self) -> Optional[str]:
        """
        The universally unique identifier (UUID) of the configuration policy or a value of SELF_MANAGED_SECURITY_HUB for a self-managed configuration
        """
        return pulumi.get(self, "configuration_policy_id")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        """
        The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetPolicyAssociationResult(GetPolicyAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyAssociationResult(
            association_identifier=self.association_identifier,
            association_status=self.association_status,
            association_status_message=self.association_status_message,
            association_type=self.association_type,
            configuration_policy_id=self.configuration_policy_id,
            updated_at=self.updated_at)


def get_policy_association(association_identifier: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyAssociationResult:
    """
    The AWS::SecurityHub::PolicyAssociation resource represents the AWS Security Hub Central Configuration Policy associations in your Target. Only the AWS Security Hub delegated administrator can create the resouce from the home region.


    :param str association_identifier: A unique identifier to indicates if the target has an association
    """
    __args__ = dict()
    __args__['associationIdentifier'] = association_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:securityhub:getPolicyAssociation', __args__, opts=opts, typ=GetPolicyAssociationResult).value

    return AwaitableGetPolicyAssociationResult(
        association_identifier=pulumi.get(__ret__, 'association_identifier'),
        association_status=pulumi.get(__ret__, 'association_status'),
        association_status_message=pulumi.get(__ret__, 'association_status_message'),
        association_type=pulumi.get(__ret__, 'association_type'),
        configuration_policy_id=pulumi.get(__ret__, 'configuration_policy_id'),
        updated_at=pulumi.get(__ret__, 'updated_at'))


@_utilities.lift_output_func(get_policy_association)
def get_policy_association_output(association_identifier: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyAssociationResult]:
    """
    The AWS::SecurityHub::PolicyAssociation resource represents the AWS Security Hub Central Configuration Policy associations in your Target. Only the AWS Security Hub delegated administrator can create the resouce from the home region.


    :param str association_identifier: A unique identifier to indicates if the target has an association
    """
    ...
