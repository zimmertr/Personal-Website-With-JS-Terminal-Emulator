var commands = [
        ["clear:\t", "Clear the text area."],
        ["echo:\t", "Display a specified line of text."],
        ["help:\t", "Print a list of commands and their descriptions."],
        ["history:\t", "Display previously executed commands."],
	["info:\t", "Query a specific server for its health information."],
        ["ipaddr:\t", "Display the IP Address of the domain."],
        ["man:\t", "Display the manual for a specified command."],
	["nslookup:\t", "Query an internet name server for information."],
        ["ping:\t", "Send an ICMP request to a webserver and display the response."],
        ["status:\t", "Show the current status of all servers."],
        ["weather:\t", "Show a weather report for the location of the server."]
];

var servers = [
	["Apache:\t", "Nix.sol.milkyway\t", "http://tjzimmerman.com:2000/"],
	["Deluge:\t", "Janus.sol.milkyway\t", "http://tjzimmerman.com:8112/"],
	["LibreNMS:\t", "Mimas.sol.milkyway\t", "http://tjzimmerman.com:8442/"],
	["Mollify:\t", "Nix.sol.milkyway\t", "http://tjzimmerman.com:2000/mollify/"],
	["Nextcloud:\t", "Nix.sol.milkyway\t", "http://tjzimmerman.com:2000/nextcloud/"],
	["OpenVPN:\t", "Titan.sol.milkyway\t", "https://tjzimmerman.com:943/admin/"],
	["Plex:\t", "Janus.sol.milkyway\t", "https://tjzimmerman.com:32400/web/index.html"],
	["PRTG:\t", "IO.sol.milkyway\t", "http://tjzimmerman.com:8445/index.htm"],
	["Grafana:\t", "Ymir.sol.milkyway\t", "http://tjzimmerman.com:8441/login"],
	["vROps:\t", "Eris.sol.milkyway\t", "https://tjzimmerman.com:8444/ui"]
]

function handle(e){
        if(e.keyCode === 13){ //If return key is pressed
		event.preventDefault(); //prevent page from refreshing when submission is made
		var input=document.getElementById('shell').value
		
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
				document.getElementById('outbox').value += commands[[i],[i]];
				document.getElementById('outbox').value += "\n";	
			}
		}


		else if (input == "history"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		}
		

		else if (input == "info"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		
		}


		else if (input == "ipaddr"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";

			var domain = location.hostname;
			var port = location.port;
			var pathname = location.pathname;
			var protocol = location.protocol;

			protocol = protocol.replace(/:$/, ""); //Remove the stupid colon after the protocol.

			document.getElementById('outbox').value += "Domain: " + domain + "\n";
			document.getElementById('outbox').value += "Port: " + port + "\n";
			document.getElementById('outbox').value += "pathname: " + pathname + "\n";
			document.getElementById('outbox').value += "protocol: " + protocol + "\n";
		}


		else if (input == "man"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		}


		else if (input == "nslookup"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		}


		else if (input == "ping"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		}


		else if (input == "status"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
		}


		else if (input == "weather"){
			document.getElementById('outbox').value += "root@tjsh > " + input + "\n";
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
