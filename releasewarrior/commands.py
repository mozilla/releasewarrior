import abc
import os
import sys
import re
import logging
import json
import datetime
from copy import deepcopy

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


def get_update_data(args):
    build_data = [
        ("graphid", args.graphid),
        ("aborted", args.aborted),
        ("issues", args.issues),
    ]
    human_tasks_data = [
        ("submitted_shipit", args.submitted_shipit),
        ("emailed_cdntest", args.emailed_cdntest),
        ("published_balrog", args.published_balrog),
        ("post_released", args.post_released),
    ]
    update_data = {}
    for key, value in build_data:
        if value:
            update_data[key] = value
    for key, value in human_tasks_data:
        if value:
            update_data["human_tasks"][key] = value
    return update_data


def data_unchanged(new_data, current_data):
    # TODO - make this more generic and elegant
    for index in range(0, len(new_data['builds'])):
        for new_data_key, new_data_value in new_data["builds"][index].items():
            current_data_value = current_data["builds"][index][new_data_key]
            # look for unique issue lists
            if new_data_key == "issues":
                if list(set(new_data_value) - set(current_data_value)):
                    return False
            elif new_data_key == "human_tasks":
                for task_key, task_value in new_data["builds"][index]["human_tasks"].items():
                    current_task_value = current_data["builds"][index]["human_tasks"][task_key]
                    if task_value != current_task_value:
                        return False
            # look for unique data strings
            elif new_data_value != current_data_value:
                return False
    return True


def release_exists(data_file, ignore_archive=False):
    searchpaths = [RELEASES_PATH] if ignore_archive else [RELEASES_PATH, ARCHIVED_RELEASES_PATH]
    data_exists = False

    def exists_in_searchpaths(target):
        for searchpath in searchpaths:
            if os.path.exists(os.path.join(searchpath, target)):
                return True
        return False

    if exists_in_searchpaths(data_file):
        data_exists = True

    return data_exists


class Command(metaclass=abc.ABCMeta):
    repo = Repo(REPO_PATH)
    product = None
    branch = None
    version = None
    data_file = None
    wiki_file = None
    commit_msg = None
    save_data_file = True  # sync doesn't touch data file

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
                          undefined=StrictUndefined, trim_blocks=True)
        template = env.get_template(wiki_template)
        return template.render(**data)

    def run(self):
        """run sub command"""
        data = self.generate_data()
        wiki = self.generate_wiki(data, os.path.basename(WIKI_TEMPLATES[self.product][self.branch]))

        abs_data_file = os.path.join(RELEASES_PATH, self.data_file)
        abs_wiki_file = os.path.join(RELEASES_PATH, self.wiki_file)

        if self.save_data_file:
            # save data to actual data_path
            logger.info("writing to data file: %s", abs_data_file)
            with open(abs_data_file, 'w') as data_file:
                json.dump(data, data_file)

        # save wiki to actual wiki_path
        logger.info("writing to wiki file: %s", abs_wiki_file)
        with open(abs_wiki_file, 'w') as wp:
            wp.write(wiki)

        self.add_and_commit(abs_data_file, abs_wiki_file, self.commit_msg)

    def add_and_commit(self, data_file, wiki_file, msg):
        self.repo.index.add([data_file, wiki_file])

        if not self.repo.index.diff("HEAD"):
            logger.warning("nothing staged for commit. has the data or wiki file changed?")
            sys.exit(1)

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

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if release_exists(self.data_file):
            logger.error("release already exists! Ensure %s doesn't exist in %s or %s dirs",
                         self.data_file, RELEASES_PATH, ARCHIVED_RELEASES_PATH)
            sys.exit(1)


class UpdateRelease(Command):

    def __init__(self, args):
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.data_file = "{}-{}-{}.json".format(self.product, self.branch, self.version)
        self.wiki_file = "{}-{}-{}.md".format(self.product, self.branch, self.version)
        self.changes = get_update_data(args)
        self.commit_msg = "updating {} {} release. updated {} wiki with changes: {}".format(
            self.product, self.version, self.wiki_file, self.changes
        )

        self.pre_run_check()

    def generate_data(self):
        new_data = {}
        current_data = {}

        logger.info("grabbing current data about release")
        with open(os.path.join(RELEASES_PATH, self.data_file)) as current_data_f:
            current_data.update(json.load(current_data_f))
            new_data.update(deepcopy(current_data))

        logger.info("updating with custom update data")
        for key_change, key_value in self.changes.items():
            if key_change == "issues":
                new_data['builds'][-1]["issues"].extend(key_value)
            elif key_change == "human_tasks":
                new_data['builds'][-1]["human_tasks"].update(key_value)
            else:
                new_data['builds'][-1][key_change] = key_value

        if new_data["builds"][-1]["aborted"]:
            logger.info("most recent buildnum has been aborted, starting a new buildnum")
            template_buildnum_data = {}
            with open(DATA_TEMPLATES[self.product][self.branch]) as data_template:
                template_buildnum_data.update(json.load(data_template)["builds"][0])
            new_data["builds"].append(template_buildnum_data)
            new_data["builds"][-1]["buildnum"] = len(new_data["builds"])

        if data_unchanged(new_data, current_data):
            logger.warning("no changes found in update call after regenerating data file.")
            logger.warning("nothing to commit. aborting.")
            sys.exit(1)

        return new_data

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if not release_exists(self.data_file, ignore_archive=True):
            logger.error("release doesn't exist! Ensure %s exists in %s or dir. "
                         "Use the `create` command to create initial data and wiki.",
                         self.data_file, self.wiki_file, RELEASES_PATH)
            sys.exit(1)


class SyncRelease(Command):

    def __init__(self, args):
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.data_file = "{}-{}-{}.json".format(self.product, self.branch, self.version)
        self.wiki_file = "{}-{}-{}.md".format(self.product, self.branch, self.version)
        self.commit_msg = "generating wiki for {} {} release with changes in current data file".format(
            self.product, self.version,
        )
        self.save_data_file = False

        self.pre_run_check()

    def generate_data(self):
        current_data = {}

        logger.info("grabbing data for release from current data file")
        with open(os.path.join(RELEASES_PATH, self.data_file)) as current_data_f:
            current_data.update(json.load(current_data_f))

        return current_data

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if not release_exists(self.data_file, ignore_archive=True):
            logger.error("release doesn't exist! Ensure %s exists in %s or dir. "
                         "Use the `create` command to create initial data and wiki.",
                         self.data_file, RELEASES_PATH)
            sys.exit(1)

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
