# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ConfigBandwidthUnits',
    'ConfigEirpUnits',
    'ConfigFrequencyUnits',
    'ConfigPolarization',
    'ConfigTrackingConfigAutotrack',
    'DataflowEndpointGroupAgentStatus',
    'DataflowEndpointGroupAuditResults',
]


class ConfigBandwidthUnits(str, Enum):
    G_HZ = "GHz"
    M_HZ = "MHz"
    K_HZ = "kHz"


class ConfigEirpUnits(str, Enum):
    DBW = "dBW"


class ConfigFrequencyUnits(str, Enum):
    G_HZ = "GHz"
    M_HZ = "MHz"
    K_HZ = "kHz"


class ConfigPolarization(str, Enum):
    LEFT_HAND = "LEFT_HAND"
    RIGHT_HAND = "RIGHT_HAND"
    NONE = "NONE"


class ConfigTrackingConfigAutotrack(str, Enum):
    """
    Specifies whether or not to use autotrack. `REMOVED` specifies that program track should only be used during the contact. `PREFERRED` specifies that autotracking is preferred during the contact but fallback to program track if the signal is lost. `REQUIRED` specifies that autotracking is required during the contact and not to use program track if the signal is lost.
    """
    REQUIRED = "REQUIRED"
    PREFERRED = "PREFERRED"
    REMOVED = "REMOVED"


class DataflowEndpointGroupAgentStatus(str, Enum):
    """
    The status of AgentEndpoint.
    """
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class DataflowEndpointGroupAuditResults(str, Enum):
    """
    The results of the audit.
    """
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
