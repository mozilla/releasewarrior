# Forewords

These steps are meant to be specifically for Fennec-53.0b1.

# High-level steps

1. noop ship-it
2. skip source
3. kick off fennec_candidates hook
4. hack candidates to release script, run manually
5. run pushapk manually
6. mark release as shipped in ship-it

# Detailed descriptions

## Noop ship-it

Nothing to do here. Yay!

## Skip source

Nothing to do here for the moment. Both in the releasetasks generated graph and the hook, the source builder shall be turned off.

## Kick off fennec_candidates hook

The hook that triggers the Fennec graph is [here](https://tools.taskcluster.net/hooks/#project-releng/candidates-fennec-beta).
* alter GECKO_HEAD_REF, GECKO_HEAD_REV to corresponding changeset from Ship-it
* bump the buildnumber to correspond to Ship-it
* trigger hook!

## Hack candidates to release script, run manually

## Run pushapk manually

### Use pushapk_scriptworker

1. Fetch the [base task definition](https://github.com/mozilla-releng/pushapkscript/blob/master/task_example.json)
2. Paste it onto [TC's task creator](https://tools.taskcluster.net/task-creator/)
3. Modify the [fields that need to be changed](https://github.com/mozilla-releng/pushapkscript#taskjson):
  * For the APKs locations, use the signed tasks.
  * Use the scope `'project:releng:googleplay:beta'`
  * Change `google_play_track` to `production`
  * Keep `dry_run` to `true`
4. You may want to attach this task to the rest of the graph. To do so, add in your task definition:
```
schedulerId: gecko-level-3
taskGroupId: $ACTUAL_TASKGROUP_ID
```
5. If everything passed, create second task with the same definition, but flip `dry_run` to false.

### Fallback steps

In the eventuality of a failure of pushapk_scriptworker, there are [instructions to manually publish APKs](https://github.com/mozilla-releng/mozapkpublisher#what-to-do-when-pushapk_scriptworker-doesnt-work).

#### manually run l10n-bumper
```
ssh buildbot-master01.bb.releng.use1.mozilla.com
sudo su - cltbld
cd /builds/l10n-bumper
/tools/python27/bin/python2.7 mozharness/scripts/l10n_bumper.py -c l10n_bumper/mozilla-beta.py
```

## Mark release as shipped in ship-it
