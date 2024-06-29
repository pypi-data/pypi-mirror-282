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

__all__ = ['FhirDatastoreArgs', 'FhirDatastore']

@pulumi.input_type
class FhirDatastoreArgs:
    def __init__(__self__, *,
                 datastore_type_version: pulumi.Input['FhirDatastoreDatastoreTypeVersion'],
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 identity_provider_configuration: Optional[pulumi.Input['FhirDatastoreIdentityProviderConfigurationArgs']] = None,
                 preload_data_config: Optional[pulumi.Input['FhirDatastorePreloadDataConfigArgs']] = None,
                 sse_configuration: Optional[pulumi.Input['FhirDatastoreSseConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a FhirDatastore resource.
        :param pulumi.Input['FhirDatastoreDatastoreTypeVersion'] datastore_type_version: The FHIR version of the data store. The only supported version is R4.
        :param pulumi.Input[str] datastore_name: The user generated name for the data store.
        :param pulumi.Input['FhirDatastoreIdentityProviderConfigurationArgs'] identity_provider_configuration: The identity provider configuration that you gave when the data store was created.
        :param pulumi.Input['FhirDatastorePreloadDataConfigArgs'] preload_data_config: The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.
        :param pulumi.Input['FhirDatastoreSseConfigurationArgs'] sse_configuration: The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        pulumi.set(__self__, "datastore_type_version", datastore_type_version)
        if datastore_name is not None:
            pulumi.set(__self__, "datastore_name", datastore_name)
        if identity_provider_configuration is not None:
            pulumi.set(__self__, "identity_provider_configuration", identity_provider_configuration)
        if preload_data_config is not None:
            pulumi.set(__self__, "preload_data_config", preload_data_config)
        if sse_configuration is not None:
            pulumi.set(__self__, "sse_configuration", sse_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="datastoreTypeVersion")
    def datastore_type_version(self) -> pulumi.Input['FhirDatastoreDatastoreTypeVersion']:
        """
        The FHIR version of the data store. The only supported version is R4.
        """
        return pulumi.get(self, "datastore_type_version")

    @datastore_type_version.setter
    def datastore_type_version(self, value: pulumi.Input['FhirDatastoreDatastoreTypeVersion']):
        pulumi.set(self, "datastore_type_version", value)

    @property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user generated name for the data store.
        """
        return pulumi.get(self, "datastore_name")

    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datastore_name", value)

    @property
    @pulumi.getter(name="identityProviderConfiguration")
    def identity_provider_configuration(self) -> Optional[pulumi.Input['FhirDatastoreIdentityProviderConfigurationArgs']]:
        """
        The identity provider configuration that you gave when the data store was created.
        """
        return pulumi.get(self, "identity_provider_configuration")

    @identity_provider_configuration.setter
    def identity_provider_configuration(self, value: Optional[pulumi.Input['FhirDatastoreIdentityProviderConfigurationArgs']]):
        pulumi.set(self, "identity_provider_configuration", value)

    @property
    @pulumi.getter(name="preloadDataConfig")
    def preload_data_config(self) -> Optional[pulumi.Input['FhirDatastorePreloadDataConfigArgs']]:
        """
        The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.
        """
        return pulumi.get(self, "preload_data_config")

    @preload_data_config.setter
    def preload_data_config(self, value: Optional[pulumi.Input['FhirDatastorePreloadDataConfigArgs']]):
        pulumi.set(self, "preload_data_config", value)

    @property
    @pulumi.getter(name="sseConfiguration")
    def sse_configuration(self) -> Optional[pulumi.Input['FhirDatastoreSseConfigurationArgs']]:
        """
        The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.
        """
        return pulumi.get(self, "sse_configuration")

    @sse_configuration.setter
    def sse_configuration(self, value: Optional[pulumi.Input['FhirDatastoreSseConfigurationArgs']]):
        pulumi.set(self, "sse_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class FhirDatastore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 datastore_type_version: Optional[pulumi.Input['FhirDatastoreDatastoreTypeVersion']] = None,
                 identity_provider_configuration: Optional[pulumi.Input[pulumi.InputType['FhirDatastoreIdentityProviderConfigurationArgs']]] = None,
                 preload_data_config: Optional[pulumi.Input[pulumi.InputType['FhirDatastorePreloadDataConfigArgs']]] = None,
                 sse_configuration: Optional[pulumi.Input[pulumi.InputType['FhirDatastoreSseConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        HealthLake FHIR Datastore

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datastore_name: The user generated name for the data store.
        :param pulumi.Input['FhirDatastoreDatastoreTypeVersion'] datastore_type_version: The FHIR version of the data store. The only supported version is R4.
        :param pulumi.Input[pulumi.InputType['FhirDatastoreIdentityProviderConfigurationArgs']] identity_provider_configuration: The identity provider configuration that you gave when the data store was created.
        :param pulumi.Input[pulumi.InputType['FhirDatastorePreloadDataConfigArgs']] preload_data_config: The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.
        :param pulumi.Input[pulumi.InputType['FhirDatastoreSseConfigurationArgs']] sse_configuration: The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FhirDatastoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        HealthLake FHIR Datastore

        :param str resource_name: The name of the resource.
        :param FhirDatastoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FhirDatastoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 datastore_type_version: Optional[pulumi.Input['FhirDatastoreDatastoreTypeVersion']] = None,
                 identity_provider_configuration: Optional[pulumi.Input[pulumi.InputType['FhirDatastoreIdentityProviderConfigurationArgs']]] = None,
                 preload_data_config: Optional[pulumi.Input[pulumi.InputType['FhirDatastorePreloadDataConfigArgs']]] = None,
                 sse_configuration: Optional[pulumi.Input[pulumi.InputType['FhirDatastoreSseConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FhirDatastoreArgs.__new__(FhirDatastoreArgs)

            __props__.__dict__["datastore_name"] = datastore_name
            if datastore_type_version is None and not opts.urn:
                raise TypeError("Missing required property 'datastore_type_version'")
            __props__.__dict__["datastore_type_version"] = datastore_type_version
            __props__.__dict__["identity_provider_configuration"] = identity_provider_configuration
            __props__.__dict__["preload_data_config"] = preload_data_config
            __props__.__dict__["sse_configuration"] = sse_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_at"] = None
            __props__.__dict__["datastore_arn"] = None
            __props__.__dict__["datastore_endpoint"] = None
            __props__.__dict__["datastore_id"] = None
            __props__.__dict__["datastore_status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["datastoreName", "datastoreTypeVersion", "identityProviderConfiguration", "preloadDataConfig", "sseConfiguration"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(FhirDatastore, __self__).__init__(
            'aws-native:healthlake:FhirDatastore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FhirDatastore':
        """
        Get an existing FhirDatastore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FhirDatastoreArgs.__new__(FhirDatastoreArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["datastore_arn"] = None
        __props__.__dict__["datastore_endpoint"] = None
        __props__.__dict__["datastore_id"] = None
        __props__.__dict__["datastore_name"] = None
        __props__.__dict__["datastore_status"] = None
        __props__.__dict__["datastore_type_version"] = None
        __props__.__dict__["identity_provider_configuration"] = None
        __props__.__dict__["preload_data_config"] = None
        __props__.__dict__["sse_configuration"] = None
        __props__.__dict__["tags"] = None
        return FhirDatastore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output['outputs.FhirDatastoreCreatedAt']:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="datastoreArn")
    def datastore_arn(self) -> pulumi.Output[str]:
        """
        The Data Store ARN is generated during the creation of the Data Store and can be found in the output from the initial Data Store creation request.
        """
        return pulumi.get(self, "datastore_arn")

    @property
    @pulumi.getter(name="datastoreEndpoint")
    def datastore_endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint for the created Data Store.
        """
        return pulumi.get(self, "datastore_endpoint")

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> pulumi.Output[str]:
        """
        The Amazon generated Data Store id. This id is in the output from the initial Data Store creation call.
        """
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> pulumi.Output[Optional[str]]:
        """
        The user generated name for the data store.
        """
        return pulumi.get(self, "datastore_name")

    @property
    @pulumi.getter(name="datastoreStatus")
    def datastore_status(self) -> pulumi.Output['FhirDatastoreDatastoreStatus']:
        """
        The status of the FHIR Data Store. Possible statuses are ‘CREATING’, ‘ACTIVE’, ‘DELETING’, ‘DELETED’.
        """
        return pulumi.get(self, "datastore_status")

    @property
    @pulumi.getter(name="datastoreTypeVersion")
    def datastore_type_version(self) -> pulumi.Output['FhirDatastoreDatastoreTypeVersion']:
        """
        The FHIR version of the data store. The only supported version is R4.
        """
        return pulumi.get(self, "datastore_type_version")

    @property
    @pulumi.getter(name="identityProviderConfiguration")
    def identity_provider_configuration(self) -> pulumi.Output[Optional['outputs.FhirDatastoreIdentityProviderConfiguration']]:
        """
        The identity provider configuration that you gave when the data store was created.
        """
        return pulumi.get(self, "identity_provider_configuration")

    @property
    @pulumi.getter(name="preloadDataConfig")
    def preload_data_config(self) -> pulumi.Output[Optional['outputs.FhirDatastorePreloadDataConfig']]:
        """
        The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.
        """
        return pulumi.get(self, "preload_data_config")

    @property
    @pulumi.getter(name="sseConfiguration")
    def sse_configuration(self) -> pulumi.Output[Optional['outputs.FhirDatastoreSseConfiguration']]:
        """
        The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.
        """
        return pulumi.get(self, "sse_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        return pulumi.get(self, "tags")

