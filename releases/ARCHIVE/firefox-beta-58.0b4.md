# Beta: Firefox 58.0b4

### Started: 2017-11-15

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Ze5SClM0T4KVuorTQnMUQA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: [Bug 1417697](https://bugzil.la/1417697) - version bump failed to tag because of the relbranch, [landed manually](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?fromchange=7ecf3934e758&tochange=4fcc0808fe85)
- nthomas: [Bug 1389312](https://bugzil.la/1389312) - release eta was in the past and Balrog complained, jlund manuallly scheduled the change
