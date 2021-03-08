#!/bin/bash

####
## Assumption: you're at the 'oscar' directory.

##
# oscar main folder location
export OSCAR_PATH=/home/kdh/oscar/oscar

##
# add neural_net folder to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$OSCAR_PATH/neural_net
