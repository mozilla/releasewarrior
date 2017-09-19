# Beta: Fennec 56.0b13

### Started 2017-09-19

## Build 1


### Beta Graph
- [task group 1](https://tools.taskcluster.net/push-inspector/#/DdNB7PYDSD-cbUpmSxegsw)
- [task group 2](https://tools.taskcluster.net/push-inspector/#/QHKmQ3eHQJ6omxy4uSHGHw)

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] emailed candidates
- [x] [run pushapk](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#run-pushapk-manually)
- [x] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- POTENTIAL ISSUE: Cross-Channel L10n will have landed for beta 57 by this release, but should not be enabled for fennec 56. See [Bug 1397721](https://bugzil.la/1397721)
- POTENTIAL ISSUES: [Bug 1347635](https://bugzil.la/1347635) - Patches to enable releaserunner2 in Fennec have been landed on Friday night so that all Fennec releases should now be handled automatically. If things go south, please default back to [manual docs](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#start-off-the-fenenc-graph)
- nthomas: Clean up template to remove 'manually kick off graph'
- jlorenzo: Version bump failed because we built off a relbranch. I manually bumped version_display.txt and tagged the repo
