# Beta: Firefox 55.0b1

### Started: 2017-06-12

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/AoGGiQ6JRKyvkT6MWV3A9w)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- nthomas: [Bug 1372461](https://bugzil.la/1372461) - l10n upload problems. Fallout from [Bug 1339870](https://bugzil.la/1339870), deploy rolled back
- jlund: [Bug 1372482](https://bugzil.la/1372482) - linux 55.0 repack betas are broken post merge because mock can't find /tools/buildbot/bin/python

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/f9xmnhxiRsWkGNE5qWqqLw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- jlund: build2 seemed to ignore fix from build1. is mozharness_revision ignored from shipit?

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/qKECaomfSd2bqElN4fgtUQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- jlund: waiting for ci builds from beta 6872377277a618b2b9e0d2b4c2b9e51765ac199e
- nthomas: [Bug 1372482](https://bugzil.la/1372482) - more linux l10n failures, this time calling compare-locales

:bomb: _aborted release. starting new build num_ :bomb:

## Build 4

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/MJ4-tjfoSia6whqBHH9Rnw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- none

:bomb: _aborted release. starting new build num_ :bomb:

## Build 5

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Ep4OjONuRNWdnXg54Zkg8A)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- nthomas: [Bug 1372798](https://bugzil.la/1372798) - be locale has returned but complete not in Balrog, so we get update and final verify errors
- jlorenzo: Special requirement: Set update rate at 0%, so devedition will be the staging population


