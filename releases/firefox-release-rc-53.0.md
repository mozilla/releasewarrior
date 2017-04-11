# RC Release: Firefox 53.0

### Started: 2017-04-10

## Build 1

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/p6Q9UsUrS9eSv1s4z0Cg3A)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- SPECIAL REQUIREMENT: [Bug 1354115](https://bugzil.la/1354115) - remove special WebSense rules for non-blacklisted and unknown WebSense users
- [Bug 1318919](https://bugzil.la/1318919) - we forgot we had to update m-r for tc linux
- docker image hg clone timeouts https://github.com/mozilla/releasetasks/pull/229


