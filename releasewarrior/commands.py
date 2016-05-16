import abc
import sys
import argparse


class Command(metaclass=abc.ABCMeta):
    parser = None

    def pre_run_check(self):
        """ensures repo is clean and nothing is incoming"""

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
        print('\o/')


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
