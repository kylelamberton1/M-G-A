#!/bin/bash

echo "Test stage"

python3 -m venv venv
source venv/bin/activate

pip3 install pytest flask_testing
pip3 install -r requirements.txt

mkdir test_reports

python3 -m pytest --cov=application \
    

deactivate
rm -rf venv