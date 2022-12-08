from abc import ABC, abstractmethod
from ..typedefs import MessageContext


class AbstractContextProcessor(ABC):

    @abstractmethod
    def annotate(self, context: MessageContext) -> None:
        """
        Add values to the message context ``context``.

        Args:
            context: the current message context
        """
        ...
