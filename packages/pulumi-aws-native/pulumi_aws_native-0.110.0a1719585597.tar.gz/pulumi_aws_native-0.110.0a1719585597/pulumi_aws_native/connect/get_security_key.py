# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSecurityKeyResult',
    'AwaitableGetSecurityKeyResult',
    'get_security_key',
    'get_security_key_output',
]

@pulumi.output_type
class GetSecurityKeyResult:
    def __init__(__self__, association_id=None):
        if association_id and not isinstance(association_id, str):
            raise TypeError("Expected argument 'association_id' to be a str")
        pulumi.set(__self__, "association_id", association_id)

    @property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[str]:
        """
        An `AssociationId` is automatically generated when a storage config is associated with an instance.
        """
        return pulumi.get(self, "association_id")


class AwaitableGetSecurityKeyResult(GetSecurityKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityKeyResult(
            association_id=self.association_id)


def get_security_key(association_id: Optional[str] = None,
                     instance_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityKeyResult:
    """
    Resource Type definition for AWS::Connect::SecurityKey


    :param str association_id: An `AssociationId` is automatically generated when a storage config is associated with an instance.
    :param str instance_id: The Amazon Resource Name (ARN) of the instance.
           
           *Minimum* : `1`
           
           *Maximum* : `100`
    """
    __args__ = dict()
    __args__['associationId'] = association_id
    __args__['instanceId'] = instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getSecurityKey', __args__, opts=opts, typ=GetSecurityKeyResult).value

    return AwaitableGetSecurityKeyResult(
        association_id=pulumi.get(__ret__, 'association_id'))


@_utilities.lift_output_func(get_security_key)
def get_security_key_output(association_id: Optional[pulumi.Input[str]] = None,
                            instance_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityKeyResult]:
    """
    Resource Type definition for AWS::Connect::SecurityKey


    :param str association_id: An `AssociationId` is automatically generated when a storage config is associated with an instance.
    :param str instance_id: The Amazon Resource Name (ARN) of the instance.
           
           *Minimum* : `1`
           
           *Maximum* : `100`
    """
    ...
