import abc
import os
import pprint
import sys
import re
import logging
import json
import datetime

from git import Repo
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from releasewarrior.config import REPO_PATH, RELEASES_PATH, TEMPLATES_PATH, ARCHIVED_RELEASES_PATH, \
    DATA_TEMPLATES, WIKI_TEMPLATES

logger = logging.getLogger('releasewarrior')


def ensure_branch_and_version_are_valid(branch, version):
    mismatch = False
    if branch == 'beta' and 'b' not in version:
        logger.error("beta specified but 'b' not found in version.")
        mismatch = True
    elif branch == 'release' and re.search('[a-zA-Z]', version):
        logger.error("release specified but an alpha char was found in version.")
        mismatch = True
    elif branch == 'esr' and 'esr' not in version:
        logger.error("esr specified but 'esr' not found in version.")
        mismatch = True
    if mismatch:
        logger.error("Was there a mistake?")
        sys.exit(1)


class Command(metaclass=abc.ABCMeta):
    repo = Repo(REPO_PATH)

    def pre_run_check(self):
        """ensures repo is clean and local repo is in sync with remote origin"""

        # TODO - uncomment
        # logger.info("ensuring releasewarrior repo is clean")
        # if self.repo.is_dirty():
        #     logger.error("releasewarrior repo is dirty. aborting run to be safe.")
        #     sys.exit(1)
        # logger.info("repo is clean!")
        #
        # # TODO - we should allow csets to exist locally that are not on remote.
        # logger.info("ensuring releasewarrior repo is up to date and in sync with origin")
        # origin = self.repo.remotes.origin
        # logger.info("fetching csets from origin")
        # origin.fetch()
        # if self.repo.head.commit.diff(origin):
        #     logger.error("diff found against origin. ensure `git diff origin/master` yields "
        #                  "nothing. if commits exist locally but are unknown to origin, "
        #                  "please push them before trying again. aborting run to be safe.")
        #     sys.exit(1)
        # logger.info("repo is up to date and in sync")

    @abc.abstractmethod
    def generate_data(self, data_path):
        """generates data file based on command arguments"""

    def generate_wiki(self, data, wiki_template):
        """generates wiki file based on data file and wiki template"""
        env = Environment(loader=FileSystemLoader(TEMPLATES_PATH),
                          undefined=StrictUndefined)
        template = env.get_template(wiki_template)
        return template.render(**data)

    @abc.abstractmethod
    def run(self):
        """run sub command"""

    def release_exists(self, data_file, wiki_file):
        for file in data_file, wiki_file:
            for path in os.path.join(ARCHIVED_RELEASES_PATH, file), os.path.join(RELEASES_PATH, file):
                # logger.debug('xxx: %s', path)
                if os.path.exists(path):
                    return True
        return False

    def get_data_path(self):
        pass

    def get_release_info(self, version, product):
        pass


class CreateRelease(Command):

    def __init__(self, args):
        super().__init__()
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.data_file = "{}-{}-{}.json".format(self.product, self.branch, self.version)
        self.wiki_file = "{}-{}-{}.md".format(self.product, self.branch, self.version)
        self.pre_run_check()

    def generate_data(self):
        data = {}

        # first grab initial data from data template
        with open(DATA_TEMPLATES[self.product][self.branch]) as data_template:
            data.update(json.load(data_template))

        # add in custom initial data
        data["version"] = self.version
        data["date"] = datetime.date.today().strftime("%y-%m-%d")

        return data

    def run(self):
        data = self.generate_data()
        wiki = self.generate_wiki(data, os.path.basename(WIKI_TEMPLATES[self.product][self.branch]))

        abs_data_file = os.path.join(RELEASES_PATH, self.data_file)
        abs_wiki_file = os.path.join(RELEASES_PATH, self.wiki_file)

        # save data to actual data_path
        logger.info("writing to data file: %s", abs_data_file)
        logger.info("contents:\n%s", pprint.pformat(data))
        with open(abs_data_file, 'w') as data_file:
            json.dump(data, data_file)

        # save wiki to actual wiki_path
        logger.info("writing to wiki file: %s", abs_wiki_file)
        logger.info("contents:\n%s", wiki)
        with open(abs_wiki_file, 'w') as wp:
            wp.write(wiki)


        # self.repo.index.add(abs_data_file)
        # self.repo.index.add(abs_wiki_file)

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if self.release_exists(self.data_file, self.wiki_file):
            logger.error("release already exists! Ensure %s and %s don't exist in %s or %s dirs",
                         self.data_file, self.wiki_file, RELEASES_PATH, ARCHIVED_RELEASES_PATH)
            sys.exit(1)


class UpdateRelease(Command):

    def __init__(self, args):
        super().__init__()
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.data_file = "{}-{}-{}.json".format(self.product, self.branch, self.version)
        self.wiki_file = "{}-{}-{}.md".format(self.product, self.branch, self.version)
        self.pre_run_check()

    def generate_data(self):
        pass

    def run(self):
        pass

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if not self.release_exists(self.data_file, self.wiki_file):
            logger.error("release doesn't exist! Ensure %s and %s exist in %s or %s dirs. "
                         "Use the `create` command to create initial data and wiki.",
                         self.data_file, self.wiki_file, RELEASES_PATH, ARCHIVED_RELEASES_PATH)
            sys.exit(1)


class SyncRelease(Command):

    def generate_data(self, data_path):
        pass

    def generate_wiki(self, data_path, wiki_template):
        pass

    def run(self):
        pass


class Postmortem(Command):

    def generate_data(self, data_path):
        pass

    def generate_wiki(self, data_path, wiki_template):
        pass

    def run(self):
        pass

    def get_complete_releases(self):
        pass

    def archive_completed(self):
        pass


class Outstanding(Command):

    def generate_data(self, data_path):
        pass

    def generate_wiki(self, data_path, wiki_template):
        pass

    def run(self):
        pass

    def get_incomplete_releases(self):
        pass
