from ..context_processors import (
    CodebuildProcessor,
    DockerImageNameProcessor,
    DockerProcessor,
    GitProcessor,
    NameVersionProcessor
)
from .base import Message


class DockerStartMessage(Message):

    template = 'docker_start.tpl'
    context_processors = [
        DockerImageNameProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]


class DockerSuccessMessage(Message):

    template = 'docker_success.tpl'
    context_processors = [
        DockerImageNameProcessor,
        DockerProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]


class DockerFailureMessage(Message):

    template  = 'docker_failed.tpl'
    context_processors = [
        DockerImageNameProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]
