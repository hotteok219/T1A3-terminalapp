#!/bin/bash

# Check if python is installed.
if [[ -x "$(command -v python)" ]]
then
    echo "The Password Generator needs Python in order to run. Please go to https://www.python.org/downloads/ to download and install Python." >&2
    exit 1
else
    # Check if venv already exists.
    if [[ -d "pwdgen-venv" ]]
    then
        echo "pwdgen-venv already exists. Activating it now."
        source pwdgen-venv/bin/activate
        echo "pwdgen-venv has been activated."
    else
        echo "pwdgen-venv doesn't exist yet. Creating it now, please wait."
        python3 -m venv pwdgen-venv
        source pwdgen-venv/bin/activate
        echo "pwdgen-venv has been created and activated."
    fi
    # Install requirements.
    echo "Installing required packages."
    pip3 install -r requirements.txt
    echo "Required packages installed."
    clear
    # Run application.
    python3 main.py
fi