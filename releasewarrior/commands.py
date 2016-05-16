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
        """ensures repo is clean and nothing is incoming"""
        logger.info("ensuring releasewarrior repo is clean")
        if self.repo.is_dirty():
            logger.error("releasewarrior repo is dirty. aborting run to be safe.")
            sys.exit(1)

        origin = self.repo.remotes.origin
        origin.fetch()
        if self.repo.head.commit.diff(origin):
            logger.error("diff found against origin. ensure `git diff origin/master` yields nothing")

        logger.info("made it here")


    @abc.abstractmethod
    def generate_data(self, data, data_path):
        """generates data file based on command arguments"""

    @abc.abstractmethod
    def generate_wiki(self, data_path, wiki_path, wiki_template):
        """generates wiki file based on data file and wiki template"""

    @abc.abstractmethod
    def run(self, args):
        """run sub command"""

    def release_exists(self, data_path):
        pass


class CreateRelease(Command):

    def generate_data(self, data, data_path):
        pass

    def generate_wiki(self, data_path, wiki_path, wiki_template):
        pass

    def run(self, args):
        logger.debug('create run call')
        self.pre_run_check()


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
