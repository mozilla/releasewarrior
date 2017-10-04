# Beta: Devedition 57.0b5

### Started: 2017-10-03

## Build 1

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/aoaObs6aROaQ4Y9T3Tlj-A)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: [Bug 1405137](https://bugzil.la/1405137) - ship-it makes a poor choice for partials
- nthomas: Lots of auto-retries for windows l10n repacks, due to price spikes in us-east-1 for b-2008-spot and we'd disabled all of us-west-2. Re-enabled 20 in the latter region.
- nthomas: [Bug 1405203](https://bugzil.la/1405203) - win32 en-ZA and eo update verify issues from duplicated l10n repack jobs
- jlorenzo: sfraser handled this special requirement: [Bug 1399849](https://bugzil.la/1399849) - Set up whatsnew pages for 57.0b4 devedition
- jlorenzo: We can't display WNP from a beta to another. Only users <56 will see WNP ([Bug 1399849](https://bugzil.la/1399849))
