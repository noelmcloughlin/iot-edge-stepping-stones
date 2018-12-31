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


    def read(self, device, sensors=None):
        """ Publish mqtt topics """

        data = []
        for s in sensors:
            data.append(device.read(s))
        return data


    def subscribe(self, client, sensors=None):
        """ Subscribe to MQTT topics """

        if sensors:
            for s in sensors:
                client.subscribe(s)

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
