# Beta: Firefox 56.0b3

### Started: 2017-08-15

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/7JYlkon0RL-lmbj45Mp8WA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Update verify errors with buildID mistmatches from special rule for manual updates. Made rule id 626 point to Firefox-56.0b3-build1 instead of 56.0b2. Reran jobs that ran out of retries.
- nthomas: [Bug 1390071](https://bugzil.la/1390071) - snap job failed, non-blocking
- nthomas: Updates - for users still on 55.0 or older Relman wants to serve 56.0b3 to 50% of background requests and 100% of manual requests. That is set up on beta-cdntest. There is a scheduled change (change id 231) set up for this which will need signoff at the same time as the main beta rule
- kmoir: had to go modify rule 32 so that it pointed to 56.0b3


