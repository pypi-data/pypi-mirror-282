# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    def __init__(__self__, created_at=None, created_by=None, description=None, domain_id=None, glossary_terms=None, id=None, last_updated_at=None, name=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if glossary_terms and not isinstance(glossary_terms, list):
            raise TypeError("Expected argument 'glossary_terms' to be a list")
        pulumi.set(__self__, "glossary_terms", glossary_terms)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_updated_at and not isinstance(last_updated_at, str):
            raise TypeError("Expected argument 'last_updated_at' to be a str")
        pulumi.set(__self__, "last_updated_at", last_updated_at)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of when the project was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The Amazon DataZone user who created the project.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the Amazon DataZone project.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[str]:
        """
        The identifier of the Amazon DataZone domain in which the project was created.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(self) -> Optional[Sequence[str]]:
        """
        The glossary terms that can be used in this Amazon DataZone project.
        """
        return pulumi.get(self, "glossary_terms")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the Amazon DataZone project.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> Optional[str]:
        """
        The timestamp of when the project was last updated.
        """
        return pulumi.get(self, "last_updated_at")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the Amazon DataZone project.
        """
        return pulumi.get(self, "name")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            created_at=self.created_at,
            created_by=self.created_by,
            description=self.description,
            domain_id=self.domain_id,
            glossary_terms=self.glossary_terms,
            id=self.id,
            last_updated_at=self.last_updated_at,
            name=self.name)


def get_project(domain_id: Optional[str] = None,
                id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Amazon DataZone projects are business use case–based groupings of people, assets (data), and tools used to simplify access to the AWS analytics.


    :param str domain_id: The identifier of the Amazon DataZone domain in which the project was created.
    :param str id: The ID of the Amazon DataZone project.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datazone:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        created_by=pulumi.get(__ret__, 'created_by'),
        description=pulumi.get(__ret__, 'description'),
        domain_id=pulumi.get(__ret__, 'domain_id'),
        glossary_terms=pulumi.get(__ret__, 'glossary_terms'),
        id=pulumi.get(__ret__, 'id'),
        last_updated_at=pulumi.get(__ret__, 'last_updated_at'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_project)
def get_project_output(domain_id: Optional[pulumi.Input[str]] = None,
                       id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Amazon DataZone projects are business use case–based groupings of people, assets (data), and tools used to simplify access to the AWS analytics.


    :param str domain_id: The identifier of the Amazon DataZone domain in which the project was created.
    :param str id: The ID of the Amazon DataZone project.
    """
    ...
