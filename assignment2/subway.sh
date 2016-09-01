#!/bin/bash

#ruter_data=$(curl --request GET "https://reisapi.ruter.no/place/getstopsruter")
ruter_data=$(<test.json)
ID_blindern=$(echo $ruter_data | grep -E -so '.{0,16}Blindern \[T-bane\].' | cut -c -7)
#blindern_data=$(curl --request GET "https://reisapi.ruter.no/stopvisit/getdepartures/$ID_blindern")
blindern_data=$(<blindern.json)
blindern_departure_time=${blindern_data#*ExpectedDepartureTime}
blindern_departure_time=${blindern_departure_time#*T}
blindern_departure_time=${blindern_departure_time%%+*}
echo $blindern_departure_time
