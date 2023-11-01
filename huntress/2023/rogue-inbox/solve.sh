#!/bin/bash

grep -o \/f757cb79-dd91-4555-a45e-520c2525d932\\\\\\\\. purview.csv | awk '{print substr($0,length,1)}' | tr -d '\n'
