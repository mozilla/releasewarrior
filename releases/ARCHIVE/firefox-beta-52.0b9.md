# Beta: Firefox 52.0b9

### Started: 2017-02-24

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Dqf8WGvBQGq_-iHo0fzn4g)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Beetmover broken due to typo, rail fixed in [Bug 1338232](https://bugzil.la/1338232). Graph cancelled to do a build2

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/BCtzrKEUR9y6QeQ-0ftmRw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Snap build failed because of an update of desktop-gtk3 [Bug 1342362](https://bugzil.la/1342362)
- Manually resolved the uptake monitoring task to skip the sha1 blocking.


