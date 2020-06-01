#!/usr/bin/env python
import pprint
import sys

import click
import slack

import ci_buildbot
from .settings import Settings
from .messages import (
    PushAndArchiveMessage
)


@click.group(invoke_without_command=True)
@click.option('--version/--no-version', '-v', default=False, help="Print the current version and exit.")
@click.pass_context
def cli(ctx, version):
    """
    buildbot command line interaface.
    """

    ctx.obj['settings'] = Settings()
    ctx.obj['slack'] = slack.WebClient(token=ctx.obj['settings'].api_token)

    if version:
        print(ci_buildbot.__version__)
        sys.exit(0)


@cli.command('settings', short_help="Print our application settings.")
@click.pass_context
def settings(ctx):
    """
    Print our settings to stdout.  This should be the completely evaluated settings including
    those imported from any environment variable.
    """
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(ctx['settings'].dict())


@cli.group('report', short_help="Report about a build step")
def report():
    pass


@report.command('archive', short_help="Report about an archive-to-code-drop step")
@click.pass_context
def archive(ctx):
    message = PushAndArchiveMessage()
    print(message.format())


def main():
    cli(obj={})


if __name__ == '__main__':
    main()
