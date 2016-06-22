# Beta: Firefox 48.0b1

### Started: 16-06-07

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#yV_QtEsZTzKOv8H8GLR8aQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [ ] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [ ] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- Bug 1278721 - source builder is broken since 48.0b1. May require build2
- many cases of Bug 1276110 - intermittent download failures from cloud-mirror.taskcluster.net
- Many retries due to ISE 500 from hg.m.o

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#-mrfxV7bSZCR8SxGiwLlDQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- many cases of Bug 1276110 - intermittent download failures from cloud-mirror.taskcluster.net


