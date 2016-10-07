#!/bin/sh

virtualenv --python=python3 local_lib; source local_lib/bin/activate
pip --version
pip install git+https://github.com/jaraco/path.py.git -I --log install.log
python my_program.py