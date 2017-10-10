This is the template we used to coordinate on the 56.0 release day with relman.   It could be updated for the next release.  Please keep in mind that 
1) release days and releaseduty folks will change.  2) The update rates etc are unique to each release
----

Current 56.0 release status

Release date and time Thurs Sept 28, 2017 9am PT
Relman representative: lizzard, jcristau
Releng representatives: kmoir, mtabara

1. Fennec 56.0build1 - signed-off  
2. Firefox 56.0build6 - QE signed off on beta-cdntest, release-localtest 
3. Firefox 52.4.0esr - pushed to esr-cdntest channel

Suggestion for action plan for this week

On Thurs:
* RelEng: I prep the WNP release blob in Balrog - use existing release blob for ff56.0-build6
* RelMan: sends us request to push to mirrors (release-cdntest) (ask relman when - from irc Liz said this will be Wed am - do we need a more specific time)
* RelEng: pushes to mirrors, which means all the artifact go under http://archive.mozilla.org/pub/firefox/releases/56.0/
* RelEng manually changes the rule in `Firefox: release-cdntest` to point to WNP-56.0-build6 as follows

Mapping: WNP 56.0-build6
Fallback Mapping: Firefox-55.0.3-build2
Rate: 100%
Version:<56.0

To do: Liz to confirm mappings on release-cdntest - done

* QE starts testing + checks if the actual https://www.mozilla.org/%LOCALE%/firefox/56.0/whatsnew/?oldversion=%OLD_VERSION% page is working live
* QE signs-off on release-cdntest

* RelMan: sends us request to push to release. This step needs to arrive at least 1h prior to the agreed time with marketing when we go live.
* RelEng schedules push-to-release channel in Balrog.  (releng: create second graph, resolve human decision task unblocks balrog scheduling job)
o I was chatting with nth.oma.s|away earlier in this channel and schedule balrog job will likely fail for not having eta set. we'll need to schedule both the changes manually
5:21 AM first we need to amend rule 624 to be < 56.0 to give them the Firefox-56.0-build6-bz2-WNP with fallback to 55.0.3-build2 first
5:22 AM following which we can also amend the default one, that would have normally been triggered by automation, ruleId 145 to will set to serve 56.0-build6 at 100% and 55.0.3-build2 as fallback)

* Relman and releng sign off on the change in balrog. 
At this point
i) this step unblocks the builder which updates the `firefox-latest` bouncer aliases that are referenced from https://www.mozilla.org/en-US/firefox/new/
ii) Only Windows users will get the 56.0 right away since that is the only platform querying the `firefox-stub`. The other platforms are versioned in the downloads page.
iii) after about ~30mins the rest of the platforms from the downloads page will get the 56.0
* RelEng changes the rule in `Firefox: release` to point to WNP-56.0-build6 as follows

Mapping: WNP 56.0-build6
Fallback Mapping: Firefox-55.0.3-build2
Rate: 10%

* RelEng, RelMan, QE signs this off in Balrog and make the change go live
* Rule goes live at the pre-set ETA from this week.
At this point:
i) 10% of user population from release channel gets the update

In 4-6 hours, change the balrog rule so 25% of users get 56.0
To do: Liz to confirm settings on release and provide proposed timeframe when we can disable updates
Disable updates at 9am PT Friday Sept 29

