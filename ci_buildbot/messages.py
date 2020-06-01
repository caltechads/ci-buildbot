import datetime
from distutils.core import run_setup
import pathlib
from typing import Dict

from git import Repo
from giturlparse import parse
from pytz import timezone

from .settings import jinja_env


class PushAndArchiveMessage:
    """
    Generate a json string suitable for sending to slack that annotates an
    the initial git push and archive to S3 step:

        * Application info (name, version)
        * Git info (branch, commit, changelog, authors)
    """

    def __init__(self):
        self.repo = Repo('.')
        self.__build_url_patterns()

    def __build_url_patterns(self):
        p = parse(self.repo.remote().url)
        origin_url = p.url2https
        self.url_patterns = {}
        if p.bitbucket:
            self.url_patterns['commit'] = f"<{origin_url}/commits/" + "{sha}|{sha}>"
            self.url_patterns['diff'] = f"{origin_url}/branches/compare/" + "{from_sha}..{to_sha}#diff"
        elif p.github:
            self.url_patterns['commit'] = f"<{origin_url}/commit/" + "{sha}|{sha}>"
            self.url_patterns['diff'] = f"{origin_url}/compare/" + "{from_sha}..{to_sha}"
        else:
            self.url_patterns['commit'] = "{sha}"
            self.url_patterns['diff'] = None
        self.url_patterns['repo'] = origin_url

    def __python(self, values: Dict[str, str]):
        """
        Extract some stuff from setup.py, if present.

        If setup.py is present, we'll add the following keys to `values`:

        * `name`: the output of `python setup.py name`
        * `version`: the output of `python setup.py version`

        """
        setup_py = pathlib.Path.cwd() / 'setup.py'
        if setup_py.exists():
            # Extract some stuff from python itself
            python_setup = run_setup(str(setup_py))
            values['name'] = python_setup.get_name()
            values['version'] = python_setup.get_version()

    def __get_last_version(self, values: Dict[str, str]):
        """
        Update the `values` dict with:

        * `previous_version`: the version number for the tag immediately preceeding ours
        * `last_version_sha`: the sha that that tag points to
        """
        # Get all tags, sorted by the authored_date on their associated commit.  We should have at least one tag -- the
        # one for this commit.
        ordered_tags = sorted(self.repo.tags, key=lambda x: x.commit.authored_date)
        if len(ordered_tags) >= 2:
            # If there are 2 or more tags, there was a previous version.
            # Extract info from the tag preceeding this one.
            values['last_version_sha'] = ordered_tags[-2].commit.hexsha
            values['previous_version'] = ordered_tags[-2].name
        else:
            # There was just our current version tag, and no previous tag.  Go back to the initial commit.
            commits = list(self.repo.iter_commits())
            commits.reverse()
            values['last_version_sha'] = commits[0].hexsha
            values['previous_version'] = "initial"

    def __git_changelog(self, values: Dict[str, str]):
        """
        Look through the commits between the current version and the last version
        Update `values` with two new keys:

        * `authors`: a list of all authors in those commits
        * `changelog`: a list of strings representing the commits
        """
        # get the changes between here and the previous tag
        changelog_commits = []
        current = self.repo.head.commit
        # Gather all commits from HEAD to `last_version_sha`
        while True:
            changelog_commits.append(current)
            if current.hexsha == values['last_version_sha']:
                break
            current = current.parents[0]
        changelog = []
        authors = set()
        for commit in changelog_commits:
            authors.add(commit.author.name)
            d = datetime.datetime.fromtimestamp(commit.committed_date).strftime("%Y/%m/%d")
            commit_link = self.url_patterns['commit'].format(sha=commit.hexsha[0:7])
            changelog.append(f"{commit_link} [{d}] {commit.summary} - {str(commit.author)}")
        values['authors'] = sorted(authors)
        values['changelog'] = changelog

    def __git(self, values: Dict[str, str]):
        """
        Extract info about the git repo.  Assume we're in the checked out clone.
        """
        headcommit = self.repo.head.commit
        values['committer'] = str(headcommit.author)
        values['sha'] = headcommit.hexsha
        values['branch'] = self.repo.head.reference.name
        self.__get_last_version(values)
        self.__git_changelog(values)
        # Add the diff URL
        if 'diff' in self.url_patterns:
            values['diff_url'] = self.url_patterns['diff'].format(
                from_sha=values['sha'][0:7],
                to_sha=values['last_version_sha'][0:7],
            )

    def format(self) -> str:
        """
        Generate the full JSON string to send to slack.
        """
        values = {}
        self.__python(values)
        self.__git(values)
        now = datetime.datetime.now(timezone('UTC'))
        now_pacific = now.astimezone(timezone('US/Pacific'))
        values['completed_date'] = now_pacific.strftime('%Y-%m-%d %H:%M %Z')
        template = jinja_env.get_template('archive.tpl')
        return(template.render(**values))
