#!/bin/bash

echo "Installing Requirements"
pip install -r conf/requirements.txt

echo "Installing DB"
python manage.py syncdb --settings=settings.local

echo "Migrating"
python manage.py migrate --settings=settings.local

echo "Install Settings"
python manage.py loaddata settings_data.json --settings=settings.local

echo "Run Server"
python manage.py runserver --settings=settings.local

