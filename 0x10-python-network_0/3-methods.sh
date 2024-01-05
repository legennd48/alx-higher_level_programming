#!/bin/bash
# Script takes argument(URL) and lists all allowed methods
curl -sI "$1" | grep 'Allow' | cut -d' ' -f2-
