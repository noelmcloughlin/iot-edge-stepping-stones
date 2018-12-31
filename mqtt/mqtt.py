#!/usr/bin/env python
#####################################
#####################################

import os, sys, time, getopt, urlparse
from subprocess import call

sys.path.append('../lib')
import osutils as utils
from mymqtt import controller, subscriber, publisher

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
    
def on_connect(client, userdata, flags, rc):
    """ On connection callback """
    print("Connection Result: " + str(rc))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed,  QOS granted: "+ str(granted_qos))

def on_publish(client, obj, mid):
    """ On publish callback """
    print("Message ID: " + str(mid))

def on_message(self, client, obj, msg):
    """ Display or Persist received message """
    print("Topic:"+msg.topic + ",Payload:" + str(msg.payload))

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
        ctrlr = controller.MyController(action, url)
        if action == 'publish':
            client = publisher.MyPublisher(ctrlr, url)
            client.mqttc.loop_start()
            board = myboard.MyBoard(self.board_name)
            while True:
                messages = {}
                data = ctrlr.read(board, sensors)
                payload = p.as_json_string(s, data)
                messages.append(p.as_json_message(p.base_topic, client, payload))
                client.publish_multiple(messages, seconds)
        else:
            client = subscriber.MySubscriber(ctrlr, url)
            ctrlr.subscribe(client, sensors)
            client.mqttc.loop_forever()
            rc = 0
            while rc == 0:
                rc = s.mqttc.loop()
            print("rc: " + str(rc))
    else:
        usage()

if __name__ == "__main__":
   main(sys.argv[1:])
exit(0)
