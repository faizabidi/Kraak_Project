#!/bin/bash

username=$1
CMD1="jupyter-notebook --no-browser --port=7777 &"
CMD2="ps -ef | grep jupyter | grep $username | awk '{print $1, $11}'"
CMD3="ssh -N -f -L localhost:7777:localhost:7777 username@anvil.sv.vt.edu"

# ssh to Anvil, and check if a jupyter notebook is 
# already running under your name
var=$(ssh $username@128.173.49.135 ps -ef | grep jupyter | grep $username | awk '{print $1, $11}')
echo $var

# if jupyter is not running, start a new notebook
# and background it
if [ -z "$var" ]; then
    echo Starting a jupyter notebook
    ssh $username@128.173.49.135 $CMD1
fi

# Open a new terminal, and do a ssh tunneling
#gnome-terminal & disown
