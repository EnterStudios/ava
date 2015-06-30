#!/bin/bash

## Use docker-compose to run the AVA test suite.

cd $(dirname $0)/..

docker-compose run --rm web src/manage.py test -v2
