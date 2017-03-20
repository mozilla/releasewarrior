# Beta: Firefox 52.0b8

### Started: 2017-02-21

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/BDPYq49qTga4WQSwIlkbng)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Failure for ``[beetmover] firefox mozilla-beta partner repacks push to releases`` due to busted boto v2.46 on pypi. They fixed that promptly with v2.46.1 so just reran the job, but why does beetmover not use internal pypi. Filed [Bug 1341154](https://bugzil.la/1341154).


