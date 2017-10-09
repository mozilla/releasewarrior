# Thunderbird 52.4.0

### Started 2017-10-03

## Build 1
:bomb: _aborted release. starting new build num_ :bomb:

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [pushed to mirrors/releases](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates#Push_to_mirrors)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: [Bug 1405177](https://bugzil.la/1405177): Needed to Install (slightly) newer pip to successfully install boto.
## Build 2
:bomb: _aborted release. starting new build num_ :bomb:

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [pushed to mirrors/releases](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates#Push_to_mirrors)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: An unrelated build/tools patch caused the release to fail (which landed on Oct 3), reran the jobs after the fix.
- callek: Repacks however used that broken tagged version of build/tools so aborted build in favor of a build 3
## Build 3

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [pushed to mirrors/releases](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates#Push_to_mirrors)
- [x] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: Publish Release How-To/Buildbot fails due to required signoffs. Had to enact the change manually.
