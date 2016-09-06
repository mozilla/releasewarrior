# Beta: Firefox 49.0b9

### Started: 2016-09-02

## Build 1

### Beta Graph
[task graph](https://tools.taskcluster.net/task-group-inspector/#jt12EvDlQ6eiOoNMsJXfQw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [emailed beta-cdntest](../how-tos/relpro.md#1-email-drivers-re-release-live-on-test-channel)
- [x] published release tasks [part 1](../how-tos/relpro.md#3-publish-release) [part 2](../how-tos/relpro.md#4-post-release-step)

### Issues
- Uptake monitoring timed out because of sha1 repacks, [Bug 1300060](https://bugzil.la/1300060), rerun
- Mark as shipped builder failed again as slaves can't talk to ship-it [Bug 1288434](https://bugzil.la/1288434). Filed [Bug 1300127](https://bugzil.la/1300127) for netops to tweak firewall


