# Beta: Fennec 49.0b2

### Started 2016-08-08

## Build 1

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- SETA Broke ([Bug 1293538](https://bugzil.la/1293538) and [Bug 1293544](https://bugzil.la/1293544)) -- I also didn't realize fennec b2 was submitted at all, so noticed the brokenness in the build not having started late at night. SETA finally fixed late-day on tuesday (Aug 9).
- Since the releaserunner bustage happened during reconfig had to backout the hg config changes to keep the config bump from actually being able to commit/push without breaking


