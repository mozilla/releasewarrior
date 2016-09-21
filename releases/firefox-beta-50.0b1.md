# Beta: Firefox 50.0b1

### Started: 2016-09-21

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/WHMAKZHxTL-_jocq0fN92g)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Release-runner error due to buildbot vs TC build on linux64 [bug 1304260](https://bugzilla.mozilla.org/show_bug.cgi?id=1304260). Reran linux64 on buildbot to update index, then started in ship-it
- source generation task failed because it's using the old gecko hierarchy [bug 1304333](https://bugzilla.mozilla.org/show_bug.cgi?id=1304333).


