#!/bin/bash

#ruter_stops=$(curl --request GET "https://reisapi.ruter.no/place/getstopsruter" > test.json)
ruter_stops=$(<test.json)


if [ $# -eq 0 ]; then
    id_stations=${ruter_stops%,\"Name\":\"Forskningsparken \[T\-bane\]*}
    id_stations=${id_stations##*\"ID\":}
    #ID_station=$(echo $ruter_data | grep -E -so '.{0,16}Forskningsparken \[T-bane\].' | cut -c -7)
elif [ "$1" == "Blindern" ]; then
    id_stations=${ruter_stops%,\"Name\":\"Blindern \[T\-bane\]*}
    id_stations=${id_stations##*\"ID\":}
    #ID_station=$(echo $ruter_data | grep -E -so '.{0,16}Blindern \[T-bane\].' | cut -c -7)
elif [ "$1" == "Ullevål stadion" ]; then
    id_stations=${ruter_stops%,\"Name\":\"Ullevål stadion \[T\-bane\]*}
    id_stations=${id_stations##*\"ID\":}
    #ID_station=$(echo $ruter_data | grep -E -so '.{0,16}Ullevål stadion \[T-bane\].' | cut -c -7)
fi

echo $id_stations
#blindern_data=$(curl --request GET "https://reisapi.ruter.no/stopvisit/getdepartures/$ID_station" > stations.json)
#blindern_data=$(<stations.json)
#blindern_departure_time=${blindern_data#*ExpectedDepartureTime}
#blindern_departure_time=${blindern_departure_time#*T}
#blindern_departure_time=${blindern_departure_time%%+*}
#echo $blindern_departure_time
