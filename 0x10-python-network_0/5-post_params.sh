#!/bin/bash
# Sends data via POST request to URL passed as argument
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
