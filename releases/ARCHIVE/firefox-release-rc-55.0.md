# RC Release: Firefox 55.0

### Started: 2017-07-31

## Build 1

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/0rKw_NbcTjKuroEEWveJmg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- SPECIAL REQUIREMENT: after first week mergeduty on 1st of August is completed, before we trigger the RC, we need to land and merge this [PR](https://github.com/mozilla-releng/releasetasks/pull/247)

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/66UUzZdpQ5-Xflty8oFCrA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [ ] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- none

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/wdkFdzfETlCApV8HXWXvxg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [x] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)

### RC graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/kzNGyB4TQLu8X6F604TImw)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- nthomas: [Bug 1387278](https://bugzil.la/1387278) - signing server cert expiry. 5 exceptions - i9sSvkGqTs203D22veGU1w is the last signing job for mac updates, blocking the graph; 4 partner or EME-free repacks. Reran the 5 tasks after catlee renewed the certs.
- mihaitabara: bn-IN win32 update verification fails in 55.0-build3. [Bug 1387404](https://bugzil.la/1387404)
- mihaitabara: Tracking bug for release day issues [Bug 1388306](https://bugzil.la/1388306)


