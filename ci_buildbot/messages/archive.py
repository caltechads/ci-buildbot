from typing import ClassVar

from ..context_processors import (
    AbstractContextProcessor,
    CodebuildProcessor,
    GitChangelogProcessor,
    GitProcessor,
    NameVersionProcessor,
)
from .base import Message


class ArchiveStartMessage(Message):
    """
    Used to send a slack message about starting to archive code tarballs to an artifactory.
    """

    template: str = "archive_start.tpl"
    context_processors: ClassVar[list[type[AbstractContextProcessor]]] = [
        NameVersionProcessor,
        GitProcessor,
        GitChangelogProcessor,
        CodebuildProcessor,
    ]


class ArchiveSuccessMessage(Message):
    """
    Used to send a slack message about archiving code tarballs to an artifactory.
    """

    template: str = "archive_success.tpl"
    context_processors: ClassVar[list[type[AbstractContextProcessor]]] = [
        NameVersionProcessor,
        GitProcessor,
        GitChangelogProcessor,
        CodebuildProcessor,
    ]

class ArchiveFailureMessage(Message):
    """
    Used to send a slack message about failing to archive code tarballs to an artifactory.
    """

    template: str = "archive_failed.tpl"
    context_processors: ClassVar[list[type[AbstractContextProcessor]]] = [
        NameVersionProcessor,
        GitProcessor,
        GitChangelogProcessor,
        CodebuildProcessor,
    ]
