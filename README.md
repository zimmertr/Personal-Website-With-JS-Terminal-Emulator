#Website With JS Terminal Emulator

This repository contains the source code for my personal website. It is principly written in Javascript but also utilizes BASH, HTML5, and CSS. 

I made this website in an attempt to learn Javascript, but also to make my personal resume website better.

On this webpage, you'll find an interactive terminal emulator that I have built. It doesn't have an artificial filesystem attached to it, but it supports a series of cool commands.

![Alt text](https://raw.githubusercontent.com/zimmertr/Website-With-JS-Terminal-Emulator/Files/screenshot.png "Terminal Emulator")

Each command has an included manpage. Some of my favorite commands are `health` and `status`. `Health` can be used to query my internal servers for their health stats and `Status` can be used to see the up/down status of each of my servers. 


Requirements to run:
-A webserver (Using Apache)
-php (For scripts to run)
-Provided scripts placed in /usr/lib/cgi-bin/
-weatherpy: https://github.com/cmcdowell/weatherpy
-Cronjob to update weather every minute: * * * * * /usr/lib/cgi-bin/getWeather.sh
