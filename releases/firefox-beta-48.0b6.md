# Beta: Firefox 48.0b6

### Started: 2016-07-07

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#Z2BNOjUqTC-P6du___P5oA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [ ] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [ ] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- BBB scheduled linux 64 l10n chunk 7 twice, what caused a race condition in the artifacts task, failing funsize and beetmover tasks. Reran the artifacts task to schedule it. Reran the corresponding l10n repack to reenerate artifacts again. Need to clean up some files under the releases directory (In [Bug 1285284](https://bugzil.la/1285284)) to make beetmover work for the new generated binaries.


