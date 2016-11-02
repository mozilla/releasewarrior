# Release: Firefox 47.0.2

### Started: 2016-10-27

## Build 1

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/sPaYGIZzQx6QVO4bjvS2zg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1313434](https://bugzil.la/1313434): Tracking bug, describing extra setup for this release
- rail cancelled publish release, final verify, publish release human task. publish release should be done manually. version bump and ship-it tasks can be triggered via tctalker directly in graph

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/lZ-KNICWRnWOC2_1K4Yu7Q)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- One of the win l10n repacks timed out cloning, retried, succeeded, but the BB log parsing logic decided to set the result to failure. All following reruns failed posting the artifacts, because the artifacts task was resolved in run 0. Cancelled the running task, reran and immidiatelly resolved it.


