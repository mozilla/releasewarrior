# MergeDuty Tasks

Tracking bug: https://bugzilla.mozilla.org/show_bug.cgi?id=1407602

What's special about this migration:

Both m-r and m-b are being migrated on the same day. Thus combining the two weeks or migrations into one.

See https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#appendix-what-to-do-if-relman-asks-1-release-to-be-on-2-trains-at-the-same-time for more details

## Merge Prep Day
### Wed, Nov 1st, 2017

- [x] read the docs: https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#day-1---prep-day-1
- [x] patch and get review for two bbot-cfgs gecko version bump patches (DONT LAND YET)
  - [x] **Unique!** patch 1: bump both m-r and m-b buildbot gecko versions (land nov 2nd). example: combine this [patch](https://hg.mozilla.org/build/buildbot-configs/rev/1b2a3ccb766f17015ca2239da14ba80cac2d7b45) with this [patch](https://reviewboard.mozilla.org/r/179748/diff/1#index_header)
  - [x] **Unique!** patch 2: bump buildbot gecko version for m-c (land nov 13th). example [patch](https://reviewboard.mozilla.org/r/182238/diff/1#index_header)
- [x] Look at blocking bugs against the merge day bugs, and ask around if there are any patches that need to land with the release migration: example: https://bugzilla.mozilla.org/showdependencytree.cgi?id=1123369&hide_resolved=0
- [x] do a no-op trial run of performing the mozilla-beta -> mozilla-release migration. e.g. `python mozharness/scripts/merge_day/gecko_migration.py -c mozharness/configs/merge_day/beta_to_release.py`
- [x] **Unique!** do a no-op trial run of performing the mozilla-central -> mozilla-beta migration. e.g. `python mozharness/scripts/merge_day/gecko_migration.py -c mozharness/configs/merge_day/central_to_beta.py`

## Release and Beta Merge Day
### Mon, March 23rd, 2015

- [x] Look at blocking bugs against the merge day bugs, and ask around if there are any patches that need to land with the release migration: example: https://bugzilla.mozilla.org/showdependencytree.cgi?id=1123369&hide_resolved=0
- [x] **Unique** land previously reviewed m-r and m-b gecko version bbotcfgs patch
- [x] reconfig via one of [three ways](https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#reconfigs-part-1)
- [x] wait for go-to-merge m-r email from release-drivers@mozilla.com before moving on
- [x] perform the [mozilla-beta -> mozilla-release migration](https://wiki.mozilla.org/ReleaseEngineering/Merge_Duty/Steps#Perform_mozilla-beta_-.3E_mozilla-release_migration)
- [x] **unique** no need to uplift locales as 57 release shall build off l10n-central with the signed-off revisions from elmo
- [x] [bump esr](https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#bump-esr-version)
- [x] ping pike and inform him we are about to migrate and push to m-b
- [x] **Unique** patch your copy of gecko_migration.py script used above to [not push any change to m-c m-c](https://gist.github.com/rail/4c56fa137d727d3e5d7ccc5140cddae1)
- [x] **Unique** [Merge central to beta](https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#merge-central-to-beta) using above uncommented script lines
- [x] **Unique** [manually tag m-c](https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#tag-m-c)
- [x] **Unique** (unique because we normally do this the 2nd week) [bump l10n bumper](https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#run-the-l10n-bumper)
- [x] **Unique** inform ryanvm that m-b has been bumped and he still needs to create a branch for fennec
- [x] reply to original "please merge" email that this is now done.


## Central Version Bump
### Mon, Nov 13th, 2017
- [ ] wait for go from relman to bump m-c
- [ ] [bump m-c version in bbot](https://reviewboard.mozilla.org/r/182238/diff/1#index_header) and reconfig
- [ ] [bump m-c](https://hg.mozilla.org/mozilla-central/rev/835a92b19e3d)
- [x] no need to trigger nightlies because we do nightlies twice a day now
- [ ] [bump wiki versions](https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#update-wikis) - now that central is bumped, we can run this script
- [ ] email that this has been done


## Update Bouncer entries for nightly
### Tues, Nov 14th, 2017

- [ ] once we have new nightlies, we can [update bouncer entries](https://github.com/mozilla/releasewarrior/blob/master/how-tos/mergeduty.md#bump-bouncer-versions)
- [ ] Update this documentation with any new changes: https://wiki.mozilla.org/ReleaseEngineering/Merge_Duty  !!!
