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
    'GetGameServerGroupResult',
    'AwaitableGetGameServerGroupResult',
    'get_game_server_group',
    'get_game_server_group_output',
]

@pulumi.output_type
class GetGameServerGroupResult:
    def __init__(__self__, auto_scaling_group_arn=None, balancing_strategy=None, game_server_group_arn=None, game_server_group_name=None, game_server_protection_policy=None, instance_definitions=None, role_arn=None):
        if auto_scaling_group_arn and not isinstance(auto_scaling_group_arn, str):
            raise TypeError("Expected argument 'auto_scaling_group_arn' to be a str")
        pulumi.set(__self__, "auto_scaling_group_arn", auto_scaling_group_arn)
        if balancing_strategy and not isinstance(balancing_strategy, str):
            raise TypeError("Expected argument 'balancing_strategy' to be a str")
        pulumi.set(__self__, "balancing_strategy", balancing_strategy)
        if game_server_group_arn and not isinstance(game_server_group_arn, str):
            raise TypeError("Expected argument 'game_server_group_arn' to be a str")
        pulumi.set(__self__, "game_server_group_arn", game_server_group_arn)
        if game_server_group_name and not isinstance(game_server_group_name, str):
            raise TypeError("Expected argument 'game_server_group_name' to be a str")
        pulumi.set(__self__, "game_server_group_name", game_server_group_name)
        if game_server_protection_policy and not isinstance(game_server_protection_policy, str):
            raise TypeError("Expected argument 'game_server_protection_policy' to be a str")
        pulumi.set(__self__, "game_server_protection_policy", game_server_protection_policy)
        if instance_definitions and not isinstance(instance_definitions, list):
            raise TypeError("Expected argument 'instance_definitions' to be a list")
        pulumi.set(__self__, "instance_definitions", instance_definitions)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> Optional[str]:
        """
        A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.
        """
        return pulumi.get(self, "auto_scaling_group_arn")

    @property
    @pulumi.getter(name="balancingStrategy")
    def balancing_strategy(self) -> Optional['GameServerGroupBalancingStrategy']:
        """
        The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
        """
        return pulumi.get(self, "balancing_strategy")

    @property
    @pulumi.getter(name="gameServerGroupArn")
    def game_server_group_arn(self) -> Optional[str]:
        """
        A generated unique ID for the game server group.
        """
        return pulumi.get(self, "game_server_group_arn")

    @property
    @pulumi.getter(name="gameServerGroupName")
    def game_server_group_name(self) -> Optional[str]:
        """
        An identifier for the new game server group.
        """
        return pulumi.get(self, "game_server_group_name")

    @property
    @pulumi.getter(name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> Optional['GameServerGroupGameServerProtectionPolicy']:
        """
        A flag that indicates whether instances in the game server group are protected from early termination.
        """
        return pulumi.get(self, "game_server_protection_policy")

    @property
    @pulumi.getter(name="instanceDefinitions")
    def instance_definitions(self) -> Optional[Sequence['outputs.GameServerGroupInstanceDefinition']]:
        """
        A set of EC2 instance types to use when creating instances in the group.
        """
        return pulumi.get(self, "instance_definitions")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
        """
        return pulumi.get(self, "role_arn")


class AwaitableGetGameServerGroupResult(GetGameServerGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGameServerGroupResult(
            auto_scaling_group_arn=self.auto_scaling_group_arn,
            balancing_strategy=self.balancing_strategy,
            game_server_group_arn=self.game_server_group_arn,
            game_server_group_name=self.game_server_group_name,
            game_server_protection_policy=self.game_server_protection_policy,
            instance_definitions=self.instance_definitions,
            role_arn=self.role_arn)


def get_game_server_group(game_server_group_arn: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGameServerGroupResult:
    """
    The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.


    :param str game_server_group_arn: A generated unique ID for the game server group.
    """
    __args__ = dict()
    __args__['gameServerGroupArn'] = game_server_group_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:gamelift:getGameServerGroup', __args__, opts=opts, typ=GetGameServerGroupResult).value

    return AwaitableGetGameServerGroupResult(
        auto_scaling_group_arn=pulumi.get(__ret__, 'auto_scaling_group_arn'),
        balancing_strategy=pulumi.get(__ret__, 'balancing_strategy'),
        game_server_group_arn=pulumi.get(__ret__, 'game_server_group_arn'),
        game_server_group_name=pulumi.get(__ret__, 'game_server_group_name'),
        game_server_protection_policy=pulumi.get(__ret__, 'game_server_protection_policy'),
        instance_definitions=pulumi.get(__ret__, 'instance_definitions'),
        role_arn=pulumi.get(__ret__, 'role_arn'))


@_utilities.lift_output_func(get_game_server_group)
def get_game_server_group_output(game_server_group_arn: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGameServerGroupResult]:
    """
    The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.


    :param str game_server_group_arn: A generated unique ID for the game server group.
    """
    ...
