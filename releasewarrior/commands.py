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

from releasewarrior.config import REPO_PATH, RELEASES_PATH, TEMPLATES_PATH, ARCHIVED_RELEASES_PATH
from releasewarrior.config import DATA_TEMPLATES, WIKI_TEMPLATES, POSTMORTEMS_PATH

logger = logging.getLogger('releasewarrior')


def get_complete_releases():
    completed_releases = {}
    for root, dirs, files in os.walk(RELEASES_PATH):
        for f in [data_file for data_file in files if data_file.endswith(".json")]:
            abs_f = os.path.join(RELEASES_PATH, f)
            if os.path.exists(abs_f):
                with open(abs_f) as data_f:
                    data = json.load(data_f)
                if all(data["builds"][-1]["human_tasks"].values()):
                    # this release is complete!
                   completed_releases[abs_f] = data
    return completed_releases


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
    update_data = {"human_tasks": {}}
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
    abs_data_file = None
    abs_wiki_file = None
    wiki_template_file = None
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
        wiki = self.generate_wiki(data, os.path.basename(self.wiki_template_file))

        if self.save_data_file:
            # save data to actual data_path
            logger.info("writing to data file: %s", self.abs_data_file)
            with open(self.abs_data_file, 'w') as data_file:
                json.dump(data, data_file)

        # save wiki to actual wiki_path
        logger.info("writing to wiki file: %s", self.abs_wiki_file)
        with open(self.abs_wiki_file, 'w') as wp:
            wp.write(wiki)

    def add_and_commit(self, files, msg):
        self.repo.index.add(files)

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
        self.abs_data_file = os.path.join(
            RELEASES_PATH, "{}-{}-{}.json".format(self.product, self.branch, self.version)
        )
        self.abs_wiki_file = os.path.join(
            RELEASES_PATH, "{}-{}-{}.md".format(self.product, self.branch, self.version)
        )
        self.wiki_template_file = WIKI_TEMPLATES[self.product][self.branch]
        self.commit_msg = "started tracking {} {} release. created {} wiki and data file".format(
            self.product, self.version, os.path.basename(self.abs_wiki_file)
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

        if release_exists(os.path.basename(self.abs_data_file)):
            logger.error("release already exists! Ensure %s doesn't exist in %s or %s dirs",
                         os.path.basename(self.abs_data_file), RELEASES_PATH, ARCHIVED_RELEASES_PATH)
            sys.exit(1)

    def run(self):
        super().run()

        self.add_and_commit([self.abs_data_file, self.abs_wiki_file], self.commit_msg)


class UpdateRelease(Command):

    def __init__(self, args):
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.abs_data_file = os.path.join(
            RELEASES_PATH, "{}-{}-{}.json".format(self.product, self.branch, self.version)
        )
        self.abs_wiki_file = os.path.join(
            RELEASES_PATH, "{}-{}-{}.md".format(self.product, self.branch, self.version)
        )
        self.wiki_template_file = WIKI_TEMPLATES[self.product][self.branch]
        self.changes = get_update_data(args)
        self.commit_msg = "updating {} {} release. updated {} wiki".format(
            self.product, self.version, os.path.basename(self.abs_wiki_file)
        )

        self.pre_run_check()

    def generate_data(self):
        new_data = {}
        current_data = {}

        logger.info("grabbing current data about release")
        with open(self.abs_data_file) as current_data_f:
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

        if not release_exists(os.path.basename(self.abs_data_file), ignore_archive=True):
            logger.error("release doesn't exist! Ensure %s exists."
                         "Use the `create` command to create initial data and wiki.",
                         self.abs_data_file)
            sys.exit(1)

    def run(self):
        super().run()
        self.add_and_commit([self.abs_data_file, self.abs_wiki_file], self.commit_msg)


class SyncRelease(Command):

    def __init__(self, args):
        self.product = args.product
        self.branch = args.branch
        self.version = args.version
        self.abs_data_file = os.path.join(
            RELEASES_PATH, "{}-{}-{}.json".format(self.product, self.branch, self.version)
        )
        self.abs_wiki_file = os.path.join(
            RELEASES_PATH, "{}-{}-{}.md".format(self.product, self.branch, self.version)
        )
        self.wiki_template_file = WIKI_TEMPLATES[self.product][self.branch]
        self.commit_msg = "generating wiki for {} {} release with changes in current data file".format(
            self.product, self.version,
        )
        self.save_data_file = False

        self.pre_run_check()

    def generate_data(self):
        current_data = {}

        logger.info("grabbing data for release from current data file")
        with open(self.abs_data_file) as current_data_f:
            current_data.update(json.load(current_data_f))

        return current_data

    def pre_run_check(self):
        super().pre_run_check()

        ensure_branch_and_version_are_valid(self.branch, self.version)

        if not release_exists(os.path.basename(self.abs_data_file), ignore_archive=True):
            logger.error("release doesn't exist! Ensure %s exists."
                         "Use the `create` command to create initial data and wiki.",
                         self.abs_data_file)
            sys.exit(1)

    def run(self):
        super().run()
        self.add_and_commit([self.abs_data_file, self.abs_wiki_file], self.commit_msg)


class Postmortem(Command):

    def __init__(self, args):
        self.date = "{}-{}-{}".format(args.date.year, args.date.month, args.date.day)
        self.abs_data_file = os.path.join(POSTMORTEMS_PATH, "{}.json".format(self.date))
        self.abs_wiki_file = os.path.join(POSTMORTEMS_PATH, "{}.md".format(self.date))
        self.wiki_template_file = WIKI_TEMPLATES["postmortem"]
        self.completed_releases = get_complete_releases()
        self.commit_msg = "updating postmortem. updated {} wiki".format(
            os.path.basename(self.abs_wiki_file)
        )

        self.pre_run_check()

    def generate_data(self):
        new_data = {
            "releases": [],
            "date": self.date,
        }

        logger.info("grabbing current data about postmortem")
        if os.path.exists(self.abs_data_file):
            with open(self.abs_data_file) as current_data_f:
                new_data.update(deepcopy(json.load(current_data_f)))

        logger.info("updating postmortem with recently completed releases.")
        for release in self.completed_releases.values():
            postmortem_release = {
                "version": release['version'],
                "product": release['product'],
                "date": release['date'],
            }
            postmortem_release["builds"] = []
            for build in release["builds"]:
                postmortem_release["builds"].append({
                    "buildnum": build["buildnum"],
                    "issues": build["issues"],
                })
            new_data["releases"].append(postmortem_release)

        return new_data

    def pre_run_check(self):
        super().pre_run_check()

        if not self.completed_releases:
            logger.error("no current releases found in %s that have all human tasks completed. "
                         "Use the `update` command to complete current release's human_tasks.",
                         RELEASES_PATH)
            sys.exit(1)

    def run(self):
        super().run()

        self.archive_completed()
        self.add_and_commit([self.abs_data_file, self.abs_wiki_file], self.commit_msg)

    def archive_completed(self):
        """moves completed releases to archive directory"""
        for abs_data_file in self.completed_releases.keys():
            archive_data_dest = os.path.join(ARCHIVED_RELEASES_PATH, os.path.basename(abs_data_file))
            self.repo.index.move([abs_data_file, archive_data_dest])

            abs_wiki_file = abs_data_file.replace(".json", ".md")
            archive_wiki_dest = os.path.join(ARCHIVED_RELEASES_PATH, os.path.basename(abs_wiki_file))
            self.repo.index.move([abs_wiki_file, archive_wiki_dest])


class Outstanding(Command):

    def generate_data(self):
        pass

    def generate_wiki(self, data_path, wiki_template):
        pass

    def run(self):
        pass

    def get_incomplete_releases(self):
        pass
