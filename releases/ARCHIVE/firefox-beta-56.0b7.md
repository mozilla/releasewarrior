# Beta: Firefox 56.0b7

### Started: 2017-08-25

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/hHor_Dn5SDW4gMZliPME2Q)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- kmoir: todo [Bug 1393447](https://bugzil.la/1393447) - implement watershed balrog rule for b7 to update 32 bit windows firefox users if 64 bit if their underlying os is 64 bit
- asasaki: [Bug 1393639](https://bugzil.la/1393639) - widevine indexes delayed starting b7
- asasaki: had to rerun docker image tasks manually
- asasaki: [Bug 1393639](https://bugzil.la/1393639) - linux shouldn't have repackage indexes specified. build2!

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/xzIcLIHqSL2rEcHsUf9j9Q)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- kmoir: [Bug 1394644](https://bugzil.la/1394644) - Missing release notifications for Firefox 56.0b7
- asasaki: firefox mozilla-beta win32 l10n repack 10 of 10 1800 second no output timeout - reran
- nthomas: [Bug 1394664](https://bugzil.la/1394664) - snap generation failing with a taskclusterProxy link problem
- nthomas: [Bug 1393705](https://bugzil.la/1393705) - binary transparency job no longer has netflow it needs, non blocking
- nthomas: Reran two linux update verify jobs for failures to clone tools
- nthomas: [Bug 1393447](https://bugzil.la/1393447) - implement watershed balrog rule for b7 to update 32 bit windows firefox users to 64 bit if their underlying os is 64 bit
- jlorenzo: Worked around by submitting tasks manually, [Bug 1395128](https://bugzil.la/1395128) - schedule publishing in balrog fails: Changes may not be scheduled in the past
- jlorenzo: Manually cancelled duplicated tasks
- NOT SHIPPED


