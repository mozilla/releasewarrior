# Beta: Firefox 49.0b5

### Started: 2016-08-19

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#17Yj4-b7Sfu9vq8eBaa31A)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [Set up a Whats New Page for zh-TW](https://bugzilla.mozilla.org/show_bug.cgi?id=1292637)
- noticed that partner push to releases task failed: https://tools.taskcluster.net/task-inspector/#nU2RLgYmTECJ-eoA0IZ0vA/
- Some problems 49.0b6 when the SHA512SUMS file differed between the candidates and release directories, see [49.0b6 notes](https://github.com/mozilla/releasewarrior/blob/master/releases/firefox-beta-49.0b6.md)


