#!/bin/bash

VENV_NAME="venv"

python3 -m venv $VENV_NAME

source $VENV_NAME/bin/activate

pip3 install -r requirements.txt

streamlit run autoddit.py