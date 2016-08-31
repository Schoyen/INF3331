#!/bin/bash

if [ $# -lt 3 ]; then # Check if the number of command line arguments are at least 3 (<operator> <arg1> <arg2>)
    echo "Usage: $0 <operator> <arg1> <arg2> ... (optional additional args)";
    exit;
fi

operator=$1; # First argument is the operator
shift; # Get the next argument

if [ $operator == "P" ]; then # Check if <operator> is product
    temp=1; # Set temp to 1 to prevent all answers from being 0
else
    temp=0; # Set temp to 0
fi

while [ $# -gt 0 ] # Loop while there are more command line arguments
do
    case "$operator" in # Pick out the correct operation
        S)
            temp=$(echo "$temp + $1" | bc -l); # Add previous value of temp to the next command line argument
            shift; ;; # Get next argument
        P)
            temp=$(echo "$temp * $1" | bc -l); # Multiply previous value of temp to the next command line argument
            shift; ;; # Get next argument
        M)
            if [ $temp -lt $1 ]; then # Check if temp < current argument
                temp=$1; # If so, current argument is the largest number
            fi
            shift; ;; # Get next argument
        m)
            if [ $temp -gt $1 ]; then # Check if temp > current argument
                temp=$1; # If so, current argument is the smallest number
            fi
            shift; ;; # Get next argument
        *)
            echo "[ERROR]: Wrong operator '$operator', use S, P, M or m (Sum, Product, Maximum or Minimum)";
            exit; ;;
    esac
done
echo $temp # Output the calculated answer
