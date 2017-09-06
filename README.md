# Personal Website With JS Terminal Emulator

__LIVE DEMO:__ https://tjzimmerman.com

## Summary
This Web Application is mostly written in Javascript. But also utilizes BASH, Perl, and Python in the backend. I made it both in an attempt to learn Javascript and to improve my personal website. In retrospective it was a poor decision to to use cgi scripts in the backend. I recognize now that a web API would have been a much better design. A future rewrite may, perhaps, include that revision. 

<p align="center">
  <img src="https://raw.githubusercontent.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator/master/screenshot.png" height="500">
</p>


## Terminal Command Information
Each command has an included manpage that can be accessed with `man >command<`. Some of my favorite commands are `health` and `status`. `Health` can be used to query my internal servers for their system & resource information and `Status` can be used to evaluate the up/down status of each of my servers. For example, try executing `health janus`. (Janus is the hostname of one of my internal servers.)

*Full list of supported commands:*

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

The application is quite simple. An event handler is spawned by `shell.js` that listens for STDINN. When a query is detected, the string in the `input field` is parsed and stored as a variable. It is then compared against a whitelist of commands. If a match is detected, one of two things will happen.

1. If the command is simple enough in nature, `man for example`, javascript can handle it will and proceed to do so.
2. If the command is complex or involves communication with my internal network, then a separate cgi script is chainloaded to complete the task. 

The resulting output is then returned to the terminal as STDOUT/STDERR. After a command has finished executing, the terminal enters the `cleanup` phase. This is used to scroll the output box to the end of STDOUT/STDERR in the event that it takes up more lines than are available. The `input field` is then purged of the executed command and a new line is inserted following the output to prepare for another command.

Some other notable things: 
```
- The application supports moderate error handling for both server-side and PEBKAC issues.
- The browser's local storage is leveraged to persist a .tjsh_history file, of sorts. for `history`.
- The vertical size of the outbox box can be adjusted by dragging the bottom right corner up and down. 
```


## Is this safe?

I _think_ so. Any commands that interact with my internal network are matched against a whitelist first. If a match is found, a separate script is then chainloaded by the server and the output is sent back to the server. If anyone wants to help me with pentesting or XSS I would really appreciate the opportunity for a learning experience. Feel free to email me at tj@tjzimmerman.com if interested.


## Mobile website

If you haven't seen the Family Guy .gif poking fun at CSS with Peter adjusting the blinds on a window, you should go Google it now. I won't pretend to be a web developer, so my CSS is pretty lousy. I've tried my best to make this website mobile friendly but it is still less dynamic than desired. Much help would be appreciated in this area. 

<p align="center">
  <img src="https://raw.githubusercontent.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator/master/screenshot_mobile.png" height="500">
</p>

## Plans for future improvement

There are a ton of things that I would like to add to this project in the future. But the goal of the project was only ever to learn javascript and to improve my website so I have since halted development.

_Some ideas I have for improvement are:_
```
1. Merging the shell prompt and the outbput box into a single field to better mimic the aesthetic of a true terminal shell.  

2. Making commands async to the browser to avoid page hangs.

3. Penetration testing. Including sanitization and encryption of input/output.  

4. Expanding local storage to create an artifical `filesystem` so that I can support commands like `ls`, `touch`, `mkdir`, & `cat`.

5. Writing my own weather script to query NOAA so that I don't have to rely on weatherpy.  

6. Migration from leveraging CGI scripts in the backend to a full web API for my domain. More secure, dynamic, and efficient.

7. Progress indication for commands that take several seconds to execute. Such as incrememntal dots. `. . . .`|

8. Fix bug with nslookup where an entry not found and the result passed back is not null. But rather "Can't find...". Fail clause for command is prepared for null and, therefore, will never display. 

9. Allow `health` to accept a second parameter so that a community string can be passed.

10. Make `weather` command perform API call on demand. Rather than on a cron. So as to alleviate load on Wundergroun's Server.

11. Make `echo` trim off double quotes when a message is echoed like such: echo "test". Current output would be "test" instead of test.

12. Error handling for `health` isn't perfect. Try executing `healthd janus` for example. I don't even know how to describe why it's like that.
```

## Requirements to run:  
```
- A webserver  
- PHP (For the execution of provided CGI scripts)  
- Provided CGI scripts placed in /usr/lib/cgi-bin/  
- weatherpy: https://github.com/JackWink/Weather (For obtaining weather information)
- Cronjob to update weather every minute: */5 * * * * /usr/lib/cgi-bin/getWeather.sh
```
