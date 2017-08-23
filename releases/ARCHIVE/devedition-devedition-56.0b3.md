# Beta: Devedition 56.0b3

### Started: 2017-08-15

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/PLbMYkzhQD67U-3kLC0aHQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: schedule signoff job failed because release_eta was 'in the past'. Manually scheduled a rule change (id 237)
- nthomas: [Bug 1391102](https://bugzil.la/1391102) - didn't get AWS instances to do post release builders. Hacked build-cloud-tools/cloudtools/buildbot.py on aws-manager2 so yesterday was 3 days ago


