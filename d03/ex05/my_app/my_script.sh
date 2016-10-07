#!/bin/sh

virtualenv --python=python3 django_venv; source django_venv/bin/activate
pip --version
pip install -r requirement.txt
cd helloworld
python manage.py runserver