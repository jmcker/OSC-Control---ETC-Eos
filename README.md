# OSC Control #

A collection of tools for controlling ETC's Eos family of lighting consoles.

### System Requirements ###
* Python 2.x
* [pyOSC](https://github.com/ptone/pyosc)

### Setup ###
1. Install Python and the pyOSC library.
2. Execute the desired Python script as below:
```python
python xxxxxxx.py target_ip listening_port
------------------------------------------------------
python xxxxxxx.py 192.168.1.8 3032
```
3. Executing with no arguments will use the default IP and port: 192.168.1.8 [3032]
4. To change the default host or port, open the script in a text editor and change the assignments to 'HOST' and 'PORT' as needed.
```python
import sys
from OSC import OSCClient, OSCMessage

def main(args):

    # Default host and port
    HOST = '192.168.1.8'
    PORT = 3032
	
	if len(args) == 2:

...
```

## Use with Multiplay ##
### Create a batch file ###
1. Open a text editor and create a new file.
2. Type *python*, the name of the script that you would like to run, and the optional IP and port information.
3. Save the file as *xxxxxxx*.bat to the same folder as the *xxxxxxx*.py command files.

```
python go.py
```
Note: To edit the batch file in the future, right click and select 'Edit'.

### Add the cue to Multiplay ###
1. Create a new launch cue in Multiplay.
2. Select the *xxxxxxx*.bat file in the **Command** field.
3. Select the parent folder of *xxxxxxx*.bat in the **Initial Directory** field.
4. Accept the changes and test the cue.

## Command Descriptions ##

### connect.py ###
Creates an OSC client, connects to it, and closes the connection. The OSC module takes about a second and a half to import.
This latency was detrimental to calls where timing was essential. Triggering connect.py shortly before needing to trigger a different command reduced (in most cases removed) the latency. This needs to be looked into...

### go.py ###
Triggers the main go button on the console.


## Creating Custom Commands ##
1. Save go.py as *command_name*.py
2. Open *command_name*.py in a text editor
3. Change the message to the desired message

A full list of the available Eos key messages is included as a PDF in the repository.

```python
...

    client = OSCClient()
    client.connect((HOST, PORT))

    # Desired message
    msg = OSCMessage("xxxxxxx");
    client.send(msg);
    client.close();

    print
    print "xxxxxxx"
    print
    exit();

...
```

### Contact ###

Jack McKernan [jmcker@outlook.com](mailto:jmcker@outlook.com)
