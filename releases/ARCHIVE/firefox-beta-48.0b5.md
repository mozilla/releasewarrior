# Beta: Firefox 48.0b5

### Started: 16-07-01

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#YXKVDa6mQg-BRxl82Os7Hw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- 9BfL484uSuCjRGDsAhR2lw - win32 l10n repack 10/10 - need rerun after upload hang - [bug 1284253](https://bugzilla.mozilla.org/show_bug.cgi?id=1284253)
- R4EizagoQsGROPpTD1nr-Q - win32 l10n repack 8/10 - stray cancel of job via self-serve. rerun. This may have been incorrect, as Run 1 failed in tc-upload with 'TaskclusterRestFailure: Run 0 was already claimed by another worker.'. Lets see what Run 2 does ...
- _UU5dNjxTFeH8qpTmfJjtQ - win64 l10n repack 8/10 - looks done in buildbot (http://bit.ly/296Ha7O), marked complete with tctalker
- [Bug 1283853](https://bugzil.la/1283853) - Update Monitoring failed, even a re-run just now. Though enough time has passed that I just marked it as complete
- R4EizagoQsGROPpTD1nr-Q - actually "failed" in TC, but artifact task has the artifacts stored so all-is-well. Need to rerun and then report_completed so that things move on
- More BBB fun - 7 out of 12 total mac repacks failed due to 'claim-expired' and caused a TC-based rerun that bbb ignored. Verified all successful in buildbot and marked as completed


