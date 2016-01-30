#!/bin/bash

## This script is used as the 'entry point' for the application
## server docker container. It runs 'migrate' on every start to
## ensure the database is built, and then executes the internal
## Django devserver.

DIRECTORY=$(dirname $0)/../..
PYTHON=python
MANAGE=${DIRECTORY}/manage.py

celery worker -A ava_core.celery_app -l debug
