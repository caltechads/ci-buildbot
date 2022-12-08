from ..context_processors import (
    CodebuildProcessor,
    GitProcessor,
    NameVersionProcessor,
    UnittestReportGroupProcessor
)
from .base import Message


class UnittestsStartMessage(Message):
    template = 'unittests_start.tpl'
    context_processors = [
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]


class UnittestsSuccessMessage(Message):
    template = 'unittests_success.tpl'
    context_processors = [
        UnittestReportGroupProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]


class UnittestsFailureMessage(Message):
    template = 'unittests_failed.tpl'
    context_processors = [
        UnittestReportGroupProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]
