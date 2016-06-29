# Beta: Firefox 48.0b4

### Started: 2016-06-27

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#PrMLynAIR6iFjr0kePkTgw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- Releaserunner failed because the jobs were not yet 'ready'. Turned out the rev supplied in shipit ([89f21e80a2ad](https://treeherder.mozilla.org/#/jobs?repo=mozilla-beta&revision=89f21e80a2ad5570d535acacacc09a6f5bd0c473)) was building android-only, Sylvestre told jlund that [676a32cdd41f](https://treeherder.mozilla.org/#/jobs?repo=mozilla-beta&revision=676a32cdd41fd372f4c6df3a4954939f73a6ef02) was also fine.
- win64 repack upload failure, rerun
- OSX EMEFree partner repack failed to report correctly, though it finished correctly -- marked task pYfHUD5JSH-ou_K-585gHw as completed
- Should have e-mailed r-d about beta-cdntest being ready, didn't until now
- Beta 4 has no partials from beta3 because beta3's status in shipit wasn't marked as SHIPPED until monday, meaning b3 wasn't offered as a partial suggestion.


