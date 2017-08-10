# Release: Firefox 55.0.1

### Started: 2017-08-09

## Build 1

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/NpIkZT7FRzyHCmp9xwI9gA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- none

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/LnnWg8vlRcSDql4q2agPdg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- nthomas: bld-lion-r5-002 was having hg-shared issues; sshed in and nuked the specific empty 7ae7fb134bf7aec6ec96a062ff47a69053dd2973/ dir
- asasaki: [Bug 1389239](https://bugzil.la/1389239) - linux+mac cdntests are pointing at tinderbox-builds; we need to help them point at the new location(s) post-tc-migration
- nthomas: We didn't set up release-cdntest with the WNP page, or the rule for <55 to get 54.0.1, which invalidated QEs testing
- nthomas: We set up scheduled changes for the special update handlig before resolving the human decision task
- nthomas: [Bug 1389312](https://bugzil.la/1389312) - publish balrog job fails because it's not submitting a scheduled change. Blocks only the email to r-d about the release channel, which was done manually


