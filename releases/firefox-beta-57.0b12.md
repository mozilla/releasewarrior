# Beta: Firefox 57.0b12

### Started: 2017-10-27

## Build 1
:bomb: _aborted release. starting new build num_ :bomb:

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/JwEu-nKsSOSz6Tt6WoZdBw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- beetmover failures building a wheel for cryptography package, we'll do a build2 with the fix from [bug 1410960](https://bugzilla.mozilla.org/show_bug.cgi?id=1410960)
## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/JHWirlAPQLWFFVsrpwUgsg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: mac signing server timeouts hit 2 locales in mac repacks (aveVfXrAT1yTTq1g5-ZgZw, Lf9KJU55SIuY20zrfDzhOw) and artifacts tasks (JtFXWF5wR_28gBZT33zhkg, c3uf8PRpThGR94ZELyTcNA). Possibly overall signing load for dep & nightly & release, reran tasks
