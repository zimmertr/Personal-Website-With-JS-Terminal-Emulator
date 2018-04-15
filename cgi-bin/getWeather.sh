#!/bin/bash
/usr/bin/weatherpy | /usr/bin/head -n -1 > /var/www/cgi-bin/weather.txt 2>&1
