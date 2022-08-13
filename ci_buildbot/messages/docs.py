from .mixins import (
    AnnotationMixin,
    NameVersionMixin,
    GitMixin,
    CodebuildMixin,
    Message,
    SphinxMixin
)


class DocsStartMessage(SphinxMixin, CodebuildMixin, GitMixin, NameVersionMixin, Message):
    template = 'docs_start.tpl'


class DocsSuccessMessage(SphinxMixin, CodebuildMixin, GitMixin, NameVersionMixin, Message):
    template = 'docs_success.tpl'


class DocsFailureMessage(SphinxMixin, CodebuildMixin, GitMixin, NameVersionMixin, Message):
    template = 'docs_failed.tpl'
