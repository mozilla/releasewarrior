# ESR: Firefox 45.5.0esr

### Started: 2016-11-01

## Build 1

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/ysRRt9SJTTKC2DgZSv7xXg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/DqYY4ZhISemFwl521q1I4w)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1310690](https://bugzil.la/1310690): some update verify tests failed because the corresponding from releases have been removed from the candidates directory. As a posible solution we can remove those versions from the patcher config.


