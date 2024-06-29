# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 domain_identifier: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 glossary_terms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] domain_identifier: The ID of the Amazon DataZone domain in which this project is created.
        :param pulumi.Input[str] description: The description of the Amazon DataZone project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] glossary_terms: The glossary terms that can be used in this Amazon DataZone project.
        :param pulumi.Input[str] name: The name of the Amazon DataZone project.
        """
        pulumi.set(__self__, "domain_identifier", domain_identifier)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if glossary_terms is not None:
            pulumi.set(__self__, "glossary_terms", glossary_terms)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[str]:
        """
        The ID of the Amazon DataZone domain in which this project is created.
        """
        return pulumi.get(self, "domain_identifier")

    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_identifier", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Amazon DataZone project.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The glossary terms that can be used in this Amazon DataZone project.
        """
        return pulumi.get(self, "glossary_terms")

    @glossary_terms.setter
    def glossary_terms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "glossary_terms", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Amazon DataZone project.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_identifier: Optional[pulumi.Input[str]] = None,
                 glossary_terms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Amazon DataZone projects are business use case–based groupings of people, assets (data), and tools used to simplify access to the AWS analytics.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Amazon DataZone project.
        :param pulumi.Input[str] domain_identifier: The ID of the Amazon DataZone domain in which this project is created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] glossary_terms: The glossary terms that can be used in this Amazon DataZone project.
        :param pulumi.Input[str] name: The name of the Amazon DataZone project.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Amazon DataZone projects are business use case–based groupings of people, assets (data), and tools used to simplify access to the AWS analytics.

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_identifier: Optional[pulumi.Input[str]] = None,
                 glossary_terms: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["description"] = description
            if domain_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'domain_identifier'")
            __props__.__dict__["domain_identifier"] = domain_identifier
            __props__.__dict__["glossary_terms"] = glossary_terms
            __props__.__dict__["name"] = name
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["domain_id"] = None
            __props__.__dict__["last_updated_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domainIdentifier"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Project, __self__).__init__(
            'aws-native:datazone:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectArgs.__new__(ProjectArgs)

        __props__.__dict__["aws_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["domain_id"] = None
        __props__.__dict__["domain_identifier"] = None
        __props__.__dict__["glossary_terms"] = None
        __props__.__dict__["last_updated_at"] = None
        __props__.__dict__["name"] = None
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        The ID of the Amazon DataZone project.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The timestamp of when the project was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        The Amazon DataZone user who created the project.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Amazon DataZone project.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        The identifier of the Amazon DataZone domain in which the project was created.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[str]:
        """
        The ID of the Amazon DataZone domain in which this project is created.
        """
        return pulumi.get(self, "domain_identifier")

    @property
    @pulumi.getter(name="glossaryTerms")
    def glossary_terms(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The glossary terms that can be used in this Amazon DataZone project.
        """
        return pulumi.get(self, "glossary_terms")

    @property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> pulumi.Output[str]:
        """
        The timestamp of when the project was last updated.
        """
        return pulumi.get(self, "last_updated_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Amazon DataZone project.
        """
        return pulumi.get(self, "name")

