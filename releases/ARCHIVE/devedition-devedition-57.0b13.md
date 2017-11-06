# Beta: Devedition 57.0b13

### Started: 2017-10-30

## Build 1

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/Z6Mm0ryySGGaDCmswoUIKA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- jlorenzo: https://tools.taskcluster.net/groups/Z6Mm0ryySGGaDCmswoUIKA/tasks/SMGhnnDVQxK_UdBgwyJY6w/runs/0/logs/public%2Flogs%2Flive_backing.log.gz failed because no release_eta was set in ship-it. I manually created U0wFN1-3SbKeR2IvELVnpw and manually resolved the original one. I5o0elGPSs2WdTkEHT35mQ is a casualty: we shouldn't introduce 'release_eta' in task.payload.properties anymore, but 'schedule_at', instead
- jlorenzo: UV test f5UXs_B1SUO82IpmVXckTw has been running for 11+ hours. I suspect somthing went wrong in BBB. I reran the task, but after we shipped that release.
