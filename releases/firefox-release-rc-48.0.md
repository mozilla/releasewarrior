# RC Release: Firefox 48.0

### Started: 2016-06-28

## Build 1

### RC graph 1
[task graph](https://tools.taskcluster.net/task-group-inspector/#i1W1g-DLRqCc01wVK8QBQA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: Do [Bug 1275607](https://bugzil.la/1275607) - add OS X 10.6-10.8 deprecation rule when 48.0 ships to release
- SPECIAL REQUIREMENT: Delete RuleID 366 and 367 (firefox, release channel) to allow updates to 48.0 from 47.0 when ready to go live
- SPECIAL REQUIREMENT: [set-up Windows watershed update](https://bugzilla.mozilla.org/show_bug.cgi?id=1284903) before shipping
- Win64 repack OdTZr1_dTQ-JgxnVRg0a1A/1 - first run hit a bash crash & a slave disconnect, was auto retried. Second run was green in buildbot but then the bridge hit an error passing that back to TC, possibly a race condition. Rail filed [Bug 1289277](https://bugzil.la/1289277) to reduce the # of hosts running the bridge; used tctalker to mark task done and make things look nice
- Terminated b-2008-spot-005 for excessive retries on 'win32 release update verification 6/12' (initially a timeout purging then undeleteable file. Also b-2008-spot-042
- Marked update verify 3HcCbjmMRqOa5N9WF1wJJw & W3ZuI4GNTXa75oZIC20WTg complete after finding green buildbot jobs
- Rerun update verify EVZZwzEHSnmH2m8syV9KEA, IAP9GaA8Q8iUFleiQ44qbQ, pZf5hgalQTqOPRCXjT-P5Q, sFimyQalQYC68rqqQ-NIiA after failures
- Failed update verify bG4ApN6HSdSDtW1nSLyFzQ has hit the 50 run limit, will need some graph surgery to rerun

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### RC graph 1
[task graph](https://tools.taskcluster.net/task-group-inspector/#79IPcIthQSyc9Jlj_OP1Kg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-release)

### RC graph 2
[task graph](https://tools.taskcluster.net/task-group-inspector/#lHf6q5g1QJeEUwaK8OrCUQ)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: Do [Bug 1275607](https://bugzil.la/1275607) - add OS X 10.6-10.8 deprecation rule when 48.0 ships to release
- SPECIAL REQUIREMENT: Delete RuleID 366 and 367 (firefox, release channel) to allow updates to 48.0 from 47.0 when ready to go live
- SPECIAL REQUIREMENT: [set-up Windows watershed update](https://bugzilla.mozilla.org/show_bug.cgi?id=1284903) before shipping
- 2x linux repacks hit the race in the buildbot bridge, marked Snq0feKWS12n7ipeOwdBag & Tz4LEkT9QuurUsXjDfseOg completed after verifying green in buildbot.
- [Bug 1290918](https://bugzil.la/1290918) - releasetasks_graph_gen.py get_partials is passed an unexpected string of partials
- Hit non-blocking balrog [Bug 1291316](https://bugzil.la/1291316) while trying to create the OSX deprecation rule
- Hit blocking balrog [Bug 1291317](https://bugzil.la/1291317) while trying to create the second OSX deprecation rule
- Setup windows watershed rule (and OSX desupport-to-48 rule) with update rate set according to the 'everyone' rate, so needs updating when rate changes throughout.


