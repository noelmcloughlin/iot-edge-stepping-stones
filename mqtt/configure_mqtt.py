#!/usr/bin/env python
#####################################
#####################################

import os, sys, time, getopt
from subprocess import call

sys.path.append('../lib')
import osutils as utils
import my_mqtt

### MAIN ####

def usage():
    print("\n%s Usage:" % os.path.basename(__file__))
    print("\n\t-a --action\t install | publish | subscribe | persist ")
    print("\n\t-u --url\t <mqtt-broker-url> ")
    print("\n\t [ -d --domain \t <mqtt-topicname> ]\t default is WEATHER_SENSEHAT")
    print("\n\t [ -b --board\t sense_hat | bme680 ]\t default is sense_hat")
    print("\n\t [ -i --interval\t <seconds>  ]\t default is 15 seconds")
    print("\n")
    sys.exit(2)
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"b:a:u:d:i:",["board=", "action=", "url=", "domain=", "interval="])
    except getopt.GetoptError:
        usage()

    if not opts:
        usage()

    ### Script Defaults ###
    domain="WEATHER_SENSEHAT"
    board="sense_hat"

    ### Script command line arguments ###
    for opt, arg in opts:
        if opt in ("-a", "--action"):
            action = arg
        elif opt in ("-u", "--url"):
            url_str = arg
        elif opt in ("-b", "--board"):
            board = arg or board
        elif opt in ("-d", "--domain"):
            domain = arg or domain
        elif opt in ("-i", "--interval"):
            seconds = arg or '15'
        else:
            usage()

    ### Script Action ### 
    if action == "install" and not url:
        install()
    elif action in ("publish", "subscribe") and url:
        url = urlparse.urlparse(url_str)
        c = MyController(url)
        c.mqtt(action, base_topic, url, board)
    else:
        usage()

if __name__ == "__main__":
   main(sys.argv[1:])
exit(0)
