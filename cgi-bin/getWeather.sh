#!/bin/bash
/usr/bin/weatherpy | /usr/bin/head -n -1 > /usr/lib/cgi-bin/weather.txt 2>&1
