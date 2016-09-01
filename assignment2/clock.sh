#!/bin/bash

while [ "true" ] # Run until CTRL-c is encountered
do
    clear # Clear terminal

    if [ "$1" == "--AMPM" ]; then # Check if additional argument is "--AMPM"
        date=$(date +"%r") # If so, get the time as a 12-hour clock
    else
        date=$(date +"%T") # If not, get time as a 24-hour clock
    fi

    echo $date # Output the time
    sleep 1 # Sleep for one second, before repeating
done
