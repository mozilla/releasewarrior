# Release: Firefox 52.0.2

### Started: 2017-03-24

## Build 1

### Release Graph
task graph url: unknown

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1350285](https://bugzil.la/1350285) - Cannot robust checkout https://hg.mozilla.org/releases/l10n/mozilla-release/nb-NO : HTTP Error 413: Request Entity Too Large
- [Bug 1350841](https://bugzil.la/1350841) - "firefox mozilla-release win64 l10n repack {,artifacts} {1,5}" have been pending for 3 days
- push_to_mirrors and publish_release tasks expired. Recreated them manually under the same graph


