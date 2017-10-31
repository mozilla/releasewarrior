# Beta: Firefox 57.0b13

### Started: 2017-10-30

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/dpUz79QfR7ek4Efz0wWbxQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- jlund: bbb was wedged. failed win repack and updates builder failed to retry in bb because bbb didn't tell tc about failed run0. [Bug 1409445](https://bugzil.la/1409445) for updates builder issue and [Bug 1413025](https://bugzil.la/1413025) for bbb wedging
- jlorenzo: 4 signing tasks remained pending after waiting for 1+ hour. It turned out jamun was taking 7 out of 8 signing-worker-v1 (in Or3X9v9vS3yR0o4UzUflNA). I cancelled the tasks there, then b13 resumed. Note: signing-worker-v1 finishes its job even though the task was cancelled on the TC-side.
