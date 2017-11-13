# Beta: Devedition 58.0b2

### Started: 2017-11-10

## Build 1

### Beta Graph
:bomb: _aborted release. starting new build num_ :bomb:

[task group](https://tools.taskcluster.net/push-inspector/#/OuBuYWhjRsusoFNj1wh3xQ)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [ ] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [ ] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- callek: Had to manually land the version_display.txt bump due to no bump existing, and revised the ship-it revision. Landed on both 'default' and a used relbranch because we were explicitly not taking tip of default for this beta.
- nthomas: Canceled mark as shipped task (c8c1mB8kRZiD-0p5M6k-ag) because we elected to not deploy [Bug 1415288](https://bugzil.la/1415288) in the change freeze
- nthomas: [Bug 1416053](https://bugzil.la/1416053) - new locale ne-NP not getting offers of partial update from 58.0b1, breaking update verify and final verify on all platforms. Adjust Devedition-58.0b1-build1, and rerun
- nthomas: win64 l10n repack 10/10 (SCuadzcTSC2XE2pRknKnLA) was perma pending (on Run 1) even though the artifacts task was done. Possible some message got lost after AWS price spikes and buildbot retries. Marked completed
- callek: QE had download issues getting 58.0b1-->58.0b2. Investigation led to this being a regression from [Bug 1348087](https://bugzil.la/1348087), and is filed as [Bug 1416295](https://bugzil.la/1416295)
- callek: At relmans request reverted devedition updates to point at 57.0b14 and reverted bouncer aliases to point -latest at deved 57b14 as well.
- callek: Due to the QE update issues and the present-in-b2 [Bug 1415214](https://bugzil.la/1415214) regression. Relman has decided to abort deved-b2 entirely.
