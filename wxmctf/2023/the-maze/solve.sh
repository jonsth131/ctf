#!/bin/bash

curl -s https://weba.jonathanw.dev:3001/room/0 | grep -oE "wxmctf{.*}"
