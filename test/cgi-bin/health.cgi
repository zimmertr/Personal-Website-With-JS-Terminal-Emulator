#!/bin/bash

echo "Content-type: text"
echo


comstring=$(nslookup $QUERY_STRING | tail -n 2 | awk '{print $2}')

#############
#Check to see if the query string exists in your DNS
############
if ((($(getent hosts $QUERY_STRING | wc -l)) == 0)); 
then
	printf "$QUERY_STRING is not a valid internal host.\n"
else


	echo $QUERY_STRING - System Information
	echo ""


	#############
	#Print CPU usage for each core. For some reason printf wouldn't display anything other than the first parameter. Had to use echo which means escape characters
	#like \t and \t aren't supported. 
	#############
	echo "CPU Usage:          $(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.25.3.3.1.2 2> /dev/null | awk '{print $4}' | sed ':a;N;$!ba;s/\n/%, /g')%"


	#############
	#Print used and total system memory
	#############
	memTotalReal=$(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING 1.3.6.1.4.1.2021.4.5.0 | awk '{print $4/1024000}' | cut -c 1-4)
	memAvailReal=$(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING 1.3.6.1.4.1.2021.4.6.0 | awk '{print $4/1024000}' | cut -c 1-4) 
	memBuffer=$(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING 1.3.6.1.4.1.2021.4.14.0 | awk '{print $4/1024000}' | cut -c 1-4)
	memCache=$(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING 1.3.6.1.4.1.2021.4.15.0 | awk '{print $4/1024000}' | cut -c 1-4)

	memFree=$(awk "BEGIN {print $memAvailReal + $memBuffer + $memCache; exit}")
	memUsed=$(awk "BEGIN {print $memTotalReal - $memFree; exit}")
	memPercent=$(awk "BEGIN {print ($memUsed / $memTotalReal)*100; exit}" | cut -c 1-4)

	printf "Memory Usage:\t$memUsed GB/$memTotalReal GB ($memPercent%%)\n"


	#############
	#Print swap space usage
	#############

	swapTotal=$(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.4.3.0 | awk '{print $4/1024000}' | cut -c 1-4)
	swapAvail=$(snmpwalk -v2c -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.4.4.0 | awk '{print $4/1024000}' | cut -c 1-4)

	swapUsed=$(awk "BEGIN {print $swapTotal - $swapAvail; exit}")
	swapPercent=$(awk "BEGIN {print ($swapUsed/ $swapTotal)*100; exit}" | cut -c 1-4)

	#Checking to see if the host has a swap space partition
	
	if [[ -z "$swapPercent" ]];
	then
		printf "Swap Usage:\t$swapUsed GB / $swapTotal GB ($swapPercent%%)\n"
	else
		printf "Swap Usage:\t$swapUsed GB / $swapTotal GB (0%%)\n"
	fi


	#############
	#Print 1, 5, and 15 minute load averages separated by tabs.
	#############
	printf "System Load:\t1M: $(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.10.1.3.1 2> /dev/null | awk '{print $4}' | tr -d '""') \t5M: $(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.10.1.3.2 2> /dev/null | awk '{print $4}' | tr -d '""') \t15M: $(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.4.1.2021.10.1.3.3 2> /dev/null | awk '{print $4}' | tr -d '""')\n"


	#############
	#Print number of users logged in
	#############
	printf "System Users:\t$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.5 | awk '{print $4}')\n"


	#############
	#Print number of users processes running on machine
	#############
	printf "Running Processes:\t$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.6 | awk '{print $4}')\n"


	#############
	#Print system uptime. SNMP output changes once > 24 hours. Had to do some hacking to get it to always look the same.
	#############
	uptime=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}')

	if [[ ${uptime} == *":"* ]];
	then
		days=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $5}')
		hours=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}' | cut -f1 -d ":")
		minutes=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}' | cut -d: -f2)
		seconds=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING .1.3.6.1.2.1.1.3.0 2> /dev/null | awk '{print $7}' | awk -F ":" '{print $3}' | cut -c 1-2)

		printf "System Uptime:\t$days days, $hours hours, $minutes minutes, $seconds seconds\n"
	else
		days=0
		hours=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.1 | awk '{print $5}' | cut -f1 -d ":")
		minutes=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.1 | awk '{print $5}' | cut -d: -f2)
		seconds=$(snmpwalk -t .5 -Os -c $comstring -v 2c $QUERY_STRING 1.3.6.1.2.1.25.1.1 | awk '{print $5}' | awk -F ":" '{print $3}' | cut -c 1-2)

		printf "System Uptime:\t0 Days, $hours hours, $minutes minutes, $seconds seconds\n"
	fi
fi
