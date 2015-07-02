#!/bin/bash

FLAKE8_ARGUMENTS="--first --ignore=E501"

cd $(dirname $0)/../

find ava -name '*.py' | xargs flake8 ${FLAKE8_ARGUMENTS}


