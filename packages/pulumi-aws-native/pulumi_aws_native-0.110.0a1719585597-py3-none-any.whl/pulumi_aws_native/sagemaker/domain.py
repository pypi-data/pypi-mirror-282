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

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 auth_mode: pulumi.Input['DomainAuthMode'],
                 default_user_settings: pulumi.Input['DomainUserSettingsArgs'],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_id: pulumi.Input[str],
                 app_network_access_type: Optional[pulumi.Input['DomainAppNetworkAccessType']] = None,
                 app_security_group_management: Optional[pulumi.Input['DomainAppSecurityGroupManagement']] = None,
                 default_space_settings: Optional[pulumi.Input['DomainDefaultSpaceSettingsArgs']] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_settings: Optional[pulumi.Input['DomainSettingsArgs']] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input['DomainAuthMode'] auth_mode: The mode of authentication that members use to access the domain.
        :param pulumi.Input['DomainUserSettingsArgs'] default_user_settings: The default user settings.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The VPC subnets that Studio uses for communication.
        :param pulumi.Input[str] vpc_id: The ID of the Amazon Virtual Private Cloud (VPC) that Studio uses for communication.
        :param pulumi.Input['DomainAppNetworkAccessType'] app_network_access_type: Specifies the VPC used for non-EFS traffic. The default value is PublicInternetOnly.
        :param pulumi.Input['DomainAppSecurityGroupManagement'] app_security_group_management: The entity that creates and manages the required security groups for inter-app communication in VPCOnly mode. Required when CreateDomain.AppNetworkAccessType is VPCOnly and DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn is provided.
        :param pulumi.Input['DomainDefaultSpaceSettingsArgs'] default_space_settings: The default space settings.
        :param pulumi.Input[str] domain_name: A name for the domain.
        :param pulumi.Input['DomainSettingsArgs'] domain_settings: A collection of settings that apply to the `SageMaker Domain` . These settings are specified through the `CreateDomain` API call.
        :param pulumi.Input[str] kms_key_id: SageMaker uses AWS KMS to encrypt the EFS volume attached to the domain with an AWS managed customer master key (CMK) by default.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]] tags: A list of tags to apply to the user profile.
        """
        pulumi.set(__self__, "auth_mode", auth_mode)
        pulumi.set(__self__, "default_user_settings", default_user_settings)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if app_network_access_type is not None:
            pulumi.set(__self__, "app_network_access_type", app_network_access_type)
        if app_security_group_management is not None:
            pulumi.set(__self__, "app_security_group_management", app_security_group_management)
        if default_space_settings is not None:
            pulumi.set(__self__, "default_space_settings", default_space_settings)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if domain_settings is not None:
            pulumi.set(__self__, "domain_settings", domain_settings)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Input['DomainAuthMode']:
        """
        The mode of authentication that members use to access the domain.
        """
        return pulumi.get(self, "auth_mode")

    @auth_mode.setter
    def auth_mode(self, value: pulumi.Input['DomainAuthMode']):
        pulumi.set(self, "auth_mode", value)

    @property
    @pulumi.getter(name="defaultUserSettings")
    def default_user_settings(self) -> pulumi.Input['DomainUserSettingsArgs']:
        """
        The default user settings.
        """
        return pulumi.get(self, "default_user_settings")

    @default_user_settings.setter
    def default_user_settings(self, value: pulumi.Input['DomainUserSettingsArgs']):
        pulumi.set(self, "default_user_settings", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The VPC subnets that Studio uses for communication.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The ID of the Amazon Virtual Private Cloud (VPC) that Studio uses for communication.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="appNetworkAccessType")
    def app_network_access_type(self) -> Optional[pulumi.Input['DomainAppNetworkAccessType']]:
        """
        Specifies the VPC used for non-EFS traffic. The default value is PublicInternetOnly.
        """
        return pulumi.get(self, "app_network_access_type")

    @app_network_access_type.setter
    def app_network_access_type(self, value: Optional[pulumi.Input['DomainAppNetworkAccessType']]):
        pulumi.set(self, "app_network_access_type", value)

    @property
    @pulumi.getter(name="appSecurityGroupManagement")
    def app_security_group_management(self) -> Optional[pulumi.Input['DomainAppSecurityGroupManagement']]:
        """
        The entity that creates and manages the required security groups for inter-app communication in VPCOnly mode. Required when CreateDomain.AppNetworkAccessType is VPCOnly and DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn is provided.
        """
        return pulumi.get(self, "app_security_group_management")

    @app_security_group_management.setter
    def app_security_group_management(self, value: Optional[pulumi.Input['DomainAppSecurityGroupManagement']]):
        pulumi.set(self, "app_security_group_management", value)

    @property
    @pulumi.getter(name="defaultSpaceSettings")
    def default_space_settings(self) -> Optional[pulumi.Input['DomainDefaultSpaceSettingsArgs']]:
        """
        The default space settings.
        """
        return pulumi.get(self, "default_space_settings")

    @default_space_settings.setter
    def default_space_settings(self, value: Optional[pulumi.Input['DomainDefaultSpaceSettingsArgs']]):
        pulumi.set(self, "default_space_settings", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="domainSettings")
    def domain_settings(self) -> Optional[pulumi.Input['DomainSettingsArgs']]:
        """
        A collection of settings that apply to the `SageMaker Domain` . These settings are specified through the `CreateDomain` API call.
        """
        return pulumi.get(self, "domain_settings")

    @domain_settings.setter
    def domain_settings(self, value: Optional[pulumi.Input['DomainSettingsArgs']]):
        pulumi.set(self, "domain_settings", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        SageMaker uses AWS KMS to encrypt the EFS volume attached to the domain with an AWS managed customer master key (CMK) by default.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]:
        """
        A list of tags to apply to the user profile.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_network_access_type: Optional[pulumi.Input['DomainAppNetworkAccessType']] = None,
                 app_security_group_management: Optional[pulumi.Input['DomainAppSecurityGroupManagement']] = None,
                 auth_mode: Optional[pulumi.Input['DomainAuthMode']] = None,
                 default_space_settings: Optional[pulumi.Input[pulumi.InputType['DomainDefaultSpaceSettingsArgs']]] = None,
                 default_user_settings: Optional[pulumi.Input[pulumi.InputType['DomainUserSettingsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_settings: Optional[pulumi.Input[pulumi.InputType['DomainSettingsArgs']]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::Domain

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['DomainAppNetworkAccessType'] app_network_access_type: Specifies the VPC used for non-EFS traffic. The default value is PublicInternetOnly.
        :param pulumi.Input['DomainAppSecurityGroupManagement'] app_security_group_management: The entity that creates and manages the required security groups for inter-app communication in VPCOnly mode. Required when CreateDomain.AppNetworkAccessType is VPCOnly and DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn is provided.
        :param pulumi.Input['DomainAuthMode'] auth_mode: The mode of authentication that members use to access the domain.
        :param pulumi.Input[pulumi.InputType['DomainDefaultSpaceSettingsArgs']] default_space_settings: The default space settings.
        :param pulumi.Input[pulumi.InputType['DomainUserSettingsArgs']] default_user_settings: The default user settings.
        :param pulumi.Input[str] domain_name: A name for the domain.
        :param pulumi.Input[pulumi.InputType['DomainSettingsArgs']] domain_settings: A collection of settings that apply to the `SageMaker Domain` . These settings are specified through the `CreateDomain` API call.
        :param pulumi.Input[str] kms_key_id: SageMaker uses AWS KMS to encrypt the EFS volume attached to the domain with an AWS managed customer master key (CMK) by default.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The VPC subnets that Studio uses for communication.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]] tags: A list of tags to apply to the user profile.
        :param pulumi.Input[str] vpc_id: The ID of the Amazon Virtual Private Cloud (VPC) that Studio uses for communication.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::Domain

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_network_access_type: Optional[pulumi.Input['DomainAppNetworkAccessType']] = None,
                 app_security_group_management: Optional[pulumi.Input['DomainAppSecurityGroupManagement']] = None,
                 auth_mode: Optional[pulumi.Input['DomainAuthMode']] = None,
                 default_space_settings: Optional[pulumi.Input[pulumi.InputType['DomainDefaultSpaceSettingsArgs']]] = None,
                 default_user_settings: Optional[pulumi.Input[pulumi.InputType['DomainUserSettingsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_settings: Optional[pulumi.Input[pulumi.InputType['DomainSettingsArgs']]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["app_network_access_type"] = app_network_access_type
            __props__.__dict__["app_security_group_management"] = app_security_group_management
            if auth_mode is None and not opts.urn:
                raise TypeError("Missing required property 'auth_mode'")
            __props__.__dict__["auth_mode"] = auth_mode
            __props__.__dict__["default_space_settings"] = default_space_settings
            if default_user_settings is None and not opts.urn:
                raise TypeError("Missing required property 'default_user_settings'")
            __props__.__dict__["default_user_settings"] = default_user_settings
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["domain_settings"] = domain_settings
            __props__.__dict__["kms_key_id"] = kms_key_id
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["domain_arn"] = None
            __props__.__dict__["domain_id"] = None
            __props__.__dict__["home_efs_file_system_id"] = None
            __props__.__dict__["security_group_id_for_domain_boundary"] = None
            __props__.__dict__["single_sign_on_application_arn"] = None
            __props__.__dict__["single_sign_on_managed_application_instance_id"] = None
            __props__.__dict__["url"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["authMode", "domainName", "domainSettings.rStudioServerProDomainSettings.defaultResourceSpec", "kmsKeyId", "tags[*]", "vpcId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Domain, __self__).__init__(
            'aws-native:sagemaker:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainArgs.__new__(DomainArgs)

        __props__.__dict__["app_network_access_type"] = None
        __props__.__dict__["app_security_group_management"] = None
        __props__.__dict__["auth_mode"] = None
        __props__.__dict__["default_space_settings"] = None
        __props__.__dict__["default_user_settings"] = None
        __props__.__dict__["domain_arn"] = None
        __props__.__dict__["domain_id"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["domain_settings"] = None
        __props__.__dict__["home_efs_file_system_id"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["security_group_id_for_domain_boundary"] = None
        __props__.__dict__["single_sign_on_application_arn"] = None
        __props__.__dict__["single_sign_on_managed_application_instance_id"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["url"] = None
        __props__.__dict__["vpc_id"] = None
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appNetworkAccessType")
    def app_network_access_type(self) -> pulumi.Output[Optional['DomainAppNetworkAccessType']]:
        """
        Specifies the VPC used for non-EFS traffic. The default value is PublicInternetOnly.
        """
        return pulumi.get(self, "app_network_access_type")

    @property
    @pulumi.getter(name="appSecurityGroupManagement")
    def app_security_group_management(self) -> pulumi.Output[Optional['DomainAppSecurityGroupManagement']]:
        """
        The entity that creates and manages the required security groups for inter-app communication in VPCOnly mode. Required when CreateDomain.AppNetworkAccessType is VPCOnly and DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn is provided.
        """
        return pulumi.get(self, "app_security_group_management")

    @property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Output['DomainAuthMode']:
        """
        The mode of authentication that members use to access the domain.
        """
        return pulumi.get(self, "auth_mode")

    @property
    @pulumi.getter(name="defaultSpaceSettings")
    def default_space_settings(self) -> pulumi.Output[Optional['outputs.DomainDefaultSpaceSettings']]:
        """
        The default space settings.
        """
        return pulumi.get(self, "default_space_settings")

    @property
    @pulumi.getter(name="defaultUserSettings")
    def default_user_settings(self) -> pulumi.Output['outputs.DomainUserSettings']:
        """
        The default user settings.
        """
        return pulumi.get(self, "default_user_settings")

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the created domain.
        """
        return pulumi.get(self, "domain_arn")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        The domain name.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        A name for the domain.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainSettings")
    def domain_settings(self) -> pulumi.Output[Optional['outputs.DomainSettings']]:
        """
        A collection of settings that apply to the `SageMaker Domain` . These settings are specified through the `CreateDomain` API call.
        """
        return pulumi.get(self, "domain_settings")

    @property
    @pulumi.getter(name="homeEfsFileSystemId")
    def home_efs_file_system_id(self) -> pulumi.Output[str]:
        """
        The ID of the Amazon Elastic File System (EFS) managed by this Domain.
        """
        return pulumi.get(self, "home_efs_file_system_id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        SageMaker uses AWS KMS to encrypt the EFS volume attached to the domain with an AWS managed customer master key (CMK) by default.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="securityGroupIdForDomainBoundary")
    def security_group_id_for_domain_boundary(self) -> pulumi.Output[str]:
        """
        The ID of the security group that authorizes traffic between the RSessionGateway apps and the RStudioServerPro app.
        """
        return pulumi.get(self, "security_group_id_for_domain_boundary")

    @property
    @pulumi.getter(name="singleSignOnApplicationArn")
    def single_sign_on_application_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the application managed by SageMaker in IAM Identity Center. This value is only returned for domains created after October 1, 2023.
        """
        return pulumi.get(self, "single_sign_on_application_arn")

    @property
    @pulumi.getter(name="singleSignOnManagedApplicationInstanceId")
    def single_sign_on_managed_application_instance_id(self) -> pulumi.Output[str]:
        """
        The SSO managed application instance ID.
        """
        return pulumi.get(self, "single_sign_on_managed_application_instance_id")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The VPC subnets that Studio uses for communication.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.CreateOnlyTag']]]:
        """
        A list of tags to apply to the user profile.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL to the created domain.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the Amazon Virtual Private Cloud (VPC) that Studio uses for communication.
        """
        return pulumi.get(self, "vpc_id")

