from abc import ABC, abstractmethod
from typing import Final

from ..typedefs import MessageContext


class AbstractContextProcessor(ABC):
    """
    Base class for all context processors.
    """

    #: The maximum length of a slack text block
    MAX_SLACK_TEXT_LENGTH: Final[int] = 3000

    def __init__(self, **kwargs):  # noqa: B027
        """
        Args:
            kwargs: the keyword arguments passed to the context processor

        """

    @abstractmethod
    def annotate(self, context: MessageContext) -> None:
        """
        Add values to the message context ``context``.

        Args:
            context: the current message context

        """
        ...
