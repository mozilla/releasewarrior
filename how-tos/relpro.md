# Pre-requirements 
## taskcluster related
* **You need 2 bookmarklets in your browser to enhance the work with taskcluster**
  * Create a new bookmark, name it `Stop`, add `javascript:stop();` to Location
  * click and drag the [sort table](https://www.squarefree.com/bookmarklets/pagedata.html#sort_table) link to your Bookmarks Toolbar. [Rail](https://github.com/rail) found a fancier sort table [here](https://gist.githubusercontent.com/rail/11314a9e04cdabb33ccabc5419ef90d0/raw/21e095893a743df2a4a735cbcc751e165f2f6d98/table%2520sorter)
* Find the email with subject: "[desktop] Build of Firefox-46.0b4-build2" - it contains a link to the task graph
* After the task graph is loaded click on the "stop" bookmarklet
* Click the "sort table" bookmarklet - you'll get "a/d" table headers
* Sort the table by "State" ascending, so you get unscheduled and  scheduled tasks first

## tctalker setup
* **You need tctalker to play nicely with taskcluster jobs**
* navigate to [Taskcluster tools](https://tools.taskcluster.net) and make sure you're logged-in
* make sure the following scopes are listed under your [Taskcluster credentials](https://tools.taskcluster.net/credentials/):
```
auth:create-client:mozilla-ldap/<ldap_username>/*
auth:create-client:project/releng/*
```
* navigate to [Taskcluster clients](https://tools.taskcluster.net/auth/clients/) and create a new clientId - dedicated for playing with tctalker. 
* it should already be pre-formatted to `mozilla-ldap/<ldap_username>/` at which you can concatenate any string. You can simply add *tctalker*.
* use *queue:** for **Client Scopes**
* hit the **Create Client** button and make sure you save the *Access token* that is generated
* create a json config file (e.g. "config.json") on disk that looks like this:

```
{
    "credentials": {
        "clientId": "you-will-never-guess",
        "accessToken": "nor here!"
    }
}
```

* clone yourself a copy of [tctalker](https://github.com/mozilla/tctalker) and change directory to the clone repo
* run the following:
```
python src/tctalker/tctalker.py --conf config.json <action> <task-id> 
```
# Actions
## 1. Publish in Balrog
* Wait for a go (can come either from RelMan or QE)
* Go to [Balrog beta](https://aus4-admin.mozilla.org/rules#product:firefox%20channel:beta) and find the rule with alias `firefox-beta` (rule id is 32 according to [the comfig](http://hg.mozilla.org/build/buildbot-configs/file/tip/mozilla/release-firefox-mozilla-beta.py.template#l124))
* Update it and point to `Firefox-46.0b4-build2`
* **don't forget to reply to RelMan's email as soon as this step is completed!**

## 2. post release step
* go to the Task Graph and find taskId of `firefox mozilla-beta post release human decision task`
* This task is blocking `firefox mozilla-beta version bump` and `firefox mozilla-beta bouncer aliases` from execution
* To resolve the human decision task run the following:
```
 tctalker --conf ~/.taskcluster/relpro.json report_completed $TASK_ID
```
