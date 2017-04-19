# ESR: Firefox 52.0.2esr

### Started: 2017-03-24

## Build 1

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/UN4gvLPIT4GDoaixLoYeIQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [x] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1350285](https://bugzil.la/1350285) - Cannot robust checkout https://hg.mozilla.org/releases/l10n/mozilla-release/nb-NO : HTTP Error 413: Request Entity Too Large
- push_to_mirrors and publish_release tasks expired. Recreated them manually under the same graph
- [Bug 1351264](https://bugzil.la/1351264) - [bbb] {release,esr} uptake monitoring jobs are going backwards in the waiting line


