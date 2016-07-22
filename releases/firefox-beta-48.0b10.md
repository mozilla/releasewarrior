# Beta: Firefox 48.0b10

### Started: 16-07-22

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#Hk5AgWWfRLOLq0yd6gHa4w)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [ ] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [ ] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- _grW4FvaRm-r-UADHEyz-g - win64 repack hit a hang in configure and ended up in exception state, reran after verifying buildbot did not retry
- Lots of slow windows repacks hitting the 2 hour job limit, bumped to 3 hours in bug 1288679


