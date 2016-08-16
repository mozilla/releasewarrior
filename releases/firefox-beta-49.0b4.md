# Beta: Firefox 49.0b4

### Started: 16-08-16

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#ZWmMsRjtSPi2rbv95BbBVw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- Lots of Balrog submission errors, https://bugzilla.mozilla.org/show_bug.cgi?id=1295450
- The balrog failures had followon affect with Update Verify ([Bug 1276506](https://bugzil.la/1276506))
- Update verify jobs failed due to dependancies not being set correctly ([Bug 1276506](https://bugzil.la/1276506)) when all the funsize stuff failed


