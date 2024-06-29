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
    'GetClusterParameterGroupResult',
    'AwaitableGetClusterParameterGroupResult',
    'get_cluster_parameter_group',
    'get_cluster_parameter_group_output',
]

@pulumi.output_type
class GetClusterParameterGroupResult:
    def __init__(__self__, parameters=None):
        if parameters and not isinstance(parameters, list):
            raise TypeError("Expected argument 'parameters' to be a list")
        pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence['outputs.ClusterParameterGroupParameter']]:
        """
        An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
        """
        return pulumi.get(self, "parameters")


class AwaitableGetClusterParameterGroupResult(GetClusterParameterGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterParameterGroupResult(
            parameters=self.parameters)


def get_cluster_parameter_group(parameter_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterParameterGroupResult:
    """
    Resource Type definition for AWS::Redshift::ClusterParameterGroup


    :param str parameter_group_name: The name of the cluster parameter group.
    """
    __args__ = dict()
    __args__['parameterGroupName'] = parameter_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:redshift:getClusterParameterGroup', __args__, opts=opts, typ=GetClusterParameterGroupResult).value

    return AwaitableGetClusterParameterGroupResult(
        parameters=pulumi.get(__ret__, 'parameters'))


@_utilities.lift_output_func(get_cluster_parameter_group)
def get_cluster_parameter_group_output(parameter_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterParameterGroupResult]:
    """
    Resource Type definition for AWS::Redshift::ClusterParameterGroup


    :param str parameter_group_name: The name of the cluster parameter group.
    """
    ...
