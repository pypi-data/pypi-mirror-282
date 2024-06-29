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
    'Namespace',
    'NamespaceSnapshotCopyConfiguration',
    'Workgroup',
    'WorkgroupConfigParameter',
    'WorkgroupEndpoint',
    'WorkgroupNetworkInterface',
    'WorkgroupVpcEndpoint',
]

@pulumi.output_type
class Namespace(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "adminPasswordSecretArn":
            suggest = "admin_password_secret_arn"
        elif key == "adminPasswordSecretKmsKeyId":
            suggest = "admin_password_secret_kms_key_id"
        elif key == "adminUsername":
            suggest = "admin_username"
        elif key == "creationDate":
            suggest = "creation_date"
        elif key == "dbName":
            suggest = "db_name"
        elif key == "defaultIamRoleArn":
            suggest = "default_iam_role_arn"
        elif key == "iamRoles":
            suggest = "iam_roles"
        elif key == "kmsKeyId":
            suggest = "kms_key_id"
        elif key == "logExports":
            suggest = "log_exports"
        elif key == "namespaceArn":
            suggest = "namespace_arn"
        elif key == "namespaceId":
            suggest = "namespace_id"
        elif key == "namespaceName":
            suggest = "namespace_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Namespace. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Namespace.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Namespace.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 admin_password_secret_arn: Optional[str] = None,
                 admin_password_secret_kms_key_id: Optional[str] = None,
                 admin_username: Optional[str] = None,
                 creation_date: Optional[str] = None,
                 db_name: Optional[str] = None,
                 default_iam_role_arn: Optional[str] = None,
                 iam_roles: Optional[Sequence[str]] = None,
                 kms_key_id: Optional[str] = None,
                 log_exports: Optional[Sequence['NamespaceLogExport']] = None,
                 namespace_arn: Optional[str] = None,
                 namespace_id: Optional[str] = None,
                 namespace_name: Optional[str] = None,
                 status: Optional['NamespaceStatus'] = None):
        """
        :param str admin_password_secret_arn: The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.
        :param str admin_password_secret_kms_key_id: The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.
        :param str admin_username: The username of the administrator for the first database created in the namespace.
        :param str creation_date: The date of when the namespace was created.
        :param str db_name: The name of the first database created in the namespace.
        :param str default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
        :param Sequence[str] iam_roles: A list of IAM roles to associate with the namespace.
        :param str kms_key_id: The ID of the AWS Key Management Service key used to encrypt your data.
        :param Sequence['NamespaceLogExport'] log_exports: The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.
        :param str namespace_arn: The Amazon Resource Name (ARN) associated with a namespace.
        :param str namespace_id: The unique identifier of a namespace.
        :param str namespace_name: The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
        :param 'NamespaceStatus' status: The status of the namespace.
        """
        if admin_password_secret_arn is not None:
            pulumi.set(__self__, "admin_password_secret_arn", admin_password_secret_arn)
        if admin_password_secret_kms_key_id is not None:
            pulumi.set(__self__, "admin_password_secret_kms_key_id", admin_password_secret_kms_key_id)
        if admin_username is not None:
            pulumi.set(__self__, "admin_username", admin_username)
        if creation_date is not None:
            pulumi.set(__self__, "creation_date", creation_date)
        if db_name is not None:
            pulumi.set(__self__, "db_name", db_name)
        if default_iam_role_arn is not None:
            pulumi.set(__self__, "default_iam_role_arn", default_iam_role_arn)
        if iam_roles is not None:
            pulumi.set(__self__, "iam_roles", iam_roles)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if log_exports is not None:
            pulumi.set(__self__, "log_exports", log_exports)
        if namespace_arn is not None:
            pulumi.set(__self__, "namespace_arn", namespace_arn)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="adminPasswordSecretArn")
    def admin_password_secret_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.
        """
        return pulumi.get(self, "admin_password_secret_arn")

    @property
    @pulumi.getter(name="adminPasswordSecretKmsKeyId")
    def admin_password_secret_kms_key_id(self) -> Optional[str]:
        """
        The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.
        """
        return pulumi.get(self, "admin_password_secret_kms_key_id")

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[str]:
        """
        The username of the administrator for the first database created in the namespace.
        """
        return pulumi.get(self, "admin_username")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        """
        The date of when the namespace was created.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[str]:
        """
        The name of the first database created in the namespace.
        """
        return pulumi.get(self, "db_name")

    @property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
        """
        return pulumi.get(self, "default_iam_role_arn")

    @property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[Sequence[str]]:
        """
        A list of IAM roles to associate with the namespace.
        """
        return pulumi.get(self, "iam_roles")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The ID of the AWS Key Management Service key used to encrypt your data.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[Sequence['NamespaceLogExport']]:
        """
        The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.
        """
        return pulumi.get(self, "log_exports")

    @property
    @pulumi.getter(name="namespaceArn")
    def namespace_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) associated with a namespace.
        """
        return pulumi.get(self, "namespace_arn")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[str]:
        """
        The unique identifier of a namespace.
        """
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[str]:
        """
        The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
        """
        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter
    def status(self) -> Optional['NamespaceStatus']:
        """
        The status of the namespace.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class NamespaceSnapshotCopyConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "destinationRegion":
            suggest = "destination_region"
        elif key == "destinationKmsKeyId":
            suggest = "destination_kms_key_id"
        elif key == "snapshotRetentionPeriod":
            suggest = "snapshot_retention_period"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NamespaceSnapshotCopyConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NamespaceSnapshotCopyConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NamespaceSnapshotCopyConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 destination_region: str,
                 destination_kms_key_id: Optional[str] = None,
                 snapshot_retention_period: Optional[int] = None):
        """
        :param str destination_region: The destination AWS Region to copy snapshots to.
        :param str destination_kms_key_id: The ID of the KMS key to use to encrypt your snapshots in the destination AWS Region .
        :param int snapshot_retention_period: The retention period of snapshots that are copied to the destination AWS Region .
        """
        pulumi.set(__self__, "destination_region", destination_region)
        if destination_kms_key_id is not None:
            pulumi.set(__self__, "destination_kms_key_id", destination_kms_key_id)
        if snapshot_retention_period is not None:
            pulumi.set(__self__, "snapshot_retention_period", snapshot_retention_period)

    @property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> str:
        """
        The destination AWS Region to copy snapshots to.
        """
        return pulumi.get(self, "destination_region")

    @property
    @pulumi.getter(name="destinationKmsKeyId")
    def destination_kms_key_id(self) -> Optional[str]:
        """
        The ID of the KMS key to use to encrypt your snapshots in the destination AWS Region .
        """
        return pulumi.get(self, "destination_kms_key_id")

    @property
    @pulumi.getter(name="snapshotRetentionPeriod")
    def snapshot_retention_period(self) -> Optional[int]:
        """
        The retention period of snapshots that are copied to the destination AWS Region .
        """
        return pulumi.get(self, "snapshot_retention_period")


@pulumi.output_type
class Workgroup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "baseCapacity":
            suggest = "base_capacity"
        elif key == "configParameters":
            suggest = "config_parameters"
        elif key == "creationDate":
            suggest = "creation_date"
        elif key == "enhancedVpcRouting":
            suggest = "enhanced_vpc_routing"
        elif key == "maxCapacity":
            suggest = "max_capacity"
        elif key == "namespaceName":
            suggest = "namespace_name"
        elif key == "publiclyAccessible":
            suggest = "publicly_accessible"
        elif key == "securityGroupIds":
            suggest = "security_group_ids"
        elif key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "workgroupArn":
            suggest = "workgroup_arn"
        elif key == "workgroupId":
            suggest = "workgroup_id"
        elif key == "workgroupName":
            suggest = "workgroup_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Workgroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Workgroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Workgroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 base_capacity: Optional[int] = None,
                 config_parameters: Optional[Sequence['outputs.WorkgroupConfigParameter']] = None,
                 creation_date: Optional[str] = None,
                 endpoint: Optional['outputs.WorkgroupEndpoint'] = None,
                 enhanced_vpc_routing: Optional[bool] = None,
                 max_capacity: Optional[int] = None,
                 namespace_name: Optional[str] = None,
                 publicly_accessible: Optional[bool] = None,
                 security_group_ids: Optional[Sequence[str]] = None,
                 status: Optional['WorkgroupStatus'] = None,
                 subnet_ids: Optional[Sequence[str]] = None,
                 workgroup_arn: Optional[str] = None,
                 workgroup_id: Optional[str] = None,
                 workgroup_name: Optional[str] = None):
        """
        :param int base_capacity: The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
        :param Sequence['WorkgroupConfigParameter'] config_parameters: An array of parameters to set for advanced control over a database. The options are `auto_mv` , `datestyle` , `enable_case_sensitive_identifier` , `enable_user_activity_logging` , `query_group` , `search_path` , `require_ssl` , `use_fips_ssl` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see [Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless) .
        :param str creation_date: The creation date of the workgroup.
        :param 'WorkgroupEndpoint' endpoint: The endpoint that is created from the workgroup.
        :param bool enhanced_vpc_routing: The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.
        :param int max_capacity: The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
        :param str namespace_name: The namespace the workgroup is associated with.
        :param bool publicly_accessible: A value that specifies whether the workgroup can be accessible from a public network.
        :param Sequence[str] security_group_ids: An array of security group IDs to associate with the workgroup.
        :param 'WorkgroupStatus' status: The status of the workgroup.
        :param Sequence[str] subnet_ids: An array of subnet IDs the workgroup is associated with.
        :param str workgroup_arn: The Amazon Resource Name (ARN) that links to the workgroup.
        :param str workgroup_id: The unique identifier of the workgroup.
        :param str workgroup_name: The name of the workgroup.
        """
        if base_capacity is not None:
            pulumi.set(__self__, "base_capacity", base_capacity)
        if config_parameters is not None:
            pulumi.set(__self__, "config_parameters", config_parameters)
        if creation_date is not None:
            pulumi.set(__self__, "creation_date", creation_date)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if enhanced_vpc_routing is not None:
            pulumi.set(__self__, "enhanced_vpc_routing", enhanced_vpc_routing)
        if max_capacity is not None:
            pulumi.set(__self__, "max_capacity", max_capacity)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if publicly_accessible is not None:
            pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if workgroup_arn is not None:
            pulumi.set(__self__, "workgroup_arn", workgroup_arn)
        if workgroup_id is not None:
            pulumi.set(__self__, "workgroup_id", workgroup_id)
        if workgroup_name is not None:
            pulumi.set(__self__, "workgroup_name", workgroup_name)

    @property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> Optional[int]:
        """
        The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
        """
        return pulumi.get(self, "base_capacity")

    @property
    @pulumi.getter(name="configParameters")
    def config_parameters(self) -> Optional[Sequence['outputs.WorkgroupConfigParameter']]:
        """
        An array of parameters to set for advanced control over a database. The options are `auto_mv` , `datestyle` , `enable_case_sensitive_identifier` , `enable_user_activity_logging` , `query_group` , `search_path` , `require_ssl` , `use_fips_ssl` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see [Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless) .
        """
        return pulumi.get(self, "config_parameters")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        """
        The creation date of the workgroup.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional['outputs.WorkgroupEndpoint']:
        """
        The endpoint that is created from the workgroup.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> Optional[bool]:
        """
        The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.
        """
        return pulumi.get(self, "enhanced_vpc_routing")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[int]:
        """
        The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[str]:
        """
        The namespace the workgroup is associated with.
        """
        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[bool]:
        """
        A value that specifies whether the workgroup can be accessible from a public network.
        """
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[str]]:
        """
        An array of security group IDs to associate with the workgroup.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter
    def status(self) -> Optional['WorkgroupStatus']:
        """
        The status of the workgroup.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        """
        An array of subnet IDs the workgroup is associated with.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="workgroupArn")
    def workgroup_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) that links to the workgroup.
        """
        return pulumi.get(self, "workgroup_arn")

    @property
    @pulumi.getter(name="workgroupId")
    def workgroup_id(self) -> Optional[str]:
        """
        The unique identifier of the workgroup.
        """
        return pulumi.get(self, "workgroup_id")

    @property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> Optional[str]:
        """
        The name of the workgroup.
        """
        return pulumi.get(self, "workgroup_name")


@pulumi.output_type
class WorkgroupConfigParameter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "parameterKey":
            suggest = "parameter_key"
        elif key == "parameterValue":
            suggest = "parameter_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkgroupConfigParameter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkgroupConfigParameter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkgroupConfigParameter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 parameter_key: Optional[str] = None,
                 parameter_value: Optional[str] = None):
        """
        :param str parameter_key: The key of the parameter. The options are `datestyle` , `enable_user_activity_logging` , `query_group` , `search_path` , `max_query_execution_time` , and `require_ssl` .
        :param str parameter_value: The value of the parameter to set.
        """
        if parameter_key is not None:
            pulumi.set(__self__, "parameter_key", parameter_key)
        if parameter_value is not None:
            pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> Optional[str]:
        """
        The key of the parameter. The options are `datestyle` , `enable_user_activity_logging` , `query_group` , `search_path` , `max_query_execution_time` , and `require_ssl` .
        """
        return pulumi.get(self, "parameter_key")

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[str]:
        """
        The value of the parameter to set.
        """
        return pulumi.get(self, "parameter_value")


@pulumi.output_type
class WorkgroupEndpoint(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vpcEndpoints":
            suggest = "vpc_endpoints"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkgroupEndpoint. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkgroupEndpoint.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkgroupEndpoint.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 address: Optional[str] = None,
                 port: Optional[int] = None,
                 vpc_endpoints: Optional[Sequence['outputs.WorkgroupVpcEndpoint']] = None):
        """
        :param str address: The DNS address of the VPC endpoint.
        :param int port: The port that Amazon Redshift Serverless listens on.
        :param Sequence['WorkgroupVpcEndpoint'] vpc_endpoints: An array of `VpcEndpoint` objects.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if vpc_endpoints is not None:
            pulumi.set(__self__, "vpc_endpoints", vpc_endpoints)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The DNS address of the VPC endpoint.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The port that Amazon Redshift Serverless listens on.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[Sequence['outputs.WorkgroupVpcEndpoint']]:
        """
        An array of `VpcEndpoint` objects.
        """
        return pulumi.get(self, "vpc_endpoints")


@pulumi.output_type
class WorkgroupNetworkInterface(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "availabilityZone":
            suggest = "availability_zone"
        elif key == "networkInterfaceId":
            suggest = "network_interface_id"
        elif key == "privateIpAddress":
            suggest = "private_ip_address"
        elif key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkgroupNetworkInterface. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkgroupNetworkInterface.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkgroupNetworkInterface.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 availability_zone: Optional[str] = None,
                 network_interface_id: Optional[str] = None,
                 private_ip_address: Optional[str] = None,
                 subnet_id: Optional[str] = None):
        """
        :param str availability_zone: The availability Zone.
        :param str network_interface_id: The unique identifier of the network interface.
        :param str private_ip_address: The IPv4 address of the network interface within the subnet.
        :param str subnet_id: The unique identifier of the subnet.
        """
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        The availability Zone.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[str]:
        """
        The unique identifier of the network interface.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[str]:
        """
        The IPv4 address of the network interface within the subnet.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        The unique identifier of the subnet.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class WorkgroupVpcEndpoint(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkInterfaces":
            suggest = "network_interfaces"
        elif key == "vpcEndpointId":
            suggest = "vpc_endpoint_id"
        elif key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkgroupVpcEndpoint. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkgroupVpcEndpoint.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkgroupVpcEndpoint.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_interfaces: Optional[Sequence['outputs.WorkgroupNetworkInterface']] = None,
                 vpc_endpoint_id: Optional[str] = None,
                 vpc_id: Optional[str] = None):
        """
        :param Sequence['WorkgroupNetworkInterface'] network_interfaces: One or more network interfaces of the endpoint. Also known as an interface endpoint.
        :param str vpc_endpoint_id: The connection endpoint ID for connecting to Amazon Redshift Serverless.
        :param str vpc_id: The VPC identifier that the endpoint is associated with.
        """
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if vpc_endpoint_id is not None:
            pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence['outputs.WorkgroupNetworkInterface']]:
        """
        One or more network interfaces of the endpoint. Also known as an interface endpoint.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[str]:
        """
        The connection endpoint ID for connecting to Amazon Redshift Serverless.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        The VPC identifier that the endpoint is associated with.
        """
        return pulumi.get(self, "vpc_id")


