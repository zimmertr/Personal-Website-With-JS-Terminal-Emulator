#!/bin/bash

echo "Content-type:\ttext"
echo

up=0
down=-1
#Alright. I know you're probably like "What the fuck? Why is that being instantiated as .2? Well, the truth is. I HAVE NO IDEA. For some reason /dev/tcp ALWAYS sets $down to 1 after it has been ran. Even if it's alive and it sets $up to 1 as well. So.. well this is my fix. Not sure if the same bug applies to $up or not... but my tests are showing the proper amount of servers are being returned with it being instatiated at 0. So ima leave it. whatever.

printf "**********Services**********\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/2000" && printf "Apache:\t\t\tUp\n" || printf "Apache:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/2000" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/io.sol.milkyway/53" && printf "BIND:\t\t\tUp\n" || printf "BIND:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/io.sol.milkyway/53" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8112" && printf "Deluge:\t\t\tUp\n" || printf "Deluge:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8112" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/mimas.sol.milkyway/3000" && printf "Grafana:\t\tUp\n" || printf "Grafana:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/mimas.sol.milkyway/3000" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/mimas.sol.milkyway/8086" && printf "InfluxDB:\t\tUp\n" || printf "InfluxDB:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/mimas.sol.milkyway/8086" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/io.sol.milkyway/19999" && printf "Netdata IO:\t\tUp\n" || printf "Netdata IO:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/io.sol.milkyway/19999" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/19999" && printf "Netdata Jupiter:\tUp\n" || printf "Netdata Jupiter:\tDown\n"
timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/19999" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/mimas.sol.milkyway/19999" && printf "Netdata Mimas:\t\tUp\n" || printf "Netdata Mimas:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/mimas.sol.milkyway/19999" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/19999" && printf "Netdata Saturn:\t\tUp\n" || printf "Netdat Saturn:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/19999" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8080" && printf "NextCloud:\t\tUp\n" || printf "NextCloud:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8080" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/tjzimmerman.com/443" && printf "Nginx:\t\t\tUp\n" || printf "Nginx:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/tjzimmerman.com/443" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/943" && printf "OpenVPN:\t\tUp\n" || printf "OpenVPN:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/943" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/80" && printf "Pi-Hole:\t\tUp\n" || printf "Pi-Hole:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/80" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/53" && printf "Pi-Hole DNS:\t\tUp\n" || printf "Pi-Hole DNS:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/53" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/32400" && printf "Plex Media Server:\tUp\n" || printf "Plex Media Server:\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/32400" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/9000" && printf "Portainer:\t\tUp\n" || printf "Portainer:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/9000" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8006" && printf "Proxmox:\t\tUp\n" || printf "Proxmox:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8006" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/7878" && printf "Radarr:\t\t\tUp\n" || printf "Radarr:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/7878" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8989" && printf "Sonarr:\t\t\tUp\n" || printf "Sonarr:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8989" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8181" && printf "Tautulli:\t\tUp\n" || printf "Tautulli:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/8181" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/8443" && printf "Unifi Controller:\tUp\n" || printf "Unifi Controller:\tDown\n"
timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/8443" && let up++ || let down++

timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/9510" && printf "Unified Remote:\t\tUp\n" || printf "Unified Remote:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/9510" && let up++ || let down++

printf "\n**********Hardware**********\n"

timeout .2 bash -c "</dev/tcp/hubble.sol.milkyway/22" && printf "Hubble:\t\t\tUp\n" || printf "Hubble:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/hubble.sol.milkyway/22" && let up++ || let down ++

timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/22" && printf "Jupiter:\t\tUp\n" || printf "Jupiter:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/jupiter.sol.milkyway/22" && let up++ || let down ++

timeout .2 bash -c "</dev/tcp/laniakea.sol.milkyway/80" && printf "Laniakea:\t\tUp\n" || printf "Laniakea:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/laniakea.sol.milkyway/80" &&let up++ || let down++ 

timeout .2 bash -c "</dev/tcp/mercury.sol.milkyway/22" && printf "Mercury:\t\tUp\n" || printf "Mercury:\t\tDown\n"
timeout .2 bash -c "</dev/tcp/mercury.sol.milkyway/22" && let up++ || let down ++

timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/22" && printf "Saturn:\t\t\tUp\n" || printf "Saturn:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/saturn.sol.milkyway/22" && let up++ || let down ++

timeout .2 bash -c "</dev/tcp/sol.sol.milkyway/22" && printf "Sol:\t\t\tUp\n" || printf "Sol:\t\t\tDown\n"
timeout .2 bash -c "</dev/tcp/sol.sol.milkyway/22" && let up++ || let down ++

echo
echo "----------------"
echo "Servers Up:   $up"
echo "Servers Down: $down"
