#!/bin/bash
#Return list of IP Addresses
#	nmap -nsP 192.168.1.1/24 | grep '192.168.1.*' | awk '{print $5}'
#Return comma deliminated list of hostname,ip.address
#	nslookup jupiter | sed '1,4d' | sed '$d' | awk '{print $2}' | tr --delete '\n'
#Check if hostname exists. Return 1 if so:
#	if ($(getent hosts $hostname | wc -l) -de 1);

#Echo iplist into nslookup command to get list of comma deliminated hostname:ipaddress
#Check comma deliminated list for existence of query string
#if query found, execute getInfo.sh with both parameters to retrieve snmp info without showing com. string.

