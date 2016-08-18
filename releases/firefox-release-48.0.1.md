# Release: Firefox 48.0.1

### Started: 2016-08-17

## Build 1

### Release Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#7ojqiqQaQ_2eSpyILLAojA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: Update balrog rule ID 375 and rule ID 374 to update to latest for SSE and OSX-Deprecation releases

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Release Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#0xJtsX1MTvmGr8VTi6ZvPg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- Scheduling problems, eg [task an7rmcZUSaSiwHmAxJcS6A](https://tools.taskcluster.net/task-inspector/#an7rmcZUSaSiwHmAxJcS6A/). Also exceptions on OxA9SOnRS8C3QidKsNo7ZQ and RezQdKkFQ-mAm2qeo5RocA

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### Release Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#nLz7ce1UR72-2TSLvOn1XQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: Update balrog rule ID 375 and rule ID 374 to update to latest for SSE and OSX-Deprecation releases
- Task https://tools.taskcluster.net/task-inspector/#LOwmt_lOSSK8j2iJX1VPAA/ failed a few times with pushing partner repacks due to content mismatches. Sha1, Emefree, etc.


