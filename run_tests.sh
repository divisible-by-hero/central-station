#!/bin/bash

echo "** Running Unit Tests **"

echo "** Core **"
coverage -x manage.py test core --settings=settings.local

echo "** WRITING COVERAGE **"
coverage html -d ./reports/coverage_html
coverage -r -m >./reports/coverage_report.txt
