from ..context_processors import (
    DeployfishTasksDeployProcessor,
    CodebuildProcessor,
    GitProcessor,
    NameVersionProcessor
)
from .base import Message


class DeployfishTasksDeployStartMessage(Message):

    template = 'deploy_tasks_start.tpl'
    context_processors = [
        DeployfishTasksDeployProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]


class DeployfishTasksDeploySuccessMessage(Message):
    template = 'deploy_tasks_success.tpl'
    context_processors = [
        DeployfishTasksDeployProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]


class DeployfishTasksDeployFailureMessage(Message):
    template = 'deploy_tasks_failed.tpl'
    context_processors = [
        DeployfishTasksDeployProcessor,
        CodebuildProcessor,
        GitProcessor,
        NameVersionProcessor
    ]
