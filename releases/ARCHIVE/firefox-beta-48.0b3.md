# Beta: Firefox 48.0b3

### Started: 16-06-24

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#mFypBVVXSKKzq4HF8I9cZQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-cdntest-channel)
- [x] [publish in Balrog](../how-tos/relpro.md#3-publish-in-balrog)
- [x] [post-release tasks](../how-tos/relpro.md#4-post-release-step)

### Issues
- win32 repack crash in update generation, retriggered
- final verification issue for win64 chunk 7 partials because of misspelled Ship it 48.0b2build1 partial instead of 48.0b2build2. Moved on as users under these conditions would be served complete mars instead of partial mars
- Bug 1281199 - caused many windows verifications and a few repacks to be RETRY state
- Buildbot Bridge had MANY issues with RETRIED buildbot jobs, failing to properly mark jobs as started or finished when they were either successful or failed
- Didn't get marked as 'shipped' in ship-it, done


