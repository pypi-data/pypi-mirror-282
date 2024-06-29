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

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 desktop_arn: pulumi.Input[str],
                 desired_software_set_id: Optional[pulumi.Input[str]] = None,
                 desktop_endpoint: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input['EnvironmentMaintenanceWindowArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 software_set_update_mode: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateMode']] = None,
                 software_set_update_schedule: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateSchedule']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[str] desktop_arn: The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.
        :param pulumi.Input[str] desired_software_set_id: The ID of the software set to apply.
        :param pulumi.Input[str] desktop_endpoint: The URL for the identity provider login (only for environments that use AppStream 2.0).
        :param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
        :param pulumi.Input['EnvironmentMaintenanceWindowArgs'] maintenance_window: A specification for a time window to apply software updates.
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input['EnvironmentSoftwareSetUpdateMode'] software_set_update_mode: An option to define which software updates to apply.
        :param pulumi.Input['EnvironmentSoftwareSetUpdateSchedule'] software_set_update_schedule: An option to define if software updates should be applied within a maintenance window.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "desktop_arn", desktop_arn)
        if desired_software_set_id is not None:
            pulumi.set(__self__, "desired_software_set_id", desired_software_set_id)
        if desktop_endpoint is not None:
            pulumi.set(__self__, "desktop_endpoint", desktop_endpoint)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if software_set_update_mode is not None:
            pulumi.set(__self__, "software_set_update_mode", software_set_update_mode)
        if software_set_update_schedule is not None:
            pulumi.set(__self__, "software_set_update_schedule", software_set_update_schedule)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="desktopArn")
    def desktop_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.
        """
        return pulumi.get(self, "desktop_arn")

    @desktop_arn.setter
    def desktop_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "desktop_arn", value)

    @property
    @pulumi.getter(name="desiredSoftwareSetId")
    def desired_software_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the software set to apply.
        """
        return pulumi.get(self, "desired_software_set_id")

    @desired_software_set_id.setter
    def desired_software_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "desired_software_set_id", value)

    @property
    @pulumi.getter(name="desktopEndpoint")
    def desktop_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The URL for the identity provider login (only for environments that use AppStream 2.0).
        """
        return pulumi.get(self, "desktop_endpoint")

    @desktop_endpoint.setter
    def desktop_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "desktop_endpoint", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input['EnvironmentMaintenanceWindowArgs']]:
        """
        A specification for a time window to apply software updates.
        """
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input['EnvironmentMaintenanceWindowArgs']]):
        pulumi.set(self, "maintenance_window", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="softwareSetUpdateMode")
    def software_set_update_mode(self) -> Optional[pulumi.Input['EnvironmentSoftwareSetUpdateMode']]:
        """
        An option to define which software updates to apply.
        """
        return pulumi.get(self, "software_set_update_mode")

    @software_set_update_mode.setter
    def software_set_update_mode(self, value: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateMode']]):
        pulumi.set(self, "software_set_update_mode", value)

    @property
    @pulumi.getter(name="softwareSetUpdateSchedule")
    def software_set_update_schedule(self) -> Optional[pulumi.Input['EnvironmentSoftwareSetUpdateSchedule']]:
        """
        An option to define if software updates should be applied within a maintenance window.
        """
        return pulumi.get(self, "software_set_update_schedule")

    @software_set_update_schedule.setter
    def software_set_update_schedule(self, value: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateSchedule']]):
        pulumi.set(self, "software_set_update_schedule", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 desired_software_set_id: Optional[pulumi.Input[str]] = None,
                 desktop_arn: Optional[pulumi.Input[str]] = None,
                 desktop_endpoint: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['EnvironmentMaintenanceWindowArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 software_set_update_mode: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateMode']] = None,
                 software_set_update_schedule: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateSchedule']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource type definition for AWS::WorkSpacesThinClient::Environment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] desired_software_set_id: The ID of the software set to apply.
        :param pulumi.Input[str] desktop_arn: The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.
        :param pulumi.Input[str] desktop_endpoint: The URL for the identity provider login (only for environments that use AppStream 2.0).
        :param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
        :param pulumi.Input[pulumi.InputType['EnvironmentMaintenanceWindowArgs']] maintenance_window: A specification for a time window to apply software updates.
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input['EnvironmentSoftwareSetUpdateMode'] software_set_update_mode: An option to define which software updates to apply.
        :param pulumi.Input['EnvironmentSoftwareSetUpdateSchedule'] software_set_update_schedule: An option to define if software updates should be applied within a maintenance window.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource type definition for AWS::WorkSpacesThinClient::Environment.

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 desired_software_set_id: Optional[pulumi.Input[str]] = None,
                 desktop_arn: Optional[pulumi.Input[str]] = None,
                 desktop_endpoint: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['EnvironmentMaintenanceWindowArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 software_set_update_mode: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateMode']] = None,
                 software_set_update_schedule: Optional[pulumi.Input['EnvironmentSoftwareSetUpdateSchedule']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            __props__.__dict__["desired_software_set_id"] = desired_software_set_id
            if desktop_arn is None and not opts.urn:
                raise TypeError("Missing required property 'desktop_arn'")
            __props__.__dict__["desktop_arn"] = desktop_arn
            __props__.__dict__["desktop_endpoint"] = desktop_endpoint
            __props__.__dict__["kms_key_arn"] = kms_key_arn
            __props__.__dict__["maintenance_window"] = maintenance_window
            __props__.__dict__["name"] = name
            __props__.__dict__["software_set_update_mode"] = software_set_update_mode
            __props__.__dict__["software_set_update_schedule"] = software_set_update_schedule
            __props__.__dict__["tags"] = tags
            __props__.__dict__["activation_code"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["desktop_type"] = None
            __props__.__dict__["pending_software_set_id"] = None
            __props__.__dict__["pending_software_set_version"] = None
            __props__.__dict__["registered_devices_count"] = None
            __props__.__dict__["software_set_compliance_status"] = None
            __props__.__dict__["updated_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["desktopArn", "kmsKeyArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Environment, __self__).__init__(
            'aws-native:workspacesthinclient:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

        __props__.__dict__["activation_code"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["desired_software_set_id"] = None
        __props__.__dict__["desktop_arn"] = None
        __props__.__dict__["desktop_endpoint"] = None
        __props__.__dict__["desktop_type"] = None
        __props__.__dict__["kms_key_arn"] = None
        __props__.__dict__["maintenance_window"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pending_software_set_id"] = None
        __props__.__dict__["pending_software_set_version"] = None
        __props__.__dict__["registered_devices_count"] = None
        __props__.__dict__["software_set_compliance_status"] = None
        __props__.__dict__["software_set_update_mode"] = None
        __props__.__dict__["software_set_update_schedule"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["updated_at"] = None
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activationCode")
    def activation_code(self) -> pulumi.Output[str]:
        """
        Activation code for devices associated with environment.
        """
        return pulumi.get(self, "activation_code")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The environment ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        Unique identifier of the environment.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The timestamp in unix epoch format when environment was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="desiredSoftwareSetId")
    def desired_software_set_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the software set to apply.
        """
        return pulumi.get(self, "desired_software_set_id")

    @property
    @pulumi.getter(name="desktopArn")
    def desktop_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.
        """
        return pulumi.get(self, "desktop_arn")

    @property
    @pulumi.getter(name="desktopEndpoint")
    def desktop_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        The URL for the identity provider login (only for environments that use AppStream 2.0).
        """
        return pulumi.get(self, "desktop_endpoint")

    @property
    @pulumi.getter(name="desktopType")
    def desktop_type(self) -> pulumi.Output['EnvironmentDesktopType']:
        """
        The type of VDI.
        """
        return pulumi.get(self, "desktop_type")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[Optional['outputs.EnvironmentMaintenanceWindow']]:
        """
        A specification for a time window to apply software updates.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pendingSoftwareSetId")
    def pending_software_set_id(self) -> pulumi.Output[str]:
        """
        The ID of the software set that is pending to be installed.
        """
        return pulumi.get(self, "pending_software_set_id")

    @property
    @pulumi.getter(name="pendingSoftwareSetVersion")
    def pending_software_set_version(self) -> pulumi.Output[str]:
        """
        The version of the software set that is pending to be installed.
        """
        return pulumi.get(self, "pending_software_set_version")

    @property
    @pulumi.getter(name="registeredDevicesCount")
    def registered_devices_count(self) -> pulumi.Output[int]:
        """
        Number of devices registered to the environment.
        """
        return pulumi.get(self, "registered_devices_count")

    @property
    @pulumi.getter(name="softwareSetComplianceStatus")
    def software_set_compliance_status(self) -> pulumi.Output['EnvironmentSoftwareSetComplianceStatus']:
        """
        Describes if the software currently installed on all devices in the environment is a supported version.
        """
        return pulumi.get(self, "software_set_compliance_status")

    @property
    @pulumi.getter(name="softwareSetUpdateMode")
    def software_set_update_mode(self) -> pulumi.Output[Optional['EnvironmentSoftwareSetUpdateMode']]:
        """
        An option to define which software updates to apply.
        """
        return pulumi.get(self, "software_set_update_mode")

    @property
    @pulumi.getter(name="softwareSetUpdateSchedule")
    def software_set_update_schedule(self) -> pulumi.Output[Optional['EnvironmentSoftwareSetUpdateSchedule']]:
        """
        An option to define if software updates should be applied within a maintenance window.
        """
        return pulumi.get(self, "software_set_update_schedule")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The timestamp in unix epoch format when environment was last updated.
        """
        return pulumi.get(self, "updated_at")

