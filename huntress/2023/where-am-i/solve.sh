#!/bin/bash

exiftool PXL_20230922_231845140_2.jpg | grep "Image Description" | cut -d ':' -f 2 | tr -d ' '| base64 -d | tr ')' '}'
