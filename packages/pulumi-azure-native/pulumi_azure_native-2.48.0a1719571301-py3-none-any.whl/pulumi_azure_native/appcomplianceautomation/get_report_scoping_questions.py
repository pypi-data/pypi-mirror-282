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
    'GetReportScopingQuestionsResult',
    'AwaitableGetReportScopingQuestionsResult',
    'get_report_scoping_questions',
    'get_report_scoping_questions_output',
]

@pulumi.output_type
class GetReportScopingQuestionsResult:
    """
    Scoping question list.
    """
    def __init__(__self__, questions=None):
        if questions and not isinstance(questions, list):
            raise TypeError("Expected argument 'questions' to be a list")
        pulumi.set(__self__, "questions", questions)

    @property
    @pulumi.getter
    def questions(self) -> Optional[Sequence['outputs.ScopingQuestionResponse']]:
        """
        List of scoping questions.
        """
        return pulumi.get(self, "questions")


class AwaitableGetReportScopingQuestionsResult(GetReportScopingQuestionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReportScopingQuestionsResult(
            questions=self.questions)


def get_report_scoping_questions(report_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReportScopingQuestionsResult:
    """
    Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed.
    Azure REST API version: 2024-06-27.


    :param str report_name: Report Name.
    """
    __args__ = dict()
    __args__['reportName'] = report_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appcomplianceautomation:getReportScopingQuestions', __args__, opts=opts, typ=GetReportScopingQuestionsResult).value

    return AwaitableGetReportScopingQuestionsResult(
        questions=pulumi.get(__ret__, 'questions'))


@_utilities.lift_output_func(get_report_scoping_questions)
def get_report_scoping_questions_output(report_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReportScopingQuestionsResult]:
    """
    Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed.
    Azure REST API version: 2024-06-27.


    :param str report_name: Report Name.
    """
    ...
