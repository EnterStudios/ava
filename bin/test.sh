#!/bin/bash

set -e

## Use docker-compose to run the AVA test suite.

cd $(dirname $0)/..

docker-compose run --rm web ./manage.py test -v2
