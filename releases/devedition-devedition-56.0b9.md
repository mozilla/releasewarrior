# Beta: Devedition 56.0b9

### Started: 2017-09-04

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/RGbLbIaeRLyWPRjfDb21FQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- kmoir: Special rules to implement on aurora-cdntest and aurora: [Bug 1393447](https://bugzilla.mozilla.org/show_bug.cgi?id=1393447) - [Bug 1393447](https://bugzil.la/1393447) - implement watershed balrog rule for b7 to update 32 bit windows firefox users if 64 bit if their underlying os is 64 bit
- jlorenzo: [Bug 1391102](https://bugzil.la/1391102) - No workers launched for end of release automation jobs
- jlorenzo: We had to add another watershed to make sure clients are sending the mig parameter https://aus4-admin.mozilla.org/rules/651


