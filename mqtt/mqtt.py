#!/usr/bin/env python
#####################################
#####################################

import os, sys, time, getopt, urlparse
from subprocess import call

sys.path.append('../lib')
import osutils as utils

### BEGIN ####

def usage():
    print("\n%s Usage:" % os.path.basename(__file__))
    print("\n\t-a --action\tinstall | publish | subscribe | persist ")
    print("\n\t-u --url\t<mqtt-topic-url>\tmqtt topic (examples ..)")
    print("\n\t\t\t- mqtt://iot.eclipse.org:1883/HIWORLD/home")
    print("\t\t\t- mqtt://broker.hivemq.com:1883/HIWORLD/home")
    print("\t\t\t- mqtt://test.mosquitto.org:1883/HIWORLD/home")
    print("\n\t[ -b --board\tsense_hat | bme680 ]\tdefault 'sense_hat'")
    print("\n\t[ -i --interval\t<seconds> ]\t\tdefault 15 secs")
    print("\n\t[ -p --persist True|False ]\t\tPersist msgs to TinyDB")
    print("\n\t[ -q --qos  0 | 1 | 2 ]\t\t\tMQTT Quality of Service")
    print("\n")
    sys.exit(2)

def install():
    utils.install_pkg(['mosquitto',])
    utils.install_pip(['paho-mqtt', 'tinyDB', 'flask', 'flask-cors',])
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"b:a:u:p:q:i:",["board=", "action=", "url=", "persist=", "qos=", "interval="])
    except getopt.GetoptError as e:
        usage()

    if not opts:
        usage()

    sensors = ['t', 'h', 'p']
    url_str=""
    qos=0
    board_name='sense_hat'
    interval=15
    persist=False

    ### Script command line arguments ###
    for opt, arg in opts:
        if opt in ("-a", "--action"):
            action = arg
        elif opt in ("-u", "--url"):
            url_str = arg or None
        elif opt in ("-q", "--qos"):
            qos = arg
            if int(arg) and (qos < 0 or qos > 2):
                usage()
        elif opt in ("-b", "--board"):
            board_name = arg
        elif opt in ("-i", "--interval"):
            interval = arg
        elif opt in ("-p", "--persist"):
            persist = arg
        else:
            usage()

    if action == "install" and not url_str:
        install()

    elif action in ("publish", "subscribe") and url_str:

        from mymqtt import controller, subscriber, publisher
        from myboard import myboard

        url = urlparse.urlparse(url_str)
        ctrlr = controller.MyController(action, url)

        if action == 'publish':
            client = publisher.MyPublisher(ctrlr, url)
            client.mqttc.loop_start()
            board = myboard.MyBoard(board_name)
            while True:
                data = ctrlr.read(board, sensors)
                print(data)
                messages = client.multiple_messages(client.base_topic, data)
                client.publish_multiple(messages, ctrlr.auth, interval)

        elif action == 'subscribe':
            client = subscriber.MySubscriber(ctrlr, url, qos, persist)
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
