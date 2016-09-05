#!/bin/bash


# This script is pretty slow as it does two API-calls. The first call is used to get information about all
# the stops Ruter has. From this call, using substring removal, we get the ID of the desired station. It is
# possible to just hardcode the ID into each station, but I found it amusing to be able to get information
# about all the subway stops (and busses, etc).

ruter_stops=$(curl --request GET "https://reisapi.ruter.no/place/getstopsruter") # Download information about all stops
direction=0 # Set a default direction, i.e both --E and --W

station_name="Forskningsparken" # Default station
id_stations=${ruter_stops%,\"Name\":\"Forskningsparken \[T\-bane\]*} # Use substring removal to get the correct field
id_stations=${id_stations##*\"ID\":} # Locate the ID of the subway using substring removal

if [ "$1" == "--E" ]; then # Check if additional parameters were specified
    direction=1 # Set new correct direction, --E
    shift # Get the next argument
elif [ "$1" == "--W" ]; then
    direction=2 # Set the new correct direction --W
    shift # Get the next argument
fi


if [ "$1" == "Blindern" ]; then # Check if a station was supplied
    station_name="Blindern" # Set new correct station name
    id_stations=${ruter_stops%,\"Name\":\"Blindern \[T\-bane\]*} # Use substring removal to get the correct field
    id_stations=${id_stations##*\"ID\":} # Locate the ID of the correct subway
elif [ "$1" == "Ullevål stadion" ]; then
    station_name="Ullevål stadion"
    id_stations=${ruter_stops%,\"Name\":\"Ullevål stadion \[T\-bane\]*}
    id_stations=${id_stations##*\"ID\":}
fi

station_data=$(curl --request GET "https://reisapi.ruter.no/stopvisit/getdepartures/$id_stations") # Download information about the desired stop
clear # Clear screen for new output


printf "\t====Departures from $station_name====\n"
for i in 1 2 3 4 5 6 # Loop six times
do

    published_line_name=${station_data#*\"PublishedLineName\":\"} # Get the subway line number
    station_data=$published_line_name # Store temporary new string as we are gradually "eating into" the string
    direction_name=${published_line_name#*\"DirectionName\":\"} # Get the direction as either 1 or 2
    destination_name=${direction_name#*\"DestinationName\":\"} # Get the name of the subway
    expected_departure_time=${destination_name#*\"ExpectedDepartureTime\":\"*T} # Get the departure time from the station
    expected_departure_time=${expected_departure_time%%+*} # Remove everything but the departure time
    destination_name=${destination_name%%\",*} # Remove everyting but the name of the subway
    direction_name=${direction_name%%\",*} # Remove everything but the direction number
    published_line_name=${published_line_name%%\",*} # Remove everything but the line number

    if [ $direction == "1" ]; then # Check if a desired direction has been specified
        if [ $direction_name == "1" ]; then # Check if the current subway is going the correct way
            printf "Line $published_line_name: $destination_name (East) platform $direction_name @ $expected_departure_time\n"
        fi
    elif [ $direction == "2" ]; then
        if [ $direction_name == "2" ]; then
            printf "Line $published_line_name: $destination_name (West) platform $direction_name @ $expected_departure_time\n"
        fi
    else
        if [ $direction_name == "1" ]; then
            printf "Line $published_line_name: $destination_name (East) platform $direction_name @ $expected_departure_time\n"
        elif [ $direction_name == "2" ]; then
            printf "Line $published_line_name: $destination_name (West) platform $direction_name @ $expected_departure_time\n"
        fi
    fi

done
