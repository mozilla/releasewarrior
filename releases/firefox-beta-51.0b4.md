# Beta: Firefox 51.0b4

### Started: 2016-11-28

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/zaVnBlMRTOOb3xD4TwBLIg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- [Bug 1303106](https://bugzil.la/1303106) broke funsize balrog submission. backed out. reran funsize docker image task (run1) but funsize tasks ignored generated image from run1 by using cache of run0. cancel'd every funsize balrog task pending/running to force funsize-balrog worker instances to die and regen. rerun'd every canceled and failed task
- final verify doesn't wait on funsize balrog submission tasks. tracking fix: https://github.com/mozilla/releasetasks/pull/209
- final verify failing (even post funsize balrog fix) because of ka,kab locales. expected. ignoring. see earlier 51 betas
- bouncer aliases and mark release as shipped ran too quickly in bbot, tc set status as exception. used tctalker to mark them as green
- like final verify, some update verify tests are failing because of ka, kab. ignored


