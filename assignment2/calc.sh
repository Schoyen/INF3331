#!/bin/bash

if [ $# -lt 3 ]; then # Check if the number of command line arguments are at least 3 (<operator> <arg1> <arg2>)
    echo "Usage: ./calc.sh <operator> <arg1> <arg2> ... (optional additional args)"
    exit
fi
