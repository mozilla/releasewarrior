# Beta: Devedition 57.0b9

### Started: 2017-10-16

## Build 1

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/X5_tOe6QTKevf0gDJGMIhg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: [Bug 1409445](https://bugzil.la/1409445) - devedition mozilla-beta updates - raced the firefox equivalent to push into the tools repo and lost. Worth retrying in-job ? RyanVM reran via treeherder, which uses bb self-serve to run but that doesn't show up in the tc graph. Did rerun and completed on b5DkgMezT9WkLWPue3ZNHA with tasckluster cli, but the bridge still grabbed it
