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
- Many failures of Bug 1276110 (issue with wget relating to cloud-mirror. One repack task failed >12 times...
- Buildbot bridge failing to properly update status on some reruns, traceback indicating scope issue, #taskcluster talk exposed that we never claimed the rerun before trying to reclaim it
- Encrypted environment vars used for beetmover expire after only 24 hours, while the task deadline is 4 days. TODO: File bug (and patch) to update the env expirey to match that of the task. Necessitates build2


