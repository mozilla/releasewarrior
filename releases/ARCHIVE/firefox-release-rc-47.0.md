# RC Release: Firefox 47.0

### Started: 16-06-01

## Build 1

### RC graph 1
[task graph](https://tools.taskcluster.net/task-group-inspector/#4K6uhGF4QO6t44fnhQ8DtA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-in-balrog)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [ ] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- yAN46JZnTJeeq7NEvOBVXg firefox mozilla-release updates run 0 failed, because the push to hg.m.o raced with http://hg.mozilla.org/build/tools/rev/154c6052d713. See http://archive.mozilla.org/pub/firefox/tinderbox-builds/mozilla-release-noarch/release-mozilla-release-firefox_updates-bm74-build1-build1.txt.gz for the details. Automatic rerun fixed the issue.
- JK2xBU-0T5u1oJAQ7aCOUA linux64 beta update verification 9/12 failed, beacuse one of the headers returned by CDN was `X-Amz-Cf-Id: KhRL4H9Z6nms0MVAC-Po0nT0cQd9G3doIMAZWMeFAILGRrONF1LhBA==` which matches the `FAIL` pattern. Automatic rerun passed

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### RC graph 1
[task graph](https://tools.taskcluster.net/task-group-inspector/#TimQHjxjRIGOsEzo0RLTug)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-in-balrog)

### RC graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [ ] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- none

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### RC graph 1
[task graph](https://tools.taskcluster.net/task-group-inspector/#X41RVzRpQtmnfyUL7qO6mA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog on Beta channel](../how-tos/relpro.md#3-publish-in-balrog)

### RC graph 2
[task graph](https://tools.taskcluster.net/task-group-inspector/#XfCBFoBbQWqmxPZZ_pgKVw)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- win32 l10n upload timeout (1v0BGWkQTVW9Z1ZJijsiew, Luklgy64RUKLYhDhztJalg); rerun
- Bug 1278312 - uptake monitoring failed. Reran and quiclky resolved using tctalker


