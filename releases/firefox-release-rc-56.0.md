# RC Release: Firefox 56.0

### Started: 2017-09-19

## Build 1
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/aUpBDSw5S2etpFHqxKSCYA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: [Bug 1397950](https://bugzilla.mozilla.org/show_bug.cgi?id=1397950) - update tc_indexes for mozilla-release. DONE
- SPECIAL REQUIREMENT: [Bug 1388460](https://bugzilla.mozilla.org/show_bug.cgi?id=1388460) https://dxr.mozilla.org/build-central/source/tools/lib/python/kickoff/__init__.py#176. DONE
- SPECIAL REQUIREMENT: [Bug 1395697](https://bugzilla.mozilla.org/show_bug.cgi?id=1395697) Generate lzma and bz2 compressed mar files as a part of release automation. We should start generating them as a part of 56.0 RC1 build and the file name pattern is *.bz2.complete.mar.  There is no automation around balrog submission and update verification yet. We will need to modify the release blobs and the rules to make update verification work.  We still need to update the docs (probably while we build 56) to reflect these changes.
- nthomas: Bouncer submission failed due to a typo in patch from [Bug 1395697](https://bugzil.la/1395697). rail fixed and landed, then cloned the failing task and updated to the new rev ([new task](https://tools.taskcluster.net/groups/Co8iBgS1RnKVNOWMZm0TUg/tasks/Co8iBgS1RnKVNOWMZm0TUg/details), no dependencies to worry about). Will have problems with uptake monitoring and boucner aliases. Expected workarounds - uptake: clone to run task, rerun original task and mark completed quickly enough that the bbb doesn't pick it up; aliases: clone. Goes away if we do a build2
- catlee: [Bug 1400141](https://bugzil.la/1400141) - balrog submission errors, reran failing tasks
- jlorenzo: [Bug 1395697](https://bugzil.la/1395697): Partial updates remained LZMA-compressed (instead of BZ2). Per catlee's suggestion, I removed the partial entries in the BZ2 release blob and reran the Update Verify jobs
- jlorenzo: [Bug 1395697](https://bugzil.la/1395697) - Update Verify jobs were still expecting partial updates. I changed the update configuration
- jlorenzo: [Bug 1395697](https://bugzil.la/1395697): I inadvertently removed some macOS locales from the blob. I reintroduced them and reran all Update Verify jobs
- jlorenzo: [Bug 1395697](https://bugzil.la/1395697): ta/linux64's mar got the wrong size and hash. I manually changed them as they were manually uploaded
- jlorenzo: Discovered [Bug 1401176](https://bugzil.la/1401176) - extract_and_run_command.py: ImportError: No module named mar
## Build 2
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/NTaoGTWTSHK66IqQSEQHMQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: [Bug 1395697](https://bugzilla.mozilla.org/show_bug.cgi?id=1395697) Generate lzma and bz2 compressed mar files as a part of release automation. We should start generating them as a part of 56.0 RC1 build and the file name pattern is *.bz2.complete.mar.  There is no automation around balrog submission and update verification yet. We will need to modify the release blobs and the rules to make update verification work, then resolve the 'firefox mozilla-release starte update verification human decision task' to start u.v.  We still need to update the docs (probably while we build 56) to reflect these changes. See ../how-tos/56.0rc-blobs.md for more details
- kmoir: typo in new signing format in releasetasks https://github.com/mozilla-releng/releasetasks/commit/d3182e13010df839d1c43ef8938473e44cf9ad15
## Build 3
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/CzFC014nSjONKlqJFELJfQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: [Bug 1395697](https://bugzilla.mozilla.org/show_bug.cgi?id=1395697) Generate lzma and bz2 compressed mar files as a part of release automation. We should start generating them as a part of 56.0 RC1 build and the file name pattern is *.bz2.complete.mar.  There is no automation around balrog submission and update verification yet. We will need to modify the release blobs and the rules to make update verification work, then resolve the 'firefox mozilla-release starte update verification human decision task' to start u.v.  We still need to update the docs (probably while we build 56) to reflect these changes. See ../how-tos/56.0rc-blobs.md for more details
- jlorenzo: Submitted BZ2+WNP blob. Started update verify tests.
## Build 4
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/F96MXdLjQ82P9NpbuHE4qg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: [Bug 1395697](https://bugzilla.mozilla.org/show_bug.cgi?id=1395697) Generate lzma and bz2 compressed mar files as a part of release automation. We should start generating them as a part of 56.0 RC1 build and the file name pattern is *.bz2.complete.mar.  There is no automation around balrog submission and update verification yet. We will need to modify the release blobs and the rules to make update verification work, then resolve the 'firefox mozilla-release starte update verification human decision task' to start u.v.  We still need to update the docs (probably while we build 56) to reflect these changes. See ../how-tos/56.0rc-blobs.md for more details - DONE
- kmoir: Publish to Balrog win64 chunk 7 for 56.0b12 failed, reran task
- kmoir: update tests for 56.0-build4 are failing https://bugzilla.mozilla.org/show_bug.cgi?id=1402656 - FIXED
## Build 5
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/BnnrBOusTpC6ZnoupBx2gA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: [Bug 1395697](https://bugzilla.mozilla.org/show_bug.cgi?id=1395697) Generate lzma and bz2 compressed mar files as a part of release automation. See ../how-tos/56.0rc-blobs.md for more details of manual work. Set beta-{local,cdn}test back to Firefox-56.0-build5 because 57.0b3 raced us; updated docs with improved script. Resolved decision task, u.v. jobs were green, set beta-{cdn,local}test back to 57.0b3 build1. DONE
## Build 6

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/GEH2MToBRfmfAaiXUe1fkQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/Sz5Y0bkTShWCPSftqmZ1XQ)

#### Status
- [x] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: [Bug 1395697](https://bugzil.la/1395697) Generate lzma and bz2 compressed mar files as a part of release automation. See ../how-tos/56.0rc-blobs.md for more details of manual work. DONE (nthomas)
- nthomas: Reran a publish to balrog task for 'balrogVPNProxy : Gateway Timeout'
- nthomas: Had to rerun the push_to_releases job a couple of times because of TC docker bustage
- kmoir: todo: signoff on balrog rule to update rate to 25% at 2pm PT
- POST-RELEASE-ISSUES:
- We had an issue with WNP for certain locales. Rail wrote up the steps https://gist.github.com/rail/4b4eb492bce3443b6e75f9545aab7a1b. We had to add two rules because the locale field in balrog was too long for the list of locales with this problem.  Balrog rules 652 and 653 were added for this condition.
- https://bugzil.la/1387622 Add latest-ssl aliases for bedrock to use
