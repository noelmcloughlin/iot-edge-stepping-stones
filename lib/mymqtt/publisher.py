#####################################
# Basic MQTT Publisher utility class
#####################################

import paho.mqtt.client as mqtt_c
import paho.mqtt.publish as mqtt_p
import json
import time

class MyPublisher():
    """ Basic MQTT Publisher class """

    def __init__(self, url):
        """ Init MQTT publisher """

        self.mqttc = mqtt_c.Client()
        self.type = 'publisher'
        self.base_topic = url.path[1:]
        self.url = url


    def json_string(self, n, v=None, t=time.time()):
        """ Create JSON string """

        json_string = "{'%s': %s, 'timestamp': %s}" % (str(n), str(v), str(t))
        return json.dumps(json_string)


    def message(self, base_topic, name='t', payload=None):
        """ Create mqtt message """

        return {'topic': "".join(base_topic) + "/".join(name), 'payload':"".join(payload)}


    def publish_multiple(self, packets, url, auth, seconds):
        """ Publish mqtt messages """

        mqtt_p.multiple(packets, hostname=url.hostname, port=url.port, auth=auth)
        print("published")
        time.sleep(seconds)
