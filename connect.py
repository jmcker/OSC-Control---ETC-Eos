import sys
from OSC import OSCClient, OSCMessage

def main(args):

    # Default host and port
    HOST = '192.168.1.8'
    PORT = 3032
    
    if len(args) == 2:
        HOST = args[0]
        PORT = args[1]
    elif len(args) == 1:
        HOST = args[0]
    elif len(args) > 2:
        errorPrint("OSC Go button accepts at most 2 arguments.\n" + len(args) + " were provided.");

    client = OSCClient()
    client.connect((HOST, PORT))
    client.close();

    print
    print "Connected"
    print
    exit();

    
        
def errorPrint(message, standardErr = ""):
    print "\n\n"
    print message
    if standardErr:
        print "Error message: ", standardErr
    print
    print "Press ENTER to exit..."
    raw_input()
    exit()

if __name__ == "__main__":
    main(sys.argv[1:])
