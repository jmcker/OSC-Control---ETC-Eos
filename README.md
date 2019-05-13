# OSC Control #

A collection of tools for controlling ETC's Eos family of lighting consoles.

### System Requirements ###
- Python 2.7 (available [here](https://www.python.org/ftp/python/2.7.14/python-2.7.14rc1.amd64.msi) for 64-bit Windows or [here](https://www.python.org/ftp/python/2.7.14/python-2.7.14rc1.msi) for 32-bit Windows)
- [pyOSC](https://github.com/ptone/pyosc)
```bash
# Install pyOSC
python2 -m pip --user install pyOSC
```


### Setup ###
1. Install Python and the pyOSC library (Use ```pip``` from above or download the repository and run the ```setup.py``` file in the root folder).
2. Execute the ```send.py``` script as below:
```python
python send.py [message] [target_ip] [listening_port]
------------------------------------------------------
python /eos/key/go_0 192.168.1.8 3032
```
3. Executing with only the message argument will use the default IP and port: ```192.168.1.8 [3032]```
4. To change the default host or port, open the script in a text editor and change the defaults as needed.
```python
...
def main(args):

    # Defaults
    # Change prefix if you always want to prefix something to the command
    # Ex: prefix = "/eos/key/"
    # This would allow you to send abbreviated commands from the command line
    prefix = ""
    command = "preload"
    HOST = "192.168.1.8"
    PORT = 3032
...
```

## Use with MultiPlay ##
### Create a batch file ###
1. Open a text editor and create a new file.
2. Type the ```python send.py [message] ...``` command as as you would normally.
3. Save the file as *xxxxxxx*.bat.
4. Make sure the path to ```send.py``` is absolue (begins with ```C:\...``` or similar) or is relative to the saved location of *xxxxxxx*.bat.

Note: To edit the batch file in the future, right click and select 'Edit'.

### Add the cue to MultiPlay ###
1. Create a new launch cue in MultiPlay.
2. Select the *xxxxxxx*.bat file in the **Command** field.
3. Select the parent folder of *xxxxxxx*.bat in the **Initial Directory** field.
4. Accept the changes and test the cue.

## Command Descriptions ##

### connect.bat ###
Creates an OSC client, connects to it, and closes the connection. The OSC module takes about a second and a half to import.
This latency was detrimental to calls where timing was essential. Triggering connect.py shortly before needing to trigger a different command reduced (in most cases removed) the latency. This needs to be looked into...

### go.bat ###
Trigger the main GO button on the console.


## Custom Commands ##
1. Any OSC command can be passed as the first argument to the ```send.py``` script.

A full list of the available Eos key messages is included as a PDF in the repository [here](reference/Eos%20OSC%20Keys.pdf).
For a more in-depth explanation of Eos OSC capabilities, see Pages 47+ of [this document](reference/EosFamily_ShowControl_UserGuide_RevC.pdf).
