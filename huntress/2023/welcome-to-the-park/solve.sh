#!/bin/bash

curl -s https://gist.githubusercontent.com/stuartjash/a7d187c44f4327739b752d037be45f01/raw/4ea401db574d5cceb0ba517feb9f84971136f067/JohnHammond.jpg -o - | strings | grep -oE 'flag{.*}'
