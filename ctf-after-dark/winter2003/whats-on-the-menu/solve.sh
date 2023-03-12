#!/bin/bash

curl -s -X POST https://whats-on-the-menu.acmcyber.com/ -H 'User-Agent: MenuBrowser' -H 'Referer: https://yelp.com' | grep flag | sed 's/.*\(flag{.*}\).*/\1/'
