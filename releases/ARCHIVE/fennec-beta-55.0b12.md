# Beta: Fennec 55.0b12

### Started 2017-07-24

## Build 1

### Beta Graph
- [task group 1](https://tools.taskcluster.net/push-inspector/#/3ocvd7YlR0awLgRzyuohRA)
- second task graph url: unknown

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [manually kick off graph](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#start-off-the-fennec-graph)
- [x] emailed beta-localtest
- [x] [run pushapk](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#run-pushapk-manually)
- [x] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- mihaitabara: We might have delays in shipping because of l10n Google Play strings website being done. [Bug 1383642](https://bugzil.la/1383642)
- mihaitabara: Pushed manually by RelMan. More details on this in [Bug 1384083](https://bugzil.la/1384083)
- mihaitabara: Mark release as shipped fails for auth errors. Will be marked by rail in ShipIt DB as builder needs tree changes to be fixed[Bug 1383121](https://bugzil.la/1383121)


