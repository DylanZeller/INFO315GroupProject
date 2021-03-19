#!/bin/bash
# Install requirements and gen fake data
python -m pip install -r requirements.txt
python scripts/gen_fake_data.py

# Build python package and install
python -m pip install --upgrade wheel
python setup.py sdist bdist_wheel
python -m pip install --force-reinstall dist/db_wrapper-0.0.1-py3-none-any.whl