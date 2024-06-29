# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetSchemaResult',
    'AwaitableGetSchemaResult',
    'get_schema',
    'get_schema_output',
]

@pulumi.output_type
class GetSchemaResult:
    def __init__(__self__, content=None, description=None, last_modified=None, schema_arn=None, schema_version=None, tags=None, type=None, version_created_date=None):
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if schema_arn and not isinstance(schema_arn, str):
            raise TypeError("Expected argument 'schema_arn' to be a str")
        pulumi.set(__self__, "schema_arn", schema_arn)
        if schema_version and not isinstance(schema_version, str):
            raise TypeError("Expected argument 'schema_version' to be a str")
        pulumi.set(__self__, "schema_version", schema_version)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version_created_date and not isinstance(version_created_date, str):
            raise TypeError("Expected argument 'version_created_date' to be a str")
        pulumi.set(__self__, "version_created_date", version_created_date)

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        The source of the schema definition.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the schema.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[str]:
        """
        The last modified time of the schema.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> Optional[str]:
        """
        The ARN of the schema.
        """
        return pulumi.get(self, "schema_arn")

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[str]:
        """
        The version number of the schema.
        """
        return pulumi.get(self, "schema_version")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Tags associated with the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of schema. Valid types include OpenApi3 and JSONSchemaDraft4.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="versionCreatedDate")
    def version_created_date(self) -> Optional[str]:
        """
        The date the schema version was created.
        """
        return pulumi.get(self, "version_created_date")


class AwaitableGetSchemaResult(GetSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchemaResult(
            content=self.content,
            description=self.description,
            last_modified=self.last_modified,
            schema_arn=self.schema_arn,
            schema_version=self.schema_version,
            tags=self.tags,
            type=self.type,
            version_created_date=self.version_created_date)


def get_schema(schema_arn: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchemaResult:
    """
    Resource Type definition for AWS::EventSchemas::Schema


    :param str schema_arn: The ARN of the schema.
    """
    __args__ = dict()
    __args__['schemaArn'] = schema_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:eventschemas:getSchema', __args__, opts=opts, typ=GetSchemaResult).value

    return AwaitableGetSchemaResult(
        content=pulumi.get(__ret__, 'content'),
        description=pulumi.get(__ret__, 'description'),
        last_modified=pulumi.get(__ret__, 'last_modified'),
        schema_arn=pulumi.get(__ret__, 'schema_arn'),
        schema_version=pulumi.get(__ret__, 'schema_version'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        version_created_date=pulumi.get(__ret__, 'version_created_date'))


@_utilities.lift_output_func(get_schema)
def get_schema_output(schema_arn: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSchemaResult]:
    """
    Resource Type definition for AWS::EventSchemas::Schema


    :param str schema_arn: The ARN of the schema.
    """
    ...
