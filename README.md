# Personal Website With JS Terminal Emulator

## LIVE DEMO: https://tjzimmerman.com

## Summary
This repository contains the source code for my personal website. It is principally written in Javascript but also utilizes BASH, HTML5, and CSS. I made this website in an attempt to learn Javascript, but also to make my personal resume website better.

On this webpage, you'll find an interactive terminal emulator that I have built that supports a dozen cool commands meant to mimic the functionality of a UNIX system. You'll also find several sections devoted to links pertaining to me for the Professional, Hobby, and Social aspects of my life. 

The vertical size of the terminal output box can be adjusted by dragging the bottom right corner up and down. This is useful for viewing the contents of the terminal after running multiple commands or commands with large amount of output.

![Alt text](https://raw.githubusercontent.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator/master/Files/screenshot.png "Terminal Emulator")


## Terminal Command Information
Each command has an included manpage. Some of my favorite commands are `health` and `status`. `Health` can be used to query my internal servers for their health stats and `Status` can be used to see the up/down status of each of my servers. For example, try executing `health mimas`. (Mimas is the hostname of one of my internal servers.)

Full list of supported commands:

| Command   | Short Description                              |
|:---------:| ---------------------------------------------- |
| about     | Return information about myself                |
| clear     | Clear the text area                            |
| echo      | Write arguements to STDOUT                     |
| health    | Query a specific server for it's health        |
| help      | List all tjsh commands to STDOUT               |
| history   | Display previously executed commands           |
| ifconfig  | Display server network information             |
| man       | Display the manual page for a command          |
| nslookup  | Query an internet name server for info         |
| ping      | Send an ICMP request to a server               |
| status    | Show the up/down status of all servers         |
| weather   | Show a weather report for the servers location |


## How does it work?

The website is mostly powered by Javascript as it was an excersise to learn Javascript. The primary Javascript file that runs the terminal emulator is called `shell.js` and is located in `/File/js/shell.js`.

The website utilizes  an event handler that listens for an `enter` keypress, your browser's local storage to remember your personal terminal history, and an array of supported commands and their descriptions. 

When a string is sent to the terminal, it is stored as a string which is then compared against strings to represent supported commands. If a match is found, the terminal executes the command with whatever parameters are provided. If an error is made in typing the command or giving a parameter, the terminal will show an appropriate error response for the user. 

Commands that interact directly with internal servers do so by chainloading CGI scripts which function as bash scripts that execute on remote servers. These files can be found in the `cgi-bin` folder in the repository. There is a different script for each command that requires one. All CGI scripts are written using BASH. 

After a command is executed in the shell, the terminal enters its `cleanup` phase. This is used to scroll the output box to the end of the output of the command in case it takes up more space than the terminal has. An empty line is added after the command is ran, and the shell prompt area is cleared of the previous command. 

## Is this safe?

It should be. No commands sent to the terminal emulator are executed locally. Instead, they are matched against a whitelist of supported commands. If a match is found, a separate script is then chainloaded by the server to execute the desired function and the output of the script is then sent back to the server to be displayed on the webpage. If anyone wants to help me with pentesting or XSS I would really appreciate the opportunity for a learning experience. Feel free to email me at tj@tjzimmerman.com if interested.

## Plans for future improvement

There are a ton of things that I would like to add to this project in the future. But the goal of the project was only ever to learn javascript and to improve my website so I have since halted development in favor of focusing my energy on learning other technologies. Some ideas I have for improvement are:

1. Merging the shell prompt and the outbput box into a single field to better mimic the aesthetic of a true terminal shell.  

2. Adding in a `wait` JS clause into the `health` and `status` commands so that the page doesn't freeze while executing commands that take several seconds. 

3. Penetration testing and better security methodologies. Including sanitization and encryption of input/output.  

4. Expanding local storage to create an artifical `filesystem` so that I can support commands like `ls`, `touch`, `mkdir`, `cat`, `echo`, etc.

5. Adding a popup window to display information about me for users who come to the website without shell-proficiency who are also looking to learn about me. 

6. Writing my own weather script to query NOAA so that I don't have to rely on weatherpy.  

7. Loading indication for commands that take several seconds to execute. Such as incrememntal dots. `. . . .`|

8. Discovered bug with nslookup. When entry not found, result passed back is not null. But rather "Can't find...". Fail clause for command is prepared for null and, therefore, will never display. 

9. Allow `health` to accept a second parameter so that a community string can be passed.

10. Make `weather` command perform API call on demand. Rather than on a cron. So as to alleviate load on Wundergroun's Server.

## Requirements to run:  
```
- A webserver  
- PHP (For the execution of provided CGI scripts)  
- Provided CGI scripts placed in /usr/lib/cgi-bin/  
- weatherpy: https://github.com/JackWink/Weather (For obtaining weather information)
- Cronjob to update weather every minute: */5 * * * * /usr/lib/cgi-bin/getWeather.sh
```
