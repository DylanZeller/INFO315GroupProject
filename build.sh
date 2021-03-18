#!/bin/bash

python -m pip install --upgrade wheel

python setup.py sdist bdist_wheel

python -m pip install --force-reinstall dist/db_wrapper-0.0.1-py3-none-any.whl