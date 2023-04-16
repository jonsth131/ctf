#!/bin/bash

dig www.jerseyctf.com TXT | grep -oE 'jctf{.*}' 
