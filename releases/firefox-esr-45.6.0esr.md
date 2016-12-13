# ESR: Firefox 45.6.0esr

### Started: 2016-12-09

## Build 1

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/gdFPlloqRUu15Dl9rR2xsg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [x] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- we forgot to bump in-tree version because there was no actual migration automation
- we exceeded release-runner maximum ship-it time without passing sanity. rail had to delete from ship-it and resubmit


