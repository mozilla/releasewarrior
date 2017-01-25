# Beta: Firefox 52.0b1

### Started: 2017-01-24

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Tr2OXLVyS5-kS58hKnMZDw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Same Ship-it issue as 51.0-build2. Known [Bug 1269627](https://bugzil.la/1269627) of tc scheduler returning 503. Rail tweaked the database <update firefox_release set status='Started', ready=1, complete=1 where name='Firefox-52.0b1-build1'>
- busted due to migration bug in macosx builds [Bug 1333443](https://bugzil.la/1333443)

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/WNGYY6nMTliD_CcUCV_Uag)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- none


