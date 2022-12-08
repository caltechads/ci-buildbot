import datetime
import json
from typing import Any, Dict, List, Optional, Type
from pytz import timezone

from ci_buildbot import __version__
from ci_buildbot.context_processors import AbstractContextProcessor

from ..exc import ImproperlyConfigured
from ..settings import jinja_env
from ..typedefs import MessageContext


class Message:

    template: Optional[str] = None
    context_processors: List[Type[AbstractContextProcessor]] = []

    def get_template(self) -> str:
        """
        Return the filename of the Jinja template to use to render our slack message.

        Returns:
            The name of the Jinja template.
        """
        if not self.template:
            raise ImproperlyConfigured('Message subclasses must define a template')
        return self.template

    def format(self, **kwargs) -> Dict[str, Any]:
        """
        Generate the full JSON blob to send to slack.

        Returns:
            The data structure to send to slack as our message.
        """
        context: MessageContext = {}
        for processor in self.context_processors:
            processor(**kwargs).annotate(context)
        now = datetime.datetime.now(timezone('UTC'))
        now_pacific = now.astimezone(timezone('US/Pacific'))
        context['completed_date'] = now_pacific.strftime('%Y-%m-%d %H:%M %Z')
        context['buildbot'] = f'ci-buildbot-{__version__}'
        template = jinja_env.get_template(self.get_template())
        rendered = template.render(**context)
        return json.loads(rendered)
