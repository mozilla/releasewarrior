# Beta: Firefox 55.0b8

### Started: 2017-07-10

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/zSNutYYNRC6R-BjnfurBVQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)

### Issues
- rail: [Bug 1366003](https://bugzil.la/1366003): Needed to update the public GPG key https://hg.mozilla.org/build/tools/rev/56b149869f76
- nthomas: beetmover image generation failed all retries while cloning mozilla-unified, tctalker rerun used
- nthomas: 6x update verifies stayed in unscheduled state when they had no outstanding deps. TC UI reported "Resource Not Found Error! Task with taskId: o4KuECYLQBe4sM5GrhU2MA run with runId: 0 task status: { "taskId": "o4KuECYLQBe4sM5GrhU2MA", "provisionerId": "buildbot-bridge", "workerType": "buildbot-bridge", "schedulerId": "task-graph-scheduler", "taskGroupId": "zSNutYYNRC6R-BjnfurBVQ", "deadline": "2017-07-14T18:26:40.522Z", "expires": "3017-07-10T18:26:40.611Z", "retriesLeft": 5, "state": "unscheduled", "runs": [] }". Used tctalker rerun on uSlPZRNnSH6DcZRdLSr7XA, C8E4RRo-TmWQPJJCJ31CeA, R9P_FlxXR7WK5fZwwXDmWQ, 4rSaFNBvR5eqG5lS8gFnig, o4KuECYLQBe4sM5GrhU2MA, o4KuECYLQBe4sM5GrhU2MA


