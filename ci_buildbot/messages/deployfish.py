from ..context_processors import (
    GitProcessor,
    NameVersionProcessor,
    CodebuildProcessor,
    DeployfishDeployProcessor
)
from .base import Message


class DeployfishDeployStartMessage(Message):
    template = 'deploy_start.tpl'
    context_processors = [
        DeployfishDeployProcessor,
        GitProcessor,
        CodebuildProcessor,
        NameVersionProcessor,
    ]


class DeployfishDeploySuccessMessage(Message):
    template = 'deploy_success.tpl'
    context_processors = [
        DeployfishDeployProcessor,
        GitProcessor,
        CodebuildProcessor,
        NameVersionProcessor,
    ]


class DeployfishDeployFailureMessage(Message):
    template = 'deploy_failed.tpl'
    context_processors = [
        DeployfishDeployProcessor,
        GitProcessor,
        CodebuildProcessor,
        NameVersionProcessor,
    ]
