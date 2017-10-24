#!/bin/bash

if [ $# != 1 ]; then
	echo "usage: reset_tools.sh location_of_your_stage-ffxbld_staging_key"
    exit
fi

K=$1

ssh -i $K stage-ffxbld_private_key_location stage-ffxbld@hg.mozilla.org edit tools 1 YES
ssh -i $K stage-ffxbld@hg.mozilla.org clone tools build/tools
