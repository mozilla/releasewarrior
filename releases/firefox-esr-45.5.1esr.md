# ESR: Firefox 45.5.1esr

### Started: 2016-11-29

## Build 1

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/n0eDkovxQW27BSJIBJjA4g)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [x] [emailed esr-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- One of the [complete MARs](http://archive.mozilla.org/pub/firefox/candidates/45.5.1esr-candidates/build1/update/win64/ga-IE/firefox-45.5.1esr.complete.mar) downloaded in update verification was reporting wrong checksum. Manually downloaded the file and compared the checksum with checksums served by balrog.


