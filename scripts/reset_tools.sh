#!/bin/bash

ssh -i staging-ffxbld_rsa stage-ffxbld@hg.mozilla.org edit tools 1 YES
ssh -i staging-ffxbld_rsa stage-ffxbld@hg.mozilla.org clone tools build/tools
