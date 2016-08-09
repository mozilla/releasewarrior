# ESR: Firefox 45.3.0esr

### Started: 2016-07-08

## Build 1

### ESR Graph 1
[task graph](https://tools.taskcluster.net/task-group-inspector/#Ir4HsJdnSpS-FCPrudV4ww)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
[task graph](https://tools.taskcluster.net/task-group-inspector/#WoBVryWKQo6D7_LxZFzRDg)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [set-up Windows watershed update](https://bugzilla.mozilla.org/show_bug.cgi?id=1284904)
- Hit [Bug 1291330](https://bugzil.la/1291330) during balrog submission, pointed the rule at 45.3 manually.


