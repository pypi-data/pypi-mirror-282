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
    'GetRepositoryResult',
    'AwaitableGetRepositoryResult',
    'get_repository',
    'get_repository_output',
]

@pulumi.output_type
class GetRepositoryResult:
    def __init__(__self__, arn=None, description=None, external_connections=None, name=None, permissions_policy_document=None, tags=None, upstreams=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if external_connections and not isinstance(external_connections, list):
            raise TypeError("Expected argument 'external_connections' to be a list")
        pulumi.set(__self__, "external_connections", external_connections)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions_policy_document and not isinstance(permissions_policy_document, dict):
            raise TypeError("Expected argument 'permissions_policy_document' to be a dict")
        pulumi.set(__self__, "permissions_policy_document", permissions_policy_document)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if upstreams and not isinstance(upstreams, list):
            raise TypeError("Expected argument 'upstreams' to be a list")
        pulumi.set(__self__, "upstreams", upstreams)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the repository.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A text description of the repository.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="externalConnections")
    def external_connections(self) -> Optional[Sequence[str]]:
        """
        A list of external connections associated with the repository.
        """
        return pulumi.get(self, "external_connections")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the repository. This is used for GetAtt
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="permissionsPolicyDocument")
    def permissions_policy_document(self) -> Optional[Any]:
        """
        The access control resource policy on the provided repository.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CodeArtifact::Repository` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "permissions_policy_document")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def upstreams(self) -> Optional[Sequence[str]]:
        """
        A list of upstream repositories associated with the repository.
        """
        return pulumi.get(self, "upstreams")


class AwaitableGetRepositoryResult(GetRepositoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryResult(
            arn=self.arn,
            description=self.description,
            external_connections=self.external_connections,
            name=self.name,
            permissions_policy_document=self.permissions_policy_document,
            tags=self.tags,
            upstreams=self.upstreams)


def get_repository(arn: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryResult:
    """
    The resource schema to create a CodeArtifact repository.


    :param str arn: The ARN of the repository.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:codeartifact:getRepository', __args__, opts=opts, typ=GetRepositoryResult).value

    return AwaitableGetRepositoryResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        external_connections=pulumi.get(__ret__, 'external_connections'),
        name=pulumi.get(__ret__, 'name'),
        permissions_policy_document=pulumi.get(__ret__, 'permissions_policy_document'),
        tags=pulumi.get(__ret__, 'tags'),
        upstreams=pulumi.get(__ret__, 'upstreams'))


@_utilities.lift_output_func(get_repository)
def get_repository_output(arn: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoryResult]:
    """
    The resource schema to create a CodeArtifact repository.


    :param str arn: The ARN of the repository.
    """
    ...
