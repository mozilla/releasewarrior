# Beta: Firefox 52.0b5

### Started: 2017-02-09

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/3nzYBIAmSI2VmQuA9up-lQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Three partner repacks 'running' for a long time - macosx64 EME-free repacks, macosx64 partner repacks, win64 EME-free repacks. Actually green in buildbot but not reflected back to TC. jonasf1 commented on irc 'looked a queue timeouts, looks like a pulse disconnect, crash and restart'. Cancel and rerun so we get logs to go with our bits


