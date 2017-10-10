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
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: NOTE: 52.4.1esr is expected to ship updates to OSX only.
- nthomas: fallout from [Bug 1387622](https://bugzil.la/1387622). When we ship we'll need to manually adjust the [firefox-sha1 alias in bouncer](https://bounceradmin.mozilla.com/admin/mirror/productalias/12/) to point at 'Firefox-52.4.1esr-sha1'. This will be fixed in future releases. mbrandt may pop up on IRC if there is a delay in updating the alias, as he has a test suite that monitors it
- callek: [Bug 1406939](https://bugzil.la/1406939) - We hit Final Verify failures due to only shipping 52.4.1esr to OSX. I backed out the automation changes to update verify configs to allow us to test what we're expecting. And re-ran the final verify task
- callek: Unable to test rules which filter on OS_VERSION because we pass 'default'. Resorted to letting SV test the update rather than manually setting BUILD_TARGET to keep testing consistent between us and users
- jlorenzo: It wasn't a problem for this macos-only release, but this bug bit us again: [Bug 1407174](https://bugzil.la/1407174) - Cannot submit scheduled change to alias "esr52": Invalid input for rule_id. Not an integer. rule_id: u'esr52' is not a 'rule_id'
- jlorenzo: We need to mark this ESR as shipped. I don't have the rights to do so. [Bug 1388323](https://bugzil.la/1388323) - Cannot mark 52esr as shipped: HTTPError: 401 Client Error: Authorization Required for url: https://ship-it.mozilla.org/csrf_token
