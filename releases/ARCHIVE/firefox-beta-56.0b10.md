# Beta: Firefox 56.0b10

### Started: 2017-09-08

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/EHY3xqeoQBahX6PVt4KKfg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Reran several windows repack jobs for exceptions getting a signing token. Partly spot instances disappearing, partly fallout from [Bug 1387194](https://bugzil.la/1387194). The latter is also causing delays as jobs try to get a token from servers other than signing-linux4 and hit a cert error, eventually they ask that one working server and continue. catlee landed a buildbotcustom change to how we verify certs.


