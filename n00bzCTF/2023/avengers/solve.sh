#!/bin/bash

ffmpeg -i flag.avi -r 1 output_%04d.png

ls -A1 output_*.png > list.txt

tesseract list.txt out

tr -cd '[01]' < out.txt | perl -lpe '$_=pack"B*",$_'

rm list.txt
rm out.txt
rm output_*.png
