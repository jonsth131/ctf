#!/bin/bash

strings flag.zip | grep CIT | sort | uniq -u
