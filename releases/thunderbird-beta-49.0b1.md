# Thunderbird 49.0b1

### Started 2016-08-05

## Build 1

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- Release Runner Sanity failures due to mozconfig differences, initially reran on theory of race condition with push/merge. Code backed out and new build 1 submitted
- 1 linux64 repack failure due to usual mock install failure
- win32 en-US failure in unified build. Got past that in a rebuild but timeout diffing xul.dll in partial generation.


