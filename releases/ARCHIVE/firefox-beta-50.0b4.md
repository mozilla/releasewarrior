# Beta: Firefox 50.0b4

### Started: 2016-10-04

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/zrxQ87rIRR2KASmRlYFvjg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Problem starting the release as only the TC build was done, and it confused release-runner. [Bug 1307326](https://bugzil.la/1307326). Worked around by waiting for buildbot and restarting in ship-it
- uptake monitoring burns out before sha1 repacks are all done. Known [Bug 1300060](https://bugzil.la/1300060). Rerun successfully with tctalker.
- win64 l10n repack 1/10 had a hg clone hiccup which eventuall ran successfully. Mozharness parsed the log as failed and reported as failed task. Following jobs retriggered by TC queue reported as failed because run 0 was claimed by another worker. They were harmless since first run actually completed successfully and attached artifacts to the corresponding job.


