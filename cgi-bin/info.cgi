#!/bin/bash

echo "Content-type: text"
echo

comstring=$(nslookup $QUERY_STRING | tail -n 2 | awk '{print $2}')
echo $QUERY_STRING - System Information
echo ""




#Print system uptime. SNMP output changes once > 24 hours. Had to do some hacking to get it to always look the same.
uptime=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}')

if [[ ${uptime} == *":"* ]];
then
	days=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $5}')
	hours=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}' | cut -f1 -d ":")
	minutes=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}' | cut -d: -f2)
	seconds=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}' | awk -F ":" '{print $3}' | cut -c 1-2)

	printf "Uptime:\t$days days, $hours hours, $minutes minutes, $seconds seconds\n"
else
	days=0
	hours=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.1 | awk '{print $5}' | cut -f1 -d ":")
	minutes=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.1 | awk '{print $5}' | cut -d: -f2)
	seconds=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.1 | awk '{print $5}' | awk -F ":" '{print $3}' | cut -c 1-2)

	printf "Uptime:\t0 Days, $hours hours, $minutes minutes, $seconds seconds\n"
fi




#Print CPU usage for each core. For some reason printf wouldn't display anything other than the first parameter. Had to use echo which means escape characters
#like \t and \t aren't supported. 
echo "CPU:                $(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.25.3.3.1.2 2> /dev/null | awk '{print $4}' | sed ':a;N;$!ba;s/\n/%, /g')%"




#Print used and total system memory
printf "Memory:\tUsed: \tTotal: $(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.2.2 | awk '{print $4/1024000}' | cut -c 1-4) GB\n"




#Print 1, 5, and 15 minute load averages separated by tabs.
printf "Load:\t1M: $(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.10.1.3.1 2> /dev/null | awk '{print $4}' | tr -d '""') \t5M: $(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.10.1.3.2 2> /dev/null | awk '{print $4}' | tr -d '""') \t15M: $(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.10.1.3.3 2> /dev/null | awk '{print $4}' | tr -d '""')\n"





