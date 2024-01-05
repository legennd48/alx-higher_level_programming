#!/bin/bash
# Script takes an argument (URL) and displays the size of the body in bytes
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
