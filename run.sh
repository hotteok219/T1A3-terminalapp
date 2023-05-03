#!/bin/bash

# check if python is installed
# check if venv already exists
python3 -m venv pwdgen-venv
source pwdgen-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py