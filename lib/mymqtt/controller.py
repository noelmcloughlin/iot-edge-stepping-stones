#####################################
# Basic MQTT Controller utility class
#####################################

import json

class MyController():

    """ Basic MQTT Controller class """

    def __init__(self, action, url):
        """ Setup a MQTT controller """

        self.action = action
        self.url = url
        self.auth=None


    def read(self, board, sensors=None, timestamp=False):
        """ Read pin values from board.
            Return a dict.
        """

        keys = []
        values = []
        for sensor in sensors:
            keys.append(sensor)
            values.append(board.read(sensor))
        return dict(zip(keys, values)) 


    def subscribe(self, client, sensors=None):
        """ Subscribe to MQTT topics """

        if sensors:
            for s in sensors:
                client.subscribe(s)

    def connect(self, mqttc, url):
        """ Parse mqtt url and connect to broker """

        if (url.username):
            self.auth = {'username': url.username, 'password': url.password}
            mqttc.username_pw_set(url.username, url.password)
        mqttc.connect(url.hostname, url.port)
