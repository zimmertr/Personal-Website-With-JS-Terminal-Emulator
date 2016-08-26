# Website With JS Terminal Emulator
This repository is a clone of my personal website. I made it both as a way to learn javascript and as a way to 'refresh" my old site. On it you will find an interactive shell created in javascript that can execute many different commands. 

root@tjsh > help
The following commands are supported: 

clear:		Clear the text area.  
echo:		Display a specified line of text.  
help:		Print a list of commands and their descriptions.  
history:	Display previously executed commands.  
info:		Query a specific server for its health information.  
ipaddr:		Display connection information for the web server.  
man:		Display the manual for a specified command.  
nslookup:	Query an internet name server for information.  
ping:		Send an ICMP request to a webserver and display the response.  
status:		Show the current status of all servers.  
weather:	Show a weather report for the location of the server.  

Requirements to run:   
-A webserver (Using Apache)  
-php (For scripts to run)  
-Provided scripts placed in /usr/lib/cgi-bin/  
-weatherpy: https://github.com/cmcdowell/weatherpy  
-Cronjob to update weather every minute: * * * * * weather fips2634000 > /usr/lib/cgi-bin/weather.txt  
