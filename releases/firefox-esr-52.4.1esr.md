# ESR: Firefox 52.4.1esr

### Started: 2017-10-05

## Build 1

### ESR Graph 1
[task group](https://tools.taskcluster.net/push-inspector/#/P4Vnq0GxS_qqUBw5kIz8nQ)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)

### ESR Graph 2
[task group](https://tools.taskcluster.net/push-inspector/#/HMYAyYCqQWGSRok7d1ResA)

#### Status
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: NOTE: 52.4.1esr is expected to ship updates to OSX only.
- nthomas: fallout from [Bug 1387622](https://bugzil.la/1387622). When we ship we'll need to manually adjust the [firefox-sha1 alias in bouncer](https://bounceradmin.mozilla.com/admin/mirror/productalias/12/) to point at 'Firefox-52.4.1esr-sha1'. This will be fixed in future releases. mbrandt may pop up on IRC if there is a delay in updating the alias, as he has a test suite that monitors it
