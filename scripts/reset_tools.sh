#!/bin/bash

ssh -i your_staging-ffxbld_private_key_location stage-ffxbld@hg.mozilla.org edit tools 1 YES
ssh -i your_staging-ffxbld_private_key_location stage-ffxbld@hg.mozilla.org clone tools build/tools
