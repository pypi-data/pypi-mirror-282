# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DashboardArgs', 'Dashboard']

@pulumi.input_type
class DashboardArgs:
    def __init__(__self__, *,
                 dashboard_body: pulumi.Input[str],
                 dashboard_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Dashboard resource.
        :param pulumi.Input[str] dashboard_body: The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard
        :param pulumi.Input[str] dashboard_name: The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.
        """
        pulumi.set(__self__, "dashboard_body", dashboard_body)
        if dashboard_name is not None:
            pulumi.set(__self__, "dashboard_name", dashboard_name)

    @property
    @pulumi.getter(name="dashboardBody")
    def dashboard_body(self) -> pulumi.Input[str]:
        """
        The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard
        """
        return pulumi.get(self, "dashboard_body")

    @dashboard_body.setter
    def dashboard_body(self, value: pulumi.Input[str]):
        pulumi.set(self, "dashboard_body", value)

    @property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.
        """
        return pulumi.get(self, "dashboard_name")

    @dashboard_name.setter
    def dashboard_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_name", value)


class Dashboard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_body: Optional[pulumi.Input[str]] = None,
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudWatch::Dashboard

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_body: The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard
        :param pulumi.Input[str] dashboard_name: The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudWatch::Dashboard

        :param str resource_name: The name of the resource.
        :param DashboardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_body: Optional[pulumi.Input[str]] = None,
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardArgs.__new__(DashboardArgs)

            if dashboard_body is None and not opts.urn:
                raise TypeError("Missing required property 'dashboard_body'")
            __props__.__dict__["dashboard_body"] = dashboard_body
            __props__.__dict__["dashboard_name"] = dashboard_name
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["dashboardName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Dashboard, __self__).__init__(
            'aws-native:cloudwatch:Dashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Dashboard':
        """
        Get an existing Dashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DashboardArgs.__new__(DashboardArgs)

        __props__.__dict__["dashboard_body"] = None
        __props__.__dict__["dashboard_name"] = None
        return Dashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardBody")
    def dashboard_body(self) -> pulumi.Output[str]:
        """
        The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard
        """
        return pulumi.get(self, "dashboard_body")

    @property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.
        """
        return pulumi.get(self, "dashboard_name")

