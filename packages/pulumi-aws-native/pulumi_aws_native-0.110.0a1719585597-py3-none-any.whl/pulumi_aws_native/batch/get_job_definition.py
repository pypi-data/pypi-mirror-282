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

__all__ = [
    'GetJobDefinitionResult',
    'AwaitableGetJobDefinitionResult',
    'get_job_definition',
    'get_job_definition_output',
]

@pulumi.output_type
class GetJobDefinitionResult:
    def __init__(__self__, container_properties=None, ecs_properties=None, eks_properties=None, id=None, node_properties=None, parameters=None, platform_capabilities=None, propagate_tags=None, retry_strategy=None, scheduling_priority=None, timeout=None, type=None):
        if container_properties and not isinstance(container_properties, dict):
            raise TypeError("Expected argument 'container_properties' to be a dict")
        pulumi.set(__self__, "container_properties", container_properties)
        if ecs_properties and not isinstance(ecs_properties, dict):
            raise TypeError("Expected argument 'ecs_properties' to be a dict")
        pulumi.set(__self__, "ecs_properties", ecs_properties)
        if eks_properties and not isinstance(eks_properties, dict):
            raise TypeError("Expected argument 'eks_properties' to be a dict")
        pulumi.set(__self__, "eks_properties", eks_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if node_properties and not isinstance(node_properties, dict):
            raise TypeError("Expected argument 'node_properties' to be a dict")
        pulumi.set(__self__, "node_properties", node_properties)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if platform_capabilities and not isinstance(platform_capabilities, list):
            raise TypeError("Expected argument 'platform_capabilities' to be a list")
        pulumi.set(__self__, "platform_capabilities", platform_capabilities)
        if propagate_tags and not isinstance(propagate_tags, bool):
            raise TypeError("Expected argument 'propagate_tags' to be a bool")
        pulumi.set(__self__, "propagate_tags", propagate_tags)
        if retry_strategy and not isinstance(retry_strategy, dict):
            raise TypeError("Expected argument 'retry_strategy' to be a dict")
        pulumi.set(__self__, "retry_strategy", retry_strategy)
        if scheduling_priority and not isinstance(scheduling_priority, int):
            raise TypeError("Expected argument 'scheduling_priority' to be a int")
        pulumi.set(__self__, "scheduling_priority", scheduling_priority)
        if timeout and not isinstance(timeout, dict):
            raise TypeError("Expected argument 'timeout' to be a dict")
        pulumi.set(__self__, "timeout", timeout)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="containerProperties")
    def container_properties(self) -> Optional['outputs.JobDefinitionContainerProperties']:
        """
        An object with properties specific to Amazon ECS-based jobs. When `containerProperties` is used in the job definition, it can't be used in addition to `eksProperties` , `ecsProperties` , or `nodeProperties` .
        """
        return pulumi.get(self, "container_properties")

    @property
    @pulumi.getter(name="ecsProperties")
    def ecs_properties(self) -> Optional['outputs.JobDefinitionEcsProperties']:
        """
        An object that contains the properties for the Amazon ECS resources of a job.When `ecsProperties` is used in the job definition, it can't be used in addition to `containerProperties` , `eksProperties` , or `nodeProperties` .
        """
        return pulumi.get(self, "ecs_properties")

    @property
    @pulumi.getter(name="eksProperties")
    def eks_properties(self) -> Optional['outputs.JobDefinitionEksProperties']:
        """
        An object with properties that are specific to Amazon EKS-based jobs. When `eksProperties` is used in the job definition, it can't be used in addition to `containerProperties` , `ecsProperties` , or `nodeProperties` .
        """
        return pulumi.get(self, "eks_properties")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nodeProperties")
    def node_properties(self) -> Optional['outputs.JobDefinitionNodeProperties']:
        """
        An object with properties that are specific to multi-node parallel jobs. When `nodeProperties` is used in the job definition, it can't be used in addition to `containerProperties` , `ecsProperties` , or `eksProperties` .

        > If the job runs on Fargate resources, don't specify `nodeProperties` . Use `containerProperties` instead.
        """
        return pulumi.get(self, "node_properties")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        """
        Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a `SubmitJob` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see [Job definition parameters](https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html) in the *AWS Batch User Guide* .

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Batch::JobDefinition` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="platformCapabilities")
    def platform_capabilities(self) -> Optional[Sequence[str]]:
        """
        The platform capabilities required by the job definition. If no value is specified, it defaults to `EC2` . Jobs run on Fargate resources specify `FARGATE` .
        """
        return pulumi.get(self, "platform_capabilities")

    @property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[bool]:
        """
        Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state.
        """
        return pulumi.get(self, "propagate_tags")

    @property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> Optional['outputs.JobDefinitionRetryStrategy']:
        """
        The retry strategy to use for failed jobs that are submitted with this job definition.
        """
        return pulumi.get(self, "retry_strategy")

    @property
    @pulumi.getter(name="schedulingPriority")
    def scheduling_priority(self) -> Optional[int]:
        """
        The scheduling priority of the job definition. This only affects jobs in job queues with a fair share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.
        """
        return pulumi.get(self, "scheduling_priority")

    @property
    @pulumi.getter
    def timeout(self) -> Optional['outputs.JobDefinitionTimeout']:
        """
        The timeout time for jobs that are submitted with this job definition. After the amount of time you specify passes, AWS Batch terminates your jobs if they aren't finished.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of job definition. For more information about multi-node parallel jobs, see [Creating a multi-node parallel job definition](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html) in the *AWS Batch User Guide* .

        - If the value is `container` , then one of the following is required: `containerProperties` , `ecsProperties` , or `eksProperties` .
        - If the value is `multinode` , then `nodeProperties` is required.

        > If the job is run on Fargate resources, then `multinode` isn't supported.
        """
        return pulumi.get(self, "type")


class AwaitableGetJobDefinitionResult(GetJobDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobDefinitionResult(
            container_properties=self.container_properties,
            ecs_properties=self.ecs_properties,
            eks_properties=self.eks_properties,
            id=self.id,
            node_properties=self.node_properties,
            parameters=self.parameters,
            platform_capabilities=self.platform_capabilities,
            propagate_tags=self.propagate_tags,
            retry_strategy=self.retry_strategy,
            scheduling_priority=self.scheduling_priority,
            timeout=self.timeout,
            type=self.type)


def get_job_definition(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobDefinitionResult:
    """
    Resource Type definition for AWS::Batch::JobDefinition
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:batch:getJobDefinition', __args__, opts=opts, typ=GetJobDefinitionResult).value

    return AwaitableGetJobDefinitionResult(
        container_properties=pulumi.get(__ret__, 'container_properties'),
        ecs_properties=pulumi.get(__ret__, 'ecs_properties'),
        eks_properties=pulumi.get(__ret__, 'eks_properties'),
        id=pulumi.get(__ret__, 'id'),
        node_properties=pulumi.get(__ret__, 'node_properties'),
        parameters=pulumi.get(__ret__, 'parameters'),
        platform_capabilities=pulumi.get(__ret__, 'platform_capabilities'),
        propagate_tags=pulumi.get(__ret__, 'propagate_tags'),
        retry_strategy=pulumi.get(__ret__, 'retry_strategy'),
        scheduling_priority=pulumi.get(__ret__, 'scheduling_priority'),
        timeout=pulumi.get(__ret__, 'timeout'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_job_definition)
def get_job_definition_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobDefinitionResult]:
    """
    Resource Type definition for AWS::Batch::JobDefinition
    """
    ...
