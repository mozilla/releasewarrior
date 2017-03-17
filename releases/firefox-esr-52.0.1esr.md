# ESR: Firefox 52.0.1esr

### Started: 2017-03-16

## Build 1

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
- en-US beetmover failed because of a missing uplift of [Bug 1343524](https://bugzil.la/1343524). Build aborted

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/LASlfgpiQnyo8yHPgOASNw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [x] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- After the uplift of [Bug 1343524](https://bugzil.la/1343524), release-runner was in an odd shape. It declared no "signed_task_id" which seems like a file in release runner was not updated. After some investigation, it might have been a .pyc that needed to be refreshed.


