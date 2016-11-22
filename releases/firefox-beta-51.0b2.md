# Beta: Firefox 51.0b2

### Started: 2016-11-21

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Iwah-Q69QBemv4GtPaqChQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- 'firefox mozilla-beta checksums builder', exception. possibly completed too quick for bbb, solution: tctalker rerun+report_completed to resolve since bbot reported that it did run green
- [Bug 1271614](https://bugzil.la/1271614): 'ka' and 'kab' locales are failing to provide partial updates. see beta-cdntest release-drivers email for details. I recommended that we ignore those failures as these are new locales that do not have completes in all versions within partial list. I've left the failing update-verify and final verify jobs as failed. Maybe they should stay red for history sake and skip right to completing the publish human decision task when requested


