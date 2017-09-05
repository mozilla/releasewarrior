# Beta: Firefox 50.0b3

### Started: 2016-09-29

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/qpqnDhgGRcijJb1LzqdF4A)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- multilocale Firefox snaps builder fails in fetching ubuntu archives - [Bug 1305651](https://bugzil.la/1305651). Forgot to deploy the fix from last week. 
- All Mac os X update verify fail due to sha512 inconsistencies. Filed [Bug 1306606](https://bugzil.la/1306606) to track with CloudOps. Clearing the cloudfront cache fixed it. Tctalker rerun the 11 updates


