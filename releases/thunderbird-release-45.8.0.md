# Thunderbird 45.8.0

### Started 2017-03-06

## Build 1

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [pushed to mirrors/releases](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates#Push_to_mirrors)
- [x] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- Windows en-US build failed due to slave missing tooltool token, reran job
- A little network flakiness resulted in repacks Linux64 7/10 and Linux 4/10 having a issues talking to clobberer, and linux64 10/10 hung during signing, and linux 3/10 failing to resolve archive.m.o. Reran all jobs
- Download error in av job, rerun
- 504 Gateway Timeout errors in linux64 update verify 2/6, rerun


