# Beta: Devedition 57.0b1

### Started: 2017-09-15

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Zi-rCIvSRUm7t-CFbAaUYw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: Verify that the patches identified for desktop in [Bug 1397721](https://bugzilla.mozilla.org/show_bug.cgi?id=1397721#c17) has landed and reconfigured. DONE!
- POTENTIAL ISSUE: Cross-Channel L10n new in this release, should use l10n-central repo. See [Bug 1397721](https://bugzil.la/1397721)
- SPECIAL REQUIREMENT: cancel bouncer aliases job after graph submission, to prevent 57.0b1 appearing as a download at end of release process. DONE!


