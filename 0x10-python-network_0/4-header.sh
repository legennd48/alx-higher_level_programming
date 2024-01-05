#!/bin/bash
# Sends header variable along with request and displays body of response
curl -sLH "X-School-User-Id: 98" "$1"
