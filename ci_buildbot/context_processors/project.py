import pathlib
import subprocess

from distutils.core import run_setup

from ..typedefs import MessageContext
from .base import AbstractContextProcessor


class NameVersionProcessor(AbstractContextProcessor):
    """
    Get our project name and our project version and add it to our message
    context.
    """

    def annotate(self, context: MessageContext) -> None:
        """
        Extract some stuff from setup.py, if present.

        If setup.py is present, we'll add the following keys to `values`:

        * ``name``: the output of ``python setup.py name``
        * ``version``: the output of ``python setup.py version``

        """
        super().annotate(context)
        setup_py = pathlib.Path.cwd() / 'setup.py'
        if setup_py.exists():
            # Extract some stuff from python itself
            python_setup = run_setup(str(setup_py))
            context['name'] = python_setup.get_name()  # type: ignore
            context['version'] = python_setup.get_version()  # type: ignore
        else:
            # No setup.py; let's try Makefile
            makefile = pathlib.Path.cwd() / 'Makefile'
            if makefile.exists():
                context['name'] = subprocess.check_output(['make', 'image_name']).decode('utf8').strip()
                context['version'] = subprocess.check_output(['make', 'version']).decode('utf8').strip()
