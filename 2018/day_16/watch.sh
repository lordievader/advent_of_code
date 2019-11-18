#!/bin/bash
while inotifywait -e close_write *.py; do
    pytest -s
done
