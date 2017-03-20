# Release: Firefox 52.0.1

### Started: 2017-03-16

## Build 1

### Release Graph
task graph url: unknown

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- en-US beetmover failed because of a missing uplift of [Bug 1343524](https://bugzil.la/1343524). Build aborted

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/WiefBqJ8QDqcKlUfLULBaw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- After the uplift of [Bug 1343524](https://bugzil.la/1343524), release-runner was in an odd shape. It declared no "signed_task_id" which seems like a file in release runner was not updated. After some investigation, it might have been a .pyc that needed to be refreshed.
- Large lag in funsize signing workers -- Aki noticed that signingworker1 was running an m-c nightly when he checked. We need to up the size of the pool, pause/stagger other tasks, or deal w/ priority levels
- watch pending doesn't spin up instances for release tasks -- publish release was stuck waiting for instances


