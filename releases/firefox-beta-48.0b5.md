# Beta: Firefox 48.0b5

### Started: 16-07-01

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#YXKVDa6mQg-BRxl82Os7Hw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [ ] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [ ] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- 9BfL484uSuCjRGDsAhR2lw - win32 l10n repack 10/10 - need rerun after upload hang
- R4EizagoQsGROPpTD1nr-Q - win32 l10n repack 8/10 - stray cancel of job via self-serve. rerun. This may have been incorrect, as Run 1 failed in tc-upload with 'TaskclusterRestFailure: Run 0 was already claimed by another worker.'. Lets see what Run 2 does ...
- _UU5dNjxTFeH8qpTmfJjtQ - win64 l10n repack 8/10 - looks done in buildbot (http://bit.ly/296Ha7O), marked complete with tctalker


