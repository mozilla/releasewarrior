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
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: mac signing server timeouts hit 2 locales in mac repacks (aveVfXrAT1yTTq1g5-ZgZw, Lf9KJU55SIuY20zrfDzhOw) and artifacts tasks (JtFXWF5wR_28gBZT33zhkg, c3uf8PRpThGR94ZELyTcNA). Possibly overall signing load for dep & nightly & release, reran tasks
- jlorenzo: Reran YhWJ1MTdRAWUQpr-V1tQWg for intermittent download error. http://archive.mozilla.org/pub/firefox/candidates/57.0b12-candidates/build2/update/win32/gd/firefox-57.0b12.complete.mar didn't have the right size. I downloaded manually and checked the file was correct on my end
- jlorenzo: YhWJ1MTdRAWUQpr-V1tQWg hung for another download error: <class 'twisted.internet.error.ConnectionLost'>: Connection to the other side was lost in a non-clean fashion. I reran it. While the job was still running, I shipped the release because this failure remains infra-related
- jlund: all beetmover tasks failed in build1 because of python package crypto issues. Basically [Bug 1408197](https://bugzil.la/1408197) came back after we updated pip version in [Bug 1297515](https://bugzil.la/1297515). Fix for build2 was to graft [Bug 1410960](https://bugzil.la/1410960)
