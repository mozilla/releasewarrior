# Beta: Firefox 48.0b2

### Started: 16-06-20

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#mfMKKf2fReKZlh1TfFpgCA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [ ] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [ ] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- Trees closed due to windows disconnects excerbated diagnosis/resolution of following issues (Bug 1281199)
- Kim Marked that beta-cdntest was ready and it wasn't (e-mail was sent).
- Many failures of Bug 1276110 (issue with wget relating to cloud-mirror. One repack task failed >12 times...
  - Once learning that it only failed in us-east and not us-west we also had the issue that there was no windows builders available in us-west due to the pricing algorithm.
- Buildbot bridge failing to properly update status on some reruns, traceback indicating scope issue, #taskcluster talk exposed that we never claimed the rerun before trying to reclaim it
- Encrypted environment vars used for beetmover expire after only 24 hours, while the task deadline is 4 days. TODO: File bug (and patch) to update the env expirey to match that of the task. Necessitates build2

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#8asrO0S6RNus6Dn8FFsc8A)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- tc-vcs cache had failed for beta, causing the generate docker image jobs (x3) to fail, as well as the source builder to fail. Manually re-ran after #taskcluster cleared the issue to success.
- 'firefox mozilla-beta win32 l10n repack 1/10' (taskid: iTnbATexRZuKEw-w1XjFSA) actually finished since artifact upload task was ready, marked as such using tctalker
- Also for:
    - 'firefox mozilla-beta win64 l10n repack 8/10' (taskid: SNGVbgRvTMe2iCgD3GcYAw)
    - 'firefox mozilla-beta win32 l10n repack 9/10' (taskid: F3EZs9CaQx-NoYUoFhZ8aA)
- 'win32 beta update verification 8/12' (taskid: stPXNzF9R_Su-ittXiNqrA) actually finished just bbb didn't report that correctly to tc, marked as such using tctalker


