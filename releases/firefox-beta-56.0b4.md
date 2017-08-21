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
- mihaitabara: nthomas also fixed [Bug 1391473](https://bugzil.la/1391473) - Add xz binaries to buildbot workers  to fix BB for Windows
- mihaitabara: the mac l10n issues fixed by [Bug 1389715](https://bugzil.la/1389715) - Install Mercurial 4.3 in TaskCluster Docker images

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/dHzoExaZT1Gn8rymeKti7Q)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: [Bug 1391560](https://bugzil.la/1391560) - Scope issue again so we backed out [b16f9e](https://github.com/mozilla-releng/releasetasks/commit/b16f9e02da4d41657d05b061928bb12da0f8d28a) from releasetasks. Bad graphs are [GjgfvPMfRcy02KAIUWua7w](https://tools.taskcluster.net/groups/GjgfvPMfRcy02KAIUWua7w) and [aWQ10bbMSIOrkZKissLfOA](https://tools.taskcluster.net/groups/aWQ10bbMSIOrkZKissLfOA)
- mihaitabara: [Bug 1391680](https://bugzil.la/1391680) - Release graph needs to specify mar_sha384 signing for releases >= 56.0b4
- mihaitabara: [Bug 1391297](https://bugzil.la/1391297) - LZMA/SHA384 watershed mess - update verification failing.
- mihaitabara: To sum-up so far, we've had: hg/git, XZ, snap scopes, rules for watershed and now signing issues.

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### Beta Graph
task graph url: unknown


#### Status
- [ ] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- mihaitabara: Canceling as it was started before we pull latest changes from tools & releasetasks on bm85

:bomb: _aborted release. starting new build num_ :bomb:

## Build 4

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Aw7QIc5YQKmYAFLMuv14Mg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- mihaitabara: If build4 ships on Friday, please enable the watershed rules from https://aus4-admin.mozilla.org/rules/scheduled_changes before automation changes are signed-off. Even by a minute but watershes must be live before the default rules go live.
- kmoir: [Bug 1391843](https://bugzil.la/1391843) - Please purge CDN caches for firefox and devedition 56.0b4
- kmoir: [Bug 1391560](https://bugzil.la/1391560) - snap builds fails release runner automation for missing scopes
- kmoir: reran the push to releases task Aw7QIc5YQKmYAFLMuv14Mg
- mihaitabara: PMARs are fine. However, all update verification is still failing. PMARs are now well signed, en-uS CMAR and PMAR as well but CMAR for l10n still failing. Found the culprit in Makefile update generation and pushed a fix https://bugzilla.mozilla.org/show_bug.cgi?id=1391297#c12. Follow-up build5

:bomb: _aborted release. starting new build num_ :bomb:

## Build 5

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/VCXbi2TPSy2TdYJVS2u3ZQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- mihaitabara: Reopened [Bug 1391843](https://bugzil.la/1391843) to purget CDN caches from build4.


