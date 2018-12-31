#####################################
# Basic MQTT Publisher utility class
#####################################

import paho.mqtt.client as mqtt_c
import paho.mqtt.publish as mqtt_p
import json
import time


class MyPublisher():
    """ Basic MQTT Publisher class """

    def __init__(self, controller, url):
        """ Initialize the mqtt publisher.
            Setup the mqtt client, event callbacks.
            Then establish the connection.
        """

        self.base_topic = url.path[1:]
        self.url = url
        self.mqttc = mqtt_c.Client()
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        controller.connect(self.mqttc, url)

    def on_connect(self, client, userdata, flags, rc):
        """ On connection callback """

        print("Connected to %s%s Result: %s" % (self.url.netloc, self.url.path, str(rc)))


    def on_publish(self, client, obj, mid):
        """ On publish callback """

        print("Message ID: " + str(mid))


    def create_json_string(self, n, v=None, t=time.time()):
        """ Create JSON string """

        jstring = "{'%s': %s, 'timestamp': %s}" % (str(n), str(v), str(t))
        return json.dumps(jstring)


    def create_json_message(self, base_topic, name='t', payload=None):
        """ Create mqtt message """

        return "{'topic': '%s/%s', 'payload': %s}" % (base_topic, name, payload)


    def publish_multiple(self, msgs, seconds=15):
        """ Publish mqtt messages """

        mqtt_p.multiple(msgs, hostname=self.url.hostname, port=self.url.port, auth=self.auth)
        print("\published")
        time.sleep(seconds)
