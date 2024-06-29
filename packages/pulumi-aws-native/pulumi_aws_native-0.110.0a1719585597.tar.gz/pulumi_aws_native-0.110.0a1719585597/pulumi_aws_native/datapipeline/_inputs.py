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
    'PipelineFieldArgs',
    'PipelineObjectArgs',
    'PipelineParameterAttributeArgs',
    'PipelineParameterObjectArgs',
    'PipelineParameterValueArgs',
]

@pulumi.input_type
class PipelineFieldArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 ref_value: Optional[pulumi.Input[str]] = None,
                 string_value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key: Specifies the name of a field for a particular object. To view valid values for a particular field, see Pipeline Object Reference in the AWS Data Pipeline Developer Guide.
        :param pulumi.Input[str] ref_value: A field value that you specify as an identifier of another object in the same pipeline definition.
        :param pulumi.Input[str] string_value: A field value that you specify as a string. To view valid values for a particular field, see Pipeline Object Reference in the AWS Data Pipeline Developer Guide.
        """
        pulumi.set(__self__, "key", key)
        if ref_value is not None:
            pulumi.set(__self__, "ref_value", ref_value)
        if string_value is not None:
            pulumi.set(__self__, "string_value", string_value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Specifies the name of a field for a particular object. To view valid values for a particular field, see Pipeline Object Reference in the AWS Data Pipeline Developer Guide.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="refValue")
    def ref_value(self) -> Optional[pulumi.Input[str]]:
        """
        A field value that you specify as an identifier of another object in the same pipeline definition.
        """
        return pulumi.get(self, "ref_value")

    @ref_value.setter
    def ref_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ref_value", value)

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[str]]:
        """
        A field value that you specify as a string. To view valid values for a particular field, see Pipeline Object Reference in the AWS Data Pipeline Developer Guide.
        """
        return pulumi.get(self, "string_value")

    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "string_value", value)


@pulumi.input_type
class PipelineObjectArgs:
    def __init__(__self__, *,
                 fields: pulumi.Input[Sequence[pulumi.Input['PipelineFieldArgs']]],
                 id: pulumi.Input[str],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['PipelineFieldArgs']]] fields: Key-value pairs that define the properties of the object.
        :param pulumi.Input[str] id: The ID of the object.
        :param pulumi.Input[str] name: The name of the object.
        """
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input['PipelineFieldArgs']]]:
        """
        Key-value pairs that define the properties of the object.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input['PipelineFieldArgs']]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The ID of the object.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class PipelineParameterAttributeArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 string_value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] key: The field identifier.
        :param pulumi.Input[str] string_value: The field value, expressed as a String.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "string_value", string_value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The field identifier.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> pulumi.Input[str]:
        """
        The field value, expressed as a String.
        """
        return pulumi.get(self, "string_value")

    @string_value.setter
    def string_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "string_value", value)


@pulumi.input_type
class PipelineParameterObjectArgs:
    def __init__(__self__, *,
                 attributes: pulumi.Input[Sequence[pulumi.Input['PipelineParameterAttributeArgs']]],
                 id: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['PipelineParameterAttributeArgs']]] attributes: The attributes of the parameter object.
        :param pulumi.Input[str] id: The ID of the parameter object.
        """
        pulumi.set(__self__, "attributes", attributes)
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Input[Sequence[pulumi.Input['PipelineParameterAttributeArgs']]]:
        """
        The attributes of the parameter object.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: pulumi.Input[Sequence[pulumi.Input['PipelineParameterAttributeArgs']]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The ID of the parameter object.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class PipelineParameterValueArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 string_value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] id: The ID of the parameter value.
        :param pulumi.Input[str] string_value: The field value, expressed as a String.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "string_value", string_value)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The ID of the parameter value.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> pulumi.Input[str]:
        """
        The field value, expressed as a String.
        """
        return pulumi.get(self, "string_value")

    @string_value.setter
    def string_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "string_value", value)


