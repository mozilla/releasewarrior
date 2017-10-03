# Beta: Firefox 57.0b5

### Started: 2017-10-03

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/bL_4ihXmQIaKac0jOUin2Q)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Lots of auto-retries for windows l10n repacks, due to price spikes in us-east-1 for b-2008-spot and we'd disabled all of us-west-2. Re-enabled 20 in the latter region.
- nthomas: Reran final verification (EKmezrCTRVOmX3jK17ygtg) for tools clone error
