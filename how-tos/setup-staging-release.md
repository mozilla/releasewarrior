# Setting up a specific branch to test staging releases

## Intro
Being releaseduty creates a certain advantage in time as it requires both squirrels to touch lots of the infrastructure and
components that form our release automation pipeline. It's expected that from time to time, whenever we need
to make significant changes to our release automation, staging releases need to be performed before we flip the changes to
production. This is where the releaseduty knowledge comes to rescue!

Historically, we have been using staging releases mostly to test `beta 1` of a new cycle. That is because a `beta` release is our most
common type of release and it is the one we usually start any transformation process with. We used it when we switched to `release
promotion` but also for `tcmigration` projects. This how-to page assumes the same, but a different type of release should behave somewhat
similar. So mainly rather larger changes to the code base, changes that actually impose a staging release beforehand.

## Simulation project branch

Project branch `jamun` has traditionally been our choice to simulate `beta`. We have been using `maple` for simulating nightlies from `central`.

Use cases:
- for `central` -> `beta` staging release we would use `from_repo_url` = `central`  and `to_repo_url` = `jamun`
- for `maple` -> `central` -> `beta` (stuff that lands in `central` and right after that goes in `beta`) staging release we would use `from_repo_url` = `maple`  and `to_repo_url` = `jamun`

## Merge scripts

1.  See the doc <a href="merge-and-staging-instance.md">AWS staging instance</a> to see if using a dedicated instance for staging releases would be helpful.

2. Use the <a href="../scripts/staging_merge.py">script</a> to run the merge for you. Parameters are the directory to run the merge in, and the repos to merge_from, and merge_to.  For example:
```
staging_merge.py merge_dir projects/maple projects/jamun
```

3. The script should have created a diff. Check that everything is okay and push to jamun
```sh
hg -R build/jamun diff
hg -R build/jamun commit -m "Uplift from central to jamun"
hg -R build/jamun out -r . jamun
hg -R build/jamun push
```

Optional: reset the staging tools repo using this <a href="../scripts/reset_tools.sh">script</a> to ensure you are using the same version as production.
Optional: reset the staging balrog db which is important for staging release builds so they include recent point releases.  This can be done by making a GET to https://balrog-admin.stage.mozaws.net/__rebuilddb__  This step will take 10-15min to complete, You can confirm by comparing the state of the rules vs production.

## Staging tools

- dev [Ship-it](https://ship-it-dev.allizom.org/)
- staging [release runner](https://dxr.mozilla.org/build-central/rev/5f83e0516fc449586bbce4db4eb759f6cede8781/puppet/manifests/moco-nodes.pp#633)
- release automation notifications [group](https://groups.google.com/a/mozilla.com/forum/?hl=en#!forum/release-automation-notifications-dev) and `#release-notifications-dev` IRC channel

## Staging configs

- release runner will consume [project branch configs](https://dxr.mozilla.org/build-central/rev/92614acc90330edf360d97d8575b7e917ddc43b2/buildbot-configs/mozilla/project_branches.py#114)
- mozharness [configs](https://dxr.mozilla.org/mozilla-central/source/testing/mozharness/configs/releases/) - all configs with `dev` prefix
- in order to avoid pushing patcher configs changes/tags to *real* [tools](http://hg.mozilla.org/build/tools/) repo, we have changed the buildbot and in-tree configs to point to the <a href="https://hg.mozilla.org/users/stage-ffxbld/tools">staging tools repo</a>) 

## Misc

- TODO Release runner is smart. It only takes into account the Tier1 stuff.
- Update verify tests are flaky and we need to invest some time to make them work. Our assumption is that we need to better flip variables [here](https://dxr.mozilla.org/mozilla-central/rev/7d2e89fb92331d7e4296391213c1e63db628e046/testing/mozharness/configs/releases/dev_updates_firefox_beta.py)


## Running staging release for releases

A few issues encountered while running releases for the 57.0 release on the jamun branch:
- Configs need to be updated for the branch <a href="https://bug1413910.bmoattachments.org/attachment.cgi?id=8924543">here</a> so we can run staging runs.
- Also, this issue arose with <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1413910#c13">bump configs</a>
- The staging tools repo needs to have <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1413910#c9">the jamun patcher configs updated</a>.
- Also, the ship-it dev instance needs to have the previous releases that you are requesting partials from available. You can add the releases in as pending builds and then ask someone with db access to mark them as complete.  This allows the release sanity to complete, otherwise it will complain about the missing releases for ithe specified partials.
