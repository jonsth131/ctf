#!/bin/bash

new_file=`tar xfvz $1`

while [[ true ]]; do
    new_file=`tar xfvz $new_file`
done

cat file.txt
