# Thunderbird 49.0b1

### Started 2016-08-05

## Build 1

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- Release Runner Sanity failures due to mozconfig differences, initially reran on theory of race condition with push/merge. Code backed out and new build 1 submitted
- 1 linux64 repack failure due to usual mock install failure
- win32 en-US failure in unified build ([Bug 1293401](https://bugzil.la/1293401)). Got past that in a rebuild but timeout diffing xul.dll in partial generation.
- mac repacks all failing because clang from tooltool not found by configure, see [Bug 1286440](https://bugzil.la/1286440)

:bomb: _**aborted release. starting new build num**_ :bomb:

## Build 2

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- win32 en-US - timeout generating partial update again, [Bug 1296449](https://bugzilla.mozilla.org/show_bug.cgi?id=1296449)
- mac repacks have a new bustage for l10n-base, patch up on [bug 1286440](https://bugzilla.mozilla.org/show_bug.cgi?id=1286440)

:bomb: _**aborted release. starting new build num**_ :bomb:

## Build 3

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- Mac repacks busted with 'No such file or directory: 'comm-beta/obj-l10n/config'' in make export, handled in [Bug 1286640](https://bugzilla.mozilla.org/show_bug.cgi?id=1286440) again
- Win32 en-US build still broken, the problem turns out to be that mbsdiff.exe can't find a MS runtime dll, make it a static binary in ([Bug 1296449](https://bugzil.la/1296449))[https://bugzilla.mozilla.org/show_bug.cgi?id=1296449]

:bomb: _**aborted release. starting new build num**_ :bomb:

## Build 4

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- Mac repacks still busted with 'No such file or directory: 'comm-beta/obj-l10n/config'' in make export, handled in [Bug 1286640](https://bugzilla.mozilla.org/show_bug.cgi?id=1286440) again
- Win32 repacks broken running tooltool [Bug 1297785](https://bugzilla.mozilla.org/show_bug.cgi?id=1297785)

:bomb: _**aborted release. starting new build num**_ :bomb:

## Build 5

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- none


