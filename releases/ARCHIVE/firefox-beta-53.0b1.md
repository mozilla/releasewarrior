# Beta: Firefox 53.0b1

### Started: 2017-03-06

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/sxhGqktmSfCNG3t-P2Bn-g)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- PRIOR TO PUBLISH: [Bug 1318921](https://bugzil.la/1318921) - Migrate desktop Firefox Beta 52 on XP/2003/Vista to ESR 52
- PRIOR TO PUBLISH: [Bug 1319442](https://bugzil.la/1319442) - Stop advertising Firefox updates to 32-bit Linux clients with SSE on beta channel
- PRIOR TO PUBLISH: [Bug 1325583](https://bugzil.la/1325583) - Stop advertising Firefox updates to 32bit Mac clients on the beta channel
- had to remove "be" from locales list. appears to be removed but still expected. will file
- shipit thought taskcluster graph submission failed but it succeeded. nthomas updated db entry to ready=1 status=Started
- shipit release row also needed complete=1. because that wasn't manually updated, releaserunner kicked off a new graph. nick fixed the row, jlund deleted the first graph with tctalker cancel_graph
- Task t7eS84E9QaqQ5NtJ_UsInw ([funsize] MAR signing task win32 en-US for 52.0b8) got stuck in a running state but had actually hit an error 'TaskclusterRestFailure: Run 0 was already claimed by another worker'. Did a cancel and rerun using tctalker
- Task G0zFcrarR9yHSFyJ4OTyZw (firefox mozilla-beta macosx64 partner repacks) had completed but TC says still pending, used report_completed from tctalker
- [Bug 1346246](https://bugzil.la/1346246) - snap failed in Firefox 53.0b1
