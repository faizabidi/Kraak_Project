#!/bin/bash

username=$1
<<<<<<< HEAD

if [ $# -eq 0 ]; then
    echo "Please pass your username as the argument"
    exit
fi

=======
>>>>>>> a54d6f14afdf451658afcdb2d20367933ed0b3c5
CMD1="jupyter-notebook --no-browser --port=7777 &"
CMD2="ssh -N -f -L localhost:7777:localhost:7777 $username@anvil.sv.vt.edu"

# ssh to Anvil, and check if a jupyter notebook is 
# already running under your name

var=$(ssh $username@128.173.49.135 ps -ef | grep jupyter | grep $username | awk '{print $1, $11}')
<<<<<<< HEAD
=======
echo $var
>>>>>>> a54d6f14afdf451658afcdb2d20367933ed0b3c5

# If jupyter is not running, start a new notebook and background it
if [ -z "$var" ]; then
    echo Starting a jupyter notebook
    ssh -f $username@128.173.49.135 $CMD1
fi

<<<<<<< HEAD
# Open a new terminal, and create a ssh tunnel
# Kill any localhost process runnig on port 7777

pkill -f localhost
xterm -hold -e $CMD2
=======
# Open a new terminal, and do a ssh tunneling
#gnome-terminal & disown
>>>>>>> a54d6f14afdf451658afcdb2d20367933ed0b3c5
