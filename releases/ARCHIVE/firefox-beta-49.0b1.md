# Beta: Firefox 49.0b1

### Started: 16-08-03

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#aLJuxvqbQ8ew_umzP-K4KQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [block non-SSE2 Windows updates](https://bugzilla.mozilla.org/show_bug.cgi?id=1284901)
- release-runner failure submitting the task graph, but work started in TC. rail updated the ship-it DB as if it had succeeded
- [Bug 1291523](https://bugzil.la/1291523) - Source tarball builder failed

:bomb: _aborted release. starting new build num_ :bomb:

## Build 2

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#AgNAIHRDRKGShWvAh2ym-A)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [ ] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [block non-SSE2 Windows updates](https://bugzilla.mozilla.org/show_bug.cgi?id=1284901)
- [Bug 1291562](https://bugzil.la/1291562) - Updates builder failed in Firefox 49.0b1
- [Bug 1291575](https://bugzil.la/1291575) - Specify vcs_share_base in version bump builder

:bomb: _aborted release. starting new build num_ :bomb:

## Build 3

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#viCpinuDQTWsLohnziFeYQ/)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- SPECIAL REQUIREMENT: [block non-SSE2 Windows updates](https://bugzilla.mozilla.org/show_bug.cgi?id=1284901)


