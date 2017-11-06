# RC Release: Firefox 57.0

### Started: 2017-11-06

## Build 1

### RC graph 1
task graph url: unknown

#### Status
- [ ] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
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
- SPECIAL REQUIREMENT: Verify that the release patch identified in [Bug 1397721](https://bugzilla.mozilla.org/show_bug.cgi?id=1397721#c17) has landed and reconfigured.
- POTENTIAL ISSUE: Cross-Channel L10n new in this release, should use l10n-central repo. See [Bug 1397721](https://bugzil.la/1397721)
- SPECIAL REQUIREMENT: Block updates for users with old JAWS software using the 'JAWS Screen Reader Compatibility' boolean on Balrog rules. See bugs 1402376, 1402411
