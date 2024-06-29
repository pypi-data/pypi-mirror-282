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
    'SchemaRegistry',
    'SchemaVersion',
    'SchemaVersionSchema',
]

@pulumi.output_type
class SchemaRegistry(dict):
    """
    Identifier for the registry which the schema is part of.
    """
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 name: Optional[str] = None):
        """
        Identifier for the registry which the schema is part of.
        :param str arn: Amazon Resource Name for the Registry.
        :param str name: Name of the registry in which the schema will be created.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name for the Registry.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the registry in which the schema will be created.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SchemaVersion(dict):
    """
    Specify checkpoint version for update. This is only required to update the Compatibility.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "isLatest":
            suggest = "is_latest"
        elif key == "versionNumber":
            suggest = "version_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SchemaVersion. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SchemaVersion.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SchemaVersion.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 is_latest: Optional[bool] = None,
                 version_number: Optional[int] = None):
        """
        Specify checkpoint version for update. This is only required to update the Compatibility.
        :param bool is_latest: Indicates if the latest version needs to be updated.
        :param int version_number: Indicates the version number in the schema to update.
        """
        if is_latest is not None:
            pulumi.set(__self__, "is_latest", is_latest)
        if version_number is not None:
            pulumi.set(__self__, "version_number", version_number)

    @property
    @pulumi.getter(name="isLatest")
    def is_latest(self) -> Optional[bool]:
        """
        Indicates if the latest version needs to be updated.
        """
        return pulumi.get(self, "is_latest")

    @property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> Optional[int]:
        """
        Indicates the version number in the schema to update.
        """
        return pulumi.get(self, "version_number")


@pulumi.output_type
class SchemaVersionSchema(dict):
    """
    Identifier for the schema where the schema version will be created.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "registryName":
            suggest = "registry_name"
        elif key == "schemaArn":
            suggest = "schema_arn"
        elif key == "schemaName":
            suggest = "schema_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SchemaVersionSchema. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SchemaVersionSchema.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SchemaVersionSchema.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 registry_name: Optional[str] = None,
                 schema_arn: Optional[str] = None,
                 schema_name: Optional[str] = None):
        """
        Identifier for the schema where the schema version will be created.
        :param str registry_name: Name of the registry to identify where the Schema is located.
        :param str schema_arn: Amazon Resource Name for the Schema. This attribute can be used to uniquely represent the Schema.
        :param str schema_name: Name of the schema. This parameter requires RegistryName to be provided.
        """
        if registry_name is not None:
            pulumi.set(__self__, "registry_name", registry_name)
        if schema_arn is not None:
            pulumi.set(__self__, "schema_arn", schema_arn)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> Optional[str]:
        """
        Name of the registry to identify where the Schema is located.
        """
        return pulumi.get(self, "registry_name")

    @property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> Optional[str]:
        """
        Amazon Resource Name for the Schema. This attribute can be used to uniquely represent the Schema.
        """
        return pulumi.get(self, "schema_arn")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[str]:
        """
        Name of the schema. This parameter requires RegistryName to be provided.
        """
        return pulumi.get(self, "schema_name")


