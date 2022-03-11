#!/bin/bash

echo "Test stage"

python3 -m venv venv
source venv/bin/activate

pip3 install pytest flask_testing
pip3 install -r requirements.txt

mkdir test_reports

python3 -m pytest --cov=application \
    --cov=frontend/application \
    --cov-report term-missing \
    --cov-report xml:test_reports.xml 
    --junitxml=junit_report.xml

deactivate
rm -rf venv