# Beta: Firefox 57.0b3

### Started: 2017-09-25

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/V4brUEQYSZGI7Ei9tf5_jg)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- POTENTIAL ISSUE: [Bug 1401620](https://bugzil.la/1401620) - Snap: Use Canonical partner config instead of a duplicated one
- kmoir: [Bug 1402955](https://bugzil.la/1402955) - bouncer submission failed for firefox 57.0b3
- kmoir: [Bug 1401620](https://bugzil.la/1401620) - Snap: Use Canonical partner config instead of a duplicated one
- nthomas: Update verify failures with buildID mismatches - the 56.0 build5 updates builder had changed the beta-cdntest channel after 57.0b3 set it up for itself. Set the mapping back to Firefox-57.0b3-build1
- kmoir: publish balrog builder failed for missing ETA from RelMan in Ship-it; fixed by manual scheduling
- mihaitabara: bouncer aliases failed for same reason as bouncer submission. cloning task same way fixed it
- mihaitabara: This time, having versioned bouncer entries actually saved us. Heh
