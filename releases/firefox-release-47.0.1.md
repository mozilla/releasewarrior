# Release: Firefox 47.0.1

### Started: 16-06-27

## Build 1

### Release Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#m6uxLjkHSJyncHOE7qr3eg)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed release-localtest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- Releasetasks didn't tell me to e-mail when release-cdntest was ready, Relman was expecting that. Will update templates.
- Balrog [Bug 1282838](https://bugzil.la/1282838) caused throttling for 47.0 ==> 47.0.1 to be set incorrectly, intended to be 0% however with 0% set it resulted in 100% uptake. Set to 'No-Update' instead with relmans understanding
- Balrog [Bug 1282838](https://bugzil.la/1282838) - ben found a workaround... with an extra rule. Callek doesn't understand it (Will discuss in mtg)


