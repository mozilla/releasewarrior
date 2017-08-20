# Thunderbird 52.3.0

### Started 2017-08-15

## Build 1

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [pushed to mirrors/releases](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates#Push_to_mirrors)
- [x] published release tasks [part 1](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Publish_in_Balrog) [part 2](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- kmoir: repacks failed on 2/10 and 10/10 linux64, 7/10 linux - reran the jobs
- kmoir: [Bug 1356562](https://bugzil.la/1356562) - [Thunderbird] update_verify: Linux updates fail because libgtk-3 is missing
- nthomas: Skipped the update_shipping_release builder because changes had already been made manually and [Bug 1388330](https://bugzil.la/1388330) would have meant it failed anyway
- nthomas: [Bug 1392138](https://bugzil.la/1392138) - checksums file not accurate, from rerunning repacks when they'd already auto-retriggered ?


