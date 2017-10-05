# Release: Firefox 56.0.1

### Started: 2017-10-03

## Build 1
:bomb: _aborted release. starting new build num_ :bomb:

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/Z6Mw4NW5ThGiAKCuvamrYw)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [ ] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT:  Use the transform_balrog_blob.py script in https://bugzilla.mozilla.org/show_bug.cgi?id=1393789 change the complete mar urls to point to bz2 mars.  Once the new release blob has been submitted to balrog we need resolve the start_update_verify_human_decision task that rail added in releasetasks
- SPECIAL REQUIREMENT: https://bugzilla.mozilla.org/show_bug.cgi?id=1391718 Add LZMA/SHA384 watershed when 56.0 ships
- SPECIAL REQUIREMENT: https://bugzilla.mozilla.org/show_bug.cgi?id=1405012 Implement a watershed for win32-win64 migration before 56.0.1 ships
- kmoir: see https://docs.google.com/document/d/1c9hWwCdN4w2MHN2lTxFZ0nIs8neH6R7VLKogIdZqhJA/edit#heading=h.5eopgyoyeruv for details on 56.0.1 win32->win64 rules
- nthomas: Funsize submitter bustage from [Bug 1402015](https://bugzil.la/1402015), rail [landed a fix](https://hg.mozilla.org/build/tools/rev/912affa82eef). We'll do a build2 to pick it up
- nthomas: Many windows l10n retries because of being outbid on spot instance
## Build 2

### Release Graph
[task group](https://tools.taskcluster.net/push-inspector/#/EHgvG8c7SdKqCkJ_06UXBA)

#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [Setup whatsnew page](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Set-up_whatsnew_page)
- [x] [pushed to mirrors/releases](../how-tos/relpro.md#2-push-to-releases-dir-mirrors)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- SPECIAL REQUIREMENT:  Use the transform_balrog_blob.py script in https://bugzilla.mozilla.org/show_bug.cgi?id=1393789 change the complete mar urls to point to bz2 mars.  Once the new release blob has been submitted to balrog we need resolve the start_update_verify_human_decision task that rail added in releasetasks
- SPECIAL REQUIREMENT: https://bugzilla.mozilla.org/show_bug.cgi?id=1391718 Add LZMA/SHA384 watershed when 56.0 ships
- SPECIAL REQUIREMENT: https://bugzilla.mozilla.org/show_bug.cgi?id=1405012 Implement a watershed for win32-win64 migration before 56.0.1 ships
- kmoir: see https://docs.google.com/document/d/1c9hWwCdN4w2MHN2lTxFZ0nIs8neH6R7VLKogIdZqhJA/edit#heading=h.5eopgyoyeruv for details on 56.0.1 win32->win64 rules
- jlorenzo: Uncharted territory: We have to manually generate win32->64 partials. [Bug 1405681](https://bugzil.la/1405681) - Create partial updates to migrate eligible 56.0 win32 users to 56.0.1 win64
