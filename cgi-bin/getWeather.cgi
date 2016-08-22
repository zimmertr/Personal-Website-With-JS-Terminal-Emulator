#!/bin/bash
#Don't forget to add a cronjob to generate the weather.txt file!
#* * * * * weather fips2634000 > /usr/lib/cgi-bin/weather.txt
echo "Content-type: text"
echo ""
cat weather.txt
