# Release: Firefox 55.0.2

### Started: 2017-08-16

## Build 1

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/PRcnpRuGTn6R2WsoqZzQOw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Got 503 errors from task scheduler API but the graph was still submitted and is running. Cleaned up ship-it db state and emailled r-d
- nthomas: Updated Balrog rule id 627 mapping from Firefox-55.0.1-build2-whatsnew to Firefox-55.0.2-build1. Will need to set it to Firefox-55.0.2-build1-whatsnew once that exists


