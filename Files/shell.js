var commands = [
        ["clear:\t", "Clear the text area."],
        ["echo:\t", "Write arguements to the standard output."],
        ["help:\t", "List all tjsh commands to the standard output."],
        ["history:\t", "Display previously executed commands."],
	["info:\t", "Query a specific server for its health information."],
        ["ipaddr:\t", "Display connection information for the web server."],
        ["man:\t", "Display the manual for a specified command."],
	["nslookup:\t", "Query an internet name server for information."],
        ["ping:\t", "Send an ICMP request to a webserver and display the response."],
        ["status:\t", "Show the current status of all servers."],
        ["weather:\t", "Show a weather report for the location of the server."]
];


//Check if localstorage history key is null. If it is, create it. If not, maintain old history.
if (localStorage.getItem("history") === null){
	localStorage.setItem('history', JSON.stringify([]));
}

function handle(e){
        if(e.keyCode === 13){ //If return key is pressed
		event.preventDefault(); //prevent page from refreshing when submission is made
		var input=document.getElementById('shell').value
	
		//Maintain history in local storage by taking the current storage, pushing it to a
		//json file, appending the new history item to the json file, and then pushing the
		//json file's contents back to the local storage. Necessary because local storage 
		//can only be given a single object at a time. Not an array. >_>	
		var tmp = localStorage.getItem('history');
		tmp = JSON.parse(tmp);
		tmp.push(input);
		localStorage.setItem('history', JSON.stringify(tmp));
		
	
		if (input == "clear"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			document.getElementById('outbox').value = "";
		}
		

		else if(input.startsWith("echo")){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			var output = "";

			if (input.length < 6 || !input.includes(" ")){ 
				if (input == "echo" || input == "echo "){
					document.getElementById('outbox').value += "What do you want to echo?\n";
				}
				else{
					document.getElementById('outbox').value += "-tjsh: command not found: " + input + "\n";
				}
			}
			else{
				output = input.substring(5); //Cut off 'echo ' from the output.
			}

			document.getElementById('outbox').value += output + "\n";	
		}


		else if(input == "help"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			document.getElementById('outbox').value += "The following commands are supported: \n\n";

			for (var i = 0; i < commands.length; i++){
				document.getElementById('outbox').value += commands[i][0] + commands[i][1];
				document.getElementById('outbox').value += "\n";	
			}
		}


		else if (input == "history"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			document.getElementById('outbox').value += JSON.parse(localStorage.getItem("history")).join('\n') + '\n';
		}
		

		else if (input == "info"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		
		}


		else if (input == "ipaddr"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			var req = new XMLHttpRequest();
			req.open('GET', '/cgi-bin/getIP.cgi', false);
			req.send(null);

			var domain = location.hostname;
			var port = location.port;
			var pathname = location.pathname;
			var protocol = location.protocol;

			protocol = protocol.replace(/:$/, ""); //Remove the stupid colon after the protocol.

			document.getElementById('outbox').value += "IP Address: " + req.responseText;
			document.getElementById('outbox').value += "Domain: " + domain + "\n";
			document.getElementById('outbox').value += "Protocol: " + protocol + "\n";
			document.getElementById('outbox').value += "Port: " + port + "\n";
			document.getElementById('outbox').value += "Path: " + pathname + "\n";
		}


		else if (input.startsWith("man")){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			if (input == "man clear"){
				document.getElementById('outbox').value += "CLEAR - Clear the text area.\n\nDESCRIPTION - Clear clears your screen if this is possible, including its scrollback buffer. Clear does not accept any arguements.\n";
			}
			else if (input == "man echo"){
                                document.getElementById('outbox').value += "ECHO - Write arguements to the standard output.\n\nDESCRIPTION - The echo utility writes any specified operands, separated by singe blank (' ') characters and followed by a newline ('\\n') character, to the standard output.\n\nSTRUCTURE - echo [string ...]\n";
                        }
                        else if (input == "man help"){
                                document.getElementById('outbox').value += "HELP - List all tjsh commands to the standard output.\n\nDESCRIPTION - The help utility writes a list of all available tjsh commands to the standard output as well as description of the purpose of each command.\n";
                        }
                        else if (input == "man history"){
                                document.getElementById('outbox').value += "HISTORY - Display previously executed commands.\n\nDESCRIPTION - History displays all previously executed commands that are held within your browser's local storage.\n";
                        }
                        else if (input == "man info"){
                                document.getElementById('outbox').value += "INFO - Query a specific server for its health information.\n\nDESCRIPTION - Info queries a server for a specified health state. Supported health information includes cpu, memory, load, swap, tx, rx, and uptime.\n\nSTRUCTURE - info [hostname] [health state]\n";
                        }
                        else if (input == "man ipaddr"){
                                document.getElementById('outbox').value += "IPADDR - Return network information about the server.\n\nDESCRIPTION - Ipaddr queries the server for information relating to it's network configuraiton. Displays the server's IP Address, domain, protocol, port, and relative path.\n";
                        }
                        else if (input == "man man"){
                                document.getElementById('outbox').value += "MAN - Format and display the on-line manual pages.\n\nDESCRIPTION - Man returns information on how to use the various commands that are supported by tjsh. ";
                        }
                        else if (input == "man nslookup"){
                                document.getElementById('outbox').value += "NSLOOKUP - Query DNS for a domain's IP configuration.\n\nDESCRIPTION - NSlookup returns IP configuration information for a domain that you specify by querying your computer's DNS.\n\nSTRUCTURE - nslookup [hostname|ip address]\n ";
                        }
                        else if (input == "man ping"){
                                document.getElementById('outbox').value += "PING - Ping a domain.\n\nDESCRIPTION - The ping utility uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway.\n\nSTRUCTURE - ping [hostname|ip address]\n";
                        }
                        else if (input == "man status"){
                                document.getElementById('outbox').value += "STATUS - Returns health of servers.\n\nDESCRIPTION - The status utility attempts to resolve a TCP connection to each of servers hosted on tjzimmerman.com If a server is detected as up, it will return an UP value. Likewise, if a server is detected as down, it will return a DOWN value.\n";
                        }
                        else if (input == "man weather"){
                                document.getElementById('outbox').value += "WEATHER - Return the current weather at the location of the server.\n\nDESCRIPTION - The weather utility queries a python script, weatherpy, for the current forceast of the location of the server. Provided information includes temperature in fahrenheit and celsius, sky conditions, wind direction, speed, and gust speed, and the relative humidity.\n";
                        }
                        else{
				document.getElementById('outbox').value += " ";
			}
		}


		else if (input.startsWith("nslookup")){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			
			if (input.length < 10 || !input.includes(" ")){
				if (input == "nslookup" || input == "nslookup "){
					document.getElementById('outbox').value += "For what domain did you want to query IP information?\n";
				}
				else{
					document.getElementById('outbox').value += "-tjsh: command not found: " + input + "\n";
				}
			}	
			else{
					
				hostname = input.substring(9);
				var req = new XMLHttpRequest();
				req.open('GET', '/cgi-bin/nslookup.cgi?'+ hostname, false);
				req.send(null);		
				
				if (req.responseText == ""){
					document.getElementById('outbox').value += "Domain or IP not found in namserver.\n";
				}
				else{			
					document.getElementById('outbox').value += req.responseText;	
				}
			}
		}


		else if (input.startsWith("ping")){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			
				if (input.length < 6 || !input.includes(" ")){
					if (input == "ping" || input == "ping "){
						document.getElementById('outbox').value += "What domain did you want to ping?\n";
					}
					else{
						document.getElementById('outbox').value += "-tjsh: command not found: " + input + "\n";
					}	
				}
				else{
					hostname = input.substring(5);
					var req = new XMLHttpRequest();
					req.open('GET', '/cgi-bin/ping.cgi?' + hostname, false);
					req.send(null);

					if (req.resposneText == ""){
						document.getElementById('outbox').value += "Domain or IP not found in nameserver.\n";
					}
					else{
						document.getElementById('outbox').value += req.responseText;
					}		
				}		
		}


		else if (input == "status"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		
				hostname = input.substring(7);
				var req = new XMLHttpRequest();
				req.open('GET', '/cgi-bin/status.cgi?'+ hostname, false);
				req.send(null);		
				
				document.getElementById('outbox').value += req.responseText;	
		}


		else if (input == "weather"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			var req = new XMLHttpRequest();
                        req.open('GET', '/cgi-bin/getWeather.cgi', false);
                        req.send(null);
			
			document.getElementById('outbox').value += req.responseText;
		}


		else {
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
			document.getElementById('outbox').value += "-tjsh: command not found: " + input + "\n";
		} 
		

		cleanUp();
		return false;

	}return false;}

function cleanUp(){
	if(document.getElementById('outbox').selectionStart == document.getElementById('outbox').selectionEnd){ //Automatically scroll to end of output.
		document.getElementById('outbox').scrollTop = document.getElementById('outbox').scrollHeight;
	}

	document.getElementById('outbox').value += "\n"; //Place an empty line after a command runs.
	document.getElementById('shell').value = ""; //Reset the shell prompt after a command runs.
}
