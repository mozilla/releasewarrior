# Beta: Firefox 56.0b12

### Started: 2017-09-14

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/R0ES6YjPQt-rzimWCAHeRQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- jlorenzo: One balrog submission task failed: Timeout to connect to balrogVpnProxy. Reran task. It passed
- jlorenzo: A dozen balrog submission tasks failed because Balrog returned 400: 'Failed to update row, old_data_version doesn't match current data_version'. Reran all tasks and they passed.
- jlorenzo: Because of issues above, cdntest email went out before Balrog got all mar info uploaded.
- jlorenzo: Failed to schedule publishing in balrog, because ETA was set in the past. I created a cloned task via task-creator with an updated ETA
- jlorenzo: As a consequence of the ETA being updated, I recreated the email r-d task to pick the right dependency and to reflect to new ETA
- jlorenzo: Cancelled version bump because 57.0 was already on mozilla-beta
- jlorenzo: Manually pushed the tags FIREFOX_56_0b12_BUILD1 FIREFOX_56_0b12_RELEASE, because they were part of the version bump


