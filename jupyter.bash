#!/bin/bash

username=$1

# ssh to Anvil, and start a jupyter notebook
ssh $1@128.173.49.135
jupyter-notebook --no-browser --port=7777
