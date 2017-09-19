# RC Release: Firefox 56.0

### Started: 2017-09-19

## Build 1

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
- SPECIAL REQUIREMENT: [Bug 1397950](https://bugzilla.mozilla.org/show_bug.cgi?id=1397950) - update tc_indexes for mozilla-release
- SPECIAL REQUIREMENT: [Bug 1388460](https://bugzilla.mozilla.org/show_bug.cgi?id=1388460) https://dxr.mozilla.org/build-central/source/tools/lib/python/kickoff/__init__.py#176
- SPECIAL REQUIREMENT: [Bug 1395697](https://bugzilla.mozilla.org/show_bug.cgi?id=1395697) Generate lzma and bz2 compressed mar files as a part of release automation. We should start generating them as a part of 56.0 RC1 build and the file name pattern is *.bz2.complete.mar.  There is no automation around balrog submission and update verification yet. We will need to modify the release blobs and the rules to make update verification work.  We still need to update the docs (probably while we build 56) to reflect these changes.
- nthomas: Bouncer submission failed due to a typo in patch from [Bug 1395697](https://bugzil.la/1395697). rail fixed and landed, then cloned the failing task and updated to the new rev (no dependencies to worry about). Will have problems with uptake monitoring and boucner aliases. Expected workarounds - uptake: clone to run task, rerun original task and mark completed quickly enough that the bbb doesn't pick it up; aliases: clone. Goes away if we do a build2
