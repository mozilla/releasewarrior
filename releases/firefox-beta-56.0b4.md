# Beta: Firefox 56.0b4

### Started: 2017-08-18

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/FFXri8qpQ-WEscEoLlMTcA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: 'Failed to start release promotion (graph ID: FFXri8qpQ-WEscEoLlMTcA). Error(s): You didn\'t give the task-graph scopes allowing it define tasks on the queue.' in ship-it. Graph does exist in TC but all tasks are unscheduled. releaserunner log has 'You only have the scopes: ['docker-worker:*']'. Transient ?? Doing a build2 for deved l10n bustage anyway

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/dHzoExaZT1Gn8rymeKti7Q)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Scope issue again so we backed out [b16f9e](https://github.com/mozilla-releng/releasetasks/commit/b16f9e02da4d41657d05b061928bb12da0f8d28a) from releasetasks. Bad graphs are [GjgfvPMfRcy02KAIUWua7w](https://tools.taskcluster.net/groups/GjgfvPMfRcy02KAIUWua7w) and [aWQ10bbMSIOrkZKissLfOA](https://tools.taskcluster.net/groups/aWQ10bbMSIOrkZKissLfOA)


