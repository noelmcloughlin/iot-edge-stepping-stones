#!/usr/bin/env python
#####################################
#####################################

import os, sys, time, getopt, urlparse
from subprocess import call

sys.path.append('../lib')
import osutils as utils
from mymqtt import controller, subscriber, publisher
from myboard import myboard

### BEGIN ####
persist=False


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
    domain='ENVIRONMENT'
    board_name='sense_hat'
    sensors = ['t', 'h', 'p']
    interval = 15

    ### Script command line arguments ###
    for opt, arg in opts:
        if opt in ("-a", "--action"):
            action = arg
        elif opt in ("-u", "--url"):
            url_str = arg
        elif opt in ("-b", "--board"):
            board_name = arg or board_name
        elif opt in ("-d", "--domain"):
            domain = arg or domain
        elif opt in ("-i", "--interval"):
            interval = arg or interval
        else:
            usage()

    if action == "install" and not url_str:
        install()

    elif action in ("publish", "subscribe") and url_str:
        url = urlparse.urlparse(url_str)
        ctrlr = controller.MyController(action, url)

        if action == 'publish':
            client = publisher.MyPublisher(ctrlr, url)
            #client.mqttc.loop_start()
            board = myboard.MyBoard(board_name)
            while True:
                data = ctrlr.read(board, sensors)
                messages = client.multiple_messages(client.base_topic, data)
                client.publish_multiple(messages, ctrlr.auth, interval)

        elif action == 'subscribe':
            client = subscriber.MySubscriber(ctrlr, url)
            ctrlr.subscribe(client, sensors)
            client.mqttc.loop_forever()
            rc = 0
            while rc == 0:
                rc = client.mqttc.loop()
            print("rc: " + str(rc))
    else:
        usage()

if __name__ == "__main__":
   main(sys.argv[1:])
exit(0)
