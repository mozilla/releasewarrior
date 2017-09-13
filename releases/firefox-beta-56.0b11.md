# Beta: Firefox 56.0b11

### Started: 2017-09-12

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/bSBKGy9xQWSbHAb-C6I_uA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: [Bug 1398964](https://bugzil.la/1398964) - rerun Publish to balrog jobs when they hit "Error calling link for balrogVPNProxy : Gateway Timeout"
- nthomas: Related to above, we had a second balrog publish failure but ran push to releases/uptake monitoring/final verification. While pushing doesn't require balrog the final verification does, so it failed and retried 3 times, then hit an hg error which didn't retry


