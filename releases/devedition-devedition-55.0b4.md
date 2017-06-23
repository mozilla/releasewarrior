# Beta: Devedition 55.0b4

### Started: 2017-06-22

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/XXLNDFv7SZSWlY7PcYwLcw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- callek: task 'devedition mozilla-beta updates' failed (through 5 retries) due to multiple signoff enabling, when trying to push updates to release cdntest. Ben filed [Bug 1375670](https://bugzil.la/1375670) to track the issue and reverted multiple signoff for now. Task re-ran
- callek: Multiple Signoff (despite being backed out) required me to manually mark the release as published.
- callek: desktop human task didn't trigger anything else, concern on IRC on if resolving it would have published the release entirely... e-mailed ben and rail, and notified r-d of delay

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
task graph url: unknown


#### Status
- [ ] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- nthomas: [Bug 1375802](https://bugzil.la/1375802) - Failure to submit 55.0b4 build2 task graphs


