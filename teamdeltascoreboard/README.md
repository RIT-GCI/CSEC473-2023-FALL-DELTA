# Scoring system


## Installation
`pip3 install paramiko requests impacket icmplib flask smbprotocol flask-cors dnspython pyodbc rocketchat-API nextcloud-api-wrapper pyad dnspython`

Just do pip3 install ___ package if it asks for one, not 100% sure on the list


## Three different servers, three different terminal instances:
Webserver that handles the routes
- `flask --app ./webserver/webserver.py run`

Main.py that runs a flask server to handle scores
- `python3 main.py`

Front end that takes and displays scores
- `npx serve ./frontend/`