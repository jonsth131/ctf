#!/bin/bash
URL="http://thesanitizationstation-1.play.hackaplaneten.se:8000"

echo "Starting ngrok..."
ngrok http 8000 > /dev/null &
sleep 5
ngrok_pid=$!

export NGROK_URL=$(curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

echo "Using ngrok url: $NGROK_URL"

python3 solve.py "$NGROK_URL" "$URL"

kill $ngrok_pid
