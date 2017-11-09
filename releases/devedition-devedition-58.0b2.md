# Beta: Devedition 58.0b2

### Started: 2017-11-10

## Build 1

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/OuBuYWhjRsusoFNj1wh3xQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: Canceled mark as shipped task (c8c1mB8kRZiD-0p5M6k-ag) because we elected to not deploy [Bug 1415288](https://bugzil.la/1415288) in the change freeze
- nthomas: [Bug 1416053](https://bugzil.la/1416053) - new locale ne-NP not getting offers of partial update from 58.0b1, breaking update verify and final verify on all platforms. Adjust Devedition-58.0b1-build1, and rerun
