# RC Release: Firefox 57.0

### Started: 2017-11-06

## Build 1
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/C4u-oWlDRqSU3QIYaIFv6Q)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [x] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: Verify that the release patch identified in [Bug 1397721](https://bugzilla.mozilla.org/show_bug.cgi?id=1397721#c17) has landed and reconfigured.
- POTENTIAL ISSUE: Cross-Channel L10n new in this release, should use l10n-central repo. See [Bug 1397721](https://bugzil.la/1397721)
- SPECIAL REQUIREMENT: Block updates for users with old JAWS software using the 'JAWS Screen Reader Compatibility' boolean on Balrog rules. See bugs 1402376, 1402411
- nthomas: win32 EME repacks (LH5h1BHURBuFZuQ87yt4kg) had a '3600 seconds without output' hang, rerun
- nthomas: release update verify 4,5,6,7,8/12 failed due to expecting 56.0 to be offered 57.0 instead of 56.0.2. We need to set up release-localtest.
- callek: update verify possibly fixable by [Bug 1415557](https://bugzil.la/1415557) now that rules are setup.
- callek: [Bug 1415276](https://bugzil.la/1415276) - Unable to publish to beta channel: KeyError: 'bz2_blob_suffix'
- callek: Due to [Bug 1415276](https://bugzil.la/1415276) manually inspected that the rc was published to balrog.
- bhearsum: Backed out [Bug 1415172](https://bugzil.la/1415172) because chunked update verify doesn't support multiple 'to' versions in the same config
- bhearsum: Another round of fixes in [Bug 1415557](https://bugzil.la/1415557) to work around issues with SYSTEM_CAPABILITIES and update verify
- jlorenzo: From now on, you can use this script to generate win64 blob (completes only) https://hg.mozilla.org/build/braindump/file/1cbcb486015e/releases-related/create_win64_migration_blob.py
## Build 2
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/GOcOYRZQRqqtMKq09A-1sg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [publish in Balrog on Beta channel](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: 55.0.3 partial left out of ship-it, fix that in build3
## Build 3
:bomb: _aborted release. starting new build num_ :bomb:

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/RZgN6UbnR_SQ5wjBVvqMNw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
task graph url: unknown

#### Status
- [x] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: funsize-update-generator docker image (ZhhoQjUdSauGrCMc2QEMNA) hit a hang while installing packages, reran
- nthomas: See [1413645#c4](https://bugzilla.mozilla.org/show_bug.cgi?id=1413645#c4) for generation of releases for Balrog. Updated release-localtest and release-cdntest channels to point to build3 releases
- jlund: nick reapplied  https://hg.mozilla.org/build/tools/pushloghtml\?fromchange\=085f6a772dad\&tochange\=59f08d95025a patcher patches that ben did
- jlund: reran all failed UV tasks via aki's braindump tc-filter.py
## Build 4

### RC graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/MdIY9Q9oTBSGeGb3aZD-Hg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### RC graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/O29EnOTETYysld8mHpQ0VQ)

#### Status
- [x] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff2 in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- none
