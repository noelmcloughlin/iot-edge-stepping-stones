#!/usr/bin/env python
#####################################
#####################################

import os, sys, time, getopt, urlparse
from subprocess import call

sys.path.append('../lib')
import osutils as utils
from mymqtt import controller, subscriber, publisher

### MAIN ####

def usage():
    print("\n%s Usage:" % os.path.basename(__file__))
    print("\n\t-a --action\t install | publish | subscribe | persist ")
    print("\n\t-u --url\t <mqtt-broker-url> ")
    print("\n\t [ -d --domain \t <mqtt-topicname> ]\t default is 'environment'")
    print("\n\t [ -b --board\t sense_hat | bme680 ]\t default is sense_hat")
    print("\n\t [ -i --interval\t <seconds>  ]\t default is 15 seconds")
    print("\n")
    sys.exit(2)

def install():
    utils.install_pkg(['mosquitto', 'mosquitto-client',])
    utils.install_pip(['paho-mqtt', 'tinyDB', 'flask', 'flask-cors',])
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"b:a:u:d:i:",["board=", "action=", "url=", "domain=", "interval="])
    except getopt.GetoptError:
        usage()

    if not opts:
        usage()

    ### Script Defaults ###
    domain='environment'
    board='sense_hat'

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
            if domain == 'environment':
                sensors = ['temperature', 'humidity', 'pressure',]
        elif opt in ("-i", "--interval"):
            seconds = arg or '15'
        else:
            usage()

    if action == "install" and not url_str:
        install()

    elif action in ("publish", "subscribe") and url_str:
        sensors = []
        if board == 'sense_hat' and domain == 'environment':
            sensors = ['temperature', 'humidity', 'pressure']
        elif board == 'bme680':
            sensors = ['temperature', 'humidity', 'pressure']

        url = urlparse.urlparse(url_str)
        c = controller.MyController(action, url)

        if action == 'publish':
            p = publisher.MyPublisher(url)
            print("\connect")
            c.connect(p.mqttc, url)
            print("\done connect")
            p.mqttc.loop_start()
            c.publish(p, sensors)
        else:
            s = subscriber.MySubscriber(url)
            c.connect(p.mqttc, url)
            s.loop_forever()
            c.subscribe(s, sensors)
            ##Continue the network loop, exit when an error occurs. ##
            rc = 0
            while rc == 0:
                rc = s.mqttc.loop()
            print("rc: " + str(rc))
    else:
        usage()

if __name__ == "__main__":
   main(sys.argv[1:])
exit(0)
