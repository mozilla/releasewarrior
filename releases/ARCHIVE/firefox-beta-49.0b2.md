# Beta: Firefox 49.0b2

### Started: 2016-08-08

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#PAvWsUQhRRSpGm9CgLEXbA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- Taskgraph scheduling timed out and returned a 500 error to client. Remote ended up actually submitting all tasks. Filed [Bug 1293744](https://bugzil.la/1293744) for moar retry and delay
- [Bug 1293651](https://bugzil.la/1293651) filed to investigate OSX update verification issues. Turns out it was a missed part of [Bug 1275632](https://bugzil.la/1275632), and this was the first train to need the latter change
- [Bug 1293707](https://bugzil.la/1293707) discovered we had forgot/missed doing [Bug 1275605](https://bugzil.la/1275605) -- which ended up stranding OSX 10.6-10.8 users -- release version of this ([Bug 1275607](https://bugzil.la/1275607)) was fixed for 49.0 already (tracked on the 48.0 release)


