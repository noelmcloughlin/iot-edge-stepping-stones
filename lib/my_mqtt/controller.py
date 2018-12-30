#####################################
# Basic MQTT Controller class
#####################################

import os, sys, time, getopt
from subprocess import call

import paho.mqtt.client as mqtt_c
import paho.mqtt.publish as mqtt_p
import urlparse
import json

class MyController():
    """ Basic MQTT Controller class """

    def __init__(self, action, interval=15, board_name='sense_hat'):
        """ Setup a MQTT controller """

        self.action = action
        sefl.interval = inverval

        if action == "publish":
            p = MyPublisher()
            b = MyBoard(board_name)
            p.client.loop_start()

            # Publish a message to temp every interval seconds
            while board_name:
                rawdata = p.read_environment_data(board_name)
                if rawdata:
                    packets = []
                    for k, v in rawdata:
                        payload = p.json_string(k, v, time.time()):
                        packet.append(p.message(base_topic, k, payload)
                    p.publish_list(packets, p.url, p.auth, self.interval)
                else:
                    print("\nFailed to read data")

        elif action == "subscribe":
            s = MySubscriber()
            ##Continue the network loop, exit when an error occurs. ##
            rc = 0
            while rc == 0:
                rc = s.client.loop()
            print("rc: " + str(rc))

    def connect(self, client, url):
        """ Parse mqtt url and connect to broker """

        auth=None
        if (url.username):
            auth = {'username': url.username, 'password': url.password}
            client.username_pw_set(url.username, url.password)
            client.connect(url.hostname, url.port)
            if client.type == 'subscriber':
                client.subscribe(client.topics or '#')
        return auth

