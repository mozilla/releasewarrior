# Beta: Firefox 56.0b12

### Started: 2017-09-14

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/R0ES6YjPQt-rzimWCAHeRQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- jlorenzo: One balrog submission task failed: Timeout to connect to balrogVpnProxy. Reran task. It passed
- jlorenzo: A dozen balrog submission tasks failed because Balrog returned 400: 'Failed to update row, old_data_version doesn't match current data_version'. Reran all tasks and they passed.
- jlorenzo: Because of issues above, cdntest email went out before Balrog got all mar info uploaded.


