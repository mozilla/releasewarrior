# Beta: Firefox 51.0b7

### Started: 2016-12-12

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/mp0Fij92SbS8QyOgvrrUqg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] [published release tasks](../how-tos/relpro.md#3-publish-release)

### Issues
- BBB reported the checksum builder as exception. Reran/resolved to workaround, but because the builder is not idempotent it regenerated the GPG signature. As a result the partner repacks push to cdns builder failed, because it refused to overwrite the signature. Forced the uptake monitoring builder to work around.


