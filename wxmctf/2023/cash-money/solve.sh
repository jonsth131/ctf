#!/bin/bash

grep COUNTRY cards.txt | cut -d ":" -f2 | cut -c2-2 | tr -d '\n' | rev
