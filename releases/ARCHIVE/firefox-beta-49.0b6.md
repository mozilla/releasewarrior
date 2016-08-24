# Beta: Firefox 49.0b6

### Started: 2016-08-22

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#mj8H1ldQQEaAg22CL0EaNw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- release-runner failed because checksums for b5 was run twice. the second time was after we pushed to releases (human error) and the first time was run before all partials were generated (automation dependancy error). the dep error is tracked here: [Bug 1297268](https://bugzil.la/1297268)
- because of checksums issue from beta5, release-runner's sanity check kept failing. fix was to locally comment out that sanity check but ftr: we also updated the SHA512SUM file in the release dir with the correct latest candidates equiv. but couldn't use it because of cloudfront caching the old one


