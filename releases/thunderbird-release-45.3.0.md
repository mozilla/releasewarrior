# Thunderbird 45.3.0

### Started 2016-08-25

## Build 1

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [pushed to mirrors/releases](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates#Push_to_mirrors)
- [x] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- Antivirus job failed to d/l file (IncompleteRead), rerunning
- update verify failures - win32 4/6 hit a 500 on a complete mar; linux64 2/6 mock-init failure; linux64 5/6 & linux 2/6 mock-install failures; linux64 2/6 slow download hit a timeout. Rerunng all.
- rerunning of antivirus and update verify succeeded


