#!/usr/bin/env python2.7

import sys
try:
    from OSC import OSCClient, OSCMessage
except:
    print "Could not find pyOSC. Please see the documentation or install using: pip install --user pyOSC"
    exit()

def main(args):

    # Defaults
    # Change prefix if you always want to prefix something to the command
    # Ex: prefix = "/eos/key/"
    # This would allow you to send abbreviated commands from the command line
    prefix = ""
    command = "preload"
    HOST = "192.168.1.8"
    PORT = 3032

    if len(args) == 3:
        command = args[0]
        HOST = args[1]
        PORT = int(args[2])
    elif len(args) == 2:
        command = args[0]
        HOST = args[1]
    elif len(args) == 1:
        command = args[0]
    elif len(args) > 3:
        print "Usage:"
        print "    python send.py [message] [host] [port]"
        errorPrint("send.py accepts at most 3 arguments.\n%s were provided." % len(args));

    client = OSCClient()
    client.connect((HOST, PORT))

    # Check for reserved commands that should do nothing but connect
    if (command != "preload" and command != "connect"):
        msg = OSCMessage(prefix + command)
        client.send(msg)

        print
        print "Sent '%(command)s' to %(HOST)s[%(PORT)d]." % locals()
        print
    else:
        print
        print "Preloaded. No message sent."
        print

    client.close()

    exit()

def errorPrint(message, standardErr = ""):
    print
    print message
    if standardErr:
        print "Error message: ", standardErr
    print
    print "Press ENTER to exit..."
    raw_input()
    exit()

if __name__ == "__main__":
    main(sys.argv[1:])