# Beta: Firefox 51.0b6

### Started: 2016-12-02

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/r0xl9AvMSTGoA8BRZuLcMQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- Several jobs showed as exception in tc while being green on buildbot: bouncer submission (TNwuOlinQy2CXyUahJwv9A), updates (WWDhk2I7TemBzz3g30BNIA), linux repack 6/10 (xbkHS9XISeOoxwl-bOTLFw), linux64 repack 2/10 (uSKcWe4oQgeyb55u7xbvIw), linux64 repack 3/10 (gQvHtKy4QR-NLwiTb7C2VA), linux64 repack 4/10 (R_6w56KESQqC5C9UXot4VQ). Tried report_completed on bouncer, and ot 409/RequestConflict/Run 0 was already claimed by another worker. Rerun also hit an exception.
- Reran the updates job to unblock update verify tests


