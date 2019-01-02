#####################################
# Basic MQTT Publisher utility class
#####################################

import paho.mqtt.client as mqtt_c
import paho.mqtt.publish as publish
import json
import time
import ast


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
        controller.connect(self.mqttc, self.url)

    def on_connect(self, client, userdata, flags, rc):
        """ On connection callback """

        print("Connected to %s%s Result: %s" % (self.url.netloc, self.url.path, str(rc)))


    def on_publish(self, client, obj, mid):
        """ On publish callback. According to MQTT protocol,
            QOS=0 messages are not acked. This means this
            method is only invoked when QOS>0.
        """

        print("Message ID: " + str(mid))


    def multiple_messages(self, base_topic, data):
        """ Create JSON messages list """

        bundle_of_messages = []
        t = time.time()
        messages = []
        for k,v in data.items():
            record = {}
            record.update({k:v, 'timestamp': t})
            messages.append(record)
            mqtt_message = {"topic": base_topic + "/" + k, 'payload': v}
            bundle_of_messages.append(mqtt_message)
        return bundle_of_messages

    def publish_multiple(self, messages, auth=None, interval=15):
        """ Publish multiple mqtt messages """

        publish.multiple(messages, hostname=self.url.hostname, port=self.url.port, auth=None)
        ## you might want to uncomment when QOS=0 to get some kind of feedback###
        #print("published")
        time.sleep(interval)
