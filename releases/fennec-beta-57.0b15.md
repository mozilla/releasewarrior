# Beta: Fennec 57.0b15

### Started 2017-11-07

## Build 1


### Beta Graph
- [task group 1](https://tools.taskcluster.net/push-inspector/#/XnXh1uxtRiuSgm0dRKNUUg)
- [task group 2](https://tools.taskcluster.net/push-inspector/#/O4EfW-iiQlGYxM03StGk1w)

### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] emailed candidates
- [x] [run pushapk](https://github.com/mozilla/releasewarrior/blob/master/how-tos/fennec-temp-relpro.md#run-pushapk-manually)
- [x] [published release tasks](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Updates_through_Shipping#Post-release_tasks)

### Issues
- nthomas: We forgot to bump version_display.txt to 57.0b15 after 57.0b14, so the initial revision wasn't usuable. RyanVM landed ca8382300eb7 in beta
