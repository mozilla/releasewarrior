# Beta: Devedition 56.0b10

### Started: 2017-09-08

## Build 1

### Beta Graph
[task group](https://tools.taskcluster.net/push-inspector/#/PFi2U7q2SCWNvW-ud7TkWw)


#### Status
- [x] [submit to Shipit](https://wiki.mozilla.org/Release:Release_Automation_on_Mercurial:Starting_a_Release#Submit_to_Ship_It)
- [x] [published release tasks](../how-tos/relpro.md#4-publish-release)
- [x] [signoff in Balrog](../how-tos/relpro.md#3-signoffs)

### Issues
- nthomas: First graph submission failed with [this error](https://irccloud.mozilla.com/pastebin/IjnmZQsp/), which is as if releasetasks wasn't on [the tip](https://github.com/mozilla-releng/releasetasks/commit/aac1b21d5ab5f931c89172c22ce4d557cd0bf42c). That's strange because Firefox 56.0b10 started fine, straight after deved failed, and AFAIK releasetasks pulls are all manual. Starting the release again ran error free


