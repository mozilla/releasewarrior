# Beta: Devedition 56.0b1

### Started: 2017-08-08

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/j9-GjuTXQdiWOsiO6fL2Ag)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- nthomas: Forgot to land some funsize fixes on beta and hit issues with python deps

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/peh4qWmITmKjaT-Nwcan8A)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- asasaki: funsize-balrog issue https://github.com/mozilla-releng/releasetasks/pull/261

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/BoyrEYDOTWCZSOZ8u23YiA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- mihaitabara: [Bug 1388312](https://bugzil.la/1388312) - 56.0b1 update tests fail: MAR_CHANNEL_MISMATCH_ERROR
- mihaitabara: [Bug 1388431](https://bugzil.la/1388431) - [win32/64, macosx64] Devedition: mars should be signed with Nightly key

:bomb: _aborted release. starting new build num_ :bomb:

## Build 4

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/LcsV9wwyTIOc_1U6_vgzDQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- mihaitabara: Trailing slash in mar tools urls. [Bug 1388312](https://bugzil.la/1388312)

:bomb: _aborted release. starting new build num_ :bomb:

## Build 5

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/8_2Lln3uQpiI0gQOq1_dzg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- asasaki: bld-lion-r5-006 was having hg-shared issues; sshed in and nuked the specific empty 7ae7fb134bf7aec6ec96a062ff47a69053dd2973/ dir
- nthomas: [Bug 1388567](https://bugzil.la/1388567) - purge CDN caches after nthomas removed builds in devedition/releases/56.0b1 from previous build
- nthomas: RelMan wanted to take back shipping after the human decision task as marked completed, so we ended up in limbo where www.mozilla.org was live but updates were disabled


