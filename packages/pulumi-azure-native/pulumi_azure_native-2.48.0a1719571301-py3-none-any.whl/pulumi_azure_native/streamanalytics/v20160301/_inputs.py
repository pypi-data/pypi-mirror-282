# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'AzureMachineLearningWebServiceFunctionBindingArgs',
    'AzureMachineLearningWebServiceInputColumnArgs',
    'AzureMachineLearningWebServiceInputsArgs',
    'AzureMachineLearningWebServiceOutputColumnArgs',
    'FunctionInputArgs',
    'FunctionOutputArgs',
    'JavaScriptFunctionBindingArgs',
    'ScalarFunctionPropertiesArgs',
]

@pulumi.input_type
class AzureMachineLearningWebServiceFunctionBindingArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 api_key: Optional[pulumi.Input[str]] = None,
                 batch_size: Optional[pulumi.Input[int]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 inputs: Optional[pulumi.Input['AzureMachineLearningWebServiceInputsArgs']] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceOutputColumnArgs']]]] = None):
        """
        The binding to an Azure Machine Learning web service.
        :param pulumi.Input[str] type: Indicates the function binding type.
               Expected value is 'Microsoft.MachineLearning/WebService'.
        :param pulumi.Input[str] api_key: The API key used to authenticate with Request-Response endpoint.
        :param pulumi.Input[int] batch_size: Number between 1 and 10000 describing maximum number of rows for every Azure ML RRS execute request. Default is 1000.
        :param pulumi.Input[str] endpoint: The Request-Response execute endpoint of the Azure Machine Learning web service. Find out more here: https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-consume-web-services#request-response-service-rrs
        :param pulumi.Input['AzureMachineLearningWebServiceInputsArgs'] inputs: The inputs for the Azure Machine Learning web service endpoint.
        :param pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceOutputColumnArgs']]] outputs: A list of outputs from the Azure Machine Learning web service endpoint execution.
        """
        pulumi.set(__self__, "type", 'Microsoft.MachineLearning/WebService')
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if batch_size is not None:
            pulumi.set(__self__, "batch_size", batch_size)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if inputs is not None:
            pulumi.set(__self__, "inputs", inputs)
        if outputs is not None:
            pulumi.set(__self__, "outputs", outputs)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Indicates the function binding type.
        Expected value is 'Microsoft.MachineLearning/WebService'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key used to authenticate with Request-Response endpoint.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[int]]:
        """
        Number between 1 and 10000 describing maximum number of rows for every Azure ML RRS execute request. Default is 1000.
        """
        return pulumi.get(self, "batch_size")

    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "batch_size", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The Request-Response execute endpoint of the Azure Machine Learning web service. Find out more here: https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-consume-web-services#request-response-service-rrs
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input['AzureMachineLearningWebServiceInputsArgs']]:
        """
        The inputs for the Azure Machine Learning web service endpoint.
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input['AzureMachineLearningWebServiceInputsArgs']]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def outputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceOutputColumnArgs']]]]:
        """
        A list of outputs from the Azure Machine Learning web service endpoint execution.
        """
        return pulumi.get(self, "outputs")

    @outputs.setter
    def outputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceOutputColumnArgs']]]]):
        pulumi.set(self, "outputs", value)


@pulumi.input_type
class AzureMachineLearningWebServiceInputColumnArgs:
    def __init__(__self__, *,
                 data_type: Optional[pulumi.Input[str]] = None,
                 map_to: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Describes an input column for the Azure Machine Learning web service endpoint.
        :param pulumi.Input[str] data_type: The (Azure Machine Learning supported) data type of the input column. A list of valid  Azure Machine Learning data types are described at https://msdn.microsoft.com/en-us/library/azure/dn905923.aspx .
        :param pulumi.Input[int] map_to: The zero based index of the function parameter this input maps to.
        :param pulumi.Input[str] name: The name of the input column.
        """
        if data_type is not None:
            pulumi.set(__self__, "data_type", data_type)
        if map_to is not None:
            pulumi.set(__self__, "map_to", map_to)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[str]]:
        """
        The (Azure Machine Learning supported) data type of the input column. A list of valid  Azure Machine Learning data types are described at https://msdn.microsoft.com/en-us/library/azure/dn905923.aspx .
        """
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_type", value)

    @property
    @pulumi.getter(name="mapTo")
    def map_to(self) -> Optional[pulumi.Input[int]]:
        """
        The zero based index of the function parameter this input maps to.
        """
        return pulumi.get(self, "map_to")

    @map_to.setter
    def map_to(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "map_to", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the input column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class AzureMachineLearningWebServiceInputsArgs:
    def __init__(__self__, *,
                 column_names: Optional[pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceInputColumnArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The inputs for the Azure Machine Learning web service endpoint.
        :param pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceInputColumnArgs']]] column_names: A list of input columns for the Azure Machine Learning web service endpoint.
        :param pulumi.Input[str] name: The name of the input. This is the name provided while authoring the endpoint.
        """
        if column_names is not None:
            pulumi.set(__self__, "column_names", column_names)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceInputColumnArgs']]]]:
        """
        A list of input columns for the Azure Machine Learning web service endpoint.
        """
        return pulumi.get(self, "column_names")

    @column_names.setter
    def column_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureMachineLearningWebServiceInputColumnArgs']]]]):
        pulumi.set(self, "column_names", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the input. This is the name provided while authoring the endpoint.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class AzureMachineLearningWebServiceOutputColumnArgs:
    def __init__(__self__, *,
                 data_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Describes an output column for the Azure Machine Learning web service endpoint.
        :param pulumi.Input[str] data_type: The (Azure Machine Learning supported) data type of the output column. A list of valid  Azure Machine Learning data types are described at https://msdn.microsoft.com/en-us/library/azure/dn905923.aspx .
        :param pulumi.Input[str] name: The name of the output column.
        """
        if data_type is not None:
            pulumi.set(__self__, "data_type", data_type)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[str]]:
        """
        The (Azure Machine Learning supported) data type of the output column. A list of valid  Azure Machine Learning data types are described at https://msdn.microsoft.com/en-us/library/azure/dn905923.aspx .
        """
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the output column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class FunctionInputArgs:
    def __init__(__self__, *,
                 data_type: Optional[pulumi.Input[str]] = None,
                 is_configuration_parameter: Optional[pulumi.Input[bool]] = None):
        """
        Describes one input parameter of a function.
        :param pulumi.Input[str] data_type: The (Azure Stream Analytics supported) data type of the function input parameter. A list of valid Azure Stream Analytics data types are described at https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
        :param pulumi.Input[bool] is_configuration_parameter: A flag indicating if the parameter is a configuration parameter. True if this input parameter is expected to be a constant. Default is false.
        """
        if data_type is not None:
            pulumi.set(__self__, "data_type", data_type)
        if is_configuration_parameter is not None:
            pulumi.set(__self__, "is_configuration_parameter", is_configuration_parameter)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[str]]:
        """
        The (Azure Stream Analytics supported) data type of the function input parameter. A list of valid Azure Stream Analytics data types are described at https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
        """
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_type", value)

    @property
    @pulumi.getter(name="isConfigurationParameter")
    def is_configuration_parameter(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag indicating if the parameter is a configuration parameter. True if this input parameter is expected to be a constant. Default is false.
        """
        return pulumi.get(self, "is_configuration_parameter")

    @is_configuration_parameter.setter
    def is_configuration_parameter(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_configuration_parameter", value)


@pulumi.input_type
class FunctionOutputArgs:
    def __init__(__self__, *,
                 data_type: Optional[pulumi.Input[str]] = None):
        """
        Describes the output of a function.
        :param pulumi.Input[str] data_type: The (Azure Stream Analytics supported) data type of the function output. A list of valid Azure Stream Analytics data types are described at https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
        """
        if data_type is not None:
            pulumi.set(__self__, "data_type", data_type)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[str]]:
        """
        The (Azure Stream Analytics supported) data type of the function output. A list of valid Azure Stream Analytics data types are described at https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
        """
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_type", value)


@pulumi.input_type
class JavaScriptFunctionBindingArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 script: Optional[pulumi.Input[str]] = None):
        """
        The binding to a JavaScript function.
        :param pulumi.Input[str] type: Indicates the function binding type.
               Expected value is 'Microsoft.StreamAnalytics/JavascriptUdf'.
        :param pulumi.Input[str] script: The JavaScript code containing a single function definition. For example: 'function (x, y) { return x + y; }'
        """
        pulumi.set(__self__, "type", 'Microsoft.StreamAnalytics/JavascriptUdf')
        if script is not None:
            pulumi.set(__self__, "script", script)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Indicates the function binding type.
        Expected value is 'Microsoft.StreamAnalytics/JavascriptUdf'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        """
        The JavaScript code containing a single function definition. For example: 'function (x, y) { return x + y; }'
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)


@pulumi.input_type
class ScalarFunctionPropertiesArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 binding: Optional[pulumi.Input[Union['AzureMachineLearningWebServiceFunctionBindingArgs', 'JavaScriptFunctionBindingArgs']]] = None,
                 inputs: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionInputArgs']]]] = None,
                 output: Optional[pulumi.Input['FunctionOutputArgs']] = None):
        """
        The properties that are associated with a scalar function.
        :param pulumi.Input[str] type: Indicates the type of function.
               Expected value is 'Scalar'.
        :param pulumi.Input[Union['AzureMachineLearningWebServiceFunctionBindingArgs', 'JavaScriptFunctionBindingArgs']] binding: The physical binding of the function. For example, in the Azure Machine Learning web service’s case, this describes the endpoint.
        :param pulumi.Input[Sequence[pulumi.Input['FunctionInputArgs']]] inputs: A list of inputs describing the parameters of the function.
        :param pulumi.Input['FunctionOutputArgs'] output: The output of the function.
        """
        pulumi.set(__self__, "type", 'Scalar')
        if binding is not None:
            pulumi.set(__self__, "binding", binding)
        if inputs is not None:
            pulumi.set(__self__, "inputs", inputs)
        if output is not None:
            pulumi.set(__self__, "output", output)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Indicates the type of function.
        Expected value is 'Scalar'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def binding(self) -> Optional[pulumi.Input[Union['AzureMachineLearningWebServiceFunctionBindingArgs', 'JavaScriptFunctionBindingArgs']]]:
        """
        The physical binding of the function. For example, in the Azure Machine Learning web service’s case, this describes the endpoint.
        """
        return pulumi.get(self, "binding")

    @binding.setter
    def binding(self, value: Optional[pulumi.Input[Union['AzureMachineLearningWebServiceFunctionBindingArgs', 'JavaScriptFunctionBindingArgs']]]):
        pulumi.set(self, "binding", value)

    @property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FunctionInputArgs']]]]:
        """
        A list of inputs describing the parameters of the function.
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionInputArgs']]]]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input['FunctionOutputArgs']]:
        """
        The output of the function.
        """
        return pulumi.get(self, "output")

    @output.setter
    def output(self, value: Optional[pulumi.Input['FunctionOutputArgs']]):
        pulumi.set(self, "output", value)


