import sys
import os
import argparse
import datetime
import logging

from releasewarrior.commands import CreateRelease, UpdateRelease, Postmortem, Outstanding
from releasewarrior.commands import SyncRelease
from releasewarrior.config import LOG_PATH


def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=os.path.join(LOG_PATH, 'releasewarrior.log'),
                        filemode='a')
    console = logging.StreamHandler()
    # flip this to INFO once done testing
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))

    # add console logging to root logger
    logging.getLogger('').addHandler(console)
    return logging.getLogger('releasewarrior')


def parse_args():
    parser = argparse.ArgumentParser(
        description="ReleaseWarrior: helping you keep track of releases in flight"
    )
    subparser = parser.add_subparsers(title='valid sub-commands',
                                      description="run `release <command> --help` for usage details")

    # sub-commands
    parser_create = subparser.add_parser(
        'create', help="start tracking a new release currently in flight"
    )
    parser_create.set_defaults(command=CreateRelease)

    parser_update = subparser.add_parser(
        'update', help="update state of an existing release"
    )
    parser_update.set_defaults(command=UpdateRelease)

    parser_postmortem = subparser.add_parser(
        'postmortem', help="archive completed releases and create postmortem based their issues"
    )
    parser_postmortem.set_defaults(command=Postmortem)

    parser_outstanding = subparser.add_parser(
        'outstanding', help="output current, incomplete tasks from all open releases"
    )
    parser_outstanding.set_defaults(command=Outstanding)

    parser_sync = subparser.add_parser(
        'sync', help="re-generates wiki of a given release based on current data file"
    )
    parser_sync.set_defaults(command=SyncRelease)

    for subcommand in [parser_create, parser_update, parser_sync]:

        # each of these sub-commands take the following 2 positional args first
        subcommand.add_argument('product', choices=['firefox', 'fennec', 'thunderbird'],
                                help='product of release in question')
        subcommand.add_argument('branch', choices=['release', 'beta', 'esr'],
                                help='release branch of release in question')
        subcommand.add_argument('version', help='version of release in question. examples: '
                                                '47.0b1, 46.0, 46.0.1, 45.0esr, or 45.0.1esr')


    # update options
    parser_update.add_argument('--graphid', '--taskcluster_graphid', dest='graphid',
                               help='taskcluster graphid used for release in question')
    parser_update.add_argument('--shipit', '--submitted-shipit', action='store_true',
                               help='update release that we submitted to ship it (started release)')
    parser_update.add_argument('--cdntest', '--emailed-cdntest', action='store_true',
                               help='update release that we emailed drivers that release is on cdntest')
    parser_update.add_argument('--balrog', '--submitted-balrog', action='store_true',
                               help='update release that we have submitted to balrog')
    parser_update.add_argument('--post', '--post-released', action='store_true',
                               help='update release that we have ran post release task')
    parser_update.add_argument('--issue', '--issue', action='append', dest='issues',
                               help='issue to add to release in question')

    # postmortem options
    parser_postmortem.add_argument('date', type=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"),
                                   help='the date of the postmortem meeting')

    return parser.parse_args()

def main():

    if sys.version_info.major != 3:
        print("y u no py 3 yo?")
        sys.exit()

    logger = setup_logging()

    args = parse_args()
    logger.debug("RUNNING with args: %s", ' '.join(sys.argv[1:]))

    args.command(args).run()  # <3 argparse for this



