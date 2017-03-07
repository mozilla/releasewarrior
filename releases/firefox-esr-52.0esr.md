# ESR: Firefox 52.0esr

### Started: 2017-02-27

## Build 1

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/xCgWXiNNTn28rKu4QKzJBw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [ ] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1343104](https://bugzil.la/1343104) - Add mozilla-esr52 to tc-vcs caches
- [Bug 1343130](https://bugzil.la/1343130) - Enable partner repacks builder on mozilla-esr52
- update verify tasks expected to fail
- need build2 for the partner repack that is failing

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/-1hg14WTSJaAE5Y2hhulig)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [ ] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1343107](https://bugzil.la/1343107) - docker image generating tasks failing bc tc-vcs hg version is old and we don't generate tarballs for esr52 yet

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### ESR Graph 1
task graph url: unknown

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [ ] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1343107](https://bugzil.la/1343107#c20): docker images don't live under the same directory whether you're on jamun or on esr52

:bomb: _aborted release. starting new build num_ :bomb:

## Build 4

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/05P3BelnQ96DyvinOdiOaQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/Edaw4v_5TcyHadEkwvU5fw)

#### Status
- [x] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- none


