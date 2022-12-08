
from ..context_processors import (
    GitProcessor,
    GitChangelogProcessor,
    CodebuildProcessor,
    NameVersionProcessor
)
from .base import Message


class ArchiveCodeMessage(Message):

    template = 'archive.tpl'
    context_processors = [
        GitProcessor,
        GitChangelogProcessor,
        CodebuildProcessor,
        NameVersionProcessor
    ]
