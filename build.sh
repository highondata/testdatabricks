#!/bin/bash

rm -r *.egg-info build dist
python3 -m unittest -v tests/*.py && python3 setup.py sdist bdist_wheel
rm -r *.egg-info build

