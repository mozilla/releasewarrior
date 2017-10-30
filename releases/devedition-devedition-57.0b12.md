# Beta: Devedition 57.0b12

### Started: 2017-10-27

## Build 1

### Beta Graph
:bomb: _aborted release. starting new build num_ :bomb:

[task group](https://tools.taskcluster.net/push-inspector/#/VEa3v9bNT9SScxyGa_u0tg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- beetmover failures building a wheel for cryptography package, we'll do a build2 with the fix from [bug 1410960](https://bugzilla.mozilla.org/show_bug.cgi?id=1410960)
## Build 2

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/LzY7wEffQMCceeknP1jhCw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Rerun beetmover En1p4KMoTJaFrW4uN2LFYQ & SaatrjEBTBiWWUTCIKVfBw for `Error: Error loading docker image. socket hang up`
- nthomas: mac signing server timeouts hit 2 locales in mac repacks (YH8_OPgpSTSfv6X2c4lsFQ, VLEvinNvRzy2htF1BqWfYg) and artifacts tasks (Cq8Q1gGaTLy3Z9w2PWWjWQ, d82MRzy7SbefU9hz2zla1w). Possibly overall signing load for dep & nightly & release, reran tasks
- jlorenzo: Reran VkfovhwiRSGzRbGpjGO18Q for intermittent download error. https://archive.mozilla.org/pub/devedition/releases/57.0b11/win32/kab/Firefox Setup 57.0b11.exe wasn't available on the CDN
- jlund: all beetmover tasks failed in build1 because of python package crypto issues. Basically [Bug 1408197](https://bugzil.la/1408197) came back after we updated pip version in [Bug 1297515](https://bugzil.la/1297515). Fix for build2 was to graft [Bug 1410960](https://bugzil.la/1410960)
