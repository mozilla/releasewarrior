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


def get_changes(args):
    return  {
        "graphid": args.graphid,
        "submitted_shipit": args.submitted_shipit,
        "emailed_cdntest": args.emailed_cdntest,
        "published_balrog": args.published_balrog,
        "post_released": args.post_released,
        "aborted": args.aborted,
    }


def release_exists(data_file, wiki_file, both_must_exist=False, ignore_archive=False):
    searchpaths = [RELEASES_PATH] if ignore_archive else [RELEASES_PATH, ARCHIVED_RELEASES_PATH]
    wiki_exists = False
    data_exists = False

    def exists_in_searchpaths(target):
        for searchpath in searchpaths:
            if os.path.exists(os.path.join(searchpath, target)):
                return True
        return False

    if exists_in_searchpaths(data_file):
        data_exists = True
    if exists_in_searchpaths(wiki_file):
        wiki_exists = True

    return data_exists and wiki_exists if both_must_exist else data_exists or wiki_exists


class Command(metaclass=abc.ABCMeta):
    repo = Repo(REPO_PATH)
    product = None
    branch = None
    version = None
    data_file = None
    wiki_file = None
    commit_msg = None

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
    def generate_data(self):
        """generates data file based on command arguments"""

    def generate_wiki(self, data, wiki_template):
        """generates wiki file based on data file and wiki template"""
        env = Environment(loader=FileSystemLoader(TEMPLATES_PATH),
                          undefined=StrictUndefined)
        template = env.get_template(wiki_template)
        return template.render(**data)

    def run(self):
        """run sub command"""
        data = self.generate_data()
        wiki = self.generate_wiki(data, os.path.basename(WIKI_TEMPLATES[self.product][self.branch]))

        abs_data_file = os.path.join(RELEASES_PATH, self.data_file)
        abs_wiki_file = os.path.join(RELEASES_PATH, self.wiki_file)

        # save data to actual data_path
        logger.info("writing to data file: %s", abs_data_file)
        with open(abs_data_file, 'w') as data_file:
            json.dump(data, data_file)

        # save wiki to actual wiki_path
        logger.info("writing to wiki file: %s", abs_wiki_file)
        with open(abs_wiki_file, 'w') as wp:
            wp.write(wiki)

    def add_and_commit(self, files, msg, check_for_diff=True):
        if check_for_diff:
            logger.info("checking for changes")
            if not self.repo.head.commit.diff():
                logger.warning("no changes found after regenerating data and wiki")
                logger.warning("nothing to commit.")
                sys.exit(1)

        logger.info("staging files for commit: %s", files)
        self.repo.index.add(files)
        logger.info("committing changes with message: %s", msg)
        commit = self.repo.index.commit(msg)
        for patch in self.repo.commit("HEAD~1").diff(commit, create_patch=True):
            logger.info(patch)


class CreateRelease(Command):

    def __init__(self, args):
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.data_file = "{}-{}-{}.json".format(self.product, self.branch, self.version)
        self.wiki_file = "{}-{}-{}.md".format(self.product, self.branch, self.version)
        self.commit_msg = "started tracking {} {} release. created {} wiki and data file".format(
            self.product, self.version, self.wiki_file
        )
        self.pre_run_check()

    def generate_data(self):
        data = {}

        logger.info("grabbing initial data for release from template")
        with open(DATA_TEMPLATES[self.product][self.branch]) as data_template:
            data.update(json.load(data_template))

        logger.info("adding custom initial data: version and date")
        data["version"] = self.version
        data["date"] = datetime.date.today().strftime("%y-%m-%d")

        return data

    def run(self):
        super().run()
        abs_data_file = os.path.join(RELEASES_PATH, self.data_file)
        abs_wiki_file = os.path.join(RELEASES_PATH, self.wiki_file)
        self.add_and_commit([abs_data_file, abs_wiki_file], self.commit_msg, check_for_diff=False)

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if release_exists(self.data_file, self.wiki_file):
            logger.error("release already exists! Ensure %s and %s don't exist in %s or %s dirs",
                         self.data_file, self.wiki_file, RELEASES_PATH, ARCHIVED_RELEASES_PATH)
            sys.exit(1)


class UpdateRelease(Command):

    def __init__(self, args):
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.data_file = "{}-{}-{}.json".format(self.product, self.branch, self.version)
        self.wiki_file = "{}-{}-{}.md".format(self.product, self.branch, self.version)
        self.changes = get_changes(args)
        self.issues = args.issues
        self.commit_msg = "updating {} {} release. updated {} wiki and data file".format(
            self.product, self.version, self.wiki_file
        )

        self.pre_run_check()

    def generate_data(self):
        data = {}

        logger.info("grabbing current data about release")
        with open(os.path.join(RELEASES_PATH, self.data_file)) as data_template:
            data.update(json.load(data_template))

        logger.info("updating with custom update data")
        data['builds'][-1].update(self.changes)
        data['builds'][-1]["issues"].extend(self.issues)

        if data["builds"][-1]["aborted"]:
            logger.info("most recent buildnum has been aborted, starting a new buildnum")
            initial_buildnum_data = {}
            with open(DATA_TEMPLATES[self.product][self.branch]) as data_template:
                initial_buildnum_data.update(json.load(data_template)["builds"][0])
                data["builds"].append(initial_buildnum_data)
                data["builds"][-1]["buildnum"] = len(data["builds"])

        return data

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if not release_exists(self.data_file, self.wiki_file, both_must_exist=True,
                                   ignore_archive=True):
            logger.error("release doesn't exist! Ensure %s and %s exist in %s or %s dirs. "
                         "Use the `create` command to create initial data and wiki.",
                         self.data_file, self.wiki_file, RELEASES_PATH, ARCHIVED_RELEASES_PATH)
            sys.exit(1)

    def run(self):
        super().run()
        abs_data_file = os.path.join(RELEASES_PATH, self.data_file)
        abs_wiki_file = os.path.join(RELEASES_PATH, self.wiki_file)
        self.add_and_commit([abs_data_file, abs_wiki_file], self.commit_msg)


class SyncRelease(Command):

    def generate_data(self):
        pass

class Postmortem(Command):

    def generate_data(self):
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

    def generate_data(self):
        pass

    def generate_wiki(self, data_path, wiki_template):
        pass

    def run(self):
        pass

    def get_incomplete_releases(self):
        pass
