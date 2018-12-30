#####################################
# Basic MQTT Publisher class
#####################################

import sys, time, json
import paho.mqtt.client as mqtt_c
import paho.mqtt.publish as mqtt_p

class MyPublisher():
    """ Basic MQTT Publisher class """

    def __init__(self, controller, url):
        """ Init MQTT publisher """

        ### order is important
        self.client = mqtt_c.Client()
        self.type = 'publisher'
        self.base_topic = url.path[1:]
        try:
            self.auth = controller.connect(self, url)
        except:
            print("\nCannot connect to %s" % url)
            exit(1)
        self.url = url

    def json_string(name='t', value=None, time=time.time()):
        """ Create JSON string """
        return json.dumps({"".join(name): "".join(value), "timestamp": "".join(time)})

    def message(base_topic, name='t', payload=None):, 
        """ Create mqtt message """
        return {'topic': "".join(base_topic) + "/".join(name), 'payload':"".join(payload)}

    def publish_multiple(packets, url, auth, seconds):
        """ Publish mqtt messages """
        mqtt_p.multiple(packets, hostname=url.hostname, port=url.port, auth=auth)
        print("published")
        time.sleep(seconds)
