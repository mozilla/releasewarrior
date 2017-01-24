# RC Release: Firefox 51.0

### Started: 2017-01-17

## Build 1

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/F-M28_kwTUCyBYgRWq7rqA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Ship-it bug - title not visible as link when partials sanity fails. [Bug 1332222](https://bugzil.la/1332222)

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/yGzF7mqtSuiSIQsVv28qVw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/CFszYBp7SVypjqHh0EAtPQ)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Ship-it bug - did not move to Reviews/Running after amending partials sanity. [Bug 1332247](https://bugzil.la/1332247)
- Because of above bug ^ we ended up having https://people-mozilla.org/~mtabara/shipit_issues.png; Rail fixed the Ship-it DBby running <update firefox_release set ready=1, complete=1 where name='Firefox-51.0-build2'>


