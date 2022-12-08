from typing import List

from ..typedefs import MessageContext
from .base import AbstractContextProcessor


class DeployfishDeployProcessor(AbstractContextProcessor):

    def __init__(self, **kwargs):
        self.service: str = kwargs['service']

    def annotate(self, context: MessageContext) -> None:
        context['service'] = self.service


class DeployfishTasksDeployProcessor(AbstractContextProcessor):

    def __init__(self, **kwargs):
        self.tasks: List[str] = kwargs['tasks']

    def annotate(self, context: MessageContext) -> None:
        context['tasks'] = self.tasks
