# Personal Website With JS Terminal Emulator

__LIVE DEMO:__ https://tjzimmerman.com

## Summary
This website is mostly written in Javascript. But also utilizes BASH, Perl, and Python in the backend. I made this website in an attempt to learn Javascript, but also to make my personal resume website better. In retrospective it's a little ghastly that I chose to use cgi scripts for the backend legwork. I recognize now that a web API would have been a much better design. A future rewrite may, perhaps, include that revision.

On my website, you'll find an interactive terminal emulator that supports a dozen commands intended to mimic the functionality of a Linux terminal. You'll also find several sections devoted to links about my online presences. 

The vertical size of the terminal output box can be adjusted by dragging the bottom right corner up and down. This is useful for viewing the contents of the terminal after running multiple commands or commands with large amount of output, such as `status`.

![Alt text](https://raw.githubusercontent.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator/master/screenshot.png "Terminal Emulator")


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

An event handler listens for a `return/enter` keypress. When a string is sent to the terminal, it is stored in a variable and compared against a whitelist of commands. If a match is found, the application executes the command with whatever parameters are provided. Basic error handling for PEBKAC & server-side issues has been included. Additionally the browser's `local storage` is leveraged to retain a temporary archive if historically executed commands.

Commands that require communication with the internal network do so by chainloading BASH scripts. These scripts were all written to perform some Linux magic to obtain the desired metrics. These files can be found in the `cgi-bin` folder. I've attempted to document them, however some parts may prove difficult to read. 

After a command is executed, the terminal enters its `cleanup` phase. This is used to scroll the output box to the end STDOUT in case it takes up more lines than the terminal has available. An empty line is added after the command is ran, and the shell prompt area is cleared of the previous command. 


## Is this safe?

It should be. No commands are executed locally. Instead, they are matched against a whitelist of supported commands. If a match is found, a separate script is then chainloaded by the server and the output is sent back to the server. If anyone wants to help me with pentesting or XSS I would really appreciate the opportunity for a learning experience. Feel free to email me at tj@tjzimmerman.com if interested.


## Mobile website

If you haven't seen the Family Guy .gif poking fun at CSS with Peter adjusting the blinds on a window, you should go Google it now. I won't pretend to be a web developer, so my CSS is pretty lousy. I've tried my best to make this website mobile friendly but it is still less dynamic than desired. Much help would be appreciated in this area. 

![Alt text](https://raw.githubusercontent.com/zimmertr/Personal-Website-With-JS-Terminal-Emulator/master/screenshot_mobile.png "Terminal Emulator - Mobile")


## Plans for future improvement

There are a ton of things that I would like to add to this project in the future. But the goal of the project was only ever to learn javascript and to improve my website so I have since halted development.

_Some ideas I have for improvement are:_

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


## Requirements to run:  
```
- A webserver  
- PHP (For the execution of provided CGI scripts)  
- Provided CGI scripts placed in /usr/lib/cgi-bin/  
- weatherpy: https://github.com/JackWink/Weather (For obtaining weather information)
- Cronjob to update weather every minute: */5 * * * * /usr/lib/cgi-bin/getWeather.sh
```
