# Beta: Devedition 56.0b5

### Started: 2017-08-21

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/95j2a8uPTBiiONz14uXYTQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- kmoir: [Bug 1392703](https://bugzil.la/1392703) - firefox mozilla-beta schedule publishing in balrog fails if human decision task was resolved after the release eta
- kmoir: had to rerun email release-drivers task as it was not scheduled because balrog task failed
- kmoir: had to fix balrog release to point to aurora rule manually because job failed (rule 10) 


