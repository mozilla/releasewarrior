# Thunderbird 57.0b1

### Started 2017-11-06

## Build 1
:bomb: _**aborted release. starting new build num**_ :bomb:

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT: Verify that the patches identified for thunderbird in [Bug 1397721](https://bugzilla.mozilla.org/show_bug.cgi?id=1397721#c17) has landed and reconfigured.
- POTENTIAL ISSUE: Cross-Channel L10n new in this release, should use l10n-central repo. See [Bug 1397721](https://bugzil.la/1397721)
- callek: [Bug 1414939](https://bugzil.la/1414939) - Filed because of failed release sanity for TB 57.0b1, this is because we didn't land the patch to enable l10n-central.
- nthomas: release-comm-beta-thunderbird_push_to_mirrors ran, but failed early and didn't have any effect. Probably the very rare scheduling strangeness we've never been able to pin down in buildbot releases
- callek: Hit a bunch of different l10n issues tracked in  [Bug 1415057](https://bugzil.la/1415057), [Bug 1415058](https://bugzil.la/1415058), [Bug 1415064](https://bugzil.la/1415064). Will require a build2
## Build 2

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Mac repacks not fixed, reopened [Bug 1415058](https://bugzil.la/1415058)
- callek: OSX repacks reran via self-serve after the buildbot fix deployed.
