# Beta: Devedition 56.0b4

### Started: 2017-08-18

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/PfSo5nyvTPWfkHBpvo1sMw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Bustage in mac l10n: 'AttributeError: 'module' object has no attribute \'vfs\'.' due to hg 4.3.1 on machines but older robustcheckout in tree. gps/RyanVM organise uplifts and we'll do build2
- nthomas: Bustage in windows l10n - [Bug 1391473](https://bugzil.la/1391473). Need xz to build complete mar files

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/_nPWDM3hRM2H7vvD5VNktg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- none

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### Beta Graph
task graph url: unknown


#### Status
- [ ] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- mihaitabara: Canceling as it was started before we pull latest changes from tools & releasetasks on bm85

:bomb: _aborted release. starting new build num_ :bomb:

## Build 4

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/SfN5zKnoQKy5EbhMisaqFw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- mihaitabara: If build4 ships on Friday, please enable the watershed rules from https://aus4-admin.mozilla.org/rules/scheduled_changes before automation changes are signed-off. Even by a minute but watershes must be live before the default rules go live.
- kmoir: reran the push to releases task Aw7QIc5YQKmYAFLMuv14Mg

:bomb: _aborted release. starting new build num_ :bomb:

## Build 5

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/pA_pmTiSSfyGWAe0QAxv1g)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- mihaitabara: Reopened [Bug 1391843](https://bugzil.la/1391843) to purget CDN caches from build4.


