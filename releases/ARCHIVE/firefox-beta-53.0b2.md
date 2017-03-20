# Beta: Firefox 53.0b2

### Started: 2017-03-13

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/awxtNzlXS5KNolDi-VqvKA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1347100](https://bugzil.la/1347100) - Update verification: FAIL: no partial update found for Firefox 53.0b2, ur locale
- Cancel and rerun every {win{32,64},macosx64} update verification job because BBB failed without reporting results


