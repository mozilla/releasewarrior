# ESR: Firefox 52.5.0esr

### Started: 2017-11-07

## Build 1
:bomb: _aborted release. starting new build num_ :bomb:

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/GqVVU9g_Tj2Q92UD0mbp_g)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
task graph url: unknown

#### Status
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: Need a build 2 due to late breaking patch uplifts.
## Build 2

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/AziNSjvYQw24URbOOKhkvA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/eXlDTG0SQJWndwcdW-KIMQ)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: [Bug 1415268](https://bugzil.la/1415268) - ISE when submitting build 2 via shipit. Addressed for build2 by not submitting as many partials
- callek: Final Verify failed due to a bad tools checkout. Reran with tc cli
- callek: ESR Balrog update failed, however buildbot reported the job as passed, manually scheduled the update.
