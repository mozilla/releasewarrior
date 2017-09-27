# Beta: Devedition 57.0b2

### Started: 2017-09-21

## Build 1

### Beta Graph
:bomb: _aborted release. starting new build num_ :bomb:

[task group](https://tools.taskcluster.net/push-inspector/#/HxbIQ2f1QiOPP0YwuGoD-Q)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: https://bugzilla.mozilla.org/show_bug.cgi?id=1400265 Make sure that Firefox 57 b1 and b2 DevEdition are background updates only, NO downloads. Cancel bouncer aliases and mark as shipped tasks after graph submission, and before resovling human decision task - DONE
- POTENTIAL BREAKAGE: Source building was re-enabled ([Bug 1400157](https://bugzil.la/1400157)). If broken, deactivation will require a respin (see comment 4).
- kmoir: [Bug 1402084](https://bugzil.la/1402084) - had to bump browser/config/version_display.txt manually for devedition 57.0b2
- kmoir: TODO: manually bump display_version.txt on beta if https://bugzilla.mozilla.org/show_bug.cgi?id=1346465 hasn't been fixed after we ship b2
- kmoir: POTENTIAL BREAKAGE: Source building was re-enabled ([Bug 1400157](https://bugzil.la/1400157)). If broken, deactivation will require a respin (see comment 4).
- kmoir: typo in new signing format in releasetasks https://github.com/mozilla-releng/releasetasks/commit/d3182e13010df839d1c43ef8938473e44cf9ad15
## Build 2

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/dY__Gv3pTt2XPK2TgKSRpA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: https://bugzilla.mozilla.org/show_bug.cgi?id=1400265 Make sure that Firefox 57 b1 and b2 DevEdition are background updates only, NO downloads. Cancel bouncer aliases and mark as shipped tasks after     graph submission, and before resovling human decision task - DONE
- POTENTIAL BREAKAGE: Source building was re-enabled ([Bug 1400157](https://bugzil.la/1400157)). If broken, deactivation will require a respin (see comment 4).
- kmoir: TODO: manually bump display_version.txt on beta if https://bugzilla.mozilla.org/show_bug.cgi?id=1346465 hasn't been fixed after we ship b2 - done by RyanVM, also he tagged for b1 and b2
- kmoir: POTENTIAL BREAKAGE: Source building was re-enabled ([Bug 1400157](https://bugzil.la/1400157)). If broken, deactivation will require a respin (see comment 4).
