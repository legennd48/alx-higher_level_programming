#!/usr/bin/env bash
# Script takes an argument (URL) and displays the size of the
# body of the responce in bytes

url=$1

curl -sI $url | grep Content-Length | cut -d' ' -f2
