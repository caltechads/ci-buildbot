from typing import Optional

from ..typedefs import MessageContext
from .base import AbstractContextProcessor


class GenericProcessor(AbstractContextProcessor):

    def __init__(self, **kwargs):
        self.label: Optional[str] = kwargs['label']

    def annotate(self, context: MessageContext) -> None:
        context['label'] = self.label
