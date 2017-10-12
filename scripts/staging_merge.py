# merge script for staging releases

import os
import logging
import requests
import subprocess

archiver_url="https://hg.mozilla.org/build/tools/raw-file/default/buildfarm/utils/archiver_client.py"
archiver_filename = archiver_url.split("/")[-1]

def run_merge(args):
    path=args.merge_dir
    from_repo_url=args.from_repo_url
    to_repo_url=args.to_repo_url
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    r=requests.get(archiver_url)
    f = open(archiver_filename, 'w')
    f.write(r.text)
    f.close()

    # call the file instead of importing it, call it because it needs to run under python27
    subprocess.check_call(['python', 'archiver_client.py', 'mozharness', '--destination', 'mozharness-central', '--repo', 'mozilla-central', '--rev', 'default', '--debug'])
    # modify mozharness-central/configs/merge_day/central_to_beta.py with the repos from the arguments and use https instead of ssh to clone
    ctobfile="mozharness-central/configs/merge_day/central_to_beta.py"
    f=open(ctobfile, 'rt')
    data=f.read()
    f.close()
    data1 = data.replace("ssh://hg.mozilla.org/mozilla-central","https://hg.mozilla.org/" + from_repo_url)
    data2 = data1.replace("ssh://hg.mozilla.org/releases/mozilla-beta","https://hg.mozilla.org/" + to_repo_url)
    # overwrite existing migration file
    f=open(ctobfile, 'w')
    f.write(data2)
    f.close()
    # run the merge script
    subprocess.check_call(['python', 'mozharness-central/scripts/merge_day/gecko_migration.py', '-c', 'merge_day/central_to_beta.py'])

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('merge_dir')
    parser.add_argument('from_repo_url')
    parser.add_argument('to_repo_url')

    logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO)

    args = parser.parse_args()
    run_merge(args)
