# Beta: Fennec 55.0b1

### Started 2017-06-12

## Build 1

### Beta Graph
- [task group 1](https://tools.taskcluster.net/push-inspector/#/FvNhYM-sS2KC8ucCDbJ4mw)
- second task graph url: unknown

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [manually kick off graph](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#start-off-the-fennec-graph)
- [ ] emailed beta-localtest
- [ ] [run pushapk](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#run-pushapk-manually)
- [ ] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- SPECIAL REQUIREMENT: [Bug 1358420](https://bugzil.la/1358420) - 55.0b1 - Allow fennec beta staged rollout
- asasaki: broken decision task; we need to remove --triggered-by=nightly from the decision task template in releasetasks for beta
- jlund: [Bug 1372487](https://bugzil.la/1372487) - remove reference to triggered_by in releasetasks for beta
- mihaitabara: Could not review/merge jlund patch due to missing write access to releasetasks. Reopened and addressed question in [Bug 1369392](https://bugzil.la/1369392).


