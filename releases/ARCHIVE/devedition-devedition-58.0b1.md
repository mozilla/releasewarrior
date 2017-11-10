# Beta: Devedition 58.0b1

### Started: 2017-11-03

## Build 1

### Beta Graph

[task group](https://tools.taskcluster.net/push-inspector/#/FX5H-YZURx6zyN8KhJ5jlA)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- jlorenzo: beetmover docker image (QzCop2FYSuSDmzFijtPtcg) timed out fetching clamav. I reran the task.
- callek: Had to manually recreate balrog submit, mark as shipped and bouncer tasks, because the human decision task reached deadline-expired. Tasks [DlDYrZwaTDuREH2O6H13qg](https://tools.taskcluster.net/groups/DlDYrZwaTDuREH2O6H13qg/tasks/DlDYrZwaTDuREH2O6H13qg/details) [VTO9PdqiQz6sxPH7WmyqKw](https://tools.taskcluster.net/groups/VTO9PdqiQz6sxPH7WmyqKw/tasks/VTO9PdqiQz6sxPH7WmyqKw/details) [ZQvBGWgTTySBNSRwMZ6dIw](https://tools.taskcluster.net/groups/ZQvBGWgTTySBNSRwMZ6dIw/tasks/ZQvBGWgTTySBNSRwMZ6dIw/details).
- callek: [Bug 1415288](https://bugzil.la/1415288) - Product details doesn't know about 58.0b1 as a primary version causing issues with deved availability.
- callek: Found issues with b1 when testing deved 58.0b2, see beta 2's entry for more details
