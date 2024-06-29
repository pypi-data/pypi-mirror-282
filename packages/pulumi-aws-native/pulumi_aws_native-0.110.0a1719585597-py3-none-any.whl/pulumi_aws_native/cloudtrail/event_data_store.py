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
from ._inputs import *

__all__ = ['EventDataStoreArgs', 'EventDataStore']

@pulumi.input_type
class EventDataStoreArgs:
    def __init__(__self__, *,
                 advanced_event_selectors: Optional[pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedEventSelectorArgs']]]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None,
                 federation_enabled: Optional[pulumi.Input[bool]] = None,
                 federation_role_arn: Optional[pulumi.Input[str]] = None,
                 ingestion_enabled: Optional[pulumi.Input[bool]] = None,
                 insight_selectors: Optional[pulumi.Input[Sequence[pulumi.Input['EventDataStoreInsightSelectorArgs']]]] = None,
                 insights_destination: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 multi_region_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_period: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 termination_protection_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a EventDataStore resource.
        :param pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedEventSelectorArgs']]] advanced_event_selectors: The advanced event selectors that were used to select events for the data store.
        :param pulumi.Input[str] billing_mode: The mode that the event data store will use to charge for event storage.
        :param pulumi.Input[bool] federation_enabled: Indicates whether federation is enabled on an event data store.
        :param pulumi.Input[str] federation_role_arn: The ARN of the role used for event data store federation.
        :param pulumi.Input[bool] ingestion_enabled: Indicates whether the event data store is ingesting events.
        :param pulumi.Input[Sequence[pulumi.Input['EventDataStoreInsightSelectorArgs']]] insight_selectors: Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing event data store. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store.
        :param pulumi.Input[str] insights_destination: Specifies the ARN of the event data store that will collect Insights events. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store
        :param pulumi.Input[str] kms_key_id: Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        :param pulumi.Input[bool] multi_region_enabled: Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
        :param pulumi.Input[str] name: The name of the event data store.
        :param pulumi.Input[bool] organization_enabled: Indicates that an event data store is collecting logged events for an organization.
        :param pulumi.Input[int] retention_period: The retention period, in days.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of tags.
        :param pulumi.Input[bool] termination_protection_enabled: Indicates whether the event data store is protected from termination.
        """
        if advanced_event_selectors is not None:
            pulumi.set(__self__, "advanced_event_selectors", advanced_event_selectors)
        if billing_mode is not None:
            pulumi.set(__self__, "billing_mode", billing_mode)
        if federation_enabled is not None:
            pulumi.set(__self__, "federation_enabled", federation_enabled)
        if federation_role_arn is not None:
            pulumi.set(__self__, "federation_role_arn", federation_role_arn)
        if ingestion_enabled is not None:
            pulumi.set(__self__, "ingestion_enabled", ingestion_enabled)
        if insight_selectors is not None:
            pulumi.set(__self__, "insight_selectors", insight_selectors)
        if insights_destination is not None:
            pulumi.set(__self__, "insights_destination", insights_destination)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if multi_region_enabled is not None:
            pulumi.set(__self__, "multi_region_enabled", multi_region_enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_enabled is not None:
            pulumi.set(__self__, "organization_enabled", organization_enabled)
        if retention_period is not None:
            pulumi.set(__self__, "retention_period", retention_period)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if termination_protection_enabled is not None:
            pulumi.set(__self__, "termination_protection_enabled", termination_protection_enabled)

    @property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedEventSelectorArgs']]]]:
        """
        The advanced event selectors that were used to select events for the data store.
        """
        return pulumi.get(self, "advanced_event_selectors")

    @advanced_event_selectors.setter
    def advanced_event_selectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EventDataStoreAdvancedEventSelectorArgs']]]]):
        pulumi.set(self, "advanced_event_selectors", value)

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The mode that the event data store will use to charge for event storage.
        """
        return pulumi.get(self, "billing_mode")

    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_mode", value)

    @property
    @pulumi.getter(name="federationEnabled")
    def federation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether federation is enabled on an event data store.
        """
        return pulumi.get(self, "federation_enabled")

    @federation_enabled.setter
    def federation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "federation_enabled", value)

    @property
    @pulumi.getter(name="federationRoleArn")
    def federation_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the role used for event data store federation.
        """
        return pulumi.get(self, "federation_role_arn")

    @federation_role_arn.setter
    def federation_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "federation_role_arn", value)

    @property
    @pulumi.getter(name="ingestionEnabled")
    def ingestion_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the event data store is ingesting events.
        """
        return pulumi.get(self, "ingestion_enabled")

    @ingestion_enabled.setter
    def ingestion_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ingestion_enabled", value)

    @property
    @pulumi.getter(name="insightSelectors")
    def insight_selectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EventDataStoreInsightSelectorArgs']]]]:
        """
        Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing event data store. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store.
        """
        return pulumi.get(self, "insight_selectors")

    @insight_selectors.setter
    def insight_selectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EventDataStoreInsightSelectorArgs']]]]):
        pulumi.set(self, "insight_selectors", value)

    @property
    @pulumi.getter(name="insightsDestination")
    def insights_destination(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ARN of the event data store that will collect Insights events. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store
        """
        return pulumi.get(self, "insights_destination")

    @insights_destination.setter
    def insights_destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "insights_destination", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="multiRegionEnabled")
    def multi_region_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
        """
        return pulumi.get(self, "multi_region_enabled")

    @multi_region_enabled.setter
    def multi_region_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multi_region_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the event data store.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="organizationEnabled")
    def organization_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates that an event data store is collecting logged events for an organization.
        """
        return pulumi.get(self, "organization_enabled")

    @organization_enabled.setter
    def organization_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "organization_enabled", value)

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[int]]:
        """
        The retention period, in days.
        """
        return pulumi.get(self, "retention_period")

    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_period", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the event data store is protected from termination.
        """
        return pulumi.get(self, "termination_protection_enabled")

    @termination_protection_enabled.setter
    def termination_protection_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "termination_protection_enabled", value)


class EventDataStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_event_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDataStoreAdvancedEventSelectorArgs']]]]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None,
                 federation_enabled: Optional[pulumi.Input[bool]] = None,
                 federation_role_arn: Optional[pulumi.Input[str]] = None,
                 ingestion_enabled: Optional[pulumi.Input[bool]] = None,
                 insight_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDataStoreInsightSelectorArgs']]]]] = None,
                 insights_destination: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 multi_region_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_period: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 termination_protection_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDataStoreAdvancedEventSelectorArgs']]]] advanced_event_selectors: The advanced event selectors that were used to select events for the data store.
        :param pulumi.Input[str] billing_mode: The mode that the event data store will use to charge for event storage.
        :param pulumi.Input[bool] federation_enabled: Indicates whether federation is enabled on an event data store.
        :param pulumi.Input[str] federation_role_arn: The ARN of the role used for event data store federation.
        :param pulumi.Input[bool] ingestion_enabled: Indicates whether the event data store is ingesting events.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDataStoreInsightSelectorArgs']]]] insight_selectors: Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing event data store. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store.
        :param pulumi.Input[str] insights_destination: Specifies the ARN of the event data store that will collect Insights events. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store
        :param pulumi.Input[str] kms_key_id: Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        :param pulumi.Input[bool] multi_region_enabled: Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
        :param pulumi.Input[str] name: The name of the event data store.
        :param pulumi.Input[bool] organization_enabled: Indicates that an event data store is collecting logged events for an organization.
        :param pulumi.Input[int] retention_period: The retention period, in days.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: A list of tags.
        :param pulumi.Input[bool] termination_protection_enabled: Indicates whether the event data store is protected from termination.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EventDataStoreArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.

        :param str resource_name: The name of the resource.
        :param EventDataStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventDataStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_event_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDataStoreAdvancedEventSelectorArgs']]]]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None,
                 federation_enabled: Optional[pulumi.Input[bool]] = None,
                 federation_role_arn: Optional[pulumi.Input[str]] = None,
                 ingestion_enabled: Optional[pulumi.Input[bool]] = None,
                 insight_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDataStoreInsightSelectorArgs']]]]] = None,
                 insights_destination: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 multi_region_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_period: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 termination_protection_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventDataStoreArgs.__new__(EventDataStoreArgs)

            __props__.__dict__["advanced_event_selectors"] = advanced_event_selectors
            __props__.__dict__["billing_mode"] = billing_mode
            __props__.__dict__["federation_enabled"] = federation_enabled
            __props__.__dict__["federation_role_arn"] = federation_role_arn
            __props__.__dict__["ingestion_enabled"] = ingestion_enabled
            __props__.__dict__["insight_selectors"] = insight_selectors
            __props__.__dict__["insights_destination"] = insights_destination
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["multi_region_enabled"] = multi_region_enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["organization_enabled"] = organization_enabled
            __props__.__dict__["retention_period"] = retention_period
            __props__.__dict__["tags"] = tags
            __props__.__dict__["termination_protection_enabled"] = termination_protection_enabled
            __props__.__dict__["created_timestamp"] = None
            __props__.__dict__["event_data_store_arn"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_timestamp"] = None
        super(EventDataStore, __self__).__init__(
            'aws-native:cloudtrail:EventDataStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventDataStore':
        """
        Get an existing EventDataStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventDataStoreArgs.__new__(EventDataStoreArgs)

        __props__.__dict__["advanced_event_selectors"] = None
        __props__.__dict__["billing_mode"] = None
        __props__.__dict__["created_timestamp"] = None
        __props__.__dict__["event_data_store_arn"] = None
        __props__.__dict__["federation_enabled"] = None
        __props__.__dict__["federation_role_arn"] = None
        __props__.__dict__["ingestion_enabled"] = None
        __props__.__dict__["insight_selectors"] = None
        __props__.__dict__["insights_destination"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["multi_region_enabled"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_enabled"] = None
        __props__.__dict__["retention_period"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["termination_protection_enabled"] = None
        __props__.__dict__["updated_timestamp"] = None
        return EventDataStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(self) -> pulumi.Output[Optional[Sequence['outputs.EventDataStoreAdvancedEventSelector']]]:
        """
        The advanced event selectors that were used to select events for the data store.
        """
        return pulumi.get(self, "advanced_event_selectors")

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The mode that the event data store will use to charge for event storage.
        """
        return pulumi.get(self, "billing_mode")

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[str]:
        """
        The timestamp of the event data store's creation.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter(name="eventDataStoreArn")
    def event_data_store_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the event data store.
        """
        return pulumi.get(self, "event_data_store_arn")

    @property
    @pulumi.getter(name="federationEnabled")
    def federation_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether federation is enabled on an event data store.
        """
        return pulumi.get(self, "federation_enabled")

    @property
    @pulumi.getter(name="federationRoleArn")
    def federation_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN of the role used for event data store federation.
        """
        return pulumi.get(self, "federation_role_arn")

    @property
    @pulumi.getter(name="ingestionEnabled")
    def ingestion_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the event data store is ingesting events.
        """
        return pulumi.get(self, "ingestion_enabled")

    @property
    @pulumi.getter(name="insightSelectors")
    def insight_selectors(self) -> pulumi.Output[Optional[Sequence['outputs.EventDataStoreInsightSelector']]]:
        """
        Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing event data store. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store.
        """
        return pulumi.get(self, "insight_selectors")

    @property
    @pulumi.getter(name="insightsDestination")
    def insights_destination(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the ARN of the event data store that will collect Insights events. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store
        """
        return pulumi.get(self, "insights_destination")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="multiRegionEnabled")
    def multi_region_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
        """
        return pulumi.get(self, "multi_region_enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the event data store.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationEnabled")
    def organization_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates that an event data store is collecting logged events for an organization.
        """
        return pulumi.get(self, "organization_enabled")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[Optional[int]]:
        """
        The retention period, in days.
        """
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of an event data store. Values are STARTING_INGESTION, ENABLED, STOPPING_INGESTION, STOPPED_INGESTION and PENDING_DELETION.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the event data store is protected from termination.
        """
        return pulumi.get(self, "termination_protection_enabled")

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[str]:
        """
        The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.
        """
        return pulumi.get(self, "updated_timestamp")

