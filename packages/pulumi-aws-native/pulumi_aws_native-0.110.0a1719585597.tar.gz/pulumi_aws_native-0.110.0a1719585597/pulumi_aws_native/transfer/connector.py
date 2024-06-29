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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['ConnectorArgs', 'Connector']

@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *,
                 access_role: pulumi.Input[str],
                 url: pulumi.Input[str],
                 as2_config: Optional[pulumi.Input['As2ConfigPropertiesArgs']] = None,
                 logging_role: Optional[pulumi.Input[str]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 sftp_config: Optional[pulumi.Input['SftpConfigPropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Connector resource.
        :param pulumi.Input[str] access_role: Specifies the access role for the connector.
        :param pulumi.Input[str] url: URL for Connector
        :param pulumi.Input['As2ConfigPropertiesArgs'] as2_config: Configuration for an AS2 connector.
        :param pulumi.Input[str] logging_role: Specifies the logging role for the connector.
        :param pulumi.Input[str] security_policy_name: Security policy for SFTP Connector
        :param pulumi.Input['SftpConfigPropertiesArgs'] sftp_config: Configuration for an SFTP connector.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.
        """
        pulumi.set(__self__, "access_role", access_role)
        pulumi.set(__self__, "url", url)
        if as2_config is not None:
            pulumi.set(__self__, "as2_config", as2_config)
        if logging_role is not None:
            pulumi.set(__self__, "logging_role", logging_role)
        if security_policy_name is not None:
            pulumi.set(__self__, "security_policy_name", security_policy_name)
        if sftp_config is not None:
            pulumi.set(__self__, "sftp_config", sftp_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> pulumi.Input[str]:
        """
        Specifies the access role for the connector.
        """
        return pulumi.get(self, "access_role")

    @access_role.setter
    def access_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_role", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL for Connector
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="as2Config")
    def as2_config(self) -> Optional[pulumi.Input['As2ConfigPropertiesArgs']]:
        """
        Configuration for an AS2 connector.
        """
        return pulumi.get(self, "as2_config")

    @as2_config.setter
    def as2_config(self, value: Optional[pulumi.Input['As2ConfigPropertiesArgs']]):
        pulumi.set(self, "as2_config", value)

    @property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the logging role for the connector.
        """
        return pulumi.get(self, "logging_role")

    @logging_role.setter
    def logging_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_role", value)

    @property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Security policy for SFTP Connector
        """
        return pulumi.get(self, "security_policy_name")

    @security_policy_name.setter
    def security_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_policy_name", value)

    @property
    @pulumi.getter(name="sftpConfig")
    def sftp_config(self) -> Optional[pulumi.Input['SftpConfigPropertiesArgs']]:
        """
        Configuration for an SFTP connector.
        """
        return pulumi.get(self, "sftp_config")

    @sftp_config.setter
    def sftp_config(self, value: Optional[pulumi.Input['SftpConfigPropertiesArgs']]):
        pulumi.set(self, "sftp_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_role: Optional[pulumi.Input[str]] = None,
                 as2_config: Optional[pulumi.Input[pulumi.InputType['As2ConfigPropertiesArgs']]] = None,
                 logging_role: Optional[pulumi.Input[str]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 sftp_config: Optional[pulumi.Input[pulumi.InputType['SftpConfigPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Transfer::Connector

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_role: Specifies the access role for the connector.
        :param pulumi.Input[pulumi.InputType['As2ConfigPropertiesArgs']] as2_config: Configuration for an AS2 connector.
        :param pulumi.Input[str] logging_role: Specifies the logging role for the connector.
        :param pulumi.Input[str] security_policy_name: Security policy for SFTP Connector
        :param pulumi.Input[pulumi.InputType['SftpConfigPropertiesArgs']] sftp_config: Configuration for an SFTP connector.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.
        :param pulumi.Input[str] url: URL for Connector
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Transfer::Connector

        :param str resource_name: The name of the resource.
        :param ConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_role: Optional[pulumi.Input[str]] = None,
                 as2_config: Optional[pulumi.Input[pulumi.InputType['As2ConfigPropertiesArgs']]] = None,
                 logging_role: Optional[pulumi.Input[str]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 sftp_config: Optional[pulumi.Input[pulumi.InputType['SftpConfigPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorArgs.__new__(ConnectorArgs)

            if access_role is None and not opts.urn:
                raise TypeError("Missing required property 'access_role'")
            __props__.__dict__["access_role"] = access_role
            __props__.__dict__["as2_config"] = as2_config
            __props__.__dict__["logging_role"] = logging_role
            __props__.__dict__["security_policy_name"] = security_policy_name
            __props__.__dict__["sftp_config"] = sftp_config
            __props__.__dict__["tags"] = tags
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["arn"] = None
            __props__.__dict__["connector_id"] = None
            __props__.__dict__["service_managed_egress_ip_addresses"] = None
        super(Connector, __self__).__init__(
            'aws-native:transfer:Connector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Connector':
        """
        Get an existing Connector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectorArgs.__new__(ConnectorArgs)

        __props__.__dict__["access_role"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["as2_config"] = None
        __props__.__dict__["connector_id"] = None
        __props__.__dict__["logging_role"] = None
        __props__.__dict__["security_policy_name"] = None
        __props__.__dict__["service_managed_egress_ip_addresses"] = None
        __props__.__dict__["sftp_config"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["url"] = None
        return Connector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> pulumi.Output[str]:
        """
        Specifies the access role for the connector.
        """
        return pulumi.get(self, "access_role")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Specifies the unique Amazon Resource Name (ARN) for the connector.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="as2Config")
    def as2_config(self) -> pulumi.Output[Optional['outputs.As2ConfigProperties']]:
        """
        Configuration for an AS2 connector.
        """
        return pulumi.get(self, "as2_config")

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for the connector.
        """
        return pulumi.get(self, "connector_id")

    @property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the logging role for the connector.
        """
        return pulumi.get(self, "logging_role")

    @property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> pulumi.Output[Optional[str]]:
        """
        Security policy for SFTP Connector
        """
        return pulumi.get(self, "security_policy_name")

    @property
    @pulumi.getter(name="serviceManagedEgressIpAddresses")
    def service_managed_egress_ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of egress IP addresses of this connector. These IP addresses are assigned automatically when you create the connector.
        """
        return pulumi.get(self, "service_managed_egress_ip_addresses")

    @property
    @pulumi.getter(name="sftpConfig")
    def sftp_config(self) -> pulumi.Output[Optional['outputs.SftpConfigProperties']]:
        """
        Configuration for an SFTP connector.
        """
        return pulumi.get(self, "sftp_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        URL for Connector
        """
        return pulumi.get(self, "url")

