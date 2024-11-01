#!/bin/bash

if ! [ -x "$(command -v minimodem)" ]; then
  echo 'Error: minimodem is not installed.' >&2
  exit 1
fi

minimodem --rx 1200 -f transmissions.wav
