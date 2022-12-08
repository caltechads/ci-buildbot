from typing import Optional

from ..typedefs import MessageContext
from .base import AbstractContextProcessor


class SphinxProcessor(AbstractContextProcessor):

    def __init__(self, **kwargs):
        self.url: Optional[str] = kwargs['url']

    def annotate(self, context: MessageContext) -> None:
        context['url'] = f'<{self.url}|Click here>'
