# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DatasetAttributesItemPropertiesAttributeType',
    'DatasetDomain',
    'DatasetGroupDomain',
    'DatasetType',
]


class DatasetAttributesItemPropertiesAttributeType(str, Enum):
    """
    Data type of the field
    """
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    TIMESTAMP = "timestamp"
    GEOLOCATION = "geolocation"


class DatasetDomain(str, Enum):
    """
    The domain associated with the dataset
    """
    RETAIL = "RETAIL"
    CUSTOM = "CUSTOM"
    INVENTORY_PLANNING = "INVENTORY_PLANNING"
    EC2_CAPACITY = "EC2_CAPACITY"
    WORK_FORCE = "WORK_FORCE"
    WEB_TRAFFIC = "WEB_TRAFFIC"
    METRICS = "METRICS"


class DatasetGroupDomain(str, Enum):
    """
    The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.
    """
    RETAIL = "RETAIL"
    CUSTOM = "CUSTOM"
    INVENTORY_PLANNING = "INVENTORY_PLANNING"
    EC2_CAPACITY = "EC2_CAPACITY"
    WORK_FORCE = "WORK_FORCE"
    WEB_TRAFFIC = "WEB_TRAFFIC"
    METRICS = "METRICS"


class DatasetType(str, Enum):
    """
    The dataset type
    """
    TARGET_TIME_SERIES = "TARGET_TIME_SERIES"
    RELATED_TIME_SERIES = "RELATED_TIME_SERIES"
    ITEM_METADATA = "ITEM_METADATA"
