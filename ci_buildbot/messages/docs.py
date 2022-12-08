from ..context_processors import (
    NameVersionProcessor,
    GitProcessor,
    CodebuildProcessor,
    SphinxProcessor
)
from .base import Message


class DocsStartMessage(Message):

    template = 'docs_start.tpl'
    context_processors = [
        NameVersionProcessor,
        GitProcessor,
        CodebuildProcessor,
        SphinxProcessor
    ]


class DocsSuccessMessage(Message):
    template = 'docs_success.tpl'
    context_processors = [
        NameVersionProcessor,
        GitProcessor,
        CodebuildProcessor,
        SphinxProcessor
    ]


class DocsFailureMessage(Message):
    template = 'docs_failed.tpl'
    context_processors = [
        NameVersionProcessor,
        GitProcessor,
        CodebuildProcessor,
        SphinxProcessor
    ]
