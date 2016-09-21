# RC Release: Firefox 49.0

### Started: 2016-09-05

## Build 1

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/1B4SgShvQ9S28KmwLXzfAw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [block non-SSE2 Windows updates](https://bugzilla.mozilla.org/show_bug.cgi?id=1284905)
- SPECIAL REQUIREMENT: [add OS X 10.6-10.8 deprecation rule before 49.0 ships to release](https://bugzilla.mozilla.org/show_bug.cgi?id=1275607)
- SPECIAL REQUIREMENT: [Set up a Whats New Page for zh-TW](https://bugzilla.mozilla.org/show_bug.cgi?id=1292637)
- Releaserunner failed, because revision did not pass release sanity (pointing to a revision before merge)

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/5tbXkRj7SWSbIzC34MDq2g)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [block non-SSE2 Windows updates](https://bugzilla.mozilla.org/show_bug.cgi?id=1284905)
- SPECIAL REQUIREMENT: [add OS X 10.6-10.8 deprecation rule before 49.0 ships to release](https://bugzilla.mozilla.org/show_bug.cgi?id=1275607)
- SPECIAL REQUIREMENT: [Set up a Whats New Page for zh-TW](https://bugzilla.mozilla.org/show_bug.cgi?id=1292637)

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/2iujXxRoSfm4pqL5KLcDiQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [block non-SSE2 Windows updates](https://bugzilla.mozilla.org/show_bug.cgi?id=1284905)
- SPECIAL REQUIREMENT: [add OS X 10.6-10.8 deprecation rule before 49.0 ships to release](https://bugzilla.mozilla.org/show_bug.cgi?id=1275607)
- SPECIAL REQUIREMENT: [Set up a Whats New Page for zh-TW](https://bugzilla.mozilla.org/show_bug.cgi?id=1292637)

:bomb: _aborted release. starting new build num_ :bomb:

## Build 4

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/Ekz_uUjtTCKUtkpEQjrqWA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/AczN0wbeSqCg0e7ck-VYdQ)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- Isntead of pushing build4 we pushed build1 to the releases directory. Cancelled tasks in P4-Eyi_zTO-0UyjXLFnbUg
- [Bug 1303909](https://bugzil.la/1303909) - Filed bug to delete files from the releases directory and purge the caches


