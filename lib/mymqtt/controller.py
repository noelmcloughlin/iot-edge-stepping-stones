#####################################
# Basic MQTT Controller utility class
#####################################

import json
from myboard import myboard

class MyController():

    """ Basic MQTT Controller class """

    def __init__(self, action, url, interval=15, board_name='sense_hat'):
        """ Setup a MQTT controller """

        self.action = action
        self.url = url
        self.interval = interval
        self.board_name = board_name
        self.auth=None


    def publish(self, p, sensors=None):
        """ Publish mqtt topics """

        #### Publish message topics every interval seconds
        b = myboard.MyBoard(self.board_name)

        while sensors:
            messages = []
            for s in sensors:
                rawvalue = b.read(s)
                if rawvalue:
                    payload = p.json_string(s, rawvalue)
                    messages.append(p.message(p.base_topic, s, payload))
                else:
                    print("\nFailed to read %s from board" % s)
            p.publish_multiple(messages, self.url, self.auth, self.interval)


    def subscribe(self, s, sensors=None):
        """ Subscribe to MQTT topics """

        if sensors:
            for s in sensors:
                s.subscribe(sensors)


    def connect(self, mqttc, url):
        """ Parse mqtt url and connect to broker """

        self.auth=None
        if (url.username):
            self.auth = {'username': url.username, 'password': url.password}
            mqttc.username_pw_set(url.username, url.password)
        try:
            mqttc.connect(url.hostname, url.port)
        except:
            print("\nCannot connect to %s" % url)
            exit(1)
        print("\nconnected to %s:%s and publishing events\n" % (url.hostname, url.port))
