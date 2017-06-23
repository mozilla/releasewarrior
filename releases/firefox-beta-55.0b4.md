# Beta: Firefox 55.0b4

### Started: 2017-06-22

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/9qI7VRlpSlac_WXD9vn9mA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- callek: ReleaseTasks failure from adding multiple signoffs. Rail did a [Pull Request](https://github.com/mozilla-releng/releasetasks/pull/251) to fix
- callek: task 'firefox mozilla-beta updates' failed (through 5 retries) due to multiple signoff enabling, when trying to push updates to release cdntest. Ben filed [Bug 1375670](https://bugzil.la/1375670) to track the issue and reverted multiple signoff for now. Task re-ran
- callek: Multiple Signoff (despite being backed out) required me to manually mark the release as published.
- callek: Completed human task didn't trigger anything else, concern on IRC on if resolving it would have published the release entirely... e-mailed ben and rail, and notified r-d of delay

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Rb_RIFg1SSuMJ6AWf9PDsg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- nthomas: [Bug 1375802](https://bugzil.la/1375802) - Failure to submit 55.0b4 build2 task graphs
- asasaki: marking signoff as done, but multi signoff is not enabled
- asasaki: rule 604 was set to 25% rollout; leftover from multiple signoffs? set to 100; probably need cleanup
- asasaki: make that, nuked rule 604 and changed rule 32 to 55.0b4-build2 100%


