# Beta: Devedition 56.0b7

### Started: 2017-08-28

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/oMIzVPOvSIeJ-POSXtmjPg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: [Bug 1394644](https://bugzil.la/1394644) - Missing release notifications for Firefox 56.0b7
- nthomas: [Bug 1394657](https://bugzil.la/1394657) - reran failing docker image generation. Accidentally reran the "devedition mozilla-beta atomic submission task" - ub9GsdY7SnKp86U3qogCGg; left it pending to avoid potential duplicate jobs
- nthomas: Reran funsize publish to balrog (Ar2wUwmRRuSkfynF1PV3Vg) for "Error calling 'link' for balrogVPNProxy : Gateway Timeout"
- kmoir: [Bug 1393447](https://bugzil.la/1393447) - implement watershed balrog rule for b7 to update 32 bit windows firefox users if 64 bit if their underlying os is 64 bit
- kmoir: BUILD NOT SHIPPED, skip to b8


