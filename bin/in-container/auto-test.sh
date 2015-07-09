#!/bin/bash

EXCLUDE='\.git|\.tmp|\~|\#'

cd $(dirname $0)/../..

clear

while true;
do
    echo
    echo "Listening for file changes, hit CTRL-C a couple times in a row to exit."
    echo
    inotifywait -qr -e CLOSE_WRITE -e CREATE -e MODIFY --exclude ${EXCLUDE} ava/
    ## Sleep briefly, during which time CTRL-C will actually exit the script.
    sleep 2 || exit 1
    clear
    ## Run the test suit, passing in any further arguments wanted.
    ./manage.py test "$@"
done
