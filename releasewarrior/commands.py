import abc
import os
import sys
import logging
from git import Repo

from releasewarrior.config import REPO_PATH, RELEASES_PATH, TEMPLATES_PATH, ARCHIVED_RELEASES_PATH

logger = logging.getLogger('releasewarrior')

class Command(metaclass=abc.ABCMeta):

    def __init__(self):
        self.repo = Repo(REPO_PATH)

    def pre_run_check(self):
        """ensures repo is clean and local repo is in sync with remote origin"""

        logger.info("ensuring releasewarrior repo is clean")
        if self.repo.is_dirty():
            logger.error("releasewarrior repo is dirty. aborting run to be safe.")
            sys.exit(1)
        logger.info("repo is clean!")

        # TODO - we should allow csets to exist locally that are not on remote.
        logger.info("ensuring releasewarrior repo is up to date and in sync with origin")
        origin = self.repo.remotes.origin
        logger.info("fetching csets from origin")
        origin.fetch()
        if self.repo.head.commit.diff(origin):
            logger.error("diff found against origin. ensure `git diff origin/master` yields "
                         "nothing. if commits exist locally but are unknown to origin, "
                         "please push them before trying again. aborting run to be safe.")
            sys.exit(1)
        logger.info("repo is up to date and in sync")

    @abc.abstractmethod
    def generate_data(self, data, data_path):
        """generates data file based on command arguments"""

    @abc.abstractmethod
    def generate_wiki(self, data_path, wiki_path, wiki_template):
        """generates wiki file based on data file and wiki template"""

    @abc.abstractmethod
    def run(self, args):
        """run sub command"""
        # TODO - uncomment
        # self.pre_run_check()

    def release_exists(self, data_path):
        pass


class CreateRelease(Command):

    def generate_data(self, data, data_path):
        pass

    def generate_wiki(self, data_path, wiki_path, wiki_template):
        pass

    def run(self, args):
        super().run(args)


class UpdateRelease(Command):

    def generate_data(self, data, data_path):
        pass

    def generate_wiki(self, data_path, wiki_path, wiki_template):
        pass

    def run(self, args):
        pass


class BumpBuildnum(Command):

    def generate_data(self, data, data_path):
        pass

    def generate_wiki(self, data_path, wiki_path, wiki_template):
        pass

    def run(self, args):
        pass


class SyncRelease(Command):

    def generate_data(self, data, data_path):
        pass

    def generate_wiki(self, data_path, wiki_path, wiki_template):
        pass

    def run(self, args):
        pass


class Postmortem(Command):

    def generate_data(self, data, data_path):
        pass

    def generate_wiki(self, data_path, wiki_path, wiki_template):
        pass

    def run(self, args):
        pass

    def get_complete_releases(self):
        pass

    def archive_completed(self):
        pass


class Outstanding(Command):

    def generate_data(self, data, data_path):
        pass

    def generate_wiki(self, data_path, wiki_path, wiki_template):
        pass

    def run(self, args):
        pass

    def get_incomplete_releases(self):
        pass
