# Fennec 51.0.4

### Started 2017-02-14

## Build 1

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [pushed to mirrors/releases](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates#Push_to_mirrors)
- [x] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- Partner-driven - not planning to push to Google Play
- Repack 9/10 hit an issue with mock and s3, rerun.
- Cleared 'is shipped' flag in ship-it because Fennec 51.0.4 appeared on https://product-details.mozilla.org/1.0/mobile_versions.json. Sylvestre reported this caused some confusion as we only published it on the release directory only (and not on Google Play).
