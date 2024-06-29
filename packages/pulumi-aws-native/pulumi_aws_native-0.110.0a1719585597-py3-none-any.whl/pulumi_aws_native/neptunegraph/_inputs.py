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
    'GraphVectorSearchConfigurationArgs',
]

@pulumi.input_type
class GraphVectorSearchConfigurationArgs:
    def __init__(__self__, *,
                 vector_search_dimension: pulumi.Input[int]):
        """
        The vector search configuration.
        :param pulumi.Input[int] vector_search_dimension: The vector search dimension
        """
        pulumi.set(__self__, "vector_search_dimension", vector_search_dimension)

    @property
    @pulumi.getter(name="vectorSearchDimension")
    def vector_search_dimension(self) -> pulumi.Input[int]:
        """
        The vector search dimension
        """
        return pulumi.get(self, "vector_search_dimension")

    @vector_search_dimension.setter
    def vector_search_dimension(self, value: pulumi.Input[int]):
        pulumi.set(self, "vector_search_dimension", value)


