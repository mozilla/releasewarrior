# Beta: Fennec 56.0b9

### Started 2017-09-04

## Build 1

### Beta Graph
- [task group 1](https://tools.taskcluster.net/push-inspector/#/cZl-gqPpRwi7i70380hMxg)
- [task group 2](https://tools.taskcluster.net/push-inspector/#/dkTyxu_OT6auOGjYNGpS_g)

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [manually kick off graph](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#start-off-the-fennec-graph)
- [ ] emailed candidates
- [ ] [run pushapk](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#run-pushapk-manually)
- [ ] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- jlorenzo: Potential source of breakage: [Bug 1384482](https://bugzilla.mozilla.org/show_bug.cgi?id=1384482) - Fennec: Make Treeherder and archive.mozilla.org broadcast the right Android API level (API-16+)
- rail: Potential source of breakage: [Bug 1395516](https://bugzilla.mozilla.org/show_bug.cgi?id=1395516) - releasetasks_graph_gen.py should use release-runner.yml, not ini
- nthomas: [Bug 1396472](https://bugzil.la/1396472) - signing tasks broken in nightly graph, a Chain of Trust problem

:bomb: _**aborted release. starting new build num**_ :bomb:

## Build 2

### Beta Graph
- [task group 1](https://tools.taskcluster.net/push-inspector/#/fOOcKf2qQlixNT1ctM39zQ)
- [task group 2](https://tools.taskcluster.net/push-inspector/#/BLJjrsnZTJmIvDBW0xCx7A)

### Status
- [ ] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [manually kick off graph](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#start-off-the-fennec-graph)
- [ ] emailed candidates
- [ ] [run pushapk](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#run-pushapk-manually)
- [ ] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- jlorenzo: [Bug 1396517](https://bugzil.la/1396517) - Chain Of Trust can't find a worker_impl for decision task of Fennec graph 1

:bomb: _**aborted release. starting new build num**_ :bomb:

## Build 3

### Beta Graph
- [task group 1](https://tools.taskcluster.net/push-inspector/#/RuNCJvZRSDazUTfLOgneVQ)
- [task group 2](https://tools.taskcluster.net/push-inspector/#/KMWiwXmNQ4-4uM2vxj-DiA)

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [manually kick off graph](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#start-off-the-fennec-graph)
- [x] emailed candidates
- [x] [run pushapk](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#run-pushapk-manually)
- [x] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- jlorenzo: Landed a hotfix for [Bug 1396517](https://bugzil.la/1396517) in build 3. Hotfix must be backed out and real fix will occur in scriptworker
- kmoir: kmoir acciddentally ran publish release from build1 instead of build3, cancelled tasks and ran publish on build3 to fix


