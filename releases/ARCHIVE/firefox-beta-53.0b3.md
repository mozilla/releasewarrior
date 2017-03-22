# Beta: Firefox 53.0b3

### Started: 2017-03-16

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/cX7gaRHARguLeGDAev_bkQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)
- [x] Update "Firefoxsignoff" rule in Balrog

### Issues
- snap failed, probably [Bug 1346246](https://bugzil.la/1346246)
- [Bug 1347100](https://bugzil.la/1347100) - Update verification: FAIL: no partial update found for Firefox 53.0b3, ur locale
- Cancelled release, because 53.0b4 came on the same day (which is sec driven). Task group cX7gaRHARguLeGDAev_bkQ has been cancelled and ship-it manually updated.
- we should clean up the releases dir for 53.0b3


