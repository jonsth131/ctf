#!/bin/bash

apktool d jninjaspeak.apk

strings jninjaspeak/lib/x86_64/* | grep -i "flag"

rm -rf jninjaspeak
