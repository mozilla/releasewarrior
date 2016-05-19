# releasewarrior

your assistant while on releaseduty

![squirrel spartan](https://pbs.twimg.com/profile_images/571907614906310658/HDB_I-Nr.jpeg)


In the spirit of [taskwarrior](https://taskwarrior.org/), releasewarrior is a tool that manages and provides a checklist for human decision tasks with releases in flight while providing documentation and troubleshooting for each task.

Rather than manually updating a wiki, releasewarrior provides commands for creating, updating, and completing releases. It does this by managing a json data file and a markdown wiki file for each release.

## Getting Started

get copy of releasewarrior
```
git clone https://github.com/lundjordan/releasewarrior
cd releasewarrior
```
install it in your virtual python environment
```
mkvirtualenv --python=/path/to/python3 releasewarrior
python setup.py install
```

## Using Commands

**pro tip**: use `release --help` and `release <subcommand> --help` lots

prior to each command your local master can not be behind origin/master. this is enforced and by design so that you always have the must up to date state

#### create new release checklist

usage: `release create $PRODUCT $BRANCH $VERSION`

example: `release create fennec beta 27.0b6`

#### update existing release checklist

usage: `release update $PRODUCT $BRANCH $VERSION --$UPD`

example: `release update firefox release-rc 26.0 --submitted-shipit --published-balrog --issue "osx compile timeout. retriggered`

#### checking current state of releases

let's do something more interesting

usage: `release status`

#### creating a postmortem

usage: `release postmortem $DATE_OF_POSTMORTEM`

example: `release postmortem 2014-06-20`

## semi-manually updating releasewarrior

of course, given that the data is just a json file and changes tracked by this repo's revision history itself, you can always manually update the data and have the tool re-create the wiki

usage: `release sync firefox esr 27.0esr`

## completely manually updating releasewarrior

you could even update the data, the associated wiki, and just commit the changes yourself.

## hand waving

* releasewarrior only knows about the `origin` remote (whatever that points to in your local copy's .git/config. It also doesn't have knowledge of any branches so best stay on `master`.
  * however saying that, feel free to fork this repo to play around. that way you don't need to rewrite revision history after you are done experimenting
* there are not templates for Thunderbird yet. I'll add support for that soon
* there are no tests because I'm a bad developer
