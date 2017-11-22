# Beta: Devedition 58.0b3

### Started: 2017-11-13

## Build 1

### Beta Graph
:bomb: _aborted release. starting new build num_ :bomb:

[task group](https://tools.taskcluster.net/push-inspector/#/PAz6EzTCSnC_3S2aQT__dA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- POTENTIAL ISSUE: Please validate beta repo has appropriate [version_display.txt](https://hg.mozilla.org/releases/mozilla-beta/file/default/browser/config/version_display.txt). Should be 58.0b3
## Build 2

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/f4jyKSLhTXSiyRcCS5LbyA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: [Bug 1416963](https://bugzil.la/1416963) for the CDN purge
- nthomas: Final verify and linux update verify failures due to missing CDN purge for Akamai. Reran those to test current state
- jlorenzo: :bomb: **BUILD NOT SHIPPED!** :bomb: Akamai CDNs are still intermittently serving old build, even after [Bug 1416963](https://bugzil.la/1416963) was done. RelMan decided to cancel 58.0b3 on Desktop and Devedition, and to respin a the same build, but branded b4.
