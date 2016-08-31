# Release: Firefox 48.0.2

### Started: 2016-08-24

## Build 1

### Release Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#NoR5NYs3QN-IZTLRDKCPVA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- firefox mozilla-release macosx64 EME-free repacks failed because signing timed out
- pulse died, bbb is unhappy, rail published release manually so that task can be cancelled but we need to make sure bouncer and version bump (post release tasks) run once tc is running again


