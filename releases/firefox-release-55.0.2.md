# Release: Firefox 55.0.2

### Started: 2017-08-16

## Build 1

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/PRcnpRuGTn6R2WsoqZzQOw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Got 503 errors from task scheduler API but the graph was still submitted and is running. Cleaned up ship-it db state and emailled r-d
- nthomas: Updated Balrog rule id 627 mapping from Firefox-55.0.1-build2-whatsnew to Firefox-55.0.2-build1. Will need to set it to Firefox-55.0.2-build1-whatsnew once that exists
- nthomas: Updates - expecting that RelMan will ask for all 55.0 and 55.0.1 users to get 55.0.2 with no what's new page; that for 54.0.1 and older some percentage of background requests will get 55.0.2 with what's new page (otherwise 54.0.1), while all manual requests should get 55.0.2 with what's new ([Bug 1389560](https://bugzil.la/1389560)). Set up release-localtest and release-cdntest to do that (rule id's 628+56 627+585) with 20% guess for background requests; that'll make QE testing hard. Added a scheduled change for release channel (change id 232).
- nthomas: Updates - [Bug 1389312](https://bugzil.la/1389312) will result in no scheduled change for the main release rule (id 145). We'll manually have to add one pointing to Firefox-55.0.2-build1, and email r-d when the change is signed off and actioned.


