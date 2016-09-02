#!/bin/bash

ruter_stops=$(curl --request GET "https://reisapi.ruter.no/place/getstopsruter")
#ruter_stops=$(<test.json)
direction=0

id_stations=${ruter_stops%,\"Name\":\"Forskningsparken \[T\-bane\]*}
id_stations=${id_stations##*\"ID\":}

if [ "$1" == "--E" ]; then
    direction=1
    shift
elif [ "$1" == "--W" ]; then
    direction=2
    shift
fi


if [ "$1" == "Blindern" ]; then
    id_stations=${ruter_stops%,\"Name\":\"Blindern \[T\-bane\]*}
    id_stations=${id_stations##*\"ID\":}
elif [ "$1" == "Ullevål stadion" ]; then
    id_stations=${ruter_stops%,\"Name\":\"Ullevål stadion \[T\-bane\]*}
    id_stations=${id_stations##*\"ID\":}
fi

station_data=$(curl --request GET "https://reisapi.ruter.no/stopvisit/getdepartures/$id_stations")
#station_data=$(<stations.json)
clear

for i in 1 2 3 4 5 6; do

    published_line_name=${station_data#*\"PublishedLineName\":\"}
    station_data=$published_line_name
    direction_name=${published_line_name#*\"DirectionName\":\"}
    destination_name=${direction_name#*\"DestinationName\":\"}
    expected_departure_time=${destination_name#*\"ExpectedDepartureTime\":\"*T}
    expected_departure_time=${expected_departure_time%%+*}
    destination_name=${destination_name%%\",*}
    direction_name=${direction_name%%\",*}
    published_line_name=${published_line_name%%\",*}

    echo "$published_line_name: $destination_name ($direction_name) @ $expected_departure_time"

done
