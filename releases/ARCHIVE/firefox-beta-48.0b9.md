# Beta: Firefox 48.0b9

### Started: 2016-07-18

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#OPqfW1yBTgSd8Ud4svhRag)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- The initial requested revision was android-only, so we had no desktop builds. Set the previous revision in ship-it
- Because b8 was skipped, the in-tree revision was not matching the revision in ship-it. Bumped the revision and pushed to beta.
- [Bug 1287665](https://bugzil.la/1287665): add-on-devel windows builds overwrote the opt build TC indexes (missing config variables). jlund landed a patch to fix it.
- release-runner sanity caught '[Bug 1287665](https://bugzil.la/1287665)'. got lucky with fix as the 'real' opt build hadn't uploaded artifacts yet so we just had to wait till it overwrote the bad indexed add-on-devel equivalent
- Mac worker disconnected and buildbot automatically retried http://archive.mozilla.org/pub/firefox/tinderbox-builds/mozilla-beta-l10n/release-mozilla-beta_firefox_macosx64_l10n_repack-bm85-build1-build117.txt.gz
- Reran a bunch of windows update verifies due to clobber timeouts.


